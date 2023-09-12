from fastapi import HTTPException
from rembg import remove
from PIL import Image
from io import BytesIO
import io
import cv2
import numpy as np
import base64

from models.validations import ImgBase64

# Validate if the image is Base64 encoded
def isBase64(uri: str) -> bool:
    """Check if string is a base64 encoded image"""
    try:
        image_data = base64.b64decode(uri.split(',')[1])
        image = Image.open(BytesIO(image_data))
        return True
    except Exception:
        return False

# Convert base64 image to PIL
def readb64(uri: str) -> Image:
    """Convert base64 image to PIL"""

    # Decode the base64 string
    image_data = base64.b64decode(uri.split(',')[1])

    # Create an image object from the decoded data
    image_arr = Image.open(io.BytesIO(image_data))

    # Return the converted image
    return image_arr

# Remove background from image
def remove_backgroud(img: Image) -> Image:
    """Remove background from image"""
    out = remove(img)

    # Return the image without background
    return out


# Perspective transform
def perspective_transform(pil_image: Image) -> str:
    
    # Transform the image to a numpy array
    pil_image_bytes = np.array(pil_image)
    _, image_encoded = cv2.imencode(".png", pil_image_bytes)

    # Begin the operations with opencv (CV2)
    image_init = cv2.imdecode(image_encoded, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image_init,cv2.COLOR_BGR2GRAY)
    _,th = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)


    contornos1,hierarchy1 = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contornos2,hierarchy2 = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contorno_credencial = max(contornos1, key=cv2.contourArea)

    convex_hull = cv2.convexHull(contorno_credencial)

    # Calcular el rectángulo de área mínima que encaja en el convex hull
    rectangulo_min_area = cv2.minAreaRect(convex_hull)
    vertices = cv2.boxPoints(rectangulo_min_area)
    vertices = np.int0(vertices)

    # Calcular el centro del rectángulo mínimo
    centro_rectangulo = np.mean(vertices, axis=0)

    # Ordenar los vértices según su distancia al centro
    puntos_ordenados = sorted(vertices, key=lambda punto: np.arctan2(punto[1] - centro_rectangulo[1], punto[0] - centro_rectangulo[0]))

    # Dibujar los vértices del rectángulo en la image_init original
    for punto in vertices:
        cv2.circle(image_init, tuple(punto), 5, (0, 255, 0), -1)

    pts1 = np.float32([puntos_ordenados[0],puntos_ordenados[1],puntos_ordenados[3],puntos_ordenados[2]])
    pts2 = np.float32([[0,0], [480,0], [0,300], [480,300]])

    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(image_init, M, (480,300))

    # cv2.drawContours(image_init, [convex_hull], -1, (0, 255, 0), 2)

    _, encoded_image = cv2.imencode(".png", dst)

    # Convert the encoded image to a base64 string
    base64_image = base64.b64encode(encoded_image).decode("utf-8")

    return base64_image


# Main function to enhace the ID image removing background and perspective transform
def id_image_enhacer(image_b64: str) -> ImgBase64:

    # First we validate if the input its a valid Base64 encoded image
    if not isBase64(image_b64):
        raise HTTPException(
            status_code=500,
            detail="Invalid image format, must be base64 encoded string"
        )

    # Get the image without background
    image_nobg = remove_backgroud(readb64(image_b64))

    # buff = BytesIO()
    # image_nobg.save(buff, format="PNG")
    # image_string = base64.b64encode(buff.getvalue()).decode("utf-8")

    # Get the image with perspective transform
    image_string = perspective_transform(image_nobg)

    id_image = ImgBase64(image_b64 = image_string)
    return id_image

def id_remove_backgroud(image_b64: str) -> ImgBase64:
    # First we validate if the input its a valid Base64 encoded image
    if not isBase64(image_b64):
        raise HTTPException(
            status_code=500,
            detail="Invalid image format, must be base64 encoded string"
        )

    # Get the image without background
    image_nobg = remove_backgroud(readb64(image_b64))

    buff = BytesIO()
    image_nobg.save(buff, format="PNG")
    image_string = base64.b64encode(buff.getvalue()).decode("utf-8")

    id_image = ImgBase64(image_b64 = image_string)
    return id_image
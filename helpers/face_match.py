from fastapi import HTTPException
from PIL import Image
from io import BytesIO
import face_recognition
import io
import base64

from models.validations import FaceIDResponse

# Validate if the image is Base64 encoded
def isBase64(uri: str) -> bool:
    """Check if string is a base64 encoded image"""
    try:
        image_data = base64.b64decode(uri.split(',')[1])
        image = Image.open(BytesIO(image_data))
        return True
    except Exception:
        return False

# Convert base64 image to byte array
def readb64(uri: str):
    """Convert base64 image to PIL"""

    # Decode the base64 string
    image_data = base64.b64decode(uri.split(',')[1])

    # Convert to numpy array
    image_arr = io.BytesIO(image_data)
    print(type(image_arr))

    # Create an image object from the decoded data (PIL)
    # image_arr = Image.open(io.BytesIO(image_data))

    # Return the converted image
    return image_arr


# Compare two images and return if they are the same person
def face_compare(img1: str, img2: str) -> FaceIDResponse:
    """Compare two images and return if they are the same person"""
    if not isBase64(img1) or not isBase64(img2):
        raise HTTPException(
            status_code=500,
            detail="Invalid image format, must be a base64 encoded string"
        )
    
    # Load images
    img1_obj = face_recognition.load_image_file(readb64(img1))
    img2_obj = face_recognition.load_image_file(readb64(img2))

    # Get the face encoding of each image
    img1_face_encoding = face_recognition.face_encodings(img1_obj)[0]
    img2_face_encoding = face_recognition.face_encodings(img2_obj)[0]

    # Compare the faces
    results = face_recognition.compare_faces([img1_face_encoding], img2_face_encoding,0.65)

    is_same_person = FaceIDResponse(isSamePerson=results[0])
    # Return the result
    return is_same_person

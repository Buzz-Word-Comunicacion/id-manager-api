import torch
from PIL import Image
from diffusers import StableDiffusionPipeline
import base64
from io import BytesIO

#Modelo
def configurar_modelo_stable_diffusion():
    model_id = "stabilityai/stable-diffusion-2-1" 
    pipe = StableDiffusionPipeline.from_pretrained(model_id).to("cuda")
    return pipe

#Genera la imagen
def generar_imagen_desde_texto(pipe, texto):
    with torch.autocast("cuda"):
        image = pipe(texto).images[0]
    return image

#Combina la imagen generada y el boceto y retorna la imagen en Base64
def combinar_imagenes_base64(boceto_path, diseño_generado):
    boceto = Image.open(boceto_path).convert("RGBA")
    diseño_generado = diseño_generado.convert("RGBA")
    diseño_generado = diseño_generado.resize(boceto.size, Image.Resampling.LANCZOS)

    mask = boceto.convert("L")  
    mask = mask.point(lambda x: 255 if x < 50 else 0, mode='1')  

    verde = (0, 255, 0) 
    for x in range(boceto.size[0]):
        for y in range(boceto.size[1]):
            if boceto.getpixel((x, y))[:3] == verde:  
                mask.putpixel((x, y), 0)

    tarjeta_final = Image.new("RGBA", boceto.size)
    for x in range(boceto.size[0]):
        for y in range(boceto.size[1]):
            if mask.getpixel((x, y)) == 255:  
                pixel_color = diseño_generado.getpixel((x, y))
                tarjeta_final.putpixel((x, y), pixel_color) 
            else:
                tarjeta_final.putpixel((x, y), boceto.getpixel((x, y)))  

    # Convertir la imagen final a Base64
    buffered = BytesIO()
    tarjeta_final.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    return img_base64

#Tematicas permitidas
def obtener_tema_validado(tema_usuario):
    tematicas_validas = ["tecnologia", "cultura", "deporte", "arte", "minimalismo", "astronomia", "videojuegos"]

    tema_usuario = tema_usuario.lower()
    if tema_usuario not in tematicas_validas:
        print("Tema no válido. Por favor, elige entre las siguientes temáticas permitidas:")
        print(", ".join([t.capitalize() for t in tematicas_validas]))
        return None

    if tema_usuario == "videojuegos":
        return "Gamer 4K"
    elif tema_usuario in ["deporte", "arte", "astronomia"]:
        return f"{tema_usuario.capitalize()} 4K"
    else:
        return tema_usuario.capitalize()

if __name__ == "__main__":
    pipe = configurar_modelo_stable_diffusion()

    while True:
        tema_usuario = input("Elige un tema para tu TDC: ") 
        tema = obtener_tema_validado(tema_usuario)
        if not tema:
            continue

        contador = 0
        max_imagenes = 4  
        
        while contador < max_imagenes:
            print(f"Generando imagen...")
            imagen_generada = generar_imagen_desde_texto(pipe, tema)
            boceto_path = "art-black.png"
            
            #Genera la imagen final y la convierte en Base64
            imagen_base64 = combinar_imagenes_base64(boceto_path, imagen_generada)
            print(f"Imagen {contador+1} en Base64: {imagen_base64[:100]}...") #Muestra solo los primeros 100 caracteres
            
            contador += 1

        repetir = input("¿Te gustaron las imágenes? (si/no): ").lower()
        if repetir != 'no':
            break
        else:
            print("Generando 4 imágenes adicionales...")

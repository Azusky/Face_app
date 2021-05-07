
from PIL import Image, ImageOps, ImageFilter
import face_recognition
from os import walk, makedirs, path

# processImage ( source, destination, size = 64 default)
# if  there is a face
# fix bag dublicat img
def processImage(source, destination, size = 64):

    _,_,files = next(walk(f'{source}'))
    i = 0
    for file in files:
        image = face_recognition.load_image_file(f"{source}/{file}")
        face_locations = face_recognition.face_locations(image)
        if face_locations != []:
            for face_location in face_locations:
                top, right, bottom, left = face_location

                face_image = image[top:bottom, left:right]
                pil_image = Image.fromarray(face_image)
                pil_image = pil_image.filter(ImageFilter.SHARPEN)
                # pil_image = pil_image.filter(ImageFilter.MinFilter)
                pil_image = pil_image.resize((size, size), Image.ANTIALIAS)
                pil_image = ImageOps.grayscale(pil_image)
            if not path.exists(f"{destination}"):
                makedirs(f'{destination}')
            pil_image.save(f'{destination}/{file}', 'jpeg')
            i += 1
            print(f'Processed Image: {i} in {len(files)}')

# processImage('./original_images/Joanna','./processed_images/Joanna')

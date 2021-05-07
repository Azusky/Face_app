import json
import requests
import base64
import face_recognition
from PIL import Image
import urllib.request
from io import BytesIO


def loadConfig(settings):
    file_settings = open(f'{settings}.json', encoding='utf8')
    settings = json.load(file_settings)
    return settings


def saveLinkImg(img_src,location, dirs, name, nameImg):
    # response = requests.get(f"{img_src}")
    ######################################
    img = urllib.request.urlopen(img_src)
    image = face_recognition.load_image_file(img)
    face_locations = face_recognition.face_locations(image)
    ######################################
    if face_locations != []:

        # save_img = open(f'{dirs}/{location}/{name}/{nameImg}.jpeg', 'wb')
        faceImage = Image.fromarray(image)
        faceImage.save(f'{dirs}/{location}/{name}/{nameImg}.jpeg', 'jpeg')
        # save_img.write(response.content)
        # save_img.close()


def saveBytesImg(img_src,location, dirs, name, nameImg):
    img = img_src.split(',')
    img_b = bytes(img[1],encoding='utf8')
    img = BytesIO(base64.b64decode(img_b))
    image = face_recognition.load_image_file(img)
    face_locations = face_recognition.face_locations(image)
    ######################################
    if face_locations != []:
        faceImage = Image.fromarray(image)
        faceImage.save(f'{dirs}/{location}/{name}/{nameImg}.jpeg', 'jpeg')

    # save_img = open(f'{dirs}/{location}/{name}/{nameImg}.jpeg', 'wb')
    # save_img.write(base64.decodebytes(img_b))
    # save_img.close()

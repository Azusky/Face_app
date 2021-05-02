import json
import requests
import base64

def loadConfig(settings):
    file_settings = open(f'{settings}.json')
    settings = json.load(file_settings)
    return settings


def saveLinkImg(img_src, dirs, name, nameImg):
    response = requests.get(f"{img_src}")
    save_img = open(f'{dirs}/{name}/{nameImg}.jpeg', 'wb')
    save_img.write(response.content)
    save_img.close()


def saveBytesImg(img_src, dirs, name, nameImg):
    img = img_src.split(',')
    img_b = bytes(img[1],encoding='utf8')
    save_img = open(f'{dirs}/{name}/{nameImg}.jpeg', 'wb')
    save_img.write(base64.decodebytes(img_b))
    save_img.close()

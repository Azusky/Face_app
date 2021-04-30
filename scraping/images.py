from os import makedirs, path, walk
import base64
import requests



def saveImage(img_src,name, dirs):

    if not path.exists(f"{dirs}/{name}"):
            makedirs(f'{dirs}/{name}')

    _,_,files = next(walk(f'{dirs}/{name}'))
    if len(files) == 0:
        nameImg = str(0).zfill(4)
    else:
        lastFile = files[-1].split('.')
        newFileName = int(lastFile[0]) + 1
        nameImg = str(newFileName).zfill(4)
        print(nameImg)

    if 'https://' in img_src:

        response = requests.get(f"{img_src}")
        save_img = open(f'{dirs}/{name}/{nameImg}.jpeg', 'wb')
        save_img.write(response.content)
        save_img.close()

    else:
        img = img_src.split(',')
        img_b = bytes(img[1],encoding='utf8')
        save_img = open(f'{dirs}/{name}/{nameImg}.jpeg', 'wb')
        save_img.write(base64.decodebytes(img_b))
        save_img.close()


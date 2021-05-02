from os import makedirs, path, walk
import fs


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
        # print(nameImg)
    if 'https://' in img_src:
        fs.saveLinkImg(img_src, dirs, name, nameImg)

    else:
        fs.saveBytesImg(img_src, dirs, name, nameImg)

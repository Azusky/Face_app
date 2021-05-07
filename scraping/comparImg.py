from PIL import Image
from PIL import ImageChops
from PIL import ImageDraw
from PIL import Image, ImageOps, ImageFilter
import face_recognition
import numpy as np


print('toat'+ 'asdf')

# imageA= Image.open("./images/pasha/WIN_20210505_19_46_53_Pro.jpg")
# imageB= Image.open("./images/pasha/WIN_20210505_19_46_55_Pro.jpg")

# dif = ImageChops.difference(imageB, imageA).getbbox()
# print(dif)
# draw = ImageDraw.Draw(imageB)
# draw.rectangle(dif)
# imageB.show()
# imageB = face_recognition.load_image_file("./images/pasha/WIN_20210505_19_41_58_Pro.jpg")
# imageA = face_recognition.load_image_file("./images/Tanya/0008_copy1.jpeg")
# # image= Image.open("./images/Tanya/0008_copy1.jpeg")
# an_array = np.array(imageA)
# another_array = np.array(imageB)

# if np.array_equal(imageA, imageB):
#     print("|")


# imgs = [imageA,imageB]
# for img in imgs:
#     face_locations = face_recognition.face_locations(img)
#     size = 128


#     for face_location in face_locations:


#         top, right, bottom, left = face_location
#         # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))


#         face_image = img[top:bottom, left:right]
#         pil_image = Image.fromarray(face_image)
#         pil_image = pil_image.filter(ImageFilter.SHARPEN)
#         # pil_image = pil_image.filter(ImageFilter.MinFilter)
#         pil_image = pil_image.resize((size, size), Image.ANTIALIAS)
#         pil_image = ImageOps.grayscale(pil_image)

# # pil_image.show()





# dif = ImageChops.difference(imageB, imageA).getbbox()

# print(dif)
# from PIL import Image
# from PIL import ImageChops
# from PIL import ImageDraw

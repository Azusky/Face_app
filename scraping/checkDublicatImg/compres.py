
from PIL import Image
import PIL
import os
import glob


file_name = '0001.jpeg'
picture = Image.open(f'images/{file_name}')
dim = picture.size
print(f"This is the current width and height of the image: {dim}")
picture.save("images/Compressed_"+file_name,optimize=True, quality=30)

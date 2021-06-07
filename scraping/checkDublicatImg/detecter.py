import os
from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2

image_folder = 'images'
image_files = [_ for _ in os.listdir(image_folder) if _.endswith('jpeg')]


print(image_files)

def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	return err

def compare_images(imageA, imageB):
	img1 = cv2.imread(imageA)
	img2 = cv2.imread(imageB)

	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

	m = mse(img1, img2)
	s = ssim(img1, img2)

	print("MSE: %.2f, SSIM: %.2f" % (m, s))

compare_images("images/0005.jpeg", "images/Compressed_0001.jpeg")

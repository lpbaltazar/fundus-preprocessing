import cv2
import numpy as np
from PIL import Image, ImageOps

file = 'im0001.ppm'
desired_size = (512, 512)

#function that will add padd to image(important for images that are already cropped)
def addPad(file):
	img = Image.open(file)
	img_with_border = ImageOps.expand(img, border = 200, fill = 'black')
	img_with_border.save(file)

#function that opens the image
def openImage(file):
	return cv2.imread(file)

#function that looks for circles in the image. used for cropping the image
def findCircles(img):
	blur = cv2.blur(img, (5,5))
	blurgray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
	circles = cv2.HoughCircles(blurgray, cv2.HOUGH_GRADIENT, dp =1, minDist = 100, param1 = 50, param2= 30, minRadius = 100, maxRadius = 1000)
	circles = np.around(circles)
	center_x = int(circles[0, 0, 0])
	center_y = int(circles[0, 0, 1])
	radius = int(circles[0, 0, 2])
	return center_x, center_y, radius

#function that crops the images
def cropImage(center_x, center_y, r, img):
	x = center_x - r
	y = center_y - r
	h = int(y + r * 2)
	w = int(x + r * 2)
	crop_img = img[y: h, x: w]
	return crop_img

#function that resizes the images
def resizeImage(crop_img, desired_size):
	res_img = cv2.resize(crop_img, (desired_size[0], desired_size[0]))
	return res_img

pad = addPad(file)
img = openImage(file)
a, b, c = findCircles(img)
crop = cropImage(a, b, c, img)
res = resizeImage(crop, desired_size)

cv2.imshow('resized', res)
cv2.waitKey(0)
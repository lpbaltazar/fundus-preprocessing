import cv2
import numpy as np

file = '20051019_38557_0100_PP.tif'

def openImage(file):
	return cv2.imread(file)

def findCircles(img):
	blur = cv2.blur(img, (5,5))
	blurgray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
	circles = cv2.HoughCircles(blurgray, cv2.HOUGH_GRADIENT, dp =1, minDist = 100, param1 = 50, param2= 30, minRadius = 100, maxRadius = 1000)
	circles = np.around(circles)
	center_x = int(circles[0, 0, 0])
	center_y = int(circles[0, 0, 1])
	radius = int(circles[0, 0, 2])
	return center_x, center_y, radius

def cropImage(center_x, center_y, r, img):
	x = center_x - r
	y = center_y - r
	h = int(y + r * 2)
	w = int(x + r * 2)
	crop_img = img[y: h, x: w]
	return crop_img

def resizeImage(crop_img):
	res_img = cv2.resize(crop_img, (512, 512))
	return res_img

img = openImage(file)
a, b, c = findCircles(img)
crop = cropImage(a, b, c, img)
res = resizeImage(crop)

cv2.imshow('resized', res)
cv2.waitKey(0)
import cv2
import numpy as np
from PIL import Image, ImageOps

#function that opens the image
def openImage(file):
	return cv2.imread(file)

#function that looks for circles in the image. used for cropping the image
def findCircles(img, size, n):
	h, w = img.shape[:2]
	size = 512
	helper = h / size
	s_h = h / helper
	s_w = w / helper
	s_img = cv2.resize(img, (int(s_w), int(s_h)))
	ret, thresh = cv2.threshold(s_img, 10, 150, cv2.THRESH_BINARY)

	gray = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
	gray = cv2.medianBlur(gray, 5)
	
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp =1 , minDist = 20, param1 = 100, param2= 20, minRadius = (int(s_h / 2.05)), maxRadius = (int(s_h / 2) + int(s_h * 0.03)))
	type_c = 0
	
	if circles is None:
		circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp = 1,minDist = 20, param1=100, param2=20, minRadius= (int(s_h/2.25)), maxRadius=(int(s_w)))
		type_c = 1
	
	if circles is None:
		circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp = 1,minDist = 20, param1=100, param2=20, minRadius= (int(s_h/2.25)), maxRadius=(int(s_h/2)-int(s_h*0.015)))
		type_c = 2
	
	mes = 0
	if circles is None:
		print('Cant find circles in image: ', n)
		mes = 1
		c_x = 0
		c_y=0
		r=0
		return c_x, c_y, r, type_c, mes
	else:
		circles = np.uint16(np.around(circles))
		rad = 0.0
		for i in circles[0, :]:
			if i[2] > rad:
				rad = i[2]
				circle = i
		c_x = int((circle[0]/s_w)*w)
		c_y = int((circle[1]/s_h)*h)
		r = int(circle[2]*helper)

		return c_x, c_y, r, type_c, mes

#function that crops the images
def cropImage(img, n):
	center_x, center_y, r, type_c, mes = findCircles(img, 512, n)
	if mes == 1:
		return img, mes
	if type_c == 1 or type_c == 0:
		y = 0
	else:
		y = center_y -r 

	x = (center_x - r) - 100
	if x <= 0:
		x = 0
	h = int(y + r * 2) + 200
	w = int(x + r * 2) + 200
	crop_img = img[y: h, x: w]

	if type_c == 1:
		crop_img = padToSquare(crop_img)
	return crop_img, mes

def padToSquare(img):
	w, l = img.shape[:2]
	if (w<l):
		border = int((l-w)/2.0)
		pad_img = cv2.copyMakeBorder(img, top = border, bottom = border, left = 0, right = 0, borderType = cv2.BORDER_CONSTANT, value = [0, 0, 0])
	else:
		border = int((w-l) / 2.0)
		pad_img = cv2.copyMakeBorder(img, top = border, bottom = border, left = 0, right = 0, borderType = cv2.BORDER_CONSTANT, value = [0, 0, 0])

	return pad_img

#function that resizes the images
def resizeImage(crop_img, desired_size):
	res_img = cv2.resize(crop_img, (desired_size[0], desired_size[0]))
	return res_img


import cv2
import numpy as np
from PIL import Image, ImageOps

def openImage(file):
	'''
	This function reads the image.
	'''
	return cv2.imread(file)

#function that looks for circles in the image. used for cropping the image
def findCircles(img, size, n):
	'''
	This function looks for circles in the fundus images to be used for cropping of the images. It returns center_x, center_y, radius and message
	type_c is the type of the circle
		0 - Circle diameter is almost same with the image height
		1 - Circle diameter is bigger than the image height
		2 - Circle diameter is smaller than the image height 
	mes returns a message wether a circle is found or not (0 - circle found, 1 - circle not found)
	'''
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

def cropImage(img, n):
	'''
	Crops the images by locating the center from the function find circles and crop the images according to the center and radius.
	If mes = 1 it returns the original image and the message
	If mes = 0 it crops the images and return the original image
	'''
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
	'''
	This function pads the image into a square.
	'''
	w, l = img.shape[:2]
	if (w<l):
		border = int((l-w)/2.0)
		pad_img = cv2.copyMakeBorder(img, top = border, bottom = border, left = 0, right = 0, borderType = cv2.BORDER_CONSTANT, value = [0, 0, 0])
	else:
		border = int((w-l) / 2.0)
		pad_img = cv2.copyMakeBorder(img, top = border, bottom = border, left = 0, right = 0, borderType = cv2.BORDER_CONSTANT, value = [0, 0, 0])

	return pad_img

def cropImageSameHeight(img, f):
	'''
	This function is used when the function findCircles failed to find any circles from the fundus images.
	It crops the images by using the height/2 as its radius
	'''
	h, w = img.shape[:2]
	border = abs(int(w / 2.0) - h / 2)
	img = cv2.copyMakeBorder(img, top = int(border), bottom = int(border), left = 0, right = 0, borderType = cv2.BORDER_CONSTANT, value = [0, 0, 0])
	h, w = img.shape[:2]
	center_x = int(w / 2)
	center_y = int(h / 2)
	r = int(w / 2)

	y = (center_y - r)
	if y <= 0:
		y = 0
	x = (center_x - r)
	h = int(y + (r * 2))
	w = int(x + (r * 2))
	crop_img = img[y: h, x : w]
	return crop_img


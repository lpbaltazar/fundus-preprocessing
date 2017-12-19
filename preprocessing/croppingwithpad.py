import cv2
import numpy as np
from PIL import Image, ImageOps


#function that will add padd to image(important for images that are already cropped)
def addPad(file):
	img = Image.open(file)
	#adds border to the image
	img_with_border = ImageOps.expand(img, border = 200, fill = 'black')
	img_with_border.save("{0}.jpg".format(file+"_pad"))

#function that opens the image
def openImage(file):
	return cv2.imread(file)

#function that looks for circles in the image. used for cropping the image
def findCircles(img, minr, maxr):
	#blurs the image to reduce noise
	blur = cv2.blur(img, (5,5))
	#convert image to gray
	blurgray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
	#detects the circles in the images
	circles = cv2.HoughCircles(blurgray, cv2.HOUGH_GRADIENT, dp =1, minDist = 100, param1 = 50, param2= 30, minRadius = minr, maxRadius = maxr)
	circles = np.around(circles)
	#returns the center x and y coordinates and the radius
	center_x = int(circles[0, 0, 0])
	center_y = int(circles[0, 0, 1])
	radius = int(circles[0, 0, 2])
	return center_x, center_y, radius

#function that crops the images
def cropImage(img, minr, maxr):
	center_x, center_y, r = findCircles(img, minr, maxr)
	x = (center_x - r) - 100
	y = (center_y - r) - 100
	h = int(y + r * 2) + 200
	w = int(x + r * 2) + 200
	crop_img = img[y: h, x: w]
	return crop_img

#function that resizes the images
def resizeImage(crop_img, desired_size):
	res_img = cv2.resize(crop_img, (desired_size[0], desired_size[0]))
	return res_img


import cv2
import numpy as np
import imutils

angle_range = 360

def rotate_image(img_obj):
	rows, cols, ch = img_obj.shape
	angle_rotation = np.random.uniform(angle_range)-angle_range/2
	dst = imutils.rotate_bound(image, angle_rotation)
	return dst

def flipImage(img):
	flip_prob = np.random.uniform(0, 1)
	if flip_prob < 0.25:
		#does nothing to the image
		flipped_img = img
	elif flip_prob < 0.50:
		#flips image horizontally
		flipped_img = cv2.flip(img, 0)
	elif flip_prob < 0.75:
		#flips image vertically
		flipped_img = cv2.flip(img, 1)
	else:
		#flips image both horizontally and vertically
		flipped_img = cv2.flip(img, -1)

	return flipped_img

import cv2
import numpy as np

angle_range = 360

def rotate_image(img_obj):
	rows, cols, ch = img_obj.shape
	angle_rotation = np.random.uniform(angle_range)-angle_range/2
	rot_matrix = cv2.getRotationMatrix2D((rows/2,cols/2), angle_rotation, 1)
	dst = cv2.warpAffine(img_obj, rot_matrix, (rows, cols))
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

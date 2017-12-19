import cv2
import numpy as np
import csv
import glob

cv_img =[]
i = 0

angle_range = 360

def rotate_image(img_obj, rows, cols):
	angle_rotation = np.random.uniform(angle_range)-angle_range/2
	rot_matrix = cv2.getRotationMatrix2D((rows/2,cols/2), angle_rotation, 1)
	dst = cv2.warpAffine(img_obj, rot_matrix, (rows, cols))
	return dst

for img in glob.glob('C:\Users\User\Desktop\SCRIPTS\IMAGES\*.jpg'):
	n = cv2.imread(img)
	rows, cols, ch = n.shape
	rotated_img = rotate_image(n, rows, cols)
	cv2.imwrite('image{:>05}.jpg'.format(i), rotated_img)
	cv_img.append(rotated_img)
	i = i + 1


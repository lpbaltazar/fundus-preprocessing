import cv2
import numpy as np

angle_range = 360

def rotate_image(img_obj):
	rows, cols, ch = img_obj.shape
	angle_rotation = np.random.uniform(angle_range)-angle_range/2
	rot_matrix = cv2.getRotationMatrix2D((rows/2,cols/2), angle_rotation, 1)
	dst = cv2.warpAffine(img_obj, rot_matrix, (rows, cols))
	return dst



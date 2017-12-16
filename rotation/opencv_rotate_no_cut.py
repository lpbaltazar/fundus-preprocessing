import cv2
import numpy as np
from PIL import Image


img = cv2.imread("image001res.png")

def rotate_bound(img, angle):
	height, width = img.shape[:2]
	center_x, center_y = (width // 2, height //2)

	M = cv2.getRotationMatrix2D((center_x,center_y), -angle, 1.0)
	cos = np.abs(M[0,0])
	sin = np.abs(M[0,1])

	new_width = int((height * sin) + (width * cos))
	new_height = int((height * cos) + (width * sin))

	M[0, 2] += (new_width / 2) - center_x
	M[1, 2] += (new_height / 2) - center_y

	return cv2.warpAffine(img, M, (new_width, new_height)) 

for angle in np.arange(0, 360, 15):
	rotated = rotate_bound(img, angle)
	cv2.imshow("Rotated (problmatic)", rotated)
	cv2.waitKey(0)
import cv2
import numpy as np

def openImage(file):
	return cv2.imread(file)

#function for brightness adjustment
def brightnessAdjustment(image):
	imghsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
	random_brightnes = 1 + np.random.uniform(-0.3, 0.3)
	# catches if random_brightnes value is greater than or equal to 1.17
	while random_brightnes >= 1.0:
		random_brightnes = 1 + np.random.uniform(-0.3, 0.3)
	imghsv[:,:,2] = imghsv[:,:,2]*random_brightnes
	imgrgb = cv2.cvtColor(imghsv, cv2.COLOR_HSV2RGB)
	return imgrgb

#function for contrast adjustment
def contrastAdjustment(image):
	imghsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
	random_contrast = np.random.uniform(-0.2, 0.2)
	imghsv[:,:,1] = imghsv[:,:,1] * random_contrast
	imgrgb = cv2.cvtColor(imghsv,cv2.COLOR_HSV2RGB)
	return imgrgb
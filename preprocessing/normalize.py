import cv2
import numpy as np
import csv

img_obj = cv2.imread('image.jpg')
i = 0


#Function for normalizing RGB image
#Output is 3 array corresponding to the normalized channels (RGB channels) of the image
def normalize_image(img_obj):
	rows, cols, ch = img_obj.shape
	#Make dummy array for future storage of each RGB channels
	norm_rchannel = np.zeros((rows, cols), np.float32)
	norm_gchannel = np.zeros((rows, cols), np.float32)
	norm_bchannel = np.zeros((rows, cols), np.float32)

	#Load RGB values to the dummy array
	rchannel = img_obj [:, :, 0].astype(float)
	gchannel = img_obj [:, :, 1].astype(float)
	bchannel = img_obj [:, :, 2].astype(float)

	#Get sum of all the pixel values for each channels
	summ = np.sum(rchannel) + np.sum(gchannel) + np.sum(bchannel)
	float(summ)

	#Normalize image pixel values for each channels
	norm_rchannel = rchannel / summ
	norm_gchannel = gchannel / summ
	norm_bchannel = bchannel / summ 
	return norm_rchannel, norm_gchannel, norm_bchannel

#Function for writing output to a csv file
#This functions creates 3  csv files containing pixel values for each RGB channels
def write_to_file(r, g, b, i):
	channels = {'rchannel': r, 'gchannel': g, 'bchannel': b}
	for filename, value in channels.items():
		img_filename = (filename + '{:>05}' + '.csv').format(i)
		np.savetxt(img_filename, value, delimiter=',')
		print('Print Done!')


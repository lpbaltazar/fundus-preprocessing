import os
import cv2
import numpy as np
import csv
from preprocessing import croppingwithpad

ROOT_PATH = "/Users/lpbaltazar/workspace/fundus-preprocessing/"
train_data_directory = os.path.join(ROOT_PATH, "train_002")
target_dir = '/Users/lpbaltazar/workspace/fundus-preprocessing/output_images/with_circles/'
target_dir2 = '/Users/lpbaltazar/workspace/fundus-preprocessing/output_images/no_circles/'
no_circles = []

def loadData(data_directory):
	for f in os.listdir(data_directory):
		file_names = os.path.join(data_directory, f)
		if file_names.endswith('.jpeg'):
			img = cv2.imread(file_names)
			crop, mes = croppingwithpad.cropImage(img, f)
			if mes == 1:
				no_circles.append(f)
				crop_no_circles = croppingwithpad.cropImageSameHeight(img, f)
				res = cv2.resize(crop_no_circles, (512, 512))
				cv2.imwrite(target_dir2 + f, res)
			if mes == 0:
				res = cv2.resize(crop, (512, 512))
				cv2.imwrite(target_dir + f , res)
	np.savetxt('no_circles.txt', no_circles, delimiter = ",", fmt = "%s" )     


loadData(train_data_directory)

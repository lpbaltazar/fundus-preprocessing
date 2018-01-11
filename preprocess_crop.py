from brightness_contrast import adjustment
from preprocessing import croppingwithpad
import glob
import shutil
import os
import cv2
import numpy as np

location = '/Users/lpbaltazar/workspace/kaggle-data/train'
file_type = '.jpeg'
target_dir = '/Users/lpbaltazar/workspace/fundus-preprocessing/output_images/'
i=0
no_circles = []
for n in glob.glob(location+'/*'+file_type):
	img = adjustment.openImage(n)
	crop, mes = croppingwithpad.cropImage(img, n)
	if mes == 1:
		no_circles.append(n)
	if mes == 0:
		res = cv2.resize(crop, (512, 512))
		cv2.imwrite(target_dir + 'image{:>05}.jpg'.format(i), res)
		i = i+1

np.savetxt('no_circles.txt', no_circles, delimeter = ",", fmt = "%s" )
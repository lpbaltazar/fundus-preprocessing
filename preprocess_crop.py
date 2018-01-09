from brightness_contrast import adjustment
from preprocessing import croppingwithpad
import glob
import shutil
import os
import cv2

location = '/Users/lpbaltazar/workspace/kaggle-data/train'
file_type = '.jpeg'
target_dir = '/Users/lpbaltazar/workspace/fundus-preprocessing/output_images/'
i=0
for n in glob.glob(location+'/*'+file_type):
	img = adjustment.openImage(n)
	crop, mes = croppingwithpad.cropImage(img, n)
	#rot = rotate_image(crop, angle)
	if mes == 0:
		res = cv2.resize(crop, (512, 512))
		cv2.imwrite(target_dir + 'image{:>05}.jpg'.format(i), res)
		i = i+1
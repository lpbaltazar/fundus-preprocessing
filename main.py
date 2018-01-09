from brightness_contrast import adjustment
from preprocessing import croppingwithpad
from preprocessing import normalize
from rotation import image_rotation
from move_to_folder import move_files, move_images
import cv2
import glob
import csv
import shutil
import os

location = '/Users/lpbaltazar/workspace/kaggle-data/train'
file_type = '.jpeg'
target_dir = '/Users/lpbaltazar/workspace/fundus-preprocessing/output_images/'

desired_size = (512, 512)
#adjust depending on the size of the image

i = 0

for img in glob.glob(location+'/*'+file_type):
	n = adjustment.openImage(img)
	rotated_img = image_rotation.rotate_image(n)
	flipped_img = image_rotation.flipImage(rotated_img)
	bright_img = adjustment.brightnessAdjustment(flipped_img)
	contrast_img = adjustment.contrastAdjustment(bright_img)
	crop_img, mes = croppingwithpad.cropImage(contrast_img, n)
	if mes == 0:
		res = cv2.resize(crop_img, (512, 512))
		cv2.imwrite(target_dir + 'image{:>05}.jpg'.format(i), res)
		i = i+1

move_files.moveCSVFiles()
print("Done!")
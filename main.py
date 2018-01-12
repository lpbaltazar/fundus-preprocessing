import cv2
import glob
import csv
import shutil
import os

from brightness_contrast import adjustment
from preprocessing import croppingwithpad
from preprocessing import normalize
from rotation import image_rotation
from move_to_folder import move_files, move_images

ROOT_PATH = "/Users/joverlyngaudillo/Desktop/local-codes/preprocess/"
train_data_directory = os.path.join(ROOT_PATH, "TRAINDATA")
target_dir = '/Users/joverlyngaudillo/Desktop/local-codes/INPUT_IMAGES/'

desired_size = (512, 512)
#adjust depending on the size of the image

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
				#cv2.imwrite(target_dir2 + f, res)
			if mes == 0:
				res = cv2.resize(crop, (512, 512))
				#cv2.imwrite(target_dir + f , res)
			rot = rotation.image_rotation(res)
			flip = rotation.flipImage(rot)
			bright = adjustment.brightnessAdjustment(flip)
			contrast = adjustment.contrastAdjustment(bright)
			cv2.imwrite(target_dir + f, contrast)

	np.savetxt('no_circles.txt', no_circles, delimiter = ",", fmt = "%s" )     

loadData(train_data_directory)
move_files.moveCSVFiles()
print("Done!")
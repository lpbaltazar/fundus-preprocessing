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
        img = cv2.imread(file_names)

        rotated_img = image_rotation.rotate_image(n)
		flipped_img = image_rotation.flipImage(rotated_img)
		bright_img = adjustment.brightnessAdjustment(flipped_img)
		contrast_img = adjustment.contrastAdjustment(bright_img)
		crop_img, mes = croppingwithpad.cropImage(contrast_img, n)
		if mes == 0:
			res = cv2.resize(crop_img, (512, 512))
			cv2.imwrite(target_dir + f + '.jpg', res)
			i = i+1

move_files.moveCSVFiles()
print("Done!")
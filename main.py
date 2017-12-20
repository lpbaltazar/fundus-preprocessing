from brightness_contrast import adjustment
from preprocessing import croppingWithPad, normalize
from rotation import image_rotation
from move_to_folder import move_files, move_images
import cv2
import glob
import csv
import shutil
import os

desired_size = (512, 512)
#adjust depending on the size of the image
minRadius = 1000
maxRadius = 2000
i = 0

for img in glob.glob('C:\Users\User\Desktop\\fundus-preprocessing\IMAGES\*.jpg'):
	croppingWithPad.addPad(img)
	n = adjustment.openImage(img+"_pad"+".jpg")
	rotated_img = image_rotation.rotate_image(n)
	bright_img = adjustment.brightnessAdjustment(rotated_img)
	contrast_img = adjustment.contrastAdjustment(bright_img)
	crop_img = croppingWithPad.cropImage(contrast_img, minRadius, maxRadius)
	resize_img = croppingWithPad.resizeImage(crop_img, desired_size)
	norm_r, norm_g, norm_b = normalize.normalize_image(resize_img)
	normalize.write_to_file(norm_r, norm_g, norm_r, i)
	cv2.imwrite('image{:>05}.jpg'.format(i), resize_img)
	i = i + 1

move_files.moveCSVFiles()
move_images.moveImages()

print("Done!")
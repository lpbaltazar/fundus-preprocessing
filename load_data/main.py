# Import modules for python
import os
import cv2
import numpy as np

# Import functions from another file
import utils

""" This is where we execute functions we created 
	from another files

	ROOTH_PATH = the directory of this project
"""
ROOT_PATH = "/Users/joverlyngaudillo/Desktop/diabetic-retinopathy"
train_data_directory = os.path.join(ROOT_PATH, "INPUTDATA")
#test_data_directory = os.path.join(ROOT_PATHc, "testing_dataset_dir")

# This line calls the function loadData from utils.py
# and executes loading of data
images, labels = utils.loadData(train_data_directory)

print(images[1400], labels[1400])
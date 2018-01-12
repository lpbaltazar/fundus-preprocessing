import os
import skimage.data
import skimage.io
import numpy as np
import cv2

from preprocessing import croppingwithpad

ROOT_PATH = "/Users/joverlyngaudillo/Desktop/local-codes/preprocess/"
train_data_directory = os.path.join(ROOT_PATH, "TRAINDATA")
target_dir = '/Users/joverlyngaudillo/Desktop/local-codes/INPUT_IMAGES/'

def loadData(data_directory):
    for f in os.listdir(data_directory):
        file_names = os.path.join(data_directory, f)
        img = cv2.imread(file_names)

        crop, mes = croppingwithpad.cropImage(img, n)

        if mes == 0:
            res = cv2.resize(crop, (512, 512))
            cv2.imwrite(target_dir + f , res)

loadData(train_data_directory)
            
   
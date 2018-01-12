import os
import cv2
import numpy as np

def loadData(data_directory):
    """ This function loads data from data_directory.

    Arguments:
            data_directory = the directory where you saved your data

    Requirements:
            > Calling this function requires that your images are saved
                to a directory named after the labels (0, 1, 2, 3, 4) 
                of the images 
            > You can do this by implementing the script inside the 
                arrange_data directory

    Returns: 
            images = list that contains array of image pixels
            labels = array that contains labels of images

    """
    # Iterates over the sub-directories inside the INPUTDATA directory
    directories = [d for d in os.listdir(data_directory) 
                   if os.path.isdir(os.path.join(data_directory, d))]

    # Initialize variables to be filled later
    labels = []
    images = []

    # Iterates over each sub-directories   
    for d in directories:
        # Full path to a sub-directory
        label_directory = os.path.join(data_directory, d)

        # List of path of images inside a sub-directory
        image_directory = [os.path.join(label_directory, f) 
                            for f in os.listdir(label_directory) 
                            if f.endswith(".jpeg")]

        # Iterates over the image paths
        for f in image_directory:
            # Reads the image
            img = cv2.imread(f)
            # Store image information to images variable
            images.append(img)
            # Store label to labels
            labels.append(int(d))
    return images, labels
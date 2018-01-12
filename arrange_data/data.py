# Import needed modules
import csv
import shutil
import os

# Initiliaze variables to be filled later
image_filename = []
image_class = []

def load_labels(filename):
	""" This function loads the labels from the trainLabels.csv.

	Arguments:
			filename = name of the csv file (trainLabels.csv)

	Returns: 
			image_filename = list of the filenames of all the images in the dataset directory
			labels = list of the labels of all the the images
	"""
	with open (filename, 'r') as csvfile:
		file_reader = csv.reader(csvfile, delimiter = ',')
		for row in file_reader:
			a = row[0]
			b = row[1]
			image_filename.append(a)
			image_class.append(b)

	return image_filename, image_class

def moveImages(img_class, img_name):
	""" This function moves images to a directory named after their corresponding class.
		Calling this function will arrange your images according to their class.

	Arguments:
			img_class = class of the image
			img_name = filename of the image

	Requirements:
			> Make a directory inside your project directory with the name INPUTDATA
			> Inside this directory, make five directories with names 0, 1, 2, 3, 4, respectively

	Returns: None
	"""
	source = '/Users/joverlyngaudillo/Desktop/diabetic-retinopathy/INPUTDATA'
	img_path = os.path.join(source, img_name)

	destination_root_path = "/Users/joverlyngaudillo/Desktop/diabetic-retinopathy/INPUTDATA"
	destination = os.path.join(destination_root_path,img_class)

	if img_name.endswith('.jpeg'):
		shutil.move(img_path, destination)
		print('Image %s' % img_name, 'successfully moved!')
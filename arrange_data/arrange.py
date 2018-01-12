import os

import data

filename = 'trainLabels.csv'

# ROOT_PATH is the path of your python project.
ROOT_PATH = "/Users/joverlyngaudillo/Desktop/diabetic-retinopathy"

# data_directory is the full path of your dataset
data_directory = os.path.join(ROOT_PATH, "INPUTDATA")

# Fills the image_filenames and image_classes lists by 
# calling the function load_labels() from data.py
image_filenames, image_classes = data.load_labels(filename)

# Iterates over the INPUTDATA directory
for f in os.listdir(data_directory):
	# Filters the content of the data_directory by choosing
	# files that with .jpeg format
	if f.endswith('.jpeg'):

		# file_names is a list paths of classes directories
		file_names = os.path.join(data_directory,f)

		img = f.replace('.jpeg', '')

		# Iterates over the image_filenames lists
		for name in image_filenames:
			if img == name:
				break

		# Gets the index of the image if matched
		index = image_filenames.index(name)		
		# Gets the class of the image
		img_class = image_classes[index]

		print('Filename:', name)
		print('Image Class:', img_class)
		
		# Moves the images to a directory that is named after their class
		# by calling the funtion moveImages() from data.py
		data.moveImages(img_class, name + '.jpeg')

		print('')

		



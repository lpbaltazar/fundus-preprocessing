import csv
import shutil
import os

image_filename = []
image_class = []

def load_labels(filename):
	with open (filename, 'r') as csvfile:
		file_reader = csv.reader(csvfile, delimiter = ',')
		for row in file_reader:
			a = row[0]
			b = row[1]
			image_filename.append(a)
			image_class.append(b)

	return image_filename, image_class

def moveImages(img_class, img_name):
	source = '/Users/joverlyngaudillo/Desktop/diabetic-retinopathy/INPUTDATA'
	img_path = os.path.join(source, img_name)

	destination_root_path = "/Users/joverlyngaudillo/Desktop/diabetic-retinopathy/INPUTDATA"
	destination = os.path.join(destination_root_path,img_class)

	if img_name.endswith('.jpeg'):
		shutil.move(img_path, destination)
		print('Image %s' % img_name, 'successfully moved!')
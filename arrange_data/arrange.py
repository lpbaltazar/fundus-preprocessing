import os

import data

filename = 'trainLabels.csv'

ROOT_PATH = "/Users/joverlyngaudillo/Desktop/diabetic-retinopathy"
data_directory = os.path.join(ROOT_PATH, "INPUTDATA")

image_filenames, image_classes = data.load_labels(filename)

for f in os.listdir(data_directory):
	if f.endswith('.jpeg'):
		file_names = os.path.join(data_directory,f)

		img = f.replace('.jpeg', '')

		for name in image_filenames:
			if img == name:
				break

		index = image_filenames.index(name)		
		img_class = image_classes[index]

		print('Filename:', name)
		print('Image Class:', img_class)
		
		data.moveImages(img_class, name + '.jpeg')

		print('')

		



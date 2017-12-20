import shutil
import os

def moveImages():
	source = os.listdir('C:\Users\User\Desktop\\fundus-preprocessing')
	destination = "C:\Users\User\Desktop\\fundus-preprocessing\output_images"

	for files in source:
		if files.endswith('.jpg'):
			shutil.move(files, destination)
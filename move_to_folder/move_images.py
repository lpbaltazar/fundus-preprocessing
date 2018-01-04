import shutil
import os

def moveImages():
	source = os.listdir('/Users/joverlyngaudillo/Documents/workspace/fundus-preprocessing')
	destination = "/Users/joverlyngaudillo/Documents/workspace/fundus-preprocessing/output_images"

	for files in source:
		if files.endswith('.jpg'):
			shutil.move(files, destination)
import shutil
import os

def moveCSVFiles():
	source = os.listdir('/Users/joverlyngaudillo/Documents/workspace/fundus-preprocessing')
	destination = "/Users/joverlyngaudillo/Documents/workspace/fundus-preprocessing/output_files"

	for files in source:
		if files.endswith('.csv'):
			shutil.move(files, destination)
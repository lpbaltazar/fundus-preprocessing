import shutil
import os

def moveCSVFiles():
	source = os.listdir('C:\Users\User\Desktop\\fundus-preprocessing')
	destination = "C:\Users\User\Desktop\\fundus-preprocessing\output_files"

	for files in source:
		if files.endswith('.csv'):
			shutil.move(files, destination)
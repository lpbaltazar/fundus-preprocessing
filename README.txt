Requirements:
	OpenCV
	Python 3.6
	Imutils
	Numpy
	
This is a python script for the preprocessing of the fundus images.
It includes the following operations:
	* Rotation
	* Flipping
	* Brightness Adjustment
	* Contrast Adjustment
	* Cropping
	* Resizing to 512 x 512 pixels

To use the script, run main.py.
	Variables:
		* location  	--> directory that contains the image to be preprocessed
		* file_type 	--> file type of the image. Can be .tif, .jpg, .ppm, .png
		* desired_size 	--> output size desired
		* minRadius	--> minimum radius of the circle. Adjust depending on the size of the image
		* maxRadius	--> maximum radius of the circle. Adjust depending on the size of the image

Output file of the image is JPEG

Change the directory of the output folders in the files:
	*move_images.py
	*move_files.py

!! Need to create the following folder to the fundus-preprocessing directory:
	* output_files
	* output_images
	
Images are saved to a separate folder: output_images
CSV files for the rgb values are saved to a separate folder: output_files

FILE: preprocess_crop.py
Crops the images and resize it 512 x 512.
Change the variables location and target_dir according to your machine.
Also returns if it cant find circle in image.
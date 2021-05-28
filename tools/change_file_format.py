import os
import cv2 as cv

working_dir = os.getcwd()
ppm_files = [each for each in os.listdir(working_dir) if each.endswith('.ppm')]

for image in ppm_files:
    i = cv.imread(image)    
    image_without_extension = image[:-4]
    cv.imwrite(f"{image_without_extension}.jpg", i)
    os.remove(image)
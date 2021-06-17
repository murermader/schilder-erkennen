import cv2 as cv
import os
import time
import sys
from mss import mss
from vision import Vision

# Generierte XML laden
cascade_geschwindigkeit = cv.CascadeClassifier("../training/GTRSB/Geschwindigkeit_30_00001/cascade_4/cascade.xml")
vision_geschwindigkeit = Vision(None)

image = cv.imread(sys.argv[1])
rectangles = cascade_geschwindigkeit.detectMultiScale(image, minNeighbors=3)
image_with_rectangles = vision_geschwindigkeit.draw_rectangles(image, rectangles)

cv.imshow("Cascade Classifier", image_with_rectangles)

cv.imwrite("result.JPEG", image_with_rectangles)

while(True):
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
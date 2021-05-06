import cv2 as cv
import os
from mss import mss
import time
from vision import Vision

# Generierte XML laden
cascade_geschwindigkeit = cv.CascadeClassifier("../training/geschwindigkeit/cascade/cascade.xml")
vision_geschwindigkeit = Vision(None)

with mss() as sct:
    # Screenshot machen und den Pfad speichern
    screenshot_path = sct.shot()

    # Screenshot als Bild einlesen
    screenshot = cv.imread(screenshot_path)
    
    # Objekterkennung durchführen
    rectangles = cascade_geschwindigkeit.detectMultiScale(screenshot, minNeighbors=3)

    screenshot_with_rectangles = vision_geschwindigkeit.draw_rectangles(screenshot, rectangles)

    cv.imshow("Bildschirm", screenshot_with_rectangles)

    while(True):
        key = cv.waitKey(1)
        if key == ord('q'):
            cv.destroyAllWindows()
            break
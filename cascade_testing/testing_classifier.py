import cv2 as cv
import os
import time
import sys
from mss import mss
from vision import Vision

# Generierte XML laden
cascade_geschwindigkeit = cv.CascadeClassifier("../training/geschwindigkeit/cascade/cascade.xml")
cascade_stop = cv.CascadeClassifier("cascade_stopsign.xml")
vision_geschwindigkeit = Vision(None)

with mss() as sct:
    # In das Verzeichnis des Skripts wechseln, damit der Screenshot mit einem
    # relativen Pfad gefunden werden kann
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Screenshot machen und den Pfad speichern
    screenshot_filename = sct.shot()

    # Screenshot als Bild einlesen
    screenshot = cv.imread(screenshot_filename)

    rectangles = []
    try:
        # Objekterkennung durchführen
        rectangles = cascade_geschwindigkeit.detectMultiScale(screenshot, minNeighbors=3)
        # rectangles = cascade_stop.detectMultiScale(screenshot, minNeighbors=3)
    except:
        print("Aus irgendeinem Grund funktioniert diese Methode nur, wenn man sich im selben Verzeichnis befindet")
        sys.exit(-1)

    screenshot_with_rectangles = vision_geschwindigkeit.draw_rectangles(screenshot, rectangles)

    cv.imshow("Bildschirm", screenshot_with_rectangles)

    while(True):
        key = cv.waitKey(1)
        if key == ord('q'):
            cv.destroyAllWindows()
            break
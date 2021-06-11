import sys
import os
import csv
from PIL import Image

# Ergebnis: Min-Width für alle Bilder ist 15|15 -> Suchfenster muss mindestens 15x15 sein, um alle
# alle Schilder erkennen zu können

csv_file = sys.argv[1]
min_width = 1000
min_height = 1000

with open(csv_file) as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=";")
    
    # Erste Zeile überspringen
    next(csvReader)
    
    with open("pos.txt", "a") as file:
        for row in csvReader:
            filename = row[0][:-4]
            x1 = int(row[3])
            y1 = int(row[4])
            x2 = int(row[5])
            y2 = int(row[6])

            width = x2 - x1
            height = y2 - y1

            min_width = min(min_width, width)
            min_height = min(min_height, height)
            
    print("Kleinste Breite: " + str(min_width))
    print("Kleinste Höhe: " + str(min_height))
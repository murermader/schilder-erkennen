import csv
import os

try:
    os.remove("pos.txt")
except:
    print("pos.txt existiert noch nicht")


with open("GT-00014.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=";")
    
    # Erste Zeile überspringen
    next(csvReader)
    
    with open("pos.txt", "a") as file:
        for row in csvReader:
            filename = row[0][:-4]
            x1 = row[3]
            y1 = row[4]
            x2 = row[5]
            y2 = row[6]
            
            file.write(f"positives/{filename}.jpg 1 {x1} {y1} {x2} {y2} \n")
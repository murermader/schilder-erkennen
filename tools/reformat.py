import csv
import os

try:
    os.remove("pos.txt")
except:
    print("pos.txt existiert noch nicht")

working_dir = os.getcwd()
csv_file = [each for each in os.listdir(working_dir) if each.endswith('.csv')][0]

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
            
            file.write(f"positives/{filename}.jpg 1 {x1} {y1} {width} {height} \n")
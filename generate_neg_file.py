#!/usr/bin/python
import sys
import os
from pathlib import Path

def main():
    args = sys.argv

    if len(args) == 1:
        # Erstes Argumetn ist immer der Pfad zum Skript
        print("Bitte geben Sie den Pfad zu einem Verzeichnis an.")
        sys.exit(-1)

    dir = args[1]
    
    if dir == "--help" or dir == "-h" or dir == "/?":
        print("Bitte geben Sie den Pfad zu einem Verzeichnis an.")
        sys.exit(-1)

    if not os.path.isdir(dir):
        print("Bitte geben sie dem Pfad zu einem Verzeichnis an.")
        sys.exit(-1)
    
    parent_dir = Path(dir).parent
    images_dir_name = Path(dir).parts[-1]

    # Wir wechseln in das Verzeichnis direkt über den Trainingsdaten, damit wir ab sofort
    # mit relativen Pfaden arbeiten können.
    os.chdir(parent_dir)

    # Datei erst entfernen, bevor wir eine neue anlegen
    os.remove("neg.txt")
    neg_file = open("neg.txt", "a")

    for file in os.listdir(images_dir_name):
        neg_file.write(f"{images_dir_name}/{file} \n")

    print("neg.txt erstellt.")

if __name__ == "__main__":
	main()
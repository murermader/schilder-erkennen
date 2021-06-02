import sys
import os
from PIL import Image

def main():

    try:
        pos_file = sys.argv[1]
    except:
        print("Kein Pfad zu pos.txt gegeben")
        sys.exit(-1)
    
    if not os.path.isfile(pos_file):
        print("Gegebener Pfad ist keine Datei")
        sys.exit(-1)
    
    # CWD zum Verzeichnis von pos.txt wechseln
    dir_path = os.path.dirname(os.path.realpath(pos_file))
    pos_filename = os.path.basename(pos_file)
    os.chdir(dir_path)

    with open(pos_filename) as file:
        for line in file.readlines():

            # Dateiformat: positives/00045_00005.jpg 1 5 6 39 40
            line_info = line.split()

            img_path = line_info[0]
            rect_count = int(line_info[1])
            x1 = int(line_info[2])
            y1 = int(line_info[3])
            x2 = int(line_info[4])
            y2 = int(line_info[5])

            img = Image.open(img_path)
            w,h = img.size

            # Schauen ob das Rect aus dem Bild herausragt
            if(x1 >= w or x2 >= w):
                print(f"x1=[{x1}], x2=[{x2}], w=[{w}]")
                break
            if(y1 >= h or y2 >= h):
                print(f"y1=[{y1}], y2=[{y2}], h=[{h}]")
                break
                
            # Schauen ob die Anzahl der Rechtecke nicht korrekt gewählt wurde
            if rect_count != 1:
                print("rect count invalid")
                break

if __name__ == "__main__":
    main()
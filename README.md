# schilder-erkennen
Machine Learning Algorithmus der eine kleine Auswahl an deutschen Straßenschilder erkennen kann.

## Konfiguration (Windows) 

Benötigte Packages:

- OpenCV
- JupyterLabs



1. venv erstellen `python3 -m venv .`, um ein virtual environment im aktuellen Verzeichnis zu erstellen
2. venv aktivieren (Windows): `.\Scripts\activate`
3. Installation mit `pip install -r requirements.txt`



## Training

Die Straßenschilder werden mit Hilfe von Cascade Classifiers entdeckt. Die Umsetzung erfolgt anhand dieses OpenCV Tutorials: [Cascade Classifier Training](https://docs.opencv.org/master/dc/d88/tutorial_traincascade.html).

- Für diesen Schritt werden die opencv Tools benötigt. Die letzte Version, die mit den Tools zum Trainieren eines Cascade Classifiers ausgestatt ist, die die Version `3.4.14`. Die korrekte Version kann [hier](https://sourceforge.net/projects/opencvlibrary/files/3.4.14/opencv-3.4.14-vc14_vc15.exe/download) heruntergeladen werden.

1. Jedes Straßenschild enthält ein Verzeichnis für positive (mit Objekt welches erkannt werden soll) und negative Dateien (ohne Objekt).
2. Es werden noch 2 weitere Dateien pos.txt und neg.txt benötigt.
   1. `pos.txt`: Enthält Pfade zu Bildern, sowie die Anzahl an enhaltenen Objekten sowie die Koordinaten zu den Objekten. Wird mit dem Tool opencv_annotations erstellt
   2. `neg.txt`: Enthält Pfade zu Bildern, welche keine Objekte enthalten, die man sucht. Wird mit dem Skript generate_neg_file.py erstellt, indem das Skript mit einem Pfad zu einem Verzeichnis ausgeführt wird.
3. Vektor-Datei erstellen: `opencv_createsamples.exe -info pos.txt -w 24 -h 24 num 1000 -vec pos.vec`
   - `-info pos.txt`: Die Datei mit allen Pfaden zu den Bildern + Markierungen in den Bildern
   - `-w 24 -h 24` ist die mindeste Größe des Suchfensters. Dieser Wert sollte mindestens so groß wie die kleinste Markierung sein
   - `num 1000`: Dieser Wert muss größer als die Anzahl aller Markierungen sein
   - `-vec pos.vec`: Wo die Vektor-Datei gespeichert wird

4. Cascade Classifier trainieren: `opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 100 -numNeg 200 -numStages 10`


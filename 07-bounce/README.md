## Python Process: Bounce
Erstelle ein einfaches GUI-Programm auf Basis der o.a. Abbildung unter Anwendung des MVC Design Patterns!

### Grundanforderungen:
* GUIs mittels Designer (in PySide inkludiert) erstellt
* Trennung von View und Controller
* Sphinx-Dokumentation
* GUI fixer Größe (kein Resize)
* Zwei Buttons: New Point und Remove Last Point
* Bei einem Klick auf "New Point" wird
    * Ein neuer Prozess erstellt und eine zufällige Geschwindigkeit und Startposition festgelegt
    * Dieser Prozess ändert in einem geteilten Speicher seine x- und y-Position in regelmäßigen Abständen (z.B. 20-mal in der Sekunde) basierend auf seiner Geschwindigkeit
    * Der Kreis "prallt" an den Kanten des Fensters ab und ändert seine Richtung, bevor er sich aus dem Fenster bewegen würde
* Bei einem Klick auf "Remove Last Point" wird
    * Der letzte Prozess sauber beendet
    * Der Kreis verschwindet von der GUI
* Der Main-Prozess zeichnet die Prozesse als Kreise und behandelt die Events
* Wenn das Programm geschlossen wird, werden alle Prozesse sauber geschlossen
* Für das manuelle Zeichnen und Behandeln von Events kannst du folgende Code-Schnipsel verwenden:

```
    def refreshloop(self):
        while not self.closing:
            time.sleep(0.025)
            c.update()
            QtGui.QApplication.processEvents()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    c = FloatingPointController()
    c.show()
    c.refreshloop()
    sys.exit()
```
### Erweiterungen:
* Die Kreise haben unterschiedliche Größen und Farben
* Das Fenster ist Resizable und die Kreise reagieren entsprechend anders darauf, wenn die Größe geändert wird
* Macht es einen Unterschied, wenn statt Threads Prozesse verwendet werden? Halte deine Erkenntnisse in deiner Lösung (Kommentare) fest!
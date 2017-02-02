## Python GUI Programmierung: Einfaches Spiel
Erstelle ein einfaches Spiel auf Basis der o.a. Abbildung unter Anwendung des MVC Design Patterns!

###Grundanforderungen:
* GUI mittels Designer (in PySide inkludiert) erstellt
* Eine eigene Klasse kümmert sich um die Statistik
* Eine eigene Klasse regelt den Ablauf des Spiels und reagiert auf die QPushButtons
* Sphinx-Dokumentation
* Signals und Slots zum Schließen des Formulars über einen eigenen Button
* Funktionalität der weiteren Buttons gemäß der Beschreibung
* GUI skaliert bei einem Resize entsprechend
* Beim Starten sowie bei einem Klick auf "Neu" werden die Zahlen zufällig gemischt

###Erweiterungen:
* Wende das Gelernte über Threads an und schreibe einen eigenen Thread
* Dieser Thread steigert die Schwierigkeit des Spiels, indem er in regelmäßigen Abständen (z.B. alle 5 Sekunden) die Buttons vertauscht - allerdings nur, wenn gerade ein Spiel läuft!
* Vergleiche die Klasse threading.Thread mit der Klasse QThread - welche Unterschiede gibt es? Wann lohnt es sich, einen QThread zu verwenden? Halte deine Erkenntnisse in einem kurzen Protokoll fest!
* Mach dir außerdem Gedanken über Threadsynchronisation - muss etwas synchronisiert werden? Wenn ja, was? Halte deine Erkenntnisse in deiner Lösung sowie deinem Protokoll fest!
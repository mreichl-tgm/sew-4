##Thread Synchronisation in Python: Summenberechnung
Schreibe ein Programm, welches die Summe von 1 bis zu einer von dem/der Benutzer/in einzugebenden (potentiell sehr großen) Zahl mithilfe von drei Threads berechnet!

###Grundanforderungen:
* Eine eigene Klasse erbt von Thread
* Die Klasse definiert eine gemeinsame Lock sowie einen gemeinsamen Counter
* Im Konstruktor wird über einen Parameter bestimmt, für welche Zahlen dieser Thread zuständig ist
* In der run-Methode wird die Summe korrekt aufsummiert, wobei der Zugriff auf den Counter über die Lock threadsicher gestaltet wird (with-Statement)
* Kommentare und Sphinx-Dokumentation
* Kurzes Protokoll über deine Vorgangsweise, Aufwand, Resultate, Beobachtungen, Schwierigkeiten, ... Bitte sauberes Dokument erstellen! (Kopf- und Fußzeile etc.)

###Erweiterungen:
* Miss die Laufzeit!
* Untersuche, wie sich die Laufzeit auf deinem System verhält, wenn du es mit mehr oder weniger Threads verwendest, z.B. Single Threaded (d.h. nur im main-Thread), mit 2 Threads, mit 3 Threads, ...
* Interpretiere die Ergebnisse und halte deine Erkenntnisse im Protokoll fest! Warum verhält es sich so?
* Finde eine Möglichkeit, wie die Performance verbessert werden kann und eventuelle Beschränkungen umgangen werden können!
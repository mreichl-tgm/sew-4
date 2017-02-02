## Python IPC: Einfacher Chat
Erstelle ein einfaches Chatprogramm auf Basis der o.a. Abbildung unter Anwendung des MVC Design Patterns!

###Grundanforderungen:
* GUIs mittels Designer (in PySide inkludiert) erstellt
* Trennung von View und Controller
* Sphinx-Dokumentation
* GUI skaliert bei einem Resize entsprechend
* Client:
    - Eingabefeld für Nachrichten und Senden-Button
    - Verbindung zum Server wird beim Starten hergestellt - im Fehlerfall wird eine MessageBox mit dem Fehler angezeigt und das Programm wieder geschlossen
    - Bei einem Klick auf "Senden" wird die Nachricht an den Server geschickt und das Textfeld geleert
    - Ein zweiter Thread liest eingehende Nachrichten vom Server und fügt sie in den Chatbereich ein
    - Wird die Verbindung geschlossen, schließt sich das Programm
    - Das Close-Event wird abgefangen und der Socket wird sauber geschlossen
* Server:
    - Horcht in einem neuen Thread auf eingehende Verbindungen - es ist wichtig, dass accept() in einem eigenen Thread aufgerufen wird, da sonst die GUI einfriert
    - Im Fehlerfall wird eine entsprechende MessageBox angezeigt und das Programm beendet
    - Neue Clients werden der Client-Liste hinzugefügt, sobald sie sich verbinden
    - Für jeden neuen Client wird ein neuer Thread erstellt, welcher auf eingehende Nachrichten wartet
    - Neue Nachrichten werden an alle Clients verteilt
    - Wenn ein Client die Verbindung beendet, wird er aus der Client-Liste entfernt
    - Wenn der Server geschlossen wird, wird die Verbindung zu allen Clients sauber beendet und die Clients werden daher automatisch geschlossen

* Achtung: GUI-spezifische Operationen (z.B. Anzeigen einer MessageBox oder Bearbeiten eines GUI-Elements) dürfen nur vom GUI-Thread durchgeführt werden - verwende hierfür eigene Signals und Slots (siehe Anleitung Python PySide)

###Erweiterungen:
* Der Client kann konfiguriert werden, bevor er die Verbindung mit dem Server herstellt: Host, IP und Chatname können eingestellt werden
* Der Server kann verbundene Clients aus der Client-Liste entfernen und die Verbindung zu ihm beenden
* Es werden HTML-Tags unterstützt (z.B. text fett machen)
* Mach dir außerdem Gedanken über Threadsynchronisation - muss etwas synchronisiert werden? Wenn ja, was? Halte deine Erkenntnisse in deiner Lösung (Kommentare) fest!
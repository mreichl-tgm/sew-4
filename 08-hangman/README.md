## Java IPC: Hangman

Nun sehen wir uns an, wie Socket-Kommunikation unter Java funktioniert. Es soll das klassische "Hangman"-Spiel als main.Server-main.Client-Variante implementiert werden:
```
(main.Client-Konsole)
1 remaining tries. _ILBE_G___EL
S
1 remaining tries. SILBE_G___EL
R
1 remaining tries. SILBERG_R_EL
T
1 remaining tries. SILBERG_RTEL
SILBERGÖRTEL
You lose. The word was: SILBERGÜRTEL
```
### Die Aufgabenstellung:
* Erstelle ein Hangman-Spiel, wobei der Server als Spiele-Host fungiert!

### Grundanforderungen:
* Server-Programm wird über die Kommandozeile gestartet, wobei der Port als Kommandozeilenparameter übergeben wird (String[] args!)
* Server wartet auf eingehende Socket-Verbindungen unter dem angegebenen Port
* Verbindet sich ein Client, wird ein zufälliges Wort aus einer konfigurierbaren Liste an Wörtern ausgewählt
* Die Liste an Wörtern befindet sich in einem eigenen Textfile
* Der Server schickt dem Client die Anzahl an verbleibenden Versuchen und das aktuelle "maskierte" Wort (mit Underscores "_")
* Der Server interpretiert die Antwort des Clients
* Schickt der Client einen einzelnen Buchstaben, werden alle Stellen des Wortes aufgedeckt, die diesen Buchstaben beinhalten
* Schickt der Client mehrere Buchstaben, so wird dies als Auflöseversuch gewertet
* Hat der Client alle Versuche verbraucht, wird "You lose" geschickt und die Verbindung beendet
* Errät der Client das Wort rechtzeitig, wird "You win" ausgegeben und die Verbindung beendet
* Der Client verbindet sich mit dem Server, wobei IP-Adresse und Port ebenfalls über Kommandozeilenparameter konfiguriert werden können
    * Anschließend schickt der Client alle Benutzereingaben an den Server und gibt dessen Antwort in der Konsole aus
* Alle Verbindungen werden sauber geschlossen
* JavaDoc-Kommentare sind vorhanden

### Erweiterungen:
* Es können mehrere Clients gleichzeitig (eigene Spiele) spielen, wobei hier ein Threadpool (Executor-Service) verwendet wird
* Clients können mehrere Partien hintereinander spielen
* Alle Nachrichten werden in einem gemeinsamen Log-File über eine statische Methode log geloggt, welche von nur einem Thread gleichzeitig aufgerufen werden kann
* Der Server kann über die Konsole beendet werden
Implementiere einen einfachen Spiele-Client zum gegebenen Spiele-Server!

## Die Regeln des Spiels:
* Es spielen immer zwei Clients gegeneinander
* Das Spielbrett ist 10x10 Felder groß, wobei man über den Rand hinausgehen kann und dann wieder auf der gegenüberliegenden Seite landet
* Ziel des Spiels ist, die Schriftrolle (mit "XX" rot markiert) einzusammeln und in die gegnerische Burg (schwarzes bzw. weißes Feld) zu bringen, um sie damit zu erobern
* Spieler 1 (P1) startet auf seiner eigenen Burg (schwarz), Spieler 2 (P2) ebenfalls (weiß)
* Es gibt außer den Burgen noch folgende Spielfelder:
    * Wiese (hellgrün): Befindet man sich auf einer Wiese, sieht man zwei Felder weit, also insgesamt 5x5 Felder
    * Wald (dunkelgrün): Hier ist die Sicht eingeschränkt und man sieht nur ein Feld weit, also insgesamt 3x3 Felder
    * Berg (grau): Am Berg hat man einen guten Ausblick und sieht drei Felder weit, also insgesamt 7x7 Felder. Allerdings kostet es zwei Züge, um auf den Berg zu klettern
    * Teich (blau): Den Teich darf man nicht betreten, da man sonst das Spiel verliert.

## Die Aufgabenstellung:
Erstelle einen Java- ODER Python-Client, der sich mit dem Server verbindet und selbstständige Entscheidungen trifft!

### Grundanforderungen:
* Nimm den simplen "manuellen" Client als Vorlage, um zu sehen, wie die Kommunikation mit dem Server funktioniert
* Dein Client-Programm wird über die Kommandozeile gestartet, wobei der Port als Kommandozeilenparameter übergeben wird
* Dein Client lässt den Benutzer einen Spielernamen wählen und überträgt diesen nach dem Verbindungsaufbau an den Server. Der Server bestätigt die Nachricht mit "OK"
* Der Client schickt anschließend basierend auf den Antworten des Servers selbstständig (ohne Benutzereingaben) Move-Befehle:
    * "UP": Nach oben bewegen
    * "RIGHT": Nach rechts bewegen
    * "DOWN": Nach unten bewegen
    * "LEFT": Nach links bewegen
* Der Client lässt die Spielfigur NICHT ins Wasser fallen
* Der Client bewegt sich zur Schriftrolle, wenn er sie sieht
* Der Client bewegt sich zur gegnerischen Burg, nachdem er die Schriftrolle eingesammelt hat
* Ansonsten erkundet der Client die Landschaft - auf der Suche nach Schriftrolle bzw. Burg
* Alle Verbindungen werden sauber geschlossen
* JavaDoc/DocString-Kommentare sowie Dokumentation (Sphinx/JavaDoc) sind vorhanden
* Protokoll über den implementierten Algorithmus

### Erweiterungen:
* Arbeite dich in den Code des Servers ein
* Erweitere den Server, sodass beliebig große Spielfelder unterstützt werden!
* Sowohl die Größe des Spielfeldes als auch die anderen Parameter (Anzahl an Waldfeldern etc.) sind über den GUI konfigurierbar

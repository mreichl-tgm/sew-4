Schreibe ein Programm, welches einen Music Player einerseits simuliert und andererseits implementiert!

### Grundanforderungen:
* Verwende die vorgegebenen Klassen:
    * main: Erzeugt entweder eine Mockup-Fabrik oder eine echte Fabrik
    * Musikstueck: Abstrakte Produkt-Klasse
    * MusikdatenbankFabrik: Abstrakte Fabrik mit Fabrik-Methode lade_musik
* Eine eigene Mockup-Klasse mockt die abspielen-Methode mit einer simplen Ausgabe (Mockup-Produkt), z.B. "Sie hören den Titel XXX von YYY aus dem Album ZZZ"
* Eine eigene Mockup-Klasse erzeugt einige beliebige Mockup-Produkte (Mockup-Fabrik)
* Eine eigene Klasse spielt die Musik ab (File-Produkt)
* Eine eigene Klasse erzeugt die echten Produkte, indem sie nach mp3-Files sucht und für jedes mp3-File ein Produkt erzeugt (File-Fabrik)
* Kommentare und Sphinx-Dokumentation
* Protokoll

**Tipp:** Verwende zum Abspielen die Library pyglet. Achtung: pyglet.app.run() endet nicht automatisch, sondern muss über ein Callback nach dem Song über pyglet.app.exit() wieder beendet werden!

### Erweiterungen:
* Recherchiere, wie aus Musikdateien automatisch Titel, Album und Interpret ausgelesen werden können
* Füge die Funktionalität deiner echten Produktfamilie hinzu, sodass die Informationen ebenfalls angezeigt werden können
* Baue eine (sehr simple) GUI für deinen Music Player

**Abgabe:** zip-File mit Source-Files, Protokoll, Sphinx-Dokumentation

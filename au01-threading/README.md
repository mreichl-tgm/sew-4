#Threading in Python: Einfache Verschlüsselung
Sieh dir auf GitHub das Beispiel CounterThread an und analysiere, wie einem Thread Parameter übergeben werden und Klassenvariablen verwendet werden können!
Erstelle anschließend eine eigene Klasse, die von Thread erbt und die parallele Verschlüsselung und Entschlüsselung von einfachen Textnachrichten erlaubt!

###Beispiel:
Which message do you want to encrypt? -> Eingabe: Hallo Welt
How many threads should encrypt the message? -> Eingabe: 3
Your encrypted message: EVTTD AGTC

##Grundanforderungen:
* Eigene Klasse erbt von Thread
* Über Parameter im Konstruktor wird geregelt, für welche Teile der Nachricht dieser Thread zuständig ist (z.B. jedes dritte Zeichen, erste Hälfte der Nachricht, ...)
* Die Nachricht wird von allen Threads geteilt und bearbeitet (verschlüsselt)
* Die Verschlüsselungstabelle für den Substitutionsalgorithmus wird von allen Threads geteilt (Idee: Dictionary, welches für jedes Ursprungszeichen das Zielzeichen speichert)
* In der run-Methode werden jene Zeichen ersetzt, für die der Thread zuständig ist. Hierbei kommen sich die Threads nicht in die Quere
* In einem Skript wird der Benutzer gefragt, welche Nachricht verschlüsselt werden soll und wie viele Threads dafür verwendet werden sollen
* Anschließend wird die Nachricht entsprechend verschlüsselt und die verschlüsselte Nachricht wird ausgegeben
* In einem zweiten Schritt wird die Nachricht wieder entschlüsselt und die Ursprungsnachricht wird wieder ausgegeben (ggf. in upper case)
* Es werden Großbuchstaben unterstützt (Eingaben in lower case werden in upper case umgewandelt); Leerzeichen bleiben Leerzeichen; Sonderzeichen müssen nicht unterstützt werden (Abfangen!)
* Der Code wird kommentiert (über Python DocStirngs)

##Erweiterungen:
* Überlege dir, wie beliebige Zeichen (auch Sonderzeichen) unterstützt werden können (eventuell gibt es eine bessere Lösung als über ein Dictionary) und implementiere es dementsprechend!
* Der "Schlüssel" wird mit jedem Programmaufruf neu und zufällig generiert
* Implementiere eine simple Benutzersteuerung, welche es erlaubt, beliebige Nachrichten zu ver- und entschlüsseln (z.B. "Was möchten Sie tun? 1: verschlüsseln, 2: entschlüsseln, 0: exit)
* Achte auf saubere Fehlerbehandlung (don't trust user input)!
* Verwende Git und gib den Link zum Git-Repository ab!

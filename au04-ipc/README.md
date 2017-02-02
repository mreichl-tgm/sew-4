## Thread Synchronisation in Python: Queues
Schreibe ein Programm, welches ein simples Erzeuger-Verbraucher-Muster implementiert!

### Grundanforderungen:
* Zwei eigene Klassen (Consumer und Producer) erben von Thread (E1 und V1)
* Die zwei Klassen sind über einen Queue verbunden
* Der Erzeuger E1 sucht nach Primzahlen. Jede gefundene Primzahl wird über die Queue an den Verbraucher V1 geschickt
* Der Verbraucher gibt die empfangene Zahl in der Konsole aus und schreibt sie außerdem in eine simple Textdatei
* Erzeuger und Verbraucher stimmen sich über Queue.task_done() und Queue.join() ab
* Kommentare und Sphinx-Dokumentation
* Kurzes Protokoll über deine Vorgangsweise, Aufwand, Resultate, Beobachtungen, Schwierigkeiten, ... Bitte sauberes Dokument erstellen! (Kopf- und Fußzeile etc.)

### Erweiterungen:
* Ein weiterer Thread nimmt Benutzereingaben entgegen
* Dieser Thread kann als ein weiterer Erzeuger E2 gesehen werden
* Wird eine (potentiell sehr große) Zahl eingegeben, so wird in einem weiteren Verbraucher V2 überprüft, ob es sich bei dieser produzierten Zahl um eine Primzahl handelt
* E2 und V2 müssen sich nicht über task_done() absprechen, d.h. E2 kann mehrere Aufträge in die Queue schicken, bevor V2 mit der Bearbeitung fertig ist
* Wird "exit" eingegeben, so werden alle Threads sauber beendet
* Achte auf Fehlerfälle!
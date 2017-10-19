## Protokoll

### Probleme
Diese Aufgabe hat besonders große Probleme durch die Komplexität der Gesamtheit bereitet.
Im Nachhinein wäre ein anderes Muster weit besser gewesen.
So würde anstatt von MVC ein Module Pattern passen und es sollten nur QtSignals anstatt von Observern verwendet werden.
Viele dieser Probleme sind erst spät aufgefallen und hätten durch ein sauberes Konzept umgangen werden können.

### Erkenntnisse
Wie erwähnt sind Module und Observer stark von Vorteil.
Weiters stellte sich heraus, dass die Controller keine Threads sein müssen,
jedoch das Empfangen der Nachrichten durch Sockets seperat laufen sollte.

### Fazit
Der Zeitaufwand für diese Aufgabe war mit über 6 Stunden nicht lohnend,
ein solcher Grad an Abstraktion und Komplexität wie hier zu sehen ist für eine einfache Aufgabe nicht zu empfehlen.
In diesem Fall gilt: Weniger = Mehr

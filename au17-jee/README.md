## JavaEE: Politische Bildung
Zurück zu: Java EE
Erstelle ein Programm, welches Unterstützung in politischer Bildung in Österreich anbietet!

Je nach Auswahl des Themas wird eine entsprechende JSP-Seite aufgerufen:
1. All capitals
2. All states
3. One state
4. Capital

Je nach ausgewähltem Bundesland wird die passende Hauptstadt ausgegeben:

### Grundanforderungen:
Verwende die angehängten Dateien zur Entwicklung:
* jsp: Erstelle alle notwendigen JSP-Files
* servlet: Erstelle das Servlet zum Dispatchen aus Basis der Usereingabe
Möglicher Aufbau des Projektes:
* src/main/java
    * model/Bundesland.java (Serialisierbare Java-Klasse, welche alle Bundesländer und Hauptstädte kennt)
    * servlet/MyServlet.java (erbt von HttpServlet und leitet je nach request-Parameter auf result.jsp oder index2.jsp weiter und holt die Daten aus dem Model)
* src/main/webapp/
    * index.jsp (ermöglicht die Wahl zwischen den drei Optionen; enthält dropdown und Submit-Button)
    * index2.jsp (Zwischenschritt für die Auswahl des Bundeslandes, von dem die Hauptstadt angezeigt werden soll)
    * result.jsp (listet das Ergebnis bzw. die Ergebnisse auf)
    * WEBINF/web.xml

### Erweiterungen:
* Ersetze die JSP-Scriplets durch JSTL!
* Verwende eine angenehme User Experience

**Abgabe:** zip-File mit Source-Files und Dokumentation
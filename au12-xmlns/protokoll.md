# Datenaustauschformate: Validität und XPath
Erstelle für dein Kundendaten-XML-Dokument ein passendes XSD-Schema!
Absolviere außerdem die ersten 10 XPath-Aufgaben von http://learn.onion.net/language=en/35426/w3c-xpath (bis inkl. Selecting the following siblings) und halte deine Lösungen als Screenshots inklusive Beschreibungen im Protokoll fest!

## Grundanforderungen:
* Definiere im Schema alle Elemente und Attribute, die du verwendest
* Verwende simpleType für einfache Datentypen
* Verwende complexType für Elemente mit Attributen und/oder Kindelementen
* Passe dein XML-Dokument so an, dass es das Schema verwendet
* Überprüfe die Validität mithilfe eines Tools
* Mach die ersten 10 XPath-Aufgaben der angegeben Webseite
* Halte dein Schema, die Überprüfung und deine XPath-Queries im Protokoll fest!

## Erweiterungen:
* Überlege dir sinnvolle restrictions für deine Elemente und baue sie ein (enumerations, max/min, patterns, ...)
* Erstelle einen eigenen Datentypen und (wieder)verwende ihn!
* Überlege dir sinnvolle Default-Werte und required-Angaben für deine Attribute und baue sie ein!
* Mache die nächsten fünf XPath-Abfragen der Webseite und halte sie ebenfalls im Protokoll fest
* Halte deine Erweiterungen im Protokoll fest!

Abgabe: Protokoll, XML-Dokument und XSD-Schema

## Schema
[Schema](db.xsd)
### Erweiterungen
* Verwendung passender Datentypen
* Min und Max Werte für Alter, Postleitzahl und Preis
* Validiert durch PyCharm

## XPath
1. //@name
2. /document/linkList[@name="A"]/*
3. concat(//lastName, ", ", //firstName)
4. //job[@priority="high"] | //job[@priority="critical"]
5. //person[@age<35]
6. //person[position() < 4]
7. //person[starts-with(@firstName, "H")]
8. //person[string-length(@firstName) < "6"]
9. sum(//number[round(.) = 34])
10. //product[@id>3]
11. //product[@id>3][@category="1"]
12. //reference/@x:href
13. //content//x:a
14. //x:a[contains(@href,"google")]
15. document/*[contains(local-name(.) , "item_")]
# Datenaustauschformate DTD

## Angabe
Definiere ein wohlgeformtes, valides XML-Dokument zur tracklist DTD aus dem Unterricht!

### Grundanforderungen:
* Verwende jedes Element zumindest einmal
* Verwende jedes Attribut zumindest einmal
* Überprüfe die Validität mithilfe eines Tools
* Halte dein Dokument und die Überprüfung im Protokoll fest!

### Erweiterungen:
* Erweitere die DTD, sodass Alben gespeichert werden können und baue sinnvolle IDREF-Attribute ein! Passe dein Dokument entsprechend an!
* Überlege dir sinnvolle Default-Werte für deine Attribute und baue sie ein!
* Halte deine Erweiterungen im Protokoll fest!

Abgabe: Protokoll, XML-Dokument und ggf. erweiterte DTD

## Validator
Verwendet wurde der folgende Online XML Validator: http://www.xmlvalidation.com

## Erweiterungen
Für die Erweiterungen waren keine Standard Werte sinnvoll, da alle weiteren Informationen über die ID Referenzen zugänglich sind.
Das Album beinhaltet einen Namen und mehrere Referenzen zu Tracks oder Interpreten. Alben werden durch ihre ID eindeutig unterschieden.
Jeder Track / Jeder Interpret MUSS eine Referenz zu einem bereits definierten Element als Attribut aufweisen.

## Abgabe
Die fertige XML Datei ist wie folgt aufgebaut:

´´´ xml
<!-- Basis -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE tracklist [
<!ELEMENT tracklist	    (album*, track*, interpret*)>

<!ELEMENT track         (name, length, review*)>
<!ATTLIST track         id  ID	#REQUIRED
                        style   (rock|funk|hiphop|klassik) "rock">
<!ELEMENT name          (#PCDATA)>
<!ELEMENT length	    (#PCDATA)>
<!ELEMENT review	    (#PCDATA | link)*>

<!ELEMENT link		    (#PCDATA)>
<!ATTLIST link          ref     IDREF   #IMPLIED>

<!ELEMENT interpret     (band | soloartist)>
<!ATTLIST interpret	    id	ID	#REQUIRED>
<!ELEMENT band		    (name, person+)>
<!ELEMENT soloartist    (person)>

<!ELEMENT person	    (firstname?, name, instrument*)>
<!ELEMENT firstname	    (#PCDATA)>
<!ELEMENT instrument    (#PCDATA)>
<!ATTLIST person        gender	(male|female) "female">
<!-- Erweiterung -->
<!ELEMENT album         (name, track_ref+, interpret_ref+)>
<!ATTLIST album         id ID #REQUIRED>

<!ELEMENT track_ref     (name)>
<!ATTLIST track_ref     ref IDREF #REQUIRED>

<!ELEMENT interpret_ref (name)>
<!ATTLIST interpret_ref ref IDREF #REQUIRED>
]>

<tracklist>
    <album id="chopin-project">
        <name>The Chopin Project</name>
        <track_ref ref="arnalds-eyesshut">
            <name>Eyes Shut</name>
        </track_ref>
        <interpret_ref ref="arnalds">
            <name>Olafur Arnalds</name>
        </interpret_ref>
    </album>
    
    <track id="arnalds-eyesshut" style="klassik">
        <name>Eyes Shut - Nocturne G Minor</name>
        <length>4.22</length>
        <review>
            A dreamlike story arc you wish would never end.
        </review>
        <review>
            <link ref="arnalds-eyesshut">https://review.com/eyesshut</link>
        </review>
    </track>
    
    <interpret id="arnalds">
        <soloartist>
            <person gender="male">
                <firstname>Olafur</firstname>
                <name>Arnalds</name>
                <instrument>Piano</instrument>
            </person>
        </soloartist>
    </interpret>
    
    <interpret id="omam">
        <band>
            <name>Of monsters and men</name>
            <person gender="female">
                <name>Nanna Bryndís Hilmarsdottir</name>
                <instrument>Vocal</instrument>
            </person>
            <person gender="male">
                <name>Krisjef Rosenkranz Krisjefsson</name>
                <instrument>Guitar</instrument>
            </person>
            <!-- Some are missing... -->
        </band>
    </interpret>
</tracklist>
´´´

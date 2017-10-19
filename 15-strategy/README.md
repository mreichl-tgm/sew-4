## Design Patterns: Strategy Sichere deine Daten!

```
Schreiben Sie ein Programm, das sowohl von der CommandLine als auch mit Standard-Optionen arbeiten kann:

Usage: do.py [options]
Note: By default this script will overwrite already created archives!

Options:
  -h, --help            show this help message and exit
  -d DESTDIR, --dest-dir=DESTDIR
                        Output destination directory (default=Current Working
                        Directory)
  -s SOURCEDIR, --source-dir=SOURCEDIR
                        Intput root directory (default=Current Working
                        Directory)
  -a ARCHIVE, --archive-engine=ARCHIVE
                        use the given archive engine (default=ZIP_STORED)
  -n NAME, --archive-name=NAME
                        name of the archive (default=archive)
```

Das Programm dient zur flexiblen Archivierung von vorhandenen Daten.

### Folgende Aufgaben werden sich bei der Verwendung nicht ändern:
* Einlesen der Files aus dem SOURCEDIR-Verzeichnis (-s)
* Festlegen des Archiv-Namens (-n)
* Festlegen des Ausgabeverzeichnisses (-d)
* Festlegen der Archiv-Engine (a)
* Verifikation des Source-Verzeichnisses (Ausgabe eines sprechenden Fehlers)
* Verifikation des Destination-Verzeichnisses (Ausgabe eines sprechenden Fehlers)
* Verifikation der Archive-Engine (Ausgabe eines sprechenden Fehlers, falls unbekannt)

### Folgende Aufgaben können sich jedoch ändern:
* Dateierweiterung (abhängig von der gewählten Archiv-Engine)
* Speicherung der ausgewählten Files

### Beispielhafte Ausgaben:
```
- python do.py -a TAURUS -d .\strategy_archivieren -s .\strategy_archivieren
- TAURUS is not a valid compression engine.
- python do.py -a TAR_STORED -d .\strategy_archivieren -s .\strategy_archivieren
- python do.py -a TAR_GZ -n test_tar_gz -d .\strategy_archivieren -s .\strategy_archivieren
```
### Folgende Archive-Engines sind umzusetzen:
* Dateierweiterung .zip: ZIP ohne Komprimierung
* Dateierweiterung .7z: ZIP mit LZMA-Komprimierung
* Dateierweiterung .bz2: ZIP mit BZIP2-Komprimierung
* Dateierweiterung .zip: ZIP mit ZIP_DEFLATED-Komprimierung
* Dateierweiterung .tar.gz: TAR mit GZIP-Komprimierung
* Dateierweiterung .tar: TAR ohne Komprimierung

### Folgende Files (in einem Archiv) sind abzugeben:
* engine.py (bereits vorhanden)
* engines.py (alle umgesetzten Archiv-Engines)
* do.py (ausführbares python-Skript)

### Erweiterung:
* do.py erkennt alle vorhandenen Archiv-Engines (in engines.py)
* do.py kann Instanzen der gewählten Archiv-Engine erstellen, ohne dass Änderungen im Sourcecode notwendig sind.
* Dateierweiterung .tar.xz: TAR mit LZMA-Komprimierung
* Dateierweiterung .tar.bz2: TAR mit BZIP2-Komprimierung

Abgabe der ausführbahren Source-Files (Python) laut Abgaberichtlinie!

Hinweis: Achten Sie auf eine gute Dokumentation!
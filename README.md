# Experiment voor Cognitiewetenschap
## Abstract
Deze code hoort bij het artikel 'Bewustzijn heeft aandacht nodig' (zie `/artikel`). We hebben een experiment ontwikkeld dat vanuit een dual-task paradigme onderzoekt in hoeverre de gistwaarneming (de hoofdlijnen van een afbeelding die 30ms wordt getoond) interfereert met de intensiviteit van een aandachtstaak.

## PsychoPy
De basis van de code is gebouwd met behulp van [PsychoPy2](http://www.psychopy.org)[1,2]. Met name het randomiseren van de stimuli is eigen code die ik heb toegevoegd. Om het experiment uit te voeren, is het volgende minimaal  nodig:
- een installatie van PsychoPy2
- de map met gist afbeeldingen (`/gist`)
- het excelbestand met de condities (`condities.xlsx`)
- het `movingDots.psyexp` bestand.

Voor problemen met installeren van PsychoPy kan het nodig zijn om eerst aanvullende pakketen te installeren zoals omschreven op de installatiepagina van PsychoPy.

## Analyse
Alle analyses uit het artikel zijn gemaakt met de bijgevoegde R code. Om deze te draaien is het nodig om `~/path/to/data/files` te vervangen met het correcte pad naar de .csv-datafiles die PsychoPy produceert.

`datagather-experiment.R` bewerkt alle .csv files totdat de data een bruikbare vorm heeft om met `analyses.R` te plotten.

Alle data van de experimenten die wij met onze groep hebben gemaakt zijn geanonimiseerd beschikbaar als het bestand `data.csv`.

----

[1]:  Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
[2]:  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
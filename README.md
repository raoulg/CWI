# Experiment voor Cognitiewetenschap
## Abstract
Deze code hoort bij het artikel 'titel artikel'. We hebben een experiment ontwikkeld dat vanuit een dual-task conditie onderzoekt in hoeverre de waarneming van de *gist* van afbeeldingen (de hoofdlijnen van een afbeelding die 30ms wordt getoond) interfereert met de intensiviteit van een aandachtstaak.

## PsychoPy
De basis van de code is gebouwd met behulp van [PsychoPy2](http://www.psychopy.org)[1,2]. Met name het randomiseren van de stimuli is eigen code die ik heb toegevoegd. Om het experiment uit te voeren, is het volgende minimaal  nodig:
- een installatie van PsychoPy2
- de map met gist afbeeldingen (`/gist`)
- het excelbestand met de condities (`condities.xlsx`)
- het `movingDots.psyexp` bestand.

----

[1]:  Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
[2]:  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
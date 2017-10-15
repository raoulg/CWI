#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on Sun Oct 15 22:50:38 2017
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'movingDots-demo-4tests'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DATA)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1280, 800), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructies_2"
instructies_2Clock = core.Clock()
image_6 = visual.ImageStim(
    win=win, name='image_6',units='pix', 
    image='gist/instructies_obj.png', mask=None,
    ori=0, pos=(300, 0), size=(230, 322),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Je ziet straks meerdere bewegende blauwe balletjes\nin beeld, die over een rode lijn heen bewegen.',
    font='Arial',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "instructies_3"
instructies_3Clock = core.Clock()
image_8 = visual.ImageStim(
    win=win, name='image_8',units='pix', 
    image='gist/man6.png', mask=None,
    ori=0, pos=(300, 0), size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text='Zeer kortdurend verschijnt er in een van de \nvier hoeken een foto van een man of vrouw.',
    font='Arial',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "instructie"
instructieClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Je hebt nu tegelijkertijd twee taken:\n\nTaak 1:\nTel hoe vaak er in totaal een blauwe balletje \nover de rode lijn gaat.\n\nFocus je blik op de rode lijn, niet op de balletjes.\n\nTaak 2:\nIs de foto een man of een vrouw?',
    font='Arial',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "instructies_4"
instructies_4Clock = core.Clock()
image_7 = visual.ImageStim(
    win=win, name='image_7',units='pix', 
    image='gist/instructies_mv.png', mask=None,
    ori=0, pos=(300, 200), size=(466, 202),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='Raporteer man of vrouw door op\nhet uiteinde van de lijn te klikken.',
    font='Arial',
    pos=(-0.5, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
image_9 = visual.ImageStim(
    win=win, name='image_9',units='pix', 
    image='gist/instructies_objcount.png', mask=None,
    ori=0, pos=(300, -200), size=(491, 206),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
text_5 = visual.TextStim(win=win, name='text_5',
    text='Raporteer het totaal aantal keer dat de\nballetjes de lijn hebben gekruist\ndoor op de getallenlijn het juiste aantal \nte selecteren.\n\nDruk nu een toets om de test te starten.',
    font='Arial',
    pos=(-0.5, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "obj4_"
obj4_Clock = core.Clock()
image_3 = visual.ImageStim(
    win=win, name='image_3',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
polygon_8 = visual.Polygon(
    win=win, name='polygon_8',units='pix', 
    edges=90, size=(5, 5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
polygon_9 = visual.Polygon(
    win=win, name='polygon_9',units='pix', 
    edges=90, size=(5, 5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
polygon_12 = visual.Polygon(
    win=win, name='polygon_12',units='pix', 
    edges=90, size=(5, 5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
polygon_13 = visual.Polygon(
    win=win, name='polygon_13',units='pix', 
    edges=90, size=(5, 5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
line_2 = visual.Rect(
    win=win, name='line_2',units='pix', 
    width=(1, 300)[0], height=(1, 300)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0.945,-1.000,-0.929], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
# setup positions for gist
xposList = [-250, 250] # initial list
xposRep = np.repeat(xposList, 120) # repeat for 60 gist images
xpos = np.ndarray.tolist(xposRep) # change objecttype to use with pop
shuffle(xpos) # randomise order 

#setup velocities for objects
list = np.arange(0.5, 1.3, 0.1) # snelheden tussen 0.5 en 1.2, in stappen van 0.1
xvelWiden = np.repeat(list, 4) # repeat voor 4 objecten
xvelInv = xvelWiden[::-1] # reverse list for pop
xvelList = np.ndarray.tolist(xvelInv) # change objecttype to use pop

#setup random gisttimes
gistTimeRand = np.random.rand(60) # 60 trials
gistTimeWiden = gistTimeRand*1.5+4 # gist tijd tussen 4 en 5.5 sec
gistTimeList = np.ndarray.tolist(gistTimeWiden) # use with pop

#setup random directions for objects
directionRand = np.random.random_integers(0, 1, size = 190) # 9 obj x 20 trials
directionWiden = directionRand*2-1 # discrete waarden -1 of 1
directionList = np.ndarray.tolist(directionWiden) # use with pop

#setup frames for x/y-sinus
yRange = np.arange(0.0, 800) # 60 fps, 6 sec = 360 frames. 720 frames voor 120fps.
yFramerate = yRange/30
xFramerate = yRange/60

#setup random order for gists across conditions
rowAr = np.arange(80) # 80 fotos
rowList = np.ndarray.tolist(rowAr)
shuffle(rowList) # random volgorde
# selecteer 21 random fotos voor elke conditie
rowCond1Full = rowList[0:21] 
rowCond2Full = rowList[22:42]
rowCond3Full = rowList[43:63]
# pop voor elke trial 1 foto
cond1 = rowCond1Full.pop()
cond2 = rowCond2Full.pop()
cond3 = rowCond3Full.pop()
# slice zodat de var gebruikt kan worden in de trial
rowCond1 = slice(cond1, cond1+1)
rowCond2 = slice(cond2, cond2+1)
rowCond3 = slice(cond3, cond3+1)

test = [1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5]
ratingMV_2 = visual.RatingScale(win=win, name='ratingMV_2', marker=u'triangle', size=1.0, pos=[0.0, 0.5], choices=[u"'man'", u"'vrouw'"], tickHeight=-1)
rating2_2 = visual.RatingScale(win=win, name='rating2_2', marker=u'triangle', size=1.0, pos=[0.0, -0.4], low=1, high=20, labels=[u"'1'", u"'20'"], scale=u'', markerStart=u'10')
text_6 = visual.TextStim(win=win, name='text_6',
    text='default text',
    font=u'Arial',
    pos=(0.9, 0.9), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-9.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructies_2"-------
t = 0
instructies_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_intro_1 = event.BuilderKeyResponse()
# keep track of which components have finished
instructies_2Components = [image_6, text_2, key_resp_intro_1]
for thisComponent in instructies_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructies_2"-------
while continueRoutine:
    # get current time
    t = instructies_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_6* updates
    if t >= 0.0 and image_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_6.tStart = t
        image_6.frameNStart = frameN  # exact frame index
        image_6.setAutoDraw(True)
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_intro_1* updates
    if t >= 0.0 and key_resp_intro_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_intro_1.tStart = t
        key_resp_intro_1.frameNStart = frameN  # exact frame index
        key_resp_intro_1.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_intro_1.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_intro_1.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_intro_1.keys = theseKeys[-1]  # just the last key pressed
            key_resp_intro_1.rt = key_resp_intro_1.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructies_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructies_2"-------
for thisComponent in instructies_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_intro_1.keys in ['', [], None]:  # No response was made
    key_resp_intro_1.keys=None
thisExp.addData('key_resp_intro_1.keys',key_resp_intro_1.keys)
if key_resp_intro_1.keys != None:  # we had a response
    thisExp.addData('key_resp_intro_1.rt', key_resp_intro_1.rt)
thisExp.nextEntry()
# the Routine "instructies_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructies_3"-------
t = 0
instructies_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
instructies_3Components = [image_8, text_4, key_resp_3]
for thisComponent in instructies_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructies_3"-------
while continueRoutine:
    # get current time
    t = instructies_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_8* updates
    if t >= 0.0 and image_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_8.tStart = t
        image_8.frameNStart = frameN  # exact frame index
        image_8.setAutoDraw(True)
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructies_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructies_3"-------
for thisComponent in instructies_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "instructies_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructie"-------
t = 0
instructieClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
instructieComponents = [text, key_resp_2]
for thisComponent in instructieComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructie"-------
while continueRoutine:
    # get current time
    t = instructieClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructieComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructie"-------
for thisComponent in instructieComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "instructie" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructies_4"-------
t = 0
instructies_4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_intro = event.BuilderKeyResponse()
# keep track of which components have finished
instructies_4Components = [image_7, text_3, key_resp_intro, image_9, text_5]
for thisComponent in instructies_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructies_4"-------
while continueRoutine:
    # get current time
    t = instructies_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_7* updates
    if t >= 0.0 and image_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_7.tStart = t
        image_7.frameNStart = frameN  # exact frame index
        image_7.setAutoDraw(True)
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # *key_resp_intro* updates
    if t >= 0.0 and key_resp_intro.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_intro.tStart = t
        key_resp_intro.frameNStart = frameN  # exact frame index
        key_resp_intro.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_intro.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_intro.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_intro.keys = theseKeys[-1]  # just the last key pressed
            key_resp_intro.rt = key_resp_intro.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *image_9* updates
    if t >= 0.0 and image_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_9.tStart = t
        image_9.frameNStart = frameN  # exact frame index
        image_9.setAutoDraw(True)
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructies_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructies_4"-------
for thisComponent in instructies_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_intro.keys in ['', [], None]:  # No response was made
    key_resp_intro.keys=None
thisExp.addData('key_resp_intro.keys',key_resp_intro.keys)
if key_resp_intro.keys != None:  # we had a response
    thisExp.addData('key_resp_intro.rt', key_resp_intro.rt)
thisExp.nextEntry()
# the Routine "instructies_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=8, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    trials_4 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions.xlsx', selection=rowCond3),
        seed=None, name='trials_4')
    thisExp.addLoop(trials_4)  # add the loop to the experiment
    thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4.keys():
            exec(paramName + '= thisTrial_4.' + paramName)
    
    for thisTrial_4 in trials_4:
        currentLoop = trials_4
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4.keys():
                exec(paramName + '= thisTrial_4.' + paramName)
        
        # ------Prepare to start Routine "obj4_"-------
        t = 0
        obj4_Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        image_3.setPos([xpos.pop(), xpos.pop()])
        image_3.setImage(imgName)
        xvel1 = (xvelList.pop()*1.0)
        xvel2 = (xvelList.pop()*0.8)
        xvel3 = (xvelList.pop()*0.8)
        xvel4 = (xvelList.pop()*0.5)
        gistTime = gistTimeList.pop()
        dir1 = directionList.pop()
        dir2 = directionList.pop()
        dir3 = directionList.pop()
        dir4 = directionList.pop()
        apndx = np.repeat(150, 30)
        apndy = np.repeat(0, 30)
        ySin1o = 50*np.sin(yFramerate*np.pi*(xvel4/2))
        ySin1r = ySin1o[::-1]
        ySin1 = np.ndarray.tolist(np.append(ySin1r, apndy))
        ySin2o = 50*np.sin(yFramerate*np.pi*(xvel3/2))
        ySin2r = ySin2o[::-1]
        ySin2 = np.ndarray.tolist(np.append(ySin2r, apndy))
        ySin3o = 50*np.sin(yFramerate*np.pi*xvel2)
        ySin3r = ySin3o[::-1]
        ySin3 = np.ndarray.tolist(np.append(ySin3r, apndy))
        ySin4o = 50*np.sin(yFramerate*np.pi*xvel1)
        ySin4r = ySin4o[::-1]
        ySin4 = np.ndarray.tolist(np.append(ySin4r, apndy))
        xCos1o = dir1*150*np.cos(xFramerate*np.pi*xvel3)
        xCos1r = xCos1o[::-1]
        xCos1 = np.ndarray.tolist(np.append(xCos1r, (apndx*dir1)))
        xCos2o = dir2*150*np.cos(xFramerate*np.pi*xvel4)
        xCos2r = xCos2o[::-1]
        xCos2 = np.ndarray.tolist(np.append(xCos2r, (apndx*dir2)))
        xCos3o = dir3*150*np.cos(xFramerate*np.pi*xvel1)
        xCos3r = xCos3o[::-1]
        xCos3 = np.ndarray.tolist(np.append(xCos3r, (apndx*dir3)))
        xCos4o = dir4*150*np.cos(xFramerate*np.pi*xvel2)
        xCos4r = xCos4o[::-1]
        xCos4 = np.ndarray.tolist(np.append(xCos4r, (apndx*dir4)))
        
        # set up counting objects
        obj4_1Count = 0
        obj4_2Count = 0
        obj4_3Count = 0
        obj4_4Count = 0
        switch4_1 = 0
        switch4_2 = 0
        switch4_3 = 0
        switch4_4 = 0
        
        cond3 = rowCond3Full.pop()
        rowCond3 = slice(cond3, cond3+1)
        ratingMV_2.reset()
        rating2_2.reset()
        text_6.setText(test.pop())
        # keep track of which components have finished
        obj4_Components = [image_3, polygon_8, polygon_9, polygon_12, polygon_13, line_2, ratingMV_2, rating2_2, text_6]
        for thisComponent in obj4_Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "obj4_"-------
        while continueRoutine:
            # get current time
            t = obj4_Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_3* updates
            if t >= gistTime and image_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_3.tStart = t
                image_3.frameNStart = frameN  # exact frame index
                image_3.setAutoDraw(True)
            frameRemains = gistTime + 0.030- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_3.status == STARTED and t >= frameRemains:
                image_3.setAutoDraw(False)
            
            # *polygon_8* updates
            if t >= 0.0 and polygon_8.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_8.tStart = t
                polygon_8.frameNStart = frameN  # exact frame index
                polygon_8.setAutoDraw(True)
            frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if polygon_8.status == STARTED and t >= frameRemains:
                polygon_8.setAutoDraw(False)
            if polygon_8.status == STARTED:  # only update if drawing
                polygon_8.setPos((xCos1.pop(), ySin1.pop()-10), log=False)
            
            # *polygon_9* updates
            if t >= 0.0 and polygon_9.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_9.tStart = t
                polygon_9.frameNStart = frameN  # exact frame index
                polygon_9.setAutoDraw(True)
            frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if polygon_9.status == STARTED and t >= frameRemains:
                polygon_9.setAutoDraw(False)
            if polygon_9.status == STARTED:  # only update if drawing
                polygon_9.setPos((xCos2.pop(), ySin2.pop()+10), log=False)
            
            # *polygon_12* updates
            if t >= 0.0 and polygon_12.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_12.tStart = t
                polygon_12.frameNStart = frameN  # exact frame index
                polygon_12.setAutoDraw(True)
            frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if polygon_12.status == STARTED and t >= frameRemains:
                polygon_12.setAutoDraw(False)
            if polygon_12.status == STARTED:  # only update if drawing
                polygon_12.setPos((xCos3.pop(), ySin3.pop()+20), log=False)
            
            # *polygon_13* updates
            if t >= 0.0 and polygon_13.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_13.tStart = t
                polygon_13.frameNStart = frameN  # exact frame index
                polygon_13.setAutoDraw(True)
            frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if polygon_13.status == STARTED and t >= frameRemains:
                polygon_13.setAutoDraw(False)
            if polygon_13.status == STARTED:  # only update if drawing
                polygon_13.setPos((xCos4.pop(), ySin4.pop()-20), log=False)
            
            # *line_2* updates
            if t >= 0.0 and line_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                line_2.tStart = t
                line_2.frameNStart = frameN  # exact frame index
                line_2.setAutoDraw(True)
            frameRemains = 0.0 + 6.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if line_2.status == STARTED and t >= frameRemains:
                line_2.setAutoDraw(False)
            if (polygon_8.pos[0] < 8) and (polygon_8.pos[0] > -8):
              switch4_1Mem = switch4_1
              switch4_1 = 1
              if switch4_1Mem == 0:
                obj4_1Count +=1
            else:
              switch4_1 = 0
            if (polygon_9.pos[0] < 8) and (polygon_9.pos[0] > -8):
              switch4_2Mem = switch4_2
              switch4_2 = 1
              if switch4_2Mem == 0:
                obj4_2Count +=1
            else:
              switch4_2 = 0
            if (polygon_12.pos[0] < 8) and (polygon_12.pos[0] > -8):
              switch4_3Mem = switch4_3
              switch4_3 = 1
              if switch4_3Mem == 0:
                obj4_3Count +=1
            else:
              switch4_3 = 0
            if (polygon_13.pos[0] < 8) and (polygon_13.pos[0] > -8):
              switch4_4Mem = switch4_4
              switch4_4 = 1
              if switch4_4Mem == 0:
                obj4_4Count +=1
            else:
              switch4_4 = 0
            # *ratingMV_2* updates
            if t >= 6.0 and ratingMV_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                ratingMV_2.tStart = t
                ratingMV_2.frameNStart = frameN  # exact frame index
                ratingMV_2.setAutoDraw(True)
            # *rating2_2* updates
            if (ratingMV_2.status==FINISHED) and rating2_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                rating2_2.tStart = t
                rating2_2.frameNStart = frameN  # exact frame index
                rating2_2.setAutoDraw(True)
            continueRoutine &= rating2_2.noResponse  # a response ends the trial
            
            # *text_6* updates
            if t >= 0.0 and text_6.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_6.tStart = t
                text_6.frameNStart = frameN  # exact frame index
                text_6.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in obj4_Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "obj4_"-------
        for thisComponent in obj4_Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_4.addData('obj4_1Count', obj4_1Count)
        trials_4.addData('obj4_2Count', obj4_2Count)
        trials_4.addData('obj4_3Count', obj4_3Count)
        trials_4.addData('obj4_4Count', obj4_4Count)
        # store data for trials_4 (TrialHandler)
        trials_4.addData('ratingMV_2.response', ratingMV_2.getRating())
        trials_4.addData('ratingMV_2.rt', ratingMV_2.getRT())
        # store data for trials_4 (TrialHandler)
        trials_4.addData('rating2_2.response', rating2_2.getRating())
        trials_4.addData('rating2_2.rt', rating2_2.getRT())
        # the Routine "obj4_" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_4'
    
    # get names of stimulus parameters
    if trials_4.trialList in ([], [None], None):
        params = []
    else:
        params = trials_4.trialList[0].keys()
    # save data for this loop
    trials_4.saveAsExcel(filename + '.xlsx', sheetName='trials_4',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_4.saveAsText(filename + 'trials_4.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 8 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

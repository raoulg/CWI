#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on Wed Oct 11 08:04:00 2017
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
expName = 'movingDots-demo'  # from the Builder filename that created this script
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

# Initialize components for Routine "instructie"
instructieClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'Taak 1:\ntel hoe vaak de blauwe balletjes over de rode lijn gaan.\nNegeer de rode balletjes.\n\nTaak 2:\nIn de periferie komt een flits van een foto.\nIs dit een man of een vrouw?',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "obj1"
obj1Clock = core.Clock()
image_4 = visual.ImageStim(
    win=win, name='image_4',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
polygon_11 = visual.Polygon(
    win=win, name='polygon_11',units='pix', 
    edges=90, size=(5, 5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
line = visual.Rect(
    win=win, name='line',units='pix', 
    width=(1, 300)[0], height=(1, 300)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0.945,-1.000,-0.929], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
xposList = [-500, 500] # initial list
xposRep = np.repeat(xposList, 120) # repeat for 120 gist images
xpos = np.ndarray.tolist(xposRep) # change objecttype to use .pop
shuffle(xpos) # randomise order 

xvelRand = np.random.rand(560) # 14 obj x 40 trials
xvelWiden = xvelRand*1.5+0.5 # maak snelheden tussen 0.5 en 2
xvelList = np.ndarray.tolist(xvelWiden) # change objecttype to use pop

gistTimeRand = np.random.rand(120) # 120 trials
gistTimeWiden = gistTimeRand*1.5+4 # gist tijd tussen 4 en 5.5 sec
gistTimeList = np.ndarray.tolist(gistTimeWiden) # use with pop

directionRand = np.random.random_integers(0, 1, size = 560) # 14 obj x 40 trials
directionWiden = directionRand*2-1 # discrete waarden -1 of 1
directionList = np.ndarray.tolist(directionWiden) # use with pop

yRange = np.arange(0.0, 800) # 60 fps, 6 sec = 360 frames
yFramerate = yRange/30
xFramerate = yRange/60
ratingMV_3 = visual.RatingScale(win=win, name='ratingMV_3', marker='triangle', size=1.0, pos=[0.0, 0.5], choices=[u"'man'", u"'vrouw'"], tickHeight=-1)
rating2_3 = visual.RatingScale(win=win, name='rating2_3', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=20, labels=["'1'", "'20'"], scale='', disappear=True, markerStart='10')

# Initialize components for Routine "obj2"
obj2Clock = core.Clock()
image_2 = visual.ImageStim(
    win=win, name='image_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
polygon = visual.Polygon(
    win=win, name='polygon',units='pix', 
    edges=90, size=(5, 5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
polygon_2 = visual.Polygon(
    win=win, name='polygon_2',units='pix', 
    edges=90, size=(5, 5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
line_3 = visual.Rect(
    win=win, name='line_3',units='pix', 
    width=(1, 300)[0], height=(1, 300)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0.945,-1.000,-0.929], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

ratingMV = visual.RatingScale(win=win, name='ratingMV', marker='triangle', size=1.0, pos=[0.0, 0.5], choices=[u"'man'", u"'vrouw'"], tickHeight=-1)
rating2 = visual.RatingScale(win=win, name='rating2', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=20, labels=["'1'", "'20'"], scale='', disappear=True, markerStart='10')

# Initialize components for Routine "obj3"
obj3Clock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(100, 100),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
polygon_10 = visual.Polygon(
    win=win, name='polygon_10',units='pix', 
    edges=90, size=(5, 5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
polygon_14 = visual.Polygon(
    win=win, name='polygon_14',units='pix', 
    edges=90, size=(5, 5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
polygon_15 = visual.Polygon(
    win=win, name='polygon_15',units='pix', 
    edges=90, size=(5, 5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
line_4 = visual.Rect(
    win=win, name='line_4',units='pix', 
    width=(1, 300)[0], height=(1, 300)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0.945,-1.000,-0.929], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

ratingMV_4 = visual.RatingScale(win=win, name='ratingMV_4', marker='triangle', size=1.0, pos=[0.0, 0.5], choices=[u"'man'", u"'vrouw'"], tickHeight=-1, disappear=True)
rating2_4 = visual.RatingScale(win=win, name='rating2_4', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=20, labels=["'1'", "'20'"], scale='', markerStart='10')

# Initialize components for Routine "obj4__2"
obj4__2Clock = core.Clock()
image_5 = visual.ImageStim(
    win=win, name='image_5',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(100, 100),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
polygon_16 = visual.Polygon(
    win=win, name='polygon_16',units='pix', 
    edges=90, size=(5, 5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
polygon_17 = visual.Polygon(
    win=win, name='polygon_17',units='pix', 
    edges=90, size=(5, 5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
polygon_18 = visual.Polygon(
    win=win, name='polygon_18',units='pix', 
    edges=90, size=(5, 5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1,-1,1], lineColorSpace='rgb',
    fillColor=[-1,-1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
polygon_19_red = visual.Polygon(
    win=win, name='polygon_19_red',units='pix', 
    edges=90, size=(5, 5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1.0,-1.0,-1.0], lineColorSpace='rgb',
    fillColor=[1.0,-1.0,-1.0], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
polygon_20_red = visual.Polygon(
    win=win, name='polygon_20_red',units='pix', 
    edges=90, size=(5, 5),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1.0,-1.0,-1.0], lineColorSpace='rgb',
    fillColor=[1.0,-1.0,-1.0], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
line_5 = visual.Rect(
    win=win, name='line_5',units='pix', 
    width=(1, 300)[0], height=(1, 300)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0.945,-1.000,-0.929], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)

ratingMV_5 = visual.RatingScale(win=win, name='ratingMV_5', marker='triangle', size=1.0, pos=[0.0, 0.5], choices=[u"'man'", u"'vrouw'"], tickHeight=-1, disappear=True)
rating2_5 = visual.RatingScale(win=win, name='rating2_5', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=20, labels=["'1'", "'20'"], scale='', markerStart='10')

# Initialize components for Routine "obj4_"
obj4_Clock = core.Clock()
image_3 = visual.ImageStim(
    win=win, name='image_3',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(100, 100),
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

ratingMV_2 = visual.RatingScale(win=win, name='ratingMV_2', marker='triangle', size=1.0, pos=[0.0, 0.5], choices=[u"'man'", u"'vrouw'"], tickHeight=-1, disappear=True)
rating2_2 = visual.RatingScale(win=win, name='rating2_2', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=20, labels=["'1'", "'20'"], scale='', markerStart='10')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

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

# ------Prepare to start Routine "obj1"-------
t = 0
obj1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
image_4.setPos([xpos.pop(), 0])
image_4.setImage('gist/vrouw5.png')
xvel1 = xvelList.pop()
gistTime = gistTimeList.pop()
dir1 = directionList.pop()
ySin1 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel1))
xCos1 = np.ndarray.tolist(150*np.cos(xFramerate*np.pi*(xvel1+0.5)))

obj1Count = 0
ratingMV_3.reset()
rating2_3.reset()
# keep track of which components have finished
obj1Components = [image_4, polygon_11, line, ratingMV_3, rating2_3]
for thisComponent in obj1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "obj1"-------
while continueRoutine:
    # get current time
    t = obj1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if t >= gistTime and image_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_4.tStart = t
        image_4.frameNStart = frameN  # exact frame index
        image_4.setAutoDraw(True)
    frameRemains = gistTime + 0.030- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image_4.status == STARTED and t >= frameRemains:
        image_4.setAutoDraw(False)
    
    # *polygon_11* updates
    if t >= 0.5 and polygon_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_11.tStart = t
        polygon_11.frameNStart = frameN  # exact frame index
        polygon_11.setAutoDraw(True)
    frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_11.status == STARTED and t >= frameRemains:
        polygon_11.setAutoDraw(False)
    if polygon_11.status == STARTED:  # only update if drawing
        polygon_11.setPos((xCos1.pop(), ySin1.pop()), log=False)
    
    # *line* updates
    if t >= 0.0 and line.status == NOT_STARTED:
        # keep track of start time/frame for later
        line.tStart = t
        line.frameNStart = frameN  # exact frame index
        line.setAutoDraw(True)
    frameRemains = 0.0 + 6.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if line.status == STARTED and t >= frameRemains:
        line.setAutoDraw(False)
    if polygon_11.pos[1] == 0:
        obj1Count = obj1Count + 1
    # *ratingMV_3* updates
    if t >= 6.0 and ratingMV_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        ratingMV_3.tStart = t
        ratingMV_3.frameNStart = frameN  # exact frame index
        ratingMV_3.setAutoDraw(True)
    # *rating2_3* updates
    if (ratingMV_3.status==FINISHED) and rating2_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating2_3.tStart = t
        rating2_3.frameNStart = frameN  # exact frame index
        rating2_3.setAutoDraw(True)
    continueRoutine &= rating2_3.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in obj1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "obj1"-------
for thisComponent in obj1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('obj1Count', obj1Count)
# store data for thisExp (ExperimentHandler)
thisExp.addData('ratingMV_3.response', ratingMV_3.getRating())
thisExp.addData('ratingMV_3.rt', ratingMV_3.getRT())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating2_3.response', rating2_3.getRating())
thisExp.addData('rating2_3.rt', rating2_3.getRT())
thisExp.nextEntry()
# the Routine "obj1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "obj2"-------
t = 0
obj2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
image_2.setPos([xpos.pop(), 0])
image_2.setImage('gist/man2.jpg')
xvel1 = xvelList.pop()
xvel2 = xvelList.pop()
gistTime = gistTimeList.pop()
dir1 = directionList.pop()
dir2 = directionList.pop()
ySin1 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel2))
ySin2 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel1))
xCos1 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel1)))
xCos2 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel2)))

obj2_1Count = 0
obj2_2Count = 0
ratingMV.reset()
rating2.reset()
# keep track of which components have finished
obj2Components = [image_2, polygon, polygon_2, line_3, ratingMV, rating2]
for thisComponent in obj2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "obj2"-------
while continueRoutine:
    # get current time
    t = obj2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_2* updates
    if t >= gistTime and image_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_2.tStart = t
        image_2.frameNStart = frameN  # exact frame index
        image_2.setAutoDraw(True)
    frameRemains = gistTime + 0.030- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image_2.status == STARTED and t >= frameRemains:
        image_2.setAutoDraw(False)
    
    # *polygon* updates
    if t >= 0.5 and polygon.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon.tStart = t
        polygon.frameNStart = frameN  # exact frame index
        polygon.setAutoDraw(True)
    frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon.status == STARTED and t >= frameRemains:
        polygon.setAutoDraw(False)
    if polygon.status == STARTED:  # only update if drawing
        polygon.setPos((xCos1.pop(), ySin1.pop()), log=False)
    
    # *polygon_2* updates
    if t >= 0.5 and polygon_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_2.tStart = t
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.setAutoDraw(True)
    frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_2.status == STARTED and t >= frameRemains:
        polygon_2.setAutoDraw(False)
    if polygon_2.status == STARTED:  # only update if drawing
        polygon_2.setPos((xCos2.pop(), 50+ySin2.pop()), log=False)
    
    # *line_3* updates
    if t >= 0.0 and line_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        line_3.tStart = t
        line_3.frameNStart = frameN  # exact frame index
        line_3.setAutoDraw(True)
    frameRemains = 0.0 + 6.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if line_3.status == STARTED and t >= frameRemains:
        line_3.setAutoDraw(False)
    if polygon.pos[1] == 0:
        obj2_1Count = obj2_1Count + 1
    if polygon_2.pos[1] == 0:
        obj2_2Count = obj2_2Count + 1
    # *ratingMV* updates
    if t >= 6.0 and ratingMV.status == NOT_STARTED:
        # keep track of start time/frame for later
        ratingMV.tStart = t
        ratingMV.frameNStart = frameN  # exact frame index
        ratingMV.setAutoDraw(True)
    # *rating2* updates
    if (ratingMV.status==FINISHED) and rating2.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating2.tStart = t
        rating2.frameNStart = frameN  # exact frame index
        rating2.setAutoDraw(True)
    continueRoutine &= rating2.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in obj2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "obj2"-------
for thisComponent in obj2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('obj2_1Count', obj2_1Count)
thisExp.addData('obj2_2Count', obj2_2Count)
# store data for thisExp (ExperimentHandler)
thisExp.addData('ratingMV.response', ratingMV.getRating())
thisExp.addData('ratingMV.rt', ratingMV.getRT())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating2.response', rating2.getRating())
thisExp.addData('rating2.rt', rating2.getRT())
thisExp.nextEntry()
# the Routine "obj2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "obj3"-------
t = 0
obj3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
image.setPos([xpos.pop(), 0])
image.setImage('gist/vrouw2.png')
xvel1 = (xvelList.pop()/2)
xvel2 = (xvelList.pop()/2)
xvel3 = (xvelList.pop()/2)

gistTime = gistTimeList.pop()
dir1 = directionList.pop()
dir2 = directionList.pop()
dir3 = directionList.pop()

ySin1 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel2))
ySin2 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel3))
ySin3 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel1))

xCos1 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel3)))
xCos2 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel1)))
xCos3 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel2)))

obj3_1Count = 0
obj3_2Count = 0
obj3_3Count = 0
ratingMV_4.reset()
rating2_4.reset()
# keep track of which components have finished
obj3Components = [image, polygon_10, polygon_14, polygon_15, line_4, ratingMV_4, rating2_4]
for thisComponent in obj3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "obj3"-------
while continueRoutine:
    # get current time
    t = obj3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if t >= gistTime and image.status == NOT_STARTED:
        # keep track of start time/frame for later
        image.tStart = t
        image.frameNStart = frameN  # exact frame index
        image.setAutoDraw(True)
    frameRemains = gistTime + 0.030- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image.status == STARTED and t >= frameRemains:
        image.setAutoDraw(False)
    
    # *polygon_10* updates
    if t >= 0.5 and polygon_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_10.tStart = t
        polygon_10.frameNStart = frameN  # exact frame index
        polygon_10.setAutoDraw(True)
    frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_10.status == STARTED and t >= frameRemains:
        polygon_10.setAutoDraw(False)
    if polygon_10.status == STARTED:  # only update if drawing
        polygon_10.setPos((xCos1.pop(), ySin1.pop()), log=False)
    
    # *polygon_14* updates
    if t >= 0.5 and polygon_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_14.tStart = t
        polygon_14.frameNStart = frameN  # exact frame index
        polygon_14.setAutoDraw(True)
    frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_14.status == STARTED and t >= frameRemains:
        polygon_14.setAutoDraw(False)
    if polygon_14.status == STARTED:  # only update if drawing
        polygon_14.setPos((xCos2.pop(), 50+ySin2.pop()), log=False)
    
    # *polygon_15* updates
    if t >= 0.5 and polygon_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_15.tStart = t
        polygon_15.frameNStart = frameN  # exact frame index
        polygon_15.setAutoDraw(True)
    frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_15.status == STARTED and t >= frameRemains:
        polygon_15.setAutoDraw(False)
    if polygon_15.status == STARTED:  # only update if drawing
        polygon_15.setPos((xCos3.pop(), 75+ySin3.pop()), log=False)
    
    # *line_4* updates
    if t >= 0.0 and line_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        line_4.tStart = t
        line_4.frameNStart = frameN  # exact frame index
        line_4.setAutoDraw(True)
    frameRemains = 0.0 + 6.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if line_4.status == STARTED and t >= frameRemains:
        line_4.setAutoDraw(False)
    if polygon_10.pos[1] == 0:
        obj3_1Count = obj3_1Count + 1
    if polygon_14.pos[1] == 0:
        obj3_2Count = obj3_2Count + 1
    if polygon_15.pos[1] == 0:
        obj3_3Count = obj3_3Count + 1
    # *ratingMV_4* updates
    if t >= 6.0 and ratingMV_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        ratingMV_4.tStart = t
        ratingMV_4.frameNStart = frameN  # exact frame index
        ratingMV_4.setAutoDraw(True)
    # *rating2_4* updates
    if (ratingMV_4.status==FINISHED) and rating2_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating2_4.tStart = t
        rating2_4.frameNStart = frameN  # exact frame index
        rating2_4.setAutoDraw(True)
    continueRoutine &= rating2_4.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in obj3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "obj3"-------
for thisComponent in obj3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('obj3_1Count', obj3_1Count)
thisExp.addData('obj3_2Count', obj3_2Count)
thisExp.addData('obj3_3Count', obj3_3Count)
# store data for thisExp (ExperimentHandler)
thisExp.addData('ratingMV_4.response', ratingMV_4.getRating())
thisExp.addData('ratingMV_4.rt', ratingMV_4.getRT())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating2_4.response', rating2_4.getRating())
thisExp.addData('rating2_4.rt', rating2_4.getRT())
thisExp.nextEntry()
# the Routine "obj3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "obj4__2"-------
t = 0
obj4__2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
image_5.setPos([xpos.pop(), 0])
image_5.setImage('gist/man2.jpg')
xvel1 = (xvelList.pop()/2)
xvel2 = (xvelList.pop()/2)
xvel3 = (xvelList.pop()/2)
xvel4 = (xvelList.pop()/2)
xvel5 = (xvelList.pop()/2)
gistTime = gistTimeList.pop()
ySin1 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel5))
ySin2 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel4))
ySin3 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel3))
ySin4 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel2))
ySin5 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel1))

xCos1 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel3)))
xCos2 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel4)))
xCos3 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel5)))
xCos4 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel1)))
xCos5 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel2)))

obj4_1Count = 0
obj4_2Count = 0
obj4_3Count = 0
ratingMV_5.reset()
rating2_5.reset()
# keep track of which components have finished
obj4__2Components = [image_5, polygon_16, polygon_17, polygon_18, polygon_19_red, polygon_20_red, line_5, ratingMV_5, rating2_5]
for thisComponent in obj4__2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "obj4__2"-------
while continueRoutine:
    # get current time
    t = obj4__2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_5* updates
    if t >= gistTime and image_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_5.tStart = t
        image_5.frameNStart = frameN  # exact frame index
        image_5.setAutoDraw(True)
    frameRemains = gistTime + 0.030- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image_5.status == STARTED and t >= frameRemains:
        image_5.setAutoDraw(False)
    
    # *polygon_16* updates
    if t >= 0.5 and polygon_16.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_16.tStart = t
        polygon_16.frameNStart = frameN  # exact frame index
        polygon_16.setAutoDraw(True)
    frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_16.status == STARTED and t >= frameRemains:
        polygon_16.setAutoDraw(False)
    if polygon_16.status == STARTED:  # only update if drawing
        polygon_16.setPos((xCos1.pop(), ySin1.pop()), log=False)
    
    # *polygon_17* updates
    if t >= 0.5 and polygon_17.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_17.tStart = t
        polygon_17.frameNStart = frameN  # exact frame index
        polygon_17.setAutoDraw(True)
    frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_17.status == STARTED and t >= frameRemains:
        polygon_17.setAutoDraw(False)
    if polygon_17.status == STARTED:  # only update if drawing
        polygon_17.setPos((xCos2.pop(), 20+ySin2.pop()), log=False)
    
    # *polygon_18* updates
    if t >= 0.5 and polygon_18.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_18.tStart = t
        polygon_18.frameNStart = frameN  # exact frame index
        polygon_18.setAutoDraw(True)
    frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_18.status == STARTED and t >= frameRemains:
        polygon_18.setAutoDraw(False)
    if polygon_18.status == STARTED:  # only update if drawing
        polygon_18.setPos((xCos3.pop(), 40+ySin3.pop()), log=False)
    
    # *polygon_19_red* updates
    if t >= 0.5 and polygon_19_red.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_19_red.tStart = t
        polygon_19_red.frameNStart = frameN  # exact frame index
        polygon_19_red.setAutoDraw(True)
    frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_19_red.status == STARTED and t >= frameRemains:
        polygon_19_red.setAutoDraw(False)
    if polygon_19_red.status == STARTED:  # only update if drawing
        polygon_19_red.setPos((xCos4.pop(), 60+ySin4.pop()), log=False)
    
    # *polygon_20_red* updates
    if t >= 0.5 and polygon_20_red.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_20_red.tStart = t
        polygon_20_red.frameNStart = frameN  # exact frame index
        polygon_20_red.setAutoDraw(True)
    frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_20_red.status == STARTED and t >= frameRemains:
        polygon_20_red.setAutoDraw(False)
    if polygon_20_red.status == STARTED:  # only update if drawing
        polygon_20_red.setPos((xCos5.pop(), 80+ySin5.pop()), log=False)
    
    # *line_5* updates
    if t >= 0.0 and line_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        line_5.tStart = t
        line_5.frameNStart = frameN  # exact frame index
        line_5.setAutoDraw(True)
    frameRemains = 0.0 + 6.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if line_5.status == STARTED and t >= frameRemains:
        line_5.setAutoDraw(False)
    if polygon_16.pos[1] == 0:
        obj4_1Count = obj4_1Count + 1
    if polygon_17.pos[1] == 0:
        obj4_2Count = obj4_2Count + 1
    if polygon_18.pos[1] == 0:
        obj4_3Count = obj4_3Count + 1
    # *ratingMV_5* updates
    if t >= 6.0 and ratingMV_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        ratingMV_5.tStart = t
        ratingMV_5.frameNStart = frameN  # exact frame index
        ratingMV_5.setAutoDraw(True)
    # *rating2_5* updates
    if (ratingMV_5.status==FINISHED) and rating2_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating2_5.tStart = t
        rating2_5.frameNStart = frameN  # exact frame index
        rating2_5.setAutoDraw(True)
    continueRoutine &= rating2_5.noResponse  # a response ends the trial
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in obj4__2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "obj4__2"-------
for thisComponent in obj4__2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('obj4_1Count', obj4_1Count)
thisExp.addData('obj4_2Count', obj4_2Count)
thisExp.addData('obj4_3Count', obj4_3Count)
# store data for thisExp (ExperimentHandler)
thisExp.addData('ratingMV_5.response', ratingMV_5.getRating())
thisExp.addData('ratingMV_5.rt', ratingMV_5.getRT())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating2_5.response', rating2_5.getRating())
thisExp.addData('rating2_5.rt', rating2_5.getRT())
thisExp.nextEntry()
# the Routine "obj4__2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "obj4_"-------
t = 0
obj4_Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
image_3.setPos([xpos.pop(), 0])
image_3.setImage('gist/dier5.png')
xvel1 = (xvelList.pop()/2)
xvel2 = (xvelList.pop()/2)
xvel3 = (xvelList.pop()/2)
xvel4 = (xvelList.pop()/2)
gistTime = gistTimeList.pop()
dir1 = directionList.pop()
dir2 = directionList.pop()
dir3 = directionList.pop()
dir4 = directionList.pop()
ySin1 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*(xvel4/2)))
ySin2 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*(xvel3/2)))
ySin3 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel2))
ySin4 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel1))
xCos1 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel3)))
xCos2 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel4)))
xCos3 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel1)))
xCos4 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel2)))

obj5_1Count = 0
obj5_2Count = 0
obj5_3Count = 0
obj5_4Count = 0
ratingMV_2.reset()
rating2_2.reset()
# keep track of which components have finished
obj4_Components = [image_3, polygon_8, polygon_9, polygon_12, polygon_13, line_2, ratingMV_2, rating2_2]
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
    if t >= 0.5 and polygon_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_8.tStart = t
        polygon_8.frameNStart = frameN  # exact frame index
        polygon_8.setAutoDraw(True)
    frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_8.status == STARTED and t >= frameRemains:
        polygon_8.setAutoDraw(False)
    if polygon_8.status == STARTED:  # only update if drawing
        polygon_8.setPos((xCos1.pop(), ySin1.pop()), log=False)
    
    # *polygon_9* updates
    if t >= 0.5 and polygon_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_9.tStart = t
        polygon_9.frameNStart = frameN  # exact frame index
        polygon_9.setAutoDraw(True)
    frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_9.status == STARTED and t >= frameRemains:
        polygon_9.setAutoDraw(False)
    if polygon_9.status == STARTED:  # only update if drawing
        polygon_9.setPos((xCos2.pop(), 25+ySin2.pop()), log=False)
    
    # *polygon_12* updates
    if t >= 0.5 and polygon_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_12.tStart = t
        polygon_12.frameNStart = frameN  # exact frame index
        polygon_12.setAutoDraw(True)
    frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_12.status == STARTED and t >= frameRemains:
        polygon_12.setAutoDraw(False)
    if polygon_12.status == STARTED:  # only update if drawing
        polygon_12.setPos((xCos3.pop(), 50+ySin3.pop()), log=False)
    
    # *polygon_13* updates
    if t >= 0.5 and polygon_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_13.tStart = t
        polygon_13.frameNStart = frameN  # exact frame index
        polygon_13.setAutoDraw(True)
    frameRemains = 6.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_13.status == STARTED and t >= frameRemains:
        polygon_13.setAutoDraw(False)
    if polygon_13.status == STARTED:  # only update if drawing
        polygon_13.setPos((xCos4.pop(), 75+ySin4.pop()), log=False)
    
    # *line_2* updates
    if t >= 0.0 and line_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        line_2.tStart = t
        line_2.frameNStart = frameN  # exact frame index
        line_2.setAutoDraw(True)
    frameRemains = 0.0 + 6.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if line_2.status == STARTED and t >= frameRemains:
        line_2.setAutoDraw(False)
    if polygon_8.pos[1] == 0:
        obj5_1Count = obj5_1Count + 1
    if polygon_9.pos[1] == 0:
        obj5_2Count = obj5_2Count + 1
    if polygon_12.pos[1] == 0:
        obj5_3Count = obj5_3Count + 1
    if polygon_13.pos[1] == 0:
        obj5_4Count = obj5_4Count + 1
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
thisExp.addData('obj5_1Count', obj5_1Count)
thisExp.addData('obj5_2Count', obj5_2Count)
thisExp.addData('obj5_3Count', obj5_3Count)
thisExp.addData('obj5_4Count', obj5_4Count)
# store data for thisExp (ExperimentHandler)
thisExp.addData('ratingMV_2.response', ratingMV_2.getRating())
thisExp.addData('ratingMV_2.rt', ratingMV_2.getRT())
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating2_2.response', rating2_2.getRating())
thisExp.addData('rating2_2.rt', rating2_2.getRT())
thisExp.nextEntry()
# the Routine "obj4_" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()





# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on Sun Oct  8 10:30:20 2017
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
expName = u'movingDots'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
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
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1280, 800), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(100, 100),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
polygon = visual.Polygon(
    win=win, name='polygon',units='pix', 
    edges=90, size=(20, 20),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[-0.992,-0.835,0.961], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
polygon_2 = visual.Polygon(
    win=win, name='polygon_2',units='pix', 
    edges=90, size=(20, 20),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-0.976,-0.773,0.953], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
polygon_3 = visual.Rect(
    win=win, name='polygon_3',units='pix', 
    width=(1, 200)[0], height=(1, 200)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0.945,-1.000,-0.929], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
xposList = [-500, 500] # initial list
xposRep = np.repeat(xposList, 5) # repeat
xpos = np.ndarray.tolist(xposRep) # change objecttype to use .pop
shuffle(xpos) # randomise order 

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=7, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
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
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setPos([xpos.pop(), 0])
    image.setImage(imgName)
    key_resp_2 = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    trialComponents = [image, polygon, polygon_2, polygon_3, key_resp_2]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 1.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 1.5 + 0.030- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon.status == STARTED and t >= frameRemains:
            polygon.setAutoDraw(False)
        if polygon.status == STARTED:  # only update if drawing
            polygon.setPos((-100+(frameN*2), 0), log=False)
        
        # *polygon_2* updates
        if t >= 0.0 and polygon_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_2.tStart = t
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon_2.status == STARTED and t >= frameRemains:
            polygon_2.setAutoDraw(False)
        if polygon_2.status == STARTED:  # only update if drawing
            polygon_2.setPos((-100+frameN, 50), log=False)
        
        # *polygon_3* updates
        if t >= 0.0 and polygon_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_3.tStart = t
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon_3.status == STARTED and t >= frameRemains:
            polygon_3.setAutoDraw(False)
        
        # *key_resp_2* updates
        if t >= 1.5 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['m', 'v'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # was this 'correct'?
                if (key_resp_2.keys == str(corrAns)) or (key_resp_2.keys == corrAns):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp_2.corr = 1  # correct non-response
        else:
           key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    trials.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 7 repeats of 'trials'


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

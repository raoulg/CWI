#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on Sun Oct 15 14:01:54 2017
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
expName = u'movingDots-demo-testobjCount'  # from the Builder filename that created this script
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
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
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
    text='Taak 1:\ntel hoe vaak de blauwe balletjes over de rode lijn gaan.\n\nTaak 2:\nIn de periferie komt een flits van een foto.\nIs dit een man of een vrouw?\n\ndruk een toets om te starten',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

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
# setup positions for gist
xposList = [-250, 250] # initial list
xposRep = np.repeat(xposList, 120) # repeat for 60 gist images
xpos = np.ndarray.tolist(xposRep) # change objecttype to use with pop
shuffle(xpos) # randomise order 

#setup velocities for objects
xvelRand = np.random.rand(190) # (2+3+4) obj x 20 trials
xvelWiden = xvelRand*0.5+0.7 # maak snelheden tussen 0.5 en 1.5
xvelList = np.ndarray.tolist(xvelWiden) # change objecttype to use pop

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
ratingMV = visual.RatingScale(win=win, name='ratingMV', marker='triangle', size=1.0, pos=[0.0, 0.5], choices=[u"'man'", u"'vrouw'"], tickHeight=-1)
rating2 = visual.RatingScale(win=win, name='rating2', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=20, labels=["'1'", "'10'", "'20'"], scale='', disappear=True, markerStart='10')

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

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=20, method='sequential', 
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
    trials_2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditionsCopy.xlsx', selection=rowCond1),
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2.keys():
                exec(paramName + '= thisTrial_2.' + paramName)
        
        # ------Prepare to start Routine "obj2"-------
        t = 0
        obj2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        image_2.setPos([xpos.pop(), xpos.pop()])
        image_2.setImage(imgName)
        xvel1 = xvelList.pop() #pop velocity
        xvel2 = xvelList.pop()/4
        gistTime = gistTimeList.pop() # pop gisttime
        dir1 = directionList.pop() # pop direction. TODO:add dir
        dir2 = directionList.pop()
        ySin1 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel2)) # pop sin movement
        ySin2 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel1*2))
        xCos1 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel1)))
        xCos2 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel2)))
        
        #setup object count
        obj2_1Count = 0
        obj2_2Count = 0
        switch2_1 = 0 #setup switch for counting
        switch2_2 = 0
        #pop image for condition
        cond1 = rowCond1Full.pop()
        rowCond1 = slice(cond1, cond1+1)
        
        
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
                polygon.setPos((xCos1.pop(), ySin1.pop()-10), log=False)
            
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
                polygon_2.setPos((xCos2.pop(), ySin2.pop()+10), log=False)
            
            # *line_3* updates
            if t >= 0.0 and line_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                line_3.tStart = t
                line_3.frameNStart = frameN  # exact frame index
                line_3.setAutoDraw(True)
            frameRemains = 0.0 + 6.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if line_3.status == STARTED and t >= frameRemains:
                line_3.setAutoDraw(False)
            
            if (polygon.pos[1] < 8) and (polygon.pos[1] > -8):
              switch2_1Mem = switch2_1
              switch2_1 = 1
              if switch2_1Mem == 0:
                obj2_1Count +=1
            else:
              switch2_1 = 0
            
            if (polygon_2.pos[1] < 8) and (polygon_2.pos[1] > -8):
              print(polygon_2.pos)
              print(polygon_2.pos[1])
              switch2_2Mem = switch2_2
              switch2_2 = 1
              if switch2_2Mem == 0:
                obj2_2Count +=1
            else:
              switch2_2 = 0
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
        trials_2.addData('obj2_1Count', obj2_1Count)
        trials_2.addData('obj2_2Count', obj2_2Count)
        # store data for trials_2 (TrialHandler)
        trials_2.addData('ratingMV.response', ratingMV.getRating())
        trials_2.addData('ratingMV.rt', ratingMV.getRT())
        # store data for trials_2 (TrialHandler)
        trials_2.addData('rating2.response', rating2.getRating())
        trials_2.addData('rating2.rt', rating2.getRT())
        # the Routine "obj2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_2'
    
    # get names of stimulus parameters
    if trials_2.trialList in ([], [None], None):
        params = []
    else:
        params = trials_2.trialList[0].keys()
    # save data for this loop
    trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_2.saveAsText(filename + 'trials_2.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 20 repeats of 'trials'

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

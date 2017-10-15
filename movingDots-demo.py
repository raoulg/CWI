#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on Sat Oct 14 09:47:58 2017
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
xposList = [-250, 250] # initial list
xposRep = np.repeat(xposList, 240) # repeat for 120 gist images
xpos = np.ndarray.tolist(xposRep) # change objecttype to use .pop
shuffle(xpos) # randomise order 

xvelRand = np.random.rand(560) # 14 obj x 40 trials
xvelWiden = xvelRand*0.5+0.7 # maak snelheden tussen 0.5 en 1.5
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

rowAr = np.arange(80)
rowList = np.ndarray.tolist(rowAr)
shuffle(rowList)
rowCond1Full = rowList[0:20]
rowCond2Full = rowList[21:41]
rowCond3Full = rowList[42:62]
cond1 = rowCond1Full.pop()
cond2 = rowCond2Full.pop()
cond3 = rowCond3Full.pop()
rowCond1 = slice(cond1, cond1+1)
rowCond2 = slice(cond2, cond2+1)
rowCond3 = slice(cond3, cond3+1)
ratingMV = visual.RatingScale(win=win, name='ratingMV', marker='triangle', size=1.0, pos=[0.0, 0.5], choices=[u"'man'", u"'vrouw'"], tickHeight=-1)
rating2 = visual.RatingScale(win=win, name='rating2', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=20, labels=["'1'", "'10'", "'20'"], scale='', disappear=True, markerStart='10')

# Initialize components for Routine "obj3"
obj3Clock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(150, 150),
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

ratingMV_4 = visual.RatingScale(win=win, name='ratingMV_4', marker='triangle', size=1.0, pos=[0.0, 0.5], choices=[u"'man'", u"'vrouw'"], tickHeight=-1)
rating2_4 = visual.RatingScale(win=win, name='rating2_4', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=20, labels=["'1'", "'10'", "'20'"], scale='', markerStart='10')

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

ratingMV_2 = visual.RatingScale(win=win, name='ratingMV_2', marker='triangle', size=1.0, pos=[0.0, 0.5], choices=[u"'man'", u"'vrouw'"], tickHeight=-1)
rating2_2 = visual.RatingScale(win=win, name='rating2_2', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=20, labels=["'1'", "'20'"], scale='', markerStart='10')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

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
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditionsCopy.xlsx', selection=rowCond2),
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3.keys():
                exec(paramName + '= thisTrial_3.' + paramName)
        
        # ------Prepare to start Routine "obj3"-------
        t = 0
        obj3Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        image.setPos([xpos.pop(), xpos.pop()])
        image.setImage(imgName)
        xvel1 = (xvelList.pop()*0.8)
        xvel2 = (xvelList.pop()*0.8)
        xvel3 = (xvelList.pop()*0.8)
        
        gistTime = gistTimeList.pop()
        dir1 = directionList.pop()
        dir2 = directionList.pop()
        dir3 = directionList.pop()
        rowCond2 = slice(rowCond2Full.pop(),rowCond2Full.pop())
        
        ySin1 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel2))
        ySin2 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel3))
        ySin3 = np.ndarray.tolist(50*np.sin(yFramerate*np.pi*xvel1))
        
        xCos1 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel3)))
        xCos2 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel1)))
        xCos3 = np.ndarray.tolist((150*np.cos(xFramerate*np.pi*xvel2)))
        
        obj3_1Count = 0
        obj3_2Count = 0
        obj3_3Count = 0
        
        
        cond2 = rowCond2Full.pop()
        rowCond2 = slice(cond2, cond2+1)
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
                polygon_10.setPos((xCos1.pop(), ySin1.pop()-10), log=False)
            
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
                polygon_14.setPos((xCos2.pop(), ySin2.pop()+10), log=False)
            
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
                polygon_15.setPos((xCos3.pop(), ySin3.pop()+20), log=False)
            
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
        # store data for trials_3 (TrialHandler)
        trials_3.addData('ratingMV_4.response', ratingMV_4.getRating())
        trials_3.addData('ratingMV_4.rt', ratingMV_4.getRT())
        # store data for trials_3 (TrialHandler)
        trials_3.addData('rating2_4.response', rating2_4.getRating())
        trials_3.addData('rating2_4.rt', rating2_4.getRT())
        # the Routine "obj3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_3'
    
    # get names of stimulus parameters
    if trials_3.trialList in ([], [None], None):
        params = []
    else:
        params = trials_3.trialList[0].keys()
    # save data for this loop
    trials_3.saveAsExcel(filename + '.xlsx', sheetName='trials_3',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    trials_4 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditionsCopy.xlsx', selection=rowCond3),
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
        xvel1 = (xvelList.pop()*0.8)
        xvel2 = (xvelList.pop()*0.8)
        xvel3 = (xvelList.pop()*0.8)
        xvel4 = (xvelList.pop()*0.8)
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
        cond3 = rowCond3Full.pop()
        rowCond3 = slice(cond3, cond3+1)
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
                polygon_8.setPos((xCos1.pop(), ySin1.pop()-10), log=False)
            
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
                polygon_9.setPos((xCos2.pop(), ySin2.pop()+10), log=False)
            
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
                polygon_12.setPos((xCos3.pop(), ySin3.pop()+20), log=False)
            
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



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

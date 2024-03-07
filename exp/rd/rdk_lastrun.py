#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on März 06, 2024, at 15:45
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import time, string, random

# sample 3 uppercase letters
letters = np.random.choice(list(string.ascii_uppercase), 3)
# convert characters into string
letters = ''.join(letters)

# take timestamp in seconds and convert to milliseconds
timestamp = round(time.time() * 1000)
# remove first 6 digits
timestamp = int(str(timestamp)[6:])
# concatenate letters and timestamp to create unique ID
participant_id = letters + str(timestamp)


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'rdk'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\GIT\\neuroscicomplabFS24\\exp\\rdk\\rdk_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1200], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "participantID"
participantIDClock = core.Clock()

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
textInstr = visual.TextStim(win=win, name='textInstr',
    text='Willkommen zum Experiment.\n\nIm Folgenden werden Sie eine Reihe von Aufgaben lösen. Ihnen wird ein Kreis voller Punkte präsentiert. Einige dieser Punkte bewegen sich entweder nach links oder nach rechts. Ihre Aufgabe ist es, zu entscheiden, in welche Richtung sie sich bewegen.\n\nDrücken Sie die linke Pfeiltaste, wenn Sie glauben, dass sich die Punkte nach links bewegen, oder die rechte Pfeiltaste, wenn Sie glauben, dass sie sich nach rechts bewegen.\n\nBevor die Punkte erscheinen, sehen Sie auf dem Bildschirm einen Pfeil, der die wahrscheinlichste Bewegungsrichtung anzeigt. Zeigt der Pfeil nach rechts, bewegen sich die Punkte mit größerer Wahrscheinlichkeit nach rechts als nach links, und umgekehrt.\n\nBitte konzentrieren Sie sich immer auf das kleine Kreuz auf dem Bildschirm, wenn nichts anderes angezeigt wird, und versuchen Sie, so schnell wie möglich zu reagieren.\n\nDrücken Sie [ Leertaste ], um mit dem Übungsdurchgang zu beginnen, wenn Sie bereit sind.\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
win.color = 'black'
respInstr = keyboard.Keyboard()

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
fixcross = visual.TextStim(win=win, name='fixcross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "dots"
dotsClock = core.Clock()
backgroundDots = visual.ShapeStim(
    win=win, name='backgroundDots',
    size=(0.75, 0.75), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
stimulusDots = visual.DotStim(
    win=win, name='stimulusDots',
    nDots=250, dotSize=10.0,
    speed=0.01, dir=1.0, coherence=0.08,
    fieldPos=(0.0, 0.0), fieldSize=0.75,fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=5.0,
    color=[1.0,1.0,1.0], colorSpace='rgb', opacity=None,
    depth=-2.0)
respDots = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
textFeedback = visual.TextStim(win=win, name='textFeedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "staircase_instruction"
staircase_instructionClock = core.Clock()
textStaircaseInstr = visual.TextStim(win=win, name='textStaircaseInstr',
    text='Aufgepasst, jetzt startet die Schwellenmessung.\n\nDrücken Sie die Leertaste, wenn Sie soweit sind.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
win.color = 'black'
respStaircaseInstr = keyboard.Keyboard()

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
fixcross = visual.TextStim(win=win, name='fixcross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "dots"
dotsClock = core.Clock()
backgroundDots = visual.ShapeStim(
    win=win, name='backgroundDots',
    size=(0.75, 0.75), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
stimulusDots = visual.DotStim(
    win=win, name='stimulusDots',
    nDots=250, dotSize=10.0,
    speed=0.01, dir=1.0, coherence=0.08,
    fieldPos=(0.0, 0.0), fieldSize=0.75,fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=5.0,
    color=[1.0,1.0,1.0], colorSpace='rgb', opacity=None,
    depth=-2.0)
respDots = keyboard.Keyboard()

# Initialize components for Routine "speed_instruction"
speed_instructionClock = core.Clock()
textSpeedInst = visual.TextStim(win=win, name='textSpeedInst',
    text='Wir sind nun mit den Übungsdurchgängen fertig und werden zum Hauptexperiment übergehen.\n\nBitte versuchen Sie, so schnell wie möglich zu antworten.\n\nDrücken Sie [ Leertaste ], um das Hauptexperiment zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
respSpeedInstr = keyboard.Keyboard()

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
fixcross = visual.TextStim(win=win, name='fixcross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "dots"
dotsClock = core.Clock()
backgroundDots = visual.ShapeStim(
    win=win, name='backgroundDots',
    size=(0.75, 0.75), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
stimulusDots = visual.DotStim(
    win=win, name='stimulusDots',
    nDots=250, dotSize=10.0,
    speed=0.01, dir=1.0, coherence=0.08,
    fieldPos=(0.0, 0.0), fieldSize=0.75,fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=5.0,
    color=[1.0,1.0,1.0], colorSpace='rgb', opacity=None,
    depth=-2.0)
respDots = keyboard.Keyboard()

# Initialize components for Routine "accuracy_instruction"
accuracy_instructionClock = core.Clock()
textAccuracyInstr = visual.TextStim(win=win, name='textAccuracyInstr',
    text='Wir sind nun mit dem ersten Hauptexperiment fertig. Sie werden nun zum zweitem Hauptexperiment übergehen.\n\nBitte versuchen Sie diesesmal so richtig wie möglich zu antworten.\n\nDrücken Sie [ Leertaste ], um das zweite Hauptexperiment zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
respAccuracyInstr = keyboard.Keyboard()

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
fixcross = visual.TextStim(win=win, name='fixcross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "dots"
dotsClock = core.Clock()
backgroundDots = visual.ShapeStim(
    win=win, name='backgroundDots',
    size=(0.75, 0.75), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
stimulusDots = visual.DotStim(
    win=win, name='stimulusDots',
    nDots=250, dotSize=10.0,
    speed=0.01, dir=1.0, coherence=0.08,
    fieldPos=(0.0, 0.0), fieldSize=0.75,fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=5.0,
    color=[1.0,1.0,1.0], colorSpace='rgb', opacity=None,
    depth=-2.0)
respDots = keyboard.Keyboard()

# Initialize components for Routine "goodbye"
goodbyeClock = core.Clock()
goodbye_text = visual.TextStim(win=win, name='goodbye_text',
    text='Sie sind am Ende angelangt. \n\nVielen Dank, dass sie an diesem Experiment teilgenommen haben. :)',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "participantID"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
participantIDComponents = []
for thisComponent in participantIDComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
participantIDClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "participantID"-------
while continueRoutine:
    # get current time
    t = participantIDClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=participantIDClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in participantIDComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "participantID"-------
for thisComponent in participantIDComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "participantID" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction"-------
continueRoutine = True
# update component parameters for each repeat
respInstr.keys = []
respInstr.rt = []
_respInstr_allKeys = []
# keep track of which components have finished
instructionComponents = [textInstr, respInstr]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textInstr* updates
    if textInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textInstr.frameNStart = frameN  # exact frame index
        textInstr.tStart = t  # local t and not account for scr refresh
        textInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textInstr, 'tStartRefresh')  # time at next scr refresh
        textInstr.setAutoDraw(True)
    
    # *respInstr* updates
    waitOnFlip = False
    if respInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        respInstr.frameNStart = frameN  # exact frame index
        respInstr.tStart = t  # local t and not account for scr refresh
        respInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respInstr, 'tStartRefresh')  # time at next scr refresh
        respInstr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(respInstr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(respInstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if respInstr.status == STARTED and not waitOnFlip:
        theseKeys = respInstr.getKeys(keyList=['space'], waitRelease=False)
        _respInstr_allKeys.extend(theseKeys)
        if len(_respInstr_allKeys):
            respInstr.keys = _respInstr_allKeys[-1].name  # just the last key pressed
            respInstr.rt = _respInstr_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textInstr.started', textInstr.tStartRefresh)
thisExp.addData('textInstr.stopped', textInstr.tStopRefresh)
# check responses
if respInstr.keys in ['', [], None]:  # No response was made
    respInstr.keys = None
thisExp.addData('respInstr.keys',respInstr.keys)
if respInstr.keys != None:  # we had a response
    thisExp.addData('respInstr.rt', respInstr.rt)
thisExp.addData('respInstr.started', respInstr.tStartRefresh)
thisExp.addData('respInstr.stopped', respInstr.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_run_loop = data.TrialHandler(nReps=8.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('rdk_conditions.csv'),
    seed=None, name='practice_run_loop')
thisExp.addLoop(practice_run_loop)  # add the loop to the experiment
thisPractice_run_loop = practice_run_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_run_loop.rgb)
if thisPractice_run_loop != None:
    for paramName in thisPractice_run_loop:
        exec('{} = thisPractice_run_loop[paramName]'.format(paramName))

for thisPractice_run_loop in practice_run_loop:
    currentLoop = practice_run_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_run_loop.rgb)
    if thisPractice_run_loop != None:
        for paramName in thisPractice_run_loop:
            exec('{} = thisPractice_run_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    # update component parameters for each repeat
    # Before the fixation cross (the one before the cue) is displayed, randomly
    # choose a duration for it. Since we are using seconds as time unit, these
    # numbers correspond to 100ms, 350ms, 800ms and 1200ms.
    fixation_pre = randchoice([0.1, 0.35, 0.8, 1.2])
    # keep track of which components have finished
    ITIComponents = [fixcross]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixcross* updates
        if fixcross.status == NOT_STARTED and tThisFlip >= fixation_pre-frameTolerance:
            # keep track of start time/frame for later
            fixcross.frameNStart = frameN  # exact frame index
            fixcross.tStart = t  # local t and not account for scr refresh
            fixcross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
            fixcross.setAutoDraw(True)
        if fixcross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixcross.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fixcross.tStop = t  # not accounting for scr refresh
                fixcross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixcross, 'tStopRefresh')  # time at next scr refresh
                fixcross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_run_loop.addData('fixcross.started', fixcross.tStartRefresh)
    practice_run_loop.addData('fixcross.stopped', fixcross.tStopRefresh)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "dots"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if direction == "right":
        dots_direction = 0
    elif direction == "left":
        dots_direction = 180
    stimulusDots.setDir(dots_direction)
    stimulusDots.refreshDots()
    respDots.keys = []
    respDots.rt = []
    _respDots_allKeys = []
    # keep track of which components have finished
    dotsComponents = [backgroundDots, stimulusDots, respDots]
    for thisComponent in dotsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    dotsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "dots"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = dotsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=dotsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *backgroundDots* updates
        if backgroundDots.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            backgroundDots.frameNStart = frameN  # exact frame index
            backgroundDots.tStart = t  # local t and not account for scr refresh
            backgroundDots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(backgroundDots, 'tStartRefresh')  # time at next scr refresh
            backgroundDots.setAutoDraw(True)
        if backgroundDots.status == STARTED:
            if frameN >= (backgroundDots.frameNStart + 90):
                # keep track of stop time/frame for later
                backgroundDots.tStop = t  # not accounting for scr refresh
                backgroundDots.frameNStop = frameN  # exact frame index
                win.timeOnFlip(backgroundDots, 'tStopRefresh')  # time at next scr refresh
                backgroundDots.setAutoDraw(False)
        
        # *stimulusDots* updates
        if stimulusDots.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            stimulusDots.frameNStart = frameN  # exact frame index
            stimulusDots.tStart = t  # local t and not account for scr refresh
            stimulusDots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulusDots, 'tStartRefresh')  # time at next scr refresh
            stimulusDots.setAutoDraw(True)
        if stimulusDots.status == STARTED:
            if frameN >= (stimulusDots.frameNStart + 90):
                # keep track of stop time/frame for later
                stimulusDots.tStop = t  # not accounting for scr refresh
                stimulusDots.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimulusDots, 'tStopRefresh')  # time at next scr refresh
                stimulusDots.setAutoDraw(False)
        
        # *respDots* updates
        waitOnFlip = False
        if respDots.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            respDots.frameNStart = frameN  # exact frame index
            respDots.tStart = t  # local t and not account for scr refresh
            respDots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respDots, 'tStartRefresh')  # time at next scr refresh
            respDots.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respDots.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respDots.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respDots.status == STARTED:
            if frameN >= (respDots.frameNStart + 90):
                # keep track of stop time/frame for later
                respDots.tStop = t  # not accounting for scr refresh
                respDots.frameNStop = frameN  # exact frame index
                win.timeOnFlip(respDots, 'tStopRefresh')  # time at next scr refresh
                respDots.status = FINISHED
        if respDots.status == STARTED and not waitOnFlip:
            theseKeys = respDots.getKeys(keyList=['left', 'right'], waitRelease=False)
            _respDots_allKeys.extend(theseKeys)
            if len(_respDots_allKeys):
                respDots.keys = _respDots_allKeys[-1].name  # just the last key pressed
                respDots.rt = _respDots_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dotsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "dots"-------
    for thisComponent in dotsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_run_loop.addData('backgroundDots.started', backgroundDots.tStartRefresh)
    practice_run_loop.addData('backgroundDots.stopped', backgroundDots.tStopRefresh)
    practice_run_loop.addData('stimulusDots.started', stimulusDots.tStartRefresh)
    practice_run_loop.addData('stimulusDots.stopped', stimulusDots.tStopRefresh)
    # check responses
    if respDots.keys in ['', [], None]:  # No response was made
        respDots.keys = None
    practice_run_loop.addData('respDots.keys',respDots.keys)
    if respDots.keys != None:  # we had a response
        practice_run_loop.addData('respDots.rt', respDots.rt)
    practice_run_loop.addData('respDots.started', respDots.tStartRefresh)
    practice_run_loop.addData('respDots.stopped', respDots.tStopRefresh)
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # If the participant did not respond at all, set the response text to 'miss'.
    # You can figure that out by checking whether the given response 'None'.
    # 'None' in Python means a values is not defined, so when
    # dots_main_keyboard_resp.keys is 'None' we know the participant did not respond.
    if respDots.keys is None:
        response_text = "verpasst"
    
    # If the response time (rt) was shorter than 100ms, set the response text to
    # 'too fast' (like Mulder et al., 2012 did).
    # You can get the response time from the Keyboard component that was used to
    # capture the response (name_of_the_keyboard_component.rt).
    elif respDots.rt <= 0.1:
        response_text = "zu schnell"
    
    # If the response time was between 100ms and 1500ms (i.e. it was valid), give
    # feedback. If the repsonse was also correct, set the response text to '+5 points',
    # if it was wrong, set the response text to '+0 points'.
    # The variable 'direction' is a loop variable storing the stimulus direction for
    # the current trial.
    else:
        if (direction == "left" and respDots.keys == "left" or 
            direction == "right" and respDots.keys == "right"
        ):
            response_text = "richtig"
        else:
            response_text = "falsch"
            
    textFeedback.setText(response_text)
    # keep track of which components have finished
    feedbackComponents = [textFeedback]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textFeedback* updates
        if textFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textFeedback.frameNStart = frameN  # exact frame index
            textFeedback.tStart = t  # local t and not account for scr refresh
            textFeedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textFeedback, 'tStartRefresh')  # time at next scr refresh
            textFeedback.setAutoDraw(True)
        if textFeedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textFeedback.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textFeedback.tStop = t  # not accounting for scr refresh
                textFeedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textFeedback, 'tStopRefresh')  # time at next scr refresh
                textFeedback.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_run_loop.addData('textFeedback.started', textFeedback.tStartRefresh)
    practice_run_loop.addData('textFeedback.stopped', textFeedback.tStopRefresh)
    thisExp.nextEntry()
    
# completed 8.0 repeats of 'practice_run_loop'


# ------Prepare to start Routine "staircase_instruction"-------
continueRoutine = True
# update component parameters for each repeat
respStaircaseInstr.keys = []
respStaircaseInstr.rt = []
_respStaircaseInstr_allKeys = []
# keep track of which components have finished
staircase_instructionComponents = [textStaircaseInstr, respStaircaseInstr]
for thisComponent in staircase_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
staircase_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "staircase_instruction"-------
while continueRoutine:
    # get current time
    t = staircase_instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=staircase_instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textStaircaseInstr* updates
    if textStaircaseInstr.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        textStaircaseInstr.frameNStart = frameN  # exact frame index
        textStaircaseInstr.tStart = t  # local t and not account for scr refresh
        textStaircaseInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textStaircaseInstr, 'tStartRefresh')  # time at next scr refresh
        textStaircaseInstr.setAutoDraw(True)
    
    # *respStaircaseInstr* updates
    waitOnFlip = False
    if respStaircaseInstr.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        respStaircaseInstr.frameNStart = frameN  # exact frame index
        respStaircaseInstr.tStart = t  # local t and not account for scr refresh
        respStaircaseInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respStaircaseInstr, 'tStartRefresh')  # time at next scr refresh
        respStaircaseInstr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(respStaircaseInstr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(respStaircaseInstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if respStaircaseInstr.status == STARTED and not waitOnFlip:
        theseKeys = respStaircaseInstr.getKeys(keyList=['space'], waitRelease=False)
        _respStaircaseInstr_allKeys.extend(theseKeys)
        if len(_respStaircaseInstr_allKeys):
            respStaircaseInstr.keys = _respStaircaseInstr_allKeys[-1].name  # just the last key pressed
            respStaircaseInstr.rt = _respStaircaseInstr_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in staircase_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "staircase_instruction"-------
for thisComponent in staircase_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textStaircaseInstr.started', textStaircaseInstr.tStartRefresh)
thisExp.addData('textStaircaseInstr.stopped', textStaircaseInstr.tStopRefresh)
# check responses
if respStaircaseInstr.keys in ['', [], None]:  # No response was made
    respStaircaseInstr.keys = None
thisExp.addData('respStaircaseInstr.keys',respStaircaseInstr.keys)
if respStaircaseInstr.keys != None:  # we had a response
    thisExp.addData('respStaircaseInstr.rt', respStaircaseInstr.rt)
thisExp.addData('respStaircaseInstr.started', respStaircaseInstr.tStartRefresh)
thisExp.addData('respStaircaseInstr.stopped', respStaircaseInstr.tStopRefresh)
thisExp.nextEntry()
# the Routine "staircase_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --------Prepare to start Staircase "staircase_run_loop" --------
# set up handler to look after next chosen value etc
staircase_run_loop = data.StairHandler(startVal=0.5, extraInfo=expInfo,
    stepSizes=[0.8,0.8,0.4,0.4,0.2], stepType='log',
    nReversals=0.0, nTrials=1.0, 
    nUp=1.0, nDown=3.0,
    minVal=0.0, maxVal=1.0,
    originPath=-1, name='staircase_run_loop')
thisExp.addLoop(staircase_run_loop)  # add the loop to the experiment
level = thisStaircase_run_loop = 0.5  # initialise some vals

for thisStaircase_run_loop in staircase_run_loop:
    currentLoop = staircase_run_loop
    level = thisStaircase_run_loop
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    # update component parameters for each repeat
    # Before the fixation cross (the one before the cue) is displayed, randomly
    # choose a duration for it. Since we are using seconds as time unit, these
    # numbers correspond to 100ms, 350ms, 800ms and 1200ms.
    fixation_pre = randchoice([0.1, 0.35, 0.8, 1.2])
    # keep track of which components have finished
    ITIComponents = [fixcross]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixcross* updates
        if fixcross.status == NOT_STARTED and tThisFlip >= fixation_pre-frameTolerance:
            # keep track of start time/frame for later
            fixcross.frameNStart = frameN  # exact frame index
            fixcross.tStart = t  # local t and not account for scr refresh
            fixcross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
            fixcross.setAutoDraw(True)
        if fixcross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixcross.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fixcross.tStop = t  # not accounting for scr refresh
                fixcross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixcross, 'tStopRefresh')  # time at next scr refresh
                fixcross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    staircase_run_loop.addOtherData('fixcross.started', fixcross.tStartRefresh)
    staircase_run_loop.addOtherData('fixcross.stopped', fixcross.tStopRefresh)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "dots"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if direction == "right":
        dots_direction = 0
    elif direction == "left":
        dots_direction = 180
    stimulusDots.setDir(dots_direction)
    stimulusDots.refreshDots()
    respDots.keys = []
    respDots.rt = []
    _respDots_allKeys = []
    # keep track of which components have finished
    dotsComponents = [backgroundDots, stimulusDots, respDots]
    for thisComponent in dotsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    dotsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "dots"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = dotsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=dotsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *backgroundDots* updates
        if backgroundDots.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            backgroundDots.frameNStart = frameN  # exact frame index
            backgroundDots.tStart = t  # local t and not account for scr refresh
            backgroundDots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(backgroundDots, 'tStartRefresh')  # time at next scr refresh
            backgroundDots.setAutoDraw(True)
        if backgroundDots.status == STARTED:
            if frameN >= (backgroundDots.frameNStart + 90):
                # keep track of stop time/frame for later
                backgroundDots.tStop = t  # not accounting for scr refresh
                backgroundDots.frameNStop = frameN  # exact frame index
                win.timeOnFlip(backgroundDots, 'tStopRefresh')  # time at next scr refresh
                backgroundDots.setAutoDraw(False)
        
        # *stimulusDots* updates
        if stimulusDots.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            stimulusDots.frameNStart = frameN  # exact frame index
            stimulusDots.tStart = t  # local t and not account for scr refresh
            stimulusDots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulusDots, 'tStartRefresh')  # time at next scr refresh
            stimulusDots.setAutoDraw(True)
        if stimulusDots.status == STARTED:
            if frameN >= (stimulusDots.frameNStart + 90):
                # keep track of stop time/frame for later
                stimulusDots.tStop = t  # not accounting for scr refresh
                stimulusDots.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimulusDots, 'tStopRefresh')  # time at next scr refresh
                stimulusDots.setAutoDraw(False)
        
        # *respDots* updates
        waitOnFlip = False
        if respDots.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            respDots.frameNStart = frameN  # exact frame index
            respDots.tStart = t  # local t and not account for scr refresh
            respDots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respDots, 'tStartRefresh')  # time at next scr refresh
            respDots.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respDots.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respDots.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respDots.status == STARTED:
            if frameN >= (respDots.frameNStart + 90):
                # keep track of stop time/frame for later
                respDots.tStop = t  # not accounting for scr refresh
                respDots.frameNStop = frameN  # exact frame index
                win.timeOnFlip(respDots, 'tStopRefresh')  # time at next scr refresh
                respDots.status = FINISHED
        if respDots.status == STARTED and not waitOnFlip:
            theseKeys = respDots.getKeys(keyList=['left', 'right'], waitRelease=False)
            _respDots_allKeys.extend(theseKeys)
            if len(_respDots_allKeys):
                respDots.keys = _respDots_allKeys[-1].name  # just the last key pressed
                respDots.rt = _respDots_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dotsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "dots"-------
    for thisComponent in dotsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    staircase_run_loop.addOtherData('backgroundDots.started', backgroundDots.tStartRefresh)
    staircase_run_loop.addOtherData('backgroundDots.stopped', backgroundDots.tStopRefresh)
    staircase_run_loop.addOtherData('stimulusDots.started', stimulusDots.tStartRefresh)
    staircase_run_loop.addOtherData('stimulusDots.stopped', stimulusDots.tStopRefresh)
    # check responses
    if respDots.keys in ['', [], None]:  # No response was made
        respDots.keys = None
    staircase_run_loop.addOtherData('respDots.started', respDots.tStartRefresh)
    staircase_run_loop.addOtherData('respDots.stopped', respDots.tStopRefresh)
    thisExp.nextEntry()
    
# staircase completed


# ------Prepare to start Routine "speed_instruction"-------
continueRoutine = True
# update component parameters for each repeat
respSpeedInstr.keys = []
respSpeedInstr.rt = []
_respSpeedInstr_allKeys = []
# keep track of which components have finished
speed_instructionComponents = [textSpeedInst, respSpeedInstr]
for thisComponent in speed_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
speed_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "speed_instruction"-------
while continueRoutine:
    # get current time
    t = speed_instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=speed_instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textSpeedInst* updates
    if textSpeedInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textSpeedInst.frameNStart = frameN  # exact frame index
        textSpeedInst.tStart = t  # local t and not account for scr refresh
        textSpeedInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textSpeedInst, 'tStartRefresh')  # time at next scr refresh
        textSpeedInst.setAutoDraw(True)
    
    # *respSpeedInstr* updates
    waitOnFlip = False
    if respSpeedInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        respSpeedInstr.frameNStart = frameN  # exact frame index
        respSpeedInstr.tStart = t  # local t and not account for scr refresh
        respSpeedInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respSpeedInstr, 'tStartRefresh')  # time at next scr refresh
        respSpeedInstr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(respSpeedInstr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(respSpeedInstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if respSpeedInstr.status == STARTED and not waitOnFlip:
        theseKeys = respSpeedInstr.getKeys(keyList=['space'], waitRelease=False)
        _respSpeedInstr_allKeys.extend(theseKeys)
        if len(_respSpeedInstr_allKeys):
            respSpeedInstr.keys = _respSpeedInstr_allKeys[-1].name  # just the last key pressed
            respSpeedInstr.rt = _respSpeedInstr_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in speed_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "speed_instruction"-------
for thisComponent in speed_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textSpeedInst.started', textSpeedInst.tStartRefresh)
thisExp.addData('textSpeedInst.stopped', textSpeedInst.tStopRefresh)
# check responses
if respSpeedInstr.keys in ['', [], None]:  # No response was made
    respSpeedInstr.keys = None
thisExp.addData('respSpeedInstr.keys',respSpeedInstr.keys)
if respSpeedInstr.keys != None:  # we had a response
    thisExp.addData('respSpeedInstr.rt', respSpeedInstr.rt)
thisExp.addData('respSpeedInstr.started', respSpeedInstr.tStartRefresh)
thisExp.addData('respSpeedInstr.stopped', respSpeedInstr.tStopRefresh)
thisExp.nextEntry()
# the Routine "speed_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
speed_run_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('rdk_conditions.csv'),
    seed=None, name='speed_run_loop')
thisExp.addLoop(speed_run_loop)  # add the loop to the experiment
thisSpeed_run_loop = speed_run_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSpeed_run_loop.rgb)
if thisSpeed_run_loop != None:
    for paramName in thisSpeed_run_loop:
        exec('{} = thisSpeed_run_loop[paramName]'.format(paramName))

for thisSpeed_run_loop in speed_run_loop:
    currentLoop = speed_run_loop
    # abbreviate parameter names if possible (e.g. rgb = thisSpeed_run_loop.rgb)
    if thisSpeed_run_loop != None:
        for paramName in thisSpeed_run_loop:
            exec('{} = thisSpeed_run_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    # update component parameters for each repeat
    # Before the fixation cross (the one before the cue) is displayed, randomly
    # choose a duration for it. Since we are using seconds as time unit, these
    # numbers correspond to 100ms, 350ms, 800ms and 1200ms.
    fixation_pre = randchoice([0.1, 0.35, 0.8, 1.2])
    # keep track of which components have finished
    ITIComponents = [fixcross]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixcross* updates
        if fixcross.status == NOT_STARTED and tThisFlip >= fixation_pre-frameTolerance:
            # keep track of start time/frame for later
            fixcross.frameNStart = frameN  # exact frame index
            fixcross.tStart = t  # local t and not account for scr refresh
            fixcross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
            fixcross.setAutoDraw(True)
        if fixcross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixcross.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fixcross.tStop = t  # not accounting for scr refresh
                fixcross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixcross, 'tStopRefresh')  # time at next scr refresh
                fixcross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    speed_run_loop.addData('fixcross.started', fixcross.tStartRefresh)
    speed_run_loop.addData('fixcross.stopped', fixcross.tStopRefresh)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "dots"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if direction == "right":
        dots_direction = 0
    elif direction == "left":
        dots_direction = 180
    stimulusDots.setDir(dots_direction)
    stimulusDots.refreshDots()
    respDots.keys = []
    respDots.rt = []
    _respDots_allKeys = []
    # keep track of which components have finished
    dotsComponents = [backgroundDots, stimulusDots, respDots]
    for thisComponent in dotsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    dotsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "dots"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = dotsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=dotsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *backgroundDots* updates
        if backgroundDots.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            backgroundDots.frameNStart = frameN  # exact frame index
            backgroundDots.tStart = t  # local t and not account for scr refresh
            backgroundDots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(backgroundDots, 'tStartRefresh')  # time at next scr refresh
            backgroundDots.setAutoDraw(True)
        if backgroundDots.status == STARTED:
            if frameN >= (backgroundDots.frameNStart + 90):
                # keep track of stop time/frame for later
                backgroundDots.tStop = t  # not accounting for scr refresh
                backgroundDots.frameNStop = frameN  # exact frame index
                win.timeOnFlip(backgroundDots, 'tStopRefresh')  # time at next scr refresh
                backgroundDots.setAutoDraw(False)
        
        # *stimulusDots* updates
        if stimulusDots.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            stimulusDots.frameNStart = frameN  # exact frame index
            stimulusDots.tStart = t  # local t and not account for scr refresh
            stimulusDots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulusDots, 'tStartRefresh')  # time at next scr refresh
            stimulusDots.setAutoDraw(True)
        if stimulusDots.status == STARTED:
            if frameN >= (stimulusDots.frameNStart + 90):
                # keep track of stop time/frame for later
                stimulusDots.tStop = t  # not accounting for scr refresh
                stimulusDots.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimulusDots, 'tStopRefresh')  # time at next scr refresh
                stimulusDots.setAutoDraw(False)
        
        # *respDots* updates
        waitOnFlip = False
        if respDots.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            respDots.frameNStart = frameN  # exact frame index
            respDots.tStart = t  # local t and not account for scr refresh
            respDots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respDots, 'tStartRefresh')  # time at next scr refresh
            respDots.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respDots.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respDots.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respDots.status == STARTED:
            if frameN >= (respDots.frameNStart + 90):
                # keep track of stop time/frame for later
                respDots.tStop = t  # not accounting for scr refresh
                respDots.frameNStop = frameN  # exact frame index
                win.timeOnFlip(respDots, 'tStopRefresh')  # time at next scr refresh
                respDots.status = FINISHED
        if respDots.status == STARTED and not waitOnFlip:
            theseKeys = respDots.getKeys(keyList=['left', 'right'], waitRelease=False)
            _respDots_allKeys.extend(theseKeys)
            if len(_respDots_allKeys):
                respDots.keys = _respDots_allKeys[-1].name  # just the last key pressed
                respDots.rt = _respDots_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dotsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "dots"-------
    for thisComponent in dotsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    speed_run_loop.addData('backgroundDots.started', backgroundDots.tStartRefresh)
    speed_run_loop.addData('backgroundDots.stopped', backgroundDots.tStopRefresh)
    speed_run_loop.addData('stimulusDots.started', stimulusDots.tStartRefresh)
    speed_run_loop.addData('stimulusDots.stopped', stimulusDots.tStopRefresh)
    # check responses
    if respDots.keys in ['', [], None]:  # No response was made
        respDots.keys = None
    speed_run_loop.addData('respDots.keys',respDots.keys)
    if respDots.keys != None:  # we had a response
        speed_run_loop.addData('respDots.rt', respDots.rt)
    speed_run_loop.addData('respDots.started', respDots.tStartRefresh)
    speed_run_loop.addData('respDots.stopped', respDots.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'speed_run_loop'


# ------Prepare to start Routine "accuracy_instruction"-------
continueRoutine = True
# update component parameters for each repeat
respAccuracyInstr.keys = []
respAccuracyInstr.rt = []
_respAccuracyInstr_allKeys = []
# keep track of which components have finished
accuracy_instructionComponents = [textAccuracyInstr, respAccuracyInstr]
for thisComponent in accuracy_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
accuracy_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "accuracy_instruction"-------
while continueRoutine:
    # get current time
    t = accuracy_instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=accuracy_instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textAccuracyInstr* updates
    if textAccuracyInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textAccuracyInstr.frameNStart = frameN  # exact frame index
        textAccuracyInstr.tStart = t  # local t and not account for scr refresh
        textAccuracyInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textAccuracyInstr, 'tStartRefresh')  # time at next scr refresh
        textAccuracyInstr.setAutoDraw(True)
    
    # *respAccuracyInstr* updates
    waitOnFlip = False
    if respAccuracyInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        respAccuracyInstr.frameNStart = frameN  # exact frame index
        respAccuracyInstr.tStart = t  # local t and not account for scr refresh
        respAccuracyInstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(respAccuracyInstr, 'tStartRefresh')  # time at next scr refresh
        respAccuracyInstr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(respAccuracyInstr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(respAccuracyInstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if respAccuracyInstr.status == STARTED and not waitOnFlip:
        theseKeys = respAccuracyInstr.getKeys(keyList=['space'], waitRelease=False)
        _respAccuracyInstr_allKeys.extend(theseKeys)
        if len(_respAccuracyInstr_allKeys):
            respAccuracyInstr.keys = _respAccuracyInstr_allKeys[-1].name  # just the last key pressed
            respAccuracyInstr.rt = _respAccuracyInstr_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in accuracy_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "accuracy_instruction"-------
for thisComponent in accuracy_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textAccuracyInstr.started', textAccuracyInstr.tStartRefresh)
thisExp.addData('textAccuracyInstr.stopped', textAccuracyInstr.tStopRefresh)
# check responses
if respAccuracyInstr.keys in ['', [], None]:  # No response was made
    respAccuracyInstr.keys = None
thisExp.addData('respAccuracyInstr.keys',respAccuracyInstr.keys)
if respAccuracyInstr.keys != None:  # we had a response
    thisExp.addData('respAccuracyInstr.rt', respAccuracyInstr.rt)
thisExp.addData('respAccuracyInstr.started', respAccuracyInstr.tStartRefresh)
thisExp.addData('respAccuracyInstr.stopped', respAccuracyInstr.tStopRefresh)
thisExp.nextEntry()
# the Routine "accuracy_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
accuracy_run_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('rdk_conditions.csv'),
    seed=None, name='accuracy_run_loop')
thisExp.addLoop(accuracy_run_loop)  # add the loop to the experiment
thisAccuracy_run_loop = accuracy_run_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAccuracy_run_loop.rgb)
if thisAccuracy_run_loop != None:
    for paramName in thisAccuracy_run_loop:
        exec('{} = thisAccuracy_run_loop[paramName]'.format(paramName))

for thisAccuracy_run_loop in accuracy_run_loop:
    currentLoop = accuracy_run_loop
    # abbreviate parameter names if possible (e.g. rgb = thisAccuracy_run_loop.rgb)
    if thisAccuracy_run_loop != None:
        for paramName in thisAccuracy_run_loop:
            exec('{} = thisAccuracy_run_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    # update component parameters for each repeat
    # Before the fixation cross (the one before the cue) is displayed, randomly
    # choose a duration for it. Since we are using seconds as time unit, these
    # numbers correspond to 100ms, 350ms, 800ms and 1200ms.
    fixation_pre = randchoice([0.1, 0.35, 0.8, 1.2])
    # keep track of which components have finished
    ITIComponents = [fixcross]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixcross* updates
        if fixcross.status == NOT_STARTED and tThisFlip >= fixation_pre-frameTolerance:
            # keep track of start time/frame for later
            fixcross.frameNStart = frameN  # exact frame index
            fixcross.tStart = t  # local t and not account for scr refresh
            fixcross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
            fixcross.setAutoDraw(True)
        if fixcross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixcross.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fixcross.tStop = t  # not accounting for scr refresh
                fixcross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixcross, 'tStopRefresh')  # time at next scr refresh
                fixcross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    accuracy_run_loop.addData('fixcross.started', fixcross.tStartRefresh)
    accuracy_run_loop.addData('fixcross.stopped', fixcross.tStopRefresh)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "dots"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if direction == "right":
        dots_direction = 0
    elif direction == "left":
        dots_direction = 180
    stimulusDots.setDir(dots_direction)
    stimulusDots.refreshDots()
    respDots.keys = []
    respDots.rt = []
    _respDots_allKeys = []
    # keep track of which components have finished
    dotsComponents = [backgroundDots, stimulusDots, respDots]
    for thisComponent in dotsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    dotsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "dots"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = dotsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=dotsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *backgroundDots* updates
        if backgroundDots.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            backgroundDots.frameNStart = frameN  # exact frame index
            backgroundDots.tStart = t  # local t and not account for scr refresh
            backgroundDots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(backgroundDots, 'tStartRefresh')  # time at next scr refresh
            backgroundDots.setAutoDraw(True)
        if backgroundDots.status == STARTED:
            if frameN >= (backgroundDots.frameNStart + 90):
                # keep track of stop time/frame for later
                backgroundDots.tStop = t  # not accounting for scr refresh
                backgroundDots.frameNStop = frameN  # exact frame index
                win.timeOnFlip(backgroundDots, 'tStopRefresh')  # time at next scr refresh
                backgroundDots.setAutoDraw(False)
        
        # *stimulusDots* updates
        if stimulusDots.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            stimulusDots.frameNStart = frameN  # exact frame index
            stimulusDots.tStart = t  # local t and not account for scr refresh
            stimulusDots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimulusDots, 'tStartRefresh')  # time at next scr refresh
            stimulusDots.setAutoDraw(True)
        if stimulusDots.status == STARTED:
            if frameN >= (stimulusDots.frameNStart + 90):
                # keep track of stop time/frame for later
                stimulusDots.tStop = t  # not accounting for scr refresh
                stimulusDots.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimulusDots, 'tStopRefresh')  # time at next scr refresh
                stimulusDots.setAutoDraw(False)
        
        # *respDots* updates
        waitOnFlip = False
        if respDots.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            respDots.frameNStart = frameN  # exact frame index
            respDots.tStart = t  # local t and not account for scr refresh
            respDots.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respDots, 'tStartRefresh')  # time at next scr refresh
            respDots.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respDots.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respDots.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respDots.status == STARTED:
            if frameN >= (respDots.frameNStart + 90):
                # keep track of stop time/frame for later
                respDots.tStop = t  # not accounting for scr refresh
                respDots.frameNStop = frameN  # exact frame index
                win.timeOnFlip(respDots, 'tStopRefresh')  # time at next scr refresh
                respDots.status = FINISHED
        if respDots.status == STARTED and not waitOnFlip:
            theseKeys = respDots.getKeys(keyList=['left', 'right'], waitRelease=False)
            _respDots_allKeys.extend(theseKeys)
            if len(_respDots_allKeys):
                respDots.keys = _respDots_allKeys[-1].name  # just the last key pressed
                respDots.rt = _respDots_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dotsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "dots"-------
    for thisComponent in dotsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    accuracy_run_loop.addData('backgroundDots.started', backgroundDots.tStartRefresh)
    accuracy_run_loop.addData('backgroundDots.stopped', backgroundDots.tStopRefresh)
    accuracy_run_loop.addData('stimulusDots.started', stimulusDots.tStartRefresh)
    accuracy_run_loop.addData('stimulusDots.stopped', stimulusDots.tStopRefresh)
    # check responses
    if respDots.keys in ['', [], None]:  # No response was made
        respDots.keys = None
    accuracy_run_loop.addData('respDots.keys',respDots.keys)
    if respDots.keys != None:  # we had a response
        accuracy_run_loop.addData('respDots.rt', respDots.rt)
    accuracy_run_loop.addData('respDots.started', respDots.tStartRefresh)
    accuracy_run_loop.addData('respDots.stopped', respDots.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'accuracy_run_loop'


# ------Prepare to start Routine "goodbye"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
goodbyeComponents = [goodbye_2, goodbye_text]
for thisComponent in goodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
goodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "goodbye"-------
while continueRoutine:
    # get current time
    t = goodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=goodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *goodbye_text* updates
    if goodbye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goodbye_text.frameNStart = frameN  # exact frame index
        goodbye_text.tStart = t  # local t and not account for scr refresh
        goodbye_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goodbye_text, 'tStartRefresh')  # time at next scr refresh
        goodbye_text.setAutoDraw(True)
    if goodbye_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > goodbye_text.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            goodbye_text.tStop = t  # not accounting for scr refresh
            goodbye_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(goodbye_text, 'tStopRefresh')  # time at next scr refresh
            goodbye_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "goodbye"-------
for thisComponent in goodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('goodbye_text.started', goodbye_text.tStartRefresh)
thisExp.addData('goodbye_text.stopped', goodbye_text.tStopRefresh)
# the Routine "goodbye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

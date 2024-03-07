#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on März 07, 2024, at 12:50
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2023.2.3')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'random_dot'  # from the Builder filename that created this script
expInfo = {
    'participant': 'sub-' + f"{randint(0, 99999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\GIT\\neuroscicomplabFS24\\exp\\rd\\random_dot_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1920, 1200], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instruction" ---
    textInstr = visual.TextStim(win=win, name='textInstr',
        text='Willkommen zum Experiment.\n\nIm Folgenden werden Sie eine Reihe von Aufgaben lösen. Ihnen wird ein Kreis voller Punkte präsentiert. Einige dieser Punkte bewegen sich entweder nach links oder nach rechts. Ihre Aufgabe ist es, zu entscheiden, in welche Richtung sie sich bewegen.\n\nDrücken Sie die linke Pfeiltaste, wenn Sie glauben, dass sich die Punkte nach links bewegen, oder die rechte Pfeiltaste, wenn Sie glauben, dass sie sich nach rechts bewegen.\n\nBitte konzentrieren Sie sich immer auf das kleine Kreuz auf dem Bildschirm, wenn nichts anderes angezeigt wird.\n\nDrücken Sie [ Leertaste ], um mit dem Übungsdurchgang zu beginnen, wenn Sie bereit sind.\n\n',
        font='Open Sans',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from codeInstr
    win.color = 'black'
    respInstr = keyboard.Keyboard()
    
    # --- Initialize components for Routine "ITI" ---
    fixcross = visual.TextStim(win=win, name='fixcross',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "dots" ---
    backgroundDots = visual.ShapeStim(
        win=win, name='backgroundDots',
        size=(0.75, 0.75), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-1.0, interpolate=True)
    stimulusDots = visual.DotStim(
        win=win, name='stimulusDots',
        nDots=250, dotSize=10.0,
        speed=0.01, dir=1.0, coherence=0.08,
        fieldPos=(0.0, 0.0), fieldSize=0.75, fieldAnchor='center', fieldShape='circle',
        signalDots='same', noiseDots='walk',dotLife=5.0,
        color=[1.0,1.0,1.0], colorSpace='rgb', opacity=None,
        depth=-2.0)
    respDots = keyboard.Keyboard()
    
    # --- Initialize components for Routine "feedback" ---
    textFeedback = visual.TextStim(win=win, name='textFeedback',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "instruction_1" ---
    textSpeedInst = visual.TextStim(win=win, name='textSpeedInst',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    respSpeedInstr = keyboard.Keyboard()
    
    # --- Initialize components for Routine "ITI" ---
    fixcross = visual.TextStim(win=win, name='fixcross',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "dots" ---
    backgroundDots = visual.ShapeStim(
        win=win, name='backgroundDots',
        size=(0.75, 0.75), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-1.0, interpolate=True)
    stimulusDots = visual.DotStim(
        win=win, name='stimulusDots',
        nDots=250, dotSize=10.0,
        speed=0.01, dir=1.0, coherence=0.08,
        fieldPos=(0.0, 0.0), fieldSize=0.75, fieldAnchor='center', fieldShape='circle',
        signalDots='same', noiseDots='walk',dotLife=5.0,
        color=[1.0,1.0,1.0], colorSpace='rgb', opacity=None,
        depth=-2.0)
    respDots = keyboard.Keyboard()
    
    # --- Initialize components for Routine "instruction_2" ---
    textAccuracyInstr = visual.TextStim(win=win, name='textAccuracyInstr',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    respAccuracyInstr = keyboard.Keyboard()
    
    # --- Initialize components for Routine "ITI" ---
    fixcross = visual.TextStim(win=win, name='fixcross',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "dots" ---
    backgroundDots = visual.ShapeStim(
        win=win, name='backgroundDots',
        size=(0.75, 0.75), vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-1.0, interpolate=True)
    stimulusDots = visual.DotStim(
        win=win, name='stimulusDots',
        nDots=250, dotSize=10.0,
        speed=0.01, dir=1.0, coherence=0.08,
        fieldPos=(0.0, 0.0), fieldSize=0.75, fieldAnchor='center', fieldShape='circle',
        signalDots='same', noiseDots='walk',dotLife=5.0,
        color=[1.0,1.0,1.0], colorSpace='rgb', opacity=None,
        depth=-2.0)
    respDots = keyboard.Keyboard()
    
    # --- Initialize components for Routine "goodbye" ---
    goodbye_text = visual.TextStim(win=win, name='goodbye_text',
        text='Sie sind am Ende angelangt. \n\nVielen Dank, dass sie an diesem Experiment teilgenommen haben. :)',
        font='Open Sans',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "instruction" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instruction.started', globalClock.getTime())
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
    frameN = -1
    
    # --- Run Routine "instruction" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textInstr* updates
        
        # if textInstr is starting this frame...
        if textInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textInstr.frameNStart = frameN  # exact frame index
            textInstr.tStart = t  # local t and not account for scr refresh
            textInstr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textInstr, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textInstr.started')
            # update status
            textInstr.status = STARTED
            textInstr.setAutoDraw(True)
        
        # if textInstr is active this frame...
        if textInstr.status == STARTED:
            # update params
            pass
        
        # *respInstr* updates
        waitOnFlip = False
        
        # if respInstr is starting this frame...
        if respInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respInstr.frameNStart = frameN  # exact frame index
            respInstr.tStart = t  # local t and not account for scr refresh
            respInstr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respInstr, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'respInstr.started')
            # update status
            respInstr.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respInstr.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respInstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respInstr.status == STARTED and not waitOnFlip:
            theseKeys = respInstr.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _respInstr_allKeys.extend(theseKeys)
            if len(_respInstr_allKeys):
                respInstr.keys = _respInstr_allKeys[-1].name  # just the last key pressed
                respInstr.rt = _respInstr_allKeys[-1].rt
                respInstr.duration = _respInstr_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction" ---
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instruction.stopped', globalClock.getTime())
    # check responses
    if respInstr.keys in ['', [], None]:  # No response was made
        respInstr.keys = None
    thisExp.addData('respInstr.keys',respInstr.keys)
    if respInstr.keys != None:  # we had a response
        thisExp.addData('respInstr.rt', respInstr.rt)
        thisExp.addData('respInstr.duration', respInstr.duration)
    thisExp.nextEntry()
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_run_loop = data.TrialHandler(nReps=10.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('random_dot_conditions.csv'),
        seed=None, name='practice_run_loop')
    thisExp.addLoop(practice_run_loop)  # add the loop to the experiment
    thisPractice_run_loop = practice_run_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_run_loop.rgb)
    if thisPractice_run_loop != None:
        for paramName in thisPractice_run_loop:
            globals()[paramName] = thisPractice_run_loop[paramName]
    
    for thisPractice_run_loop in practice_run_loop:
        currentLoop = practice_run_loop
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_run_loop.rgb)
        if thisPractice_run_loop != None:
            for paramName in thisPractice_run_loop:
                globals()[paramName] = thisPractice_run_loop[paramName]
        
        # --- Prepare to start Routine "ITI" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('ITI.started', globalClock.getTime())
        # Run 'Begin Routine' code from preFixcross
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
        frameN = -1
        
        # --- Run Routine "ITI" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixcross* updates
            
            # if fixcross is starting this frame...
            if fixcross.status == NOT_STARTED and tThisFlip >= fixation_pre-frameTolerance:
                # keep track of start time/frame for later
                fixcross.frameNStart = frameN  # exact frame index
                fixcross.tStart = t  # local t and not account for scr refresh
                fixcross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixcross.started')
                # update status
                fixcross.status = STARTED
                fixcross.setAutoDraw(True)
            
            # if fixcross is active this frame...
            if fixcross.status == STARTED:
                # update params
                pass
            
            # if fixcross is stopping this frame...
            if fixcross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixcross.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    fixcross.tStop = t  # not accounting for scr refresh
                    fixcross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixcross.stopped')
                    # update status
                    fixcross.status = FINISHED
                    fixcross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('ITI.stopped', globalClock.getTime())
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "dots" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('dots.started', globalClock.getTime())
        # Run 'Begin Routine' code from codeDots
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
        frameN = -1
        
        # --- Run Routine "dots" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *backgroundDots* updates
            
            # if backgroundDots is starting this frame...
            if backgroundDots.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                backgroundDots.frameNStart = frameN  # exact frame index
                backgroundDots.tStart = t  # local t and not account for scr refresh
                backgroundDots.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(backgroundDots, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'backgroundDots.started')
                # update status
                backgroundDots.status = STARTED
                backgroundDots.setAutoDraw(True)
            
            # if backgroundDots is active this frame...
            if backgroundDots.status == STARTED:
                # update params
                pass
            
            # if backgroundDots is stopping this frame...
            if backgroundDots.status == STARTED:
                if frameN >= (backgroundDots.frameNStart + 90):
                    # keep track of stop time/frame for later
                    backgroundDots.tStop = t  # not accounting for scr refresh
                    backgroundDots.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'backgroundDots.stopped')
                    # update status
                    backgroundDots.status = FINISHED
                    backgroundDots.setAutoDraw(False)
            
            # *stimulusDots* updates
            
            # if stimulusDots is starting this frame...
            if stimulusDots.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                stimulusDots.frameNStart = frameN  # exact frame index
                stimulusDots.tStart = t  # local t and not account for scr refresh
                stimulusDots.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulusDots, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulusDots.started')
                # update status
                stimulusDots.status = STARTED
                stimulusDots.setAutoDraw(True)
            
            # if stimulusDots is active this frame...
            if stimulusDots.status == STARTED:
                # update params
                pass
            
            # if stimulusDots is stopping this frame...
            if stimulusDots.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 5-frameTolerance:
                    # keep track of stop time/frame for later
                    stimulusDots.tStop = t  # not accounting for scr refresh
                    stimulusDots.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimulusDots.stopped')
                    # update status
                    stimulusDots.status = FINISHED
                    stimulusDots.setAutoDraw(False)
            
            # *respDots* updates
            waitOnFlip = False
            
            # if respDots is starting this frame...
            if respDots.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                respDots.frameNStart = frameN  # exact frame index
                respDots.tStart = t  # local t and not account for scr refresh
                respDots.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respDots, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respDots.started')
                # update status
                respDots.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respDots.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respDots.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respDots.status == STARTED and not waitOnFlip:
                theseKeys = respDots.getKeys(keyList=['left', 'right'], ignoreKeys=["escape"], waitRelease=False)
                _respDots_allKeys.extend(theseKeys)
                if len(_respDots_allKeys):
                    respDots.keys = _respDots_allKeys[-1].name  # just the last key pressed
                    respDots.rt = _respDots_allKeys[-1].rt
                    respDots.duration = _respDots_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in dotsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "dots" ---
        for thisComponent in dotsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('dots.stopped', globalClock.getTime())
        # check responses
        if respDots.keys in ['', [], None]:  # No response was made
            respDots.keys = None
        practice_run_loop.addData('respDots.keys',respDots.keys)
        if respDots.keys != None:  # we had a response
            practice_run_loop.addData('respDots.rt', respDots.rt)
            practice_run_loop.addData('respDots.duration', respDots.duration)
        # the Routine "dots" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime())
        # Run 'Begin Routine' code from codeFeedback
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
        frameN = -1
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textFeedback* updates
            
            # if textFeedback is starting this frame...
            if textFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textFeedback.frameNStart = frameN  # exact frame index
                textFeedback.tStart = t  # local t and not account for scr refresh
                textFeedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textFeedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textFeedback.started')
                # update status
                textFeedback.status = STARTED
                textFeedback.setAutoDraw(True)
            
            # if textFeedback is active this frame...
            if textFeedback.status == STARTED:
                # update params
                pass
            
            # if textFeedback is stopping this frame...
            if textFeedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textFeedback.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    textFeedback.tStop = t  # not accounting for scr refresh
                    textFeedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textFeedback.stopped')
                    # update status
                    textFeedback.status = FINISHED
                    textFeedback.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 10.0 repeats of 'practice_run_loop'
    
    
    # --- Prepare to start Routine "instruction_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instruction_1.started', globalClock.getTime())
    # Run 'Begin Routine' code from codeInstr_2
    #from psychopy import visual, core, event
    import random
    
    # Liste der beiden möglichen Anweisungen
    instructions = ['speed', 'accuracy']
    
    # Zufällige Auswahl einer Anweisung aus der Liste
    selected_instruction = random.choice(instructions)
    
    # Initialisiere die Variable instruction_text
    instruction_text = ""
    
    # Überprüfe, welche Anweisung ausgewählt wurde
    if selected_instruction == "speed":
        instruction_text = "Wir sind nun mit dem Übungsdurchgang fertig und werden zum Hauptexperiment übergehen. Bitte versuchen Sie so schnell wie möglich zu antworten. Drücken Sie [Leertaste], um das Experiment zu starten."
    elif selected_instruction == "accuracy":
        instruction_text = "Wir sind nun mit dem Übungsdurchgang fertig und werden zum Hauptexperiment übergehen. Bitte versuchen Sie so genau wie möglich zu antworten. Drücken Sie [Leertaste], um das Experiment zu starten."
    
    # Anzeige der Anweisung
    #print(instruction_text)
    
    textSpeedInst.setText(instruction_text)
    respSpeedInstr.keys = []
    respSpeedInstr.rt = []
    _respSpeedInstr_allKeys = []
    # keep track of which components have finished
    instruction_1Components = [textSpeedInst, respSpeedInstr]
    for thisComponent in instruction_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textSpeedInst* updates
        
        # if textSpeedInst is starting this frame...
        if textSpeedInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textSpeedInst.frameNStart = frameN  # exact frame index
            textSpeedInst.tStart = t  # local t and not account for scr refresh
            textSpeedInst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textSpeedInst, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textSpeedInst.started')
            # update status
            textSpeedInst.status = STARTED
            textSpeedInst.setAutoDraw(True)
        
        # if textSpeedInst is active this frame...
        if textSpeedInst.status == STARTED:
            # update params
            pass
        
        # *respSpeedInstr* updates
        waitOnFlip = False
        
        # if respSpeedInstr is starting this frame...
        if respSpeedInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respSpeedInstr.frameNStart = frameN  # exact frame index
            respSpeedInstr.tStart = t  # local t and not account for scr refresh
            respSpeedInstr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respSpeedInstr, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'respSpeedInstr.started')
            # update status
            respSpeedInstr.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respSpeedInstr.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respSpeedInstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respSpeedInstr.status == STARTED and not waitOnFlip:
            theseKeys = respSpeedInstr.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _respSpeedInstr_allKeys.extend(theseKeys)
            if len(_respSpeedInstr_allKeys):
                respSpeedInstr.keys = _respSpeedInstr_allKeys[-1].name  # just the last key pressed
                respSpeedInstr.rt = _respSpeedInstr_allKeys[-1].rt
                respSpeedInstr.duration = _respSpeedInstr_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_1" ---
    for thisComponent in instruction_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instruction_1.stopped', globalClock.getTime())
    # check responses
    if respSpeedInstr.keys in ['', [], None]:  # No response was made
        respSpeedInstr.keys = None
    thisExp.addData('respSpeedInstr.keys',respSpeedInstr.keys)
    if respSpeedInstr.keys != None:  # we had a response
        thisExp.addData('respSpeedInstr.rt', respSpeedInstr.rt)
        thisExp.addData('respSpeedInstr.duration', respSpeedInstr.duration)
    thisExp.nextEntry()
    # the Routine "instruction_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    first_run_loop = data.TrialHandler(nReps=20.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('random_dot_conditions.csv'),
        seed=None, name='first_run_loop')
    thisExp.addLoop(first_run_loop)  # add the loop to the experiment
    thisFirst_run_loop = first_run_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFirst_run_loop.rgb)
    if thisFirst_run_loop != None:
        for paramName in thisFirst_run_loop:
            globals()[paramName] = thisFirst_run_loop[paramName]
    
    for thisFirst_run_loop in first_run_loop:
        currentLoop = first_run_loop
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisFirst_run_loop.rgb)
        if thisFirst_run_loop != None:
            for paramName in thisFirst_run_loop:
                globals()[paramName] = thisFirst_run_loop[paramName]
        
        # --- Prepare to start Routine "ITI" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('ITI.started', globalClock.getTime())
        # Run 'Begin Routine' code from preFixcross
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
        frameN = -1
        
        # --- Run Routine "ITI" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixcross* updates
            
            # if fixcross is starting this frame...
            if fixcross.status == NOT_STARTED and tThisFlip >= fixation_pre-frameTolerance:
                # keep track of start time/frame for later
                fixcross.frameNStart = frameN  # exact frame index
                fixcross.tStart = t  # local t and not account for scr refresh
                fixcross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixcross.started')
                # update status
                fixcross.status = STARTED
                fixcross.setAutoDraw(True)
            
            # if fixcross is active this frame...
            if fixcross.status == STARTED:
                # update params
                pass
            
            # if fixcross is stopping this frame...
            if fixcross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixcross.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    fixcross.tStop = t  # not accounting for scr refresh
                    fixcross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixcross.stopped')
                    # update status
                    fixcross.status = FINISHED
                    fixcross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('ITI.stopped', globalClock.getTime())
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "dots" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('dots.started', globalClock.getTime())
        # Run 'Begin Routine' code from codeDots
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
        frameN = -1
        
        # --- Run Routine "dots" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *backgroundDots* updates
            
            # if backgroundDots is starting this frame...
            if backgroundDots.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                backgroundDots.frameNStart = frameN  # exact frame index
                backgroundDots.tStart = t  # local t and not account for scr refresh
                backgroundDots.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(backgroundDots, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'backgroundDots.started')
                # update status
                backgroundDots.status = STARTED
                backgroundDots.setAutoDraw(True)
            
            # if backgroundDots is active this frame...
            if backgroundDots.status == STARTED:
                # update params
                pass
            
            # if backgroundDots is stopping this frame...
            if backgroundDots.status == STARTED:
                if frameN >= (backgroundDots.frameNStart + 90):
                    # keep track of stop time/frame for later
                    backgroundDots.tStop = t  # not accounting for scr refresh
                    backgroundDots.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'backgroundDots.stopped')
                    # update status
                    backgroundDots.status = FINISHED
                    backgroundDots.setAutoDraw(False)
            
            # *stimulusDots* updates
            
            # if stimulusDots is starting this frame...
            if stimulusDots.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                stimulusDots.frameNStart = frameN  # exact frame index
                stimulusDots.tStart = t  # local t and not account for scr refresh
                stimulusDots.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulusDots, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulusDots.started')
                # update status
                stimulusDots.status = STARTED
                stimulusDots.setAutoDraw(True)
            
            # if stimulusDots is active this frame...
            if stimulusDots.status == STARTED:
                # update params
                pass
            
            # if stimulusDots is stopping this frame...
            if stimulusDots.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 5-frameTolerance:
                    # keep track of stop time/frame for later
                    stimulusDots.tStop = t  # not accounting for scr refresh
                    stimulusDots.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimulusDots.stopped')
                    # update status
                    stimulusDots.status = FINISHED
                    stimulusDots.setAutoDraw(False)
            
            # *respDots* updates
            waitOnFlip = False
            
            # if respDots is starting this frame...
            if respDots.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                respDots.frameNStart = frameN  # exact frame index
                respDots.tStart = t  # local t and not account for scr refresh
                respDots.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respDots, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respDots.started')
                # update status
                respDots.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respDots.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respDots.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respDots.status == STARTED and not waitOnFlip:
                theseKeys = respDots.getKeys(keyList=['left', 'right'], ignoreKeys=["escape"], waitRelease=False)
                _respDots_allKeys.extend(theseKeys)
                if len(_respDots_allKeys):
                    respDots.keys = _respDots_allKeys[-1].name  # just the last key pressed
                    respDots.rt = _respDots_allKeys[-1].rt
                    respDots.duration = _respDots_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in dotsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "dots" ---
        for thisComponent in dotsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('dots.stopped', globalClock.getTime())
        # check responses
        if respDots.keys in ['', [], None]:  # No response was made
            respDots.keys = None
        first_run_loop.addData('respDots.keys',respDots.keys)
        if respDots.keys != None:  # we had a response
            first_run_loop.addData('respDots.rt', respDots.rt)
            first_run_loop.addData('respDots.duration', respDots.duration)
        # the Routine "dots" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 20.0 repeats of 'first_run_loop'
    
    
    # --- Prepare to start Routine "instruction_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instruction_2.started', globalClock.getTime())
    # Run 'Begin Routine' code from codeInstr_3
    import random
    if selected_instruction == "accuracy":
        instruction_text_2 = "Wir sind nun mit dem ersten Hauptexperiment fertig und werden zum zweiten Hauptexperiment übergehen. Bitte versuchen Sie dieses Mal so schnell wie möglich zu antworten. Drücken Sie [Leertaste], um das Hauptexperiment zu starten."
    elif selected_instruction == "speed":
        instruction_text_2 = "Wir sind nun mit dem ersten Hauptexperiment fertig und werden zum zweiten Hauptexperiment übergehen. Bitte versuchen Sie dieses Mal so genau wie möglich zu antworten. Drücken Sie [Leertaste], um das zweite Hauptexperiment zu starten."
    
    
    
    
    
    textAccuracyInstr.setText(instruction_text_2
    )
    respAccuracyInstr.keys = []
    respAccuracyInstr.rt = []
    _respAccuracyInstr_allKeys = []
    # keep track of which components have finished
    instruction_2Components = [textAccuracyInstr, respAccuracyInstr]
    for thisComponent in instruction_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textAccuracyInstr* updates
        
        # if textAccuracyInstr is starting this frame...
        if textAccuracyInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textAccuracyInstr.frameNStart = frameN  # exact frame index
            textAccuracyInstr.tStart = t  # local t and not account for scr refresh
            textAccuracyInstr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textAccuracyInstr, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textAccuracyInstr.started')
            # update status
            textAccuracyInstr.status = STARTED
            textAccuracyInstr.setAutoDraw(True)
        
        # if textAccuracyInstr is active this frame...
        if textAccuracyInstr.status == STARTED:
            # update params
            pass
        
        # *respAccuracyInstr* updates
        waitOnFlip = False
        
        # if respAccuracyInstr is starting this frame...
        if respAccuracyInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respAccuracyInstr.frameNStart = frameN  # exact frame index
            respAccuracyInstr.tStart = t  # local t and not account for scr refresh
            respAccuracyInstr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respAccuracyInstr, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'respAccuracyInstr.started')
            # update status
            respAccuracyInstr.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(respAccuracyInstr.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(respAccuracyInstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if respAccuracyInstr.status == STARTED and not waitOnFlip:
            theseKeys = respAccuracyInstr.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _respAccuracyInstr_allKeys.extend(theseKeys)
            if len(_respAccuracyInstr_allKeys):
                respAccuracyInstr.keys = _respAccuracyInstr_allKeys[-1].name  # just the last key pressed
                respAccuracyInstr.rt = _respAccuracyInstr_allKeys[-1].rt
                respAccuracyInstr.duration = _respAccuracyInstr_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_2" ---
    for thisComponent in instruction_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instruction_2.stopped', globalClock.getTime())
    # check responses
    if respAccuracyInstr.keys in ['', [], None]:  # No response was made
        respAccuracyInstr.keys = None
    thisExp.addData('respAccuracyInstr.keys',respAccuracyInstr.keys)
    if respAccuracyInstr.keys != None:  # we had a response
        thisExp.addData('respAccuracyInstr.rt', respAccuracyInstr.rt)
        thisExp.addData('respAccuracyInstr.duration', respAccuracyInstr.duration)
    thisExp.nextEntry()
    # the Routine "instruction_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    second_run_loop = data.TrialHandler(nReps=20.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('random_dot_conditions.csv'),
        seed=None, name='second_run_loop')
    thisExp.addLoop(second_run_loop)  # add the loop to the experiment
    thisSecond_run_loop = second_run_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSecond_run_loop.rgb)
    if thisSecond_run_loop != None:
        for paramName in thisSecond_run_loop:
            globals()[paramName] = thisSecond_run_loop[paramName]
    
    for thisSecond_run_loop in second_run_loop:
        currentLoop = second_run_loop
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisSecond_run_loop.rgb)
        if thisSecond_run_loop != None:
            for paramName in thisSecond_run_loop:
                globals()[paramName] = thisSecond_run_loop[paramName]
        
        # --- Prepare to start Routine "ITI" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('ITI.started', globalClock.getTime())
        # Run 'Begin Routine' code from preFixcross
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
        frameN = -1
        
        # --- Run Routine "ITI" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixcross* updates
            
            # if fixcross is starting this frame...
            if fixcross.status == NOT_STARTED and tThisFlip >= fixation_pre-frameTolerance:
                # keep track of start time/frame for later
                fixcross.frameNStart = frameN  # exact frame index
                fixcross.tStart = t  # local t and not account for scr refresh
                fixcross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixcross.started')
                # update status
                fixcross.status = STARTED
                fixcross.setAutoDraw(True)
            
            # if fixcross is active this frame...
            if fixcross.status == STARTED:
                # update params
                pass
            
            # if fixcross is stopping this frame...
            if fixcross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixcross.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    fixcross.tStop = t  # not accounting for scr refresh
                    fixcross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixcross.stopped')
                    # update status
                    fixcross.status = FINISHED
                    fixcross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('ITI.stopped', globalClock.getTime())
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "dots" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('dots.started', globalClock.getTime())
        # Run 'Begin Routine' code from codeDots
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
        frameN = -1
        
        # --- Run Routine "dots" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *backgroundDots* updates
            
            # if backgroundDots is starting this frame...
            if backgroundDots.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                backgroundDots.frameNStart = frameN  # exact frame index
                backgroundDots.tStart = t  # local t and not account for scr refresh
                backgroundDots.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(backgroundDots, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'backgroundDots.started')
                # update status
                backgroundDots.status = STARTED
                backgroundDots.setAutoDraw(True)
            
            # if backgroundDots is active this frame...
            if backgroundDots.status == STARTED:
                # update params
                pass
            
            # if backgroundDots is stopping this frame...
            if backgroundDots.status == STARTED:
                if frameN >= (backgroundDots.frameNStart + 90):
                    # keep track of stop time/frame for later
                    backgroundDots.tStop = t  # not accounting for scr refresh
                    backgroundDots.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'backgroundDots.stopped')
                    # update status
                    backgroundDots.status = FINISHED
                    backgroundDots.setAutoDraw(False)
            
            # *stimulusDots* updates
            
            # if stimulusDots is starting this frame...
            if stimulusDots.status == NOT_STARTED and frameN >= 0.0:
                # keep track of start time/frame for later
                stimulusDots.frameNStart = frameN  # exact frame index
                stimulusDots.tStart = t  # local t and not account for scr refresh
                stimulusDots.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulusDots, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulusDots.started')
                # update status
                stimulusDots.status = STARTED
                stimulusDots.setAutoDraw(True)
            
            # if stimulusDots is active this frame...
            if stimulusDots.status == STARTED:
                # update params
                pass
            
            # if stimulusDots is stopping this frame...
            if stimulusDots.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 5-frameTolerance:
                    # keep track of stop time/frame for later
                    stimulusDots.tStop = t  # not accounting for scr refresh
                    stimulusDots.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimulusDots.stopped')
                    # update status
                    stimulusDots.status = FINISHED
                    stimulusDots.setAutoDraw(False)
            
            # *respDots* updates
            waitOnFlip = False
            
            # if respDots is starting this frame...
            if respDots.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                respDots.frameNStart = frameN  # exact frame index
                respDots.tStart = t  # local t and not account for scr refresh
                respDots.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respDots, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respDots.started')
                # update status
                respDots.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respDots.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respDots.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respDots.status == STARTED and not waitOnFlip:
                theseKeys = respDots.getKeys(keyList=['left', 'right'], ignoreKeys=["escape"], waitRelease=False)
                _respDots_allKeys.extend(theseKeys)
                if len(_respDots_allKeys):
                    respDots.keys = _respDots_allKeys[-1].name  # just the last key pressed
                    respDots.rt = _respDots_allKeys[-1].rt
                    respDots.duration = _respDots_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in dotsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "dots" ---
        for thisComponent in dotsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('dots.stopped', globalClock.getTime())
        # check responses
        if respDots.keys in ['', [], None]:  # No response was made
            respDots.keys = None
        second_run_loop.addData('respDots.keys',respDots.keys)
        if respDots.keys != None:  # we had a response
            second_run_loop.addData('respDots.rt', respDots.rt)
            second_run_loop.addData('respDots.duration', respDots.duration)
        # the Routine "dots" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 20.0 repeats of 'second_run_loop'
    
    
    # --- Prepare to start Routine "goodbye" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('goodbye.started', globalClock.getTime())
    # keep track of which components have finished
    goodbyeComponents = [goodbye_text]
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
    frameN = -1
    
    # --- Run Routine "goodbye" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *goodbye_text* updates
        
        # if goodbye_text is starting this frame...
        if goodbye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goodbye_text.frameNStart = frameN  # exact frame index
            goodbye_text.tStart = t  # local t and not account for scr refresh
            goodbye_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goodbye_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'goodbye_text.started')
            # update status
            goodbye_text.status = STARTED
            goodbye_text.setAutoDraw(True)
        
        # if goodbye_text is active this frame...
        if goodbye_text.status == STARTED:
            # update params
            pass
        
        # if goodbye_text is stopping this frame...
        if goodbye_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > goodbye_text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                goodbye_text.tStop = t  # not accounting for scr refresh
                goodbye_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'goodbye_text.stopped')
                # update status
                goodbye_text.status = FINISHED
                goodbye_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in goodbyeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "goodbye" ---
    for thisComponent in goodbyeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('goodbye.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)

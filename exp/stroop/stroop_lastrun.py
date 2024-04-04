#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Mon Mar 11 10:51:27 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

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
expName = 'stroop_test'  # from the Builder filename that created this script
expInfo = {
    'participant': 'sub-' + f"{randint(0, 999999):06.0f}" ,
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
        originPath='/Users/dafitze/UNI/GIT/neuroscicomplabFS24/exp/stroop/stroop_lastrun.py',
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
    instr_text = visual.TextStim(win=win, name='instr_text',
        text='Willkommen zum Stroop-Test!\n\nVielen Dank, dass Sie an diesem Experiment teilnehmen. \n\nBitte stellen Sie sicher, dass die Farben auf Ihrem Bildschirm korrekt angezeigt werden. Stellen Sie sicher, dass Sie sich in einer ruhigen Umgebung befinden, in der Sie sich konzentrieren können.\n\nEs gibt zwei Übungsdurchgänge und einen Test-Durchgang.\n\nIn jedem Durchgang werden ihnen unterschiedliche Wörter präsentiert. Ihre Aufgabe ist es, die Farbe jedes Wortes anzugeben. \n\nLegen sie den Mittelfinger der linken Hand auf die R-Taste und den Zeigfinger auf die G-Taste.\nLegen sie den Zeigfinger der rechten Hand auf die B-Taste.\n\n\n\n\n\n\n\n\n\nWenn Sie bereit sind, drücken sie die Leertaste, damit sie zum Übungsdurchgang gelangen. \n',
        font='Open Sans',
        pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from instr_code
    win.color = 'black'
    instr_image = visual.ImageStim(
        win=win,
        name='instr_image', 
        image='illustration_keyborad.PNG', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.18), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    instr_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "begin_color_to_key" ---
    instr_ctk = visual.TextStim(win=win, name='instr_ctk',
        text='Aufgepasst, jetzt startet der erste Übungsdurchgang.\n\nDrücken Sie die Leertaste, wenn Sie soweit sind.',
        font='Open Sans',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    resp_ctk = keyboard.Keyboard()
    # Run 'Begin Experiment' code from code_ctk
    win.color = 'black'
    
    # --- Initialize components for Routine "ITI" ---
    fixcross = visual.TextStim(win=win, name='fixcross',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "color_to_key_run" ---
    text_CTK = visual.TextStim(win=win, name='text_CTK',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_CTK = keyboard.Keyboard()
    
    # --- Initialize components for Routine "begin_practice" ---
    practice_text = visual.TextStim(win=win, name='practice_text',
        text='Aufgepasst, jetzt startet der zweite Übungsdurchgang!\n\nDrücken Sie die Leertaste, wenn Sie soweit sind.',
        font='Open Sans',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    practice_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "ITI" ---
    fixcross = visual.TextStim(win=win, name='fixcross',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "practice_run" ---
    stimulus_practice = visual.TextStim(win=win, name='stimulus_practice',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    respPractice = keyboard.Keyboard()
    
    # --- Initialize components for Routine "practice_feedback" ---
    textFeedback = visual.TextStim(win=win, name='textFeedback',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "begin_test" ---
    begin_test_text = visual.TextStim(win=win, name='begin_test_text',
        text='Aufgepasst, jetzt startet der Testdurchgang!\n\nDrücken Sie die Leertaste, wenn Sie soweit sind.',
        font='Open Sans',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    begin_test_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "ITI" ---
    fixcross = visual.TextStim(win=win, name='fixcross',
        text='+',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "test_run" ---
    text = visual.TextStim(win=win, name='text',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "goodbye" ---
    textGoodbye = visual.TextStim(win=win, name='textGoodbye',
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
    instr_resp.keys = []
    instr_resp.rt = []
    _instr_resp_allKeys = []
    # keep track of which components have finished
    instructionComponents = [instr_text, instr_image, instr_resp]
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
        
        # *instr_text* updates
        
        # if instr_text is starting this frame...
        if instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_text.frameNStart = frameN  # exact frame index
            instr_text.tStart = t  # local t and not account for scr refresh
            instr_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_text.started')
            # update status
            instr_text.status = STARTED
            instr_text.setAutoDraw(True)
        
        # if instr_text is active this frame...
        if instr_text.status == STARTED:
            # update params
            pass
        
        # *instr_image* updates
        
        # if instr_image is starting this frame...
        if instr_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_image.frameNStart = frameN  # exact frame index
            instr_image.tStart = t  # local t and not account for scr refresh
            instr_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_image.started')
            # update status
            instr_image.status = STARTED
            instr_image.setAutoDraw(True)
        
        # if instr_image is active this frame...
        if instr_image.status == STARTED:
            # update params
            pass
        
        # *instr_resp* updates
        waitOnFlip = False
        
        # if instr_resp is starting this frame...
        if instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_resp.frameNStart = frameN  # exact frame index
            instr_resp.tStart = t  # local t and not account for scr refresh
            instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_resp.started')
            # update status
            instr_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instr_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instr_resp.status == STARTED and not waitOnFlip:
            theseKeys = instr_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _instr_resp_allKeys.extend(theseKeys)
            if len(_instr_resp_allKeys):
                instr_resp.keys = _instr_resp_allKeys[-1].name  # just the last key pressed
                instr_resp.rt = _instr_resp_allKeys[-1].rt
                instr_resp.duration = _instr_resp_allKeys[-1].duration
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
    if instr_resp.keys in ['', [], None]:  # No response was made
        instr_resp.keys = None
    thisExp.addData('instr_resp.keys',instr_resp.keys)
    if instr_resp.keys != None:  # we had a response
        thisExp.addData('instr_resp.rt', instr_resp.rt)
        thisExp.addData('instr_resp.duration', instr_resp.duration)
    thisExp.nextEntry()
    # the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "begin_color_to_key" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('begin_color_to_key.started', globalClock.getTime())
    resp_ctk.keys = []
    resp_ctk.rt = []
    _resp_ctk_allKeys = []
    # keep track of which components have finished
    begin_color_to_keyComponents = [instr_ctk, resp_ctk]
    for thisComponent in begin_color_to_keyComponents:
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
    
    # --- Run Routine "begin_color_to_key" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_ctk* updates
        
        # if instr_ctk is starting this frame...
        if instr_ctk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_ctk.frameNStart = frameN  # exact frame index
            instr_ctk.tStart = t  # local t and not account for scr refresh
            instr_ctk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_ctk, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_ctk.started')
            # update status
            instr_ctk.status = STARTED
            instr_ctk.setAutoDraw(True)
        
        # if instr_ctk is active this frame...
        if instr_ctk.status == STARTED:
            # update params
            pass
        
        # *resp_ctk* updates
        waitOnFlip = False
        
        # if resp_ctk is starting this frame...
        if resp_ctk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_ctk.frameNStart = frameN  # exact frame index
            resp_ctk.tStart = t  # local t and not account for scr refresh
            resp_ctk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_ctk, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp_ctk.started')
            # update status
            resp_ctk.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_ctk.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_ctk.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_ctk.status == STARTED and not waitOnFlip:
            theseKeys = resp_ctk.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _resp_ctk_allKeys.extend(theseKeys)
            if len(_resp_ctk_allKeys):
                resp_ctk.keys = _resp_ctk_allKeys[-1].name  # just the last key pressed
                resp_ctk.rt = _resp_ctk_allKeys[-1].rt
                resp_ctk.duration = _resp_ctk_allKeys[-1].duration
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
        for thisComponent in begin_color_to_keyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "begin_color_to_key" ---
    for thisComponent in begin_color_to_keyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('begin_color_to_key.stopped', globalClock.getTime())
    # check responses
    if resp_ctk.keys in ['', [], None]:  # No response was made
        resp_ctk.keys = None
    thisExp.addData('resp_ctk.keys',resp_ctk.keys)
    if resp_ctk.keys != None:  # we had a response
        thisExp.addData('resp_ctk.rt', resp_ctk.rt)
        thisExp.addData('resp_ctk.duration', resp_ctk.duration)
    thisExp.nextEntry()
    # the Routine "begin_color_to_key" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_CTK = data.TrialHandler(nReps=3.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stroop_condition_file_CTK.xlsx'),
        seed=None, name='trials_CTK')
    thisExp.addLoop(trials_CTK)  # add the loop to the experiment
    thisTrials_CTK = trials_CTK.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_CTK.rgb)
    if thisTrials_CTK != None:
        for paramName in thisTrials_CTK:
            globals()[paramName] = thisTrials_CTK[paramName]
    
    for thisTrials_CTK in trials_CTK:
        currentLoop = trials_CTK
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_CTK.rgb)
        if thisTrials_CTK != None:
            for paramName in thisTrials_CTK:
                globals()[paramName] = thisTrials_CTK[paramName]
        
        # --- Prepare to start Routine "ITI" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('ITI.started', globalClock.getTime())
        # Run 'Begin Routine' code from pre_fixcross
        # Before the fixation cross (the one before the cue) is displayed, randomly
        # choose a duration for it. Since we are using seconds as time unit, these
        # numbers correspond to 100ms, 350ms, 800ms and 1200ms.
        pre_fixcross = randchoice([0.1, 0.35, 0.8, 1.2])
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
            if fixcross.status == NOT_STARTED and tThisFlip >= pre_fixcross-frameTolerance:
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
        
        # --- Prepare to start Routine "color_to_key_run" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('color_to_key_run.started', globalClock.getTime())
        text_CTK.setColor(colorCTK, colorSpace='rgb')
        text_CTK.setText(wordCTK)
        key_resp_CTK.keys = []
        key_resp_CTK.rt = []
        _key_resp_CTK_allKeys = []
        # keep track of which components have finished
        color_to_key_runComponents = [text_CTK, key_resp_CTK]
        for thisComponent in color_to_key_runComponents:
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
        
        # --- Run Routine "color_to_key_run" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_CTK* updates
            
            # if text_CTK is starting this frame...
            if text_CTK.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text_CTK.frameNStart = frameN  # exact frame index
                text_CTK.tStart = t  # local t and not account for scr refresh
                text_CTK.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_CTK, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_CTK.started')
                # update status
                text_CTK.status = STARTED
                text_CTK.setAutoDraw(True)
            
            # if text_CTK is active this frame...
            if text_CTK.status == STARTED:
                # update params
                pass
            
            # *key_resp_CTK* updates
            waitOnFlip = False
            
            # if key_resp_CTK is starting this frame...
            if key_resp_CTK.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_CTK.frameNStart = frameN  # exact frame index
                key_resp_CTK.tStart = t  # local t and not account for scr refresh
                key_resp_CTK.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_CTK, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_CTK.started')
                # update status
                key_resp_CTK.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_CTK.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_CTK.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_CTK.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_CTK.getKeys(keyList=['r', 'g', 'b'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_CTK_allKeys.extend(theseKeys)
                if len(_key_resp_CTK_allKeys):
                    key_resp_CTK.keys = _key_resp_CTK_allKeys[-1].name  # just the last key pressed
                    key_resp_CTK.rt = _key_resp_CTK_allKeys[-1].rt
                    key_resp_CTK.duration = _key_resp_CTK_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_CTK.keys == str(corrAnsCTK)) or (key_resp_CTK.keys == corrAnsCTK):
                        key_resp_CTK.corr = 1
                    else:
                        key_resp_CTK.corr = 0
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
            for thisComponent in color_to_key_runComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "color_to_key_run" ---
        for thisComponent in color_to_key_runComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('color_to_key_run.stopped', globalClock.getTime())
        # check responses
        if key_resp_CTK.keys in ['', [], None]:  # No response was made
            key_resp_CTK.keys = None
            # was no response the correct answer?!
            if str(corrAnsCTK).lower() == 'none':
               key_resp_CTK.corr = 1;  # correct non-response
            else:
               key_resp_CTK.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_CTK (TrialHandler)
        trials_CTK.addData('key_resp_CTK.keys',key_resp_CTK.keys)
        trials_CTK.addData('key_resp_CTK.corr', key_resp_CTK.corr)
        if key_resp_CTK.keys != None:  # we had a response
            trials_CTK.addData('key_resp_CTK.rt', key_resp_CTK.rt)
            trials_CTK.addData('key_resp_CTK.duration', key_resp_CTK.duration)
        # the Routine "color_to_key_run" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 3.0 repeats of 'trials_CTK'
    
    
    # --- Prepare to start Routine "begin_practice" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('begin_practice.started', globalClock.getTime())
    practice_resp.keys = []
    practice_resp.rt = []
    _practice_resp_allKeys = []
    # keep track of which components have finished
    begin_practiceComponents = [practice_text, practice_resp]
    for thisComponent in begin_practiceComponents:
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
    
    # --- Run Routine "begin_practice" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_text* updates
        
        # if practice_text is starting this frame...
        if practice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_text.frameNStart = frameN  # exact frame index
            practice_text.tStart = t  # local t and not account for scr refresh
            practice_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_text.started')
            # update status
            practice_text.status = STARTED
            practice_text.setAutoDraw(True)
        
        # if practice_text is active this frame...
        if practice_text.status == STARTED:
            # update params
            pass
        
        # if practice_text is stopping this frame...
        if practice_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practice_text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                practice_text.tStop = t  # not accounting for scr refresh
                practice_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_text.stopped')
                # update status
                practice_text.status = FINISHED
                practice_text.setAutoDraw(False)
        
        # *practice_resp* updates
        waitOnFlip = False
        
        # if practice_resp is starting this frame...
        if practice_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_resp.frameNStart = frameN  # exact frame index
            practice_resp.tStart = t  # local t and not account for scr refresh
            practice_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_resp.started')
            # update status
            practice_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(practice_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(practice_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if practice_resp.status == STARTED and not waitOnFlip:
            theseKeys = practice_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _practice_resp_allKeys.extend(theseKeys)
            if len(_practice_resp_allKeys):
                practice_resp.keys = _practice_resp_allKeys[-1].name  # just the last key pressed
                practice_resp.rt = _practice_resp_allKeys[-1].rt
                practice_resp.duration = _practice_resp_allKeys[-1].duration
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
        for thisComponent in begin_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "begin_practice" ---
    for thisComponent in begin_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('begin_practice.stopped', globalClock.getTime())
    # check responses
    if practice_resp.keys in ['', [], None]:  # No response was made
        practice_resp.keys = None
    thisExp.addData('practice_resp.keys',practice_resp.keys)
    if practice_resp.keys != None:  # we had a response
        thisExp.addData('practice_resp.rt', practice_resp.rt)
        thisExp.addData('practice_resp.duration', practice_resp.duration)
    thisExp.nextEntry()
    # the Routine "begin_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_practice = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stroop_condition_file_practice.xlsx'),
        seed=None, name='trials_practice')
    thisExp.addLoop(trials_practice)  # add the loop to the experiment
    thisTrials_practice = trials_practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_practice.rgb)
    if thisTrials_practice != None:
        for paramName in thisTrials_practice:
            globals()[paramName] = thisTrials_practice[paramName]
    
    for thisTrials_practice in trials_practice:
        currentLoop = trials_practice
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_practice.rgb)
        if thisTrials_practice != None:
            for paramName in thisTrials_practice:
                globals()[paramName] = thisTrials_practice[paramName]
        
        # --- Prepare to start Routine "ITI" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('ITI.started', globalClock.getTime())
        # Run 'Begin Routine' code from pre_fixcross
        # Before the fixation cross (the one before the cue) is displayed, randomly
        # choose a duration for it. Since we are using seconds as time unit, these
        # numbers correspond to 100ms, 350ms, 800ms and 1200ms.
        pre_fixcross = randchoice([0.1, 0.35, 0.8, 1.2])
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
            if fixcross.status == NOT_STARTED and tThisFlip >= pre_fixcross-frameTolerance:
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
        
        # --- Prepare to start Routine "practice_run" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('practice_run.started', globalClock.getTime())
        stimulus_practice.setColor(colorPractice, colorSpace='rgb')
        stimulus_practice.setText(wordPractice)
        respPractice.keys = []
        respPractice.rt = []
        _respPractice_allKeys = []
        # keep track of which components have finished
        practice_runComponents = [stimulus_practice, respPractice]
        for thisComponent in practice_runComponents:
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
        
        # --- Run Routine "practice_run" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimulus_practice* updates
            
            # if stimulus_practice is starting this frame...
            if stimulus_practice.status == NOT_STARTED and tThisFlip >= pre_fixcross-frameTolerance:
                # keep track of start time/frame for later
                stimulus_practice.frameNStart = frameN  # exact frame index
                stimulus_practice.tStart = t  # local t and not account for scr refresh
                stimulus_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulus_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stimulus_practice.started')
                # update status
                stimulus_practice.status = STARTED
                stimulus_practice.setAutoDraw(True)
            
            # if stimulus_practice is active this frame...
            if stimulus_practice.status == STARTED:
                # update params
                pass
            
            # *respPractice* updates
            waitOnFlip = False
            
            # if respPractice is starting this frame...
            if respPractice.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                respPractice.frameNStart = frameN  # exact frame index
                respPractice.tStart = t  # local t and not account for scr refresh
                respPractice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respPractice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respPractice.started')
                # update status
                respPractice.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respPractice.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respPractice.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respPractice.status == STARTED and not waitOnFlip:
                theseKeys = respPractice.getKeys(keyList=['r', 'g', 'b'], ignoreKeys=["escape"], waitRelease=False)
                _respPractice_allKeys.extend(theseKeys)
                if len(_respPractice_allKeys):
                    respPractice.keys = _respPractice_allKeys[-1].name  # just the last key pressed
                    respPractice.rt = _respPractice_allKeys[-1].rt
                    respPractice.duration = _respPractice_allKeys[-1].duration
                    # was this correct?
                    if (respPractice.keys == str(corrAnsPractice)) or (respPractice.keys == corrAnsPractice):
                        respPractice.corr = 1
                    else:
                        respPractice.corr = 0
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
            for thisComponent in practice_runComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_run" ---
        for thisComponent in practice_runComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('practice_run.stopped', globalClock.getTime())
        # check responses
        if respPractice.keys in ['', [], None]:  # No response was made
            respPractice.keys = None
            # was no response the correct answer?!
            if str(corrAnsPractice).lower() == 'none':
               respPractice.corr = 1;  # correct non-response
            else:
               respPractice.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_practice (TrialHandler)
        trials_practice.addData('respPractice.keys',respPractice.keys)
        trials_practice.addData('respPractice.corr', respPractice.corr)
        if respPractice.keys != None:  # we had a response
            trials_practice.addData('respPractice.rt', respPractice.rt)
            trials_practice.addData('respPractice.duration', respPractice.duration)
        # the Routine "practice_run" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "practice_feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('practice_feedback.started', globalClock.getTime())
        # Run 'Begin Routine' code from codeFeedback
        if (respPractice.keys == "r" and corrAnsPractice == "r" or 
            respPractice.keys == "g" and corrAnsPractice == "g" or 
            respPractice.keys == "b" and corrAnsPractice == "b"):
            response_text = "richtig"
        elif (respPractice.keys == "r" and corrAnsPractice == "b" or 
            respPractice.keys == "r" and corrAnsPractice == "g" or 
            respPractice.keys == "b" and corrAnsPractice == "r" or
            respPractice.keys == "b" and corrAnsPractice == "g" or
            respPractice.keys == "g" and corrAnsPractice == "r" or 
            respPractice.keys == "g" and corrAnsPractice == "b"):
            response_text = "falsch"
        
        textFeedback.setColor('white', colorSpace='rgb')
        textFeedback.setText(response_text)
        # keep track of which components have finished
        practice_feedbackComponents = [textFeedback]
        for thisComponent in practice_feedbackComponents:
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
        
        # --- Run Routine "practice_feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
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
                if tThisFlipGlobal > textFeedback.tStartRefresh + 1.0-frameTolerance:
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
            for thisComponent in practice_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_feedback" ---
        for thisComponent in practice_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('practice_feedback.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 5.0 repeats of 'trials_practice'
    
    
    # --- Prepare to start Routine "begin_test" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('begin_test.started', globalClock.getTime())
    begin_test_resp.keys = []
    begin_test_resp.rt = []
    _begin_test_resp_allKeys = []
    # keep track of which components have finished
    begin_testComponents = [begin_test_text, begin_test_resp]
    for thisComponent in begin_testComponents:
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
    
    # --- Run Routine "begin_test" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *begin_test_text* updates
        
        # if begin_test_text is starting this frame...
        if begin_test_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            begin_test_text.frameNStart = frameN  # exact frame index
            begin_test_text.tStart = t  # local t and not account for scr refresh
            begin_test_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(begin_test_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'begin_test_text.started')
            # update status
            begin_test_text.status = STARTED
            begin_test_text.setAutoDraw(True)
        
        # if begin_test_text is active this frame...
        if begin_test_text.status == STARTED:
            # update params
            pass
        
        # if begin_test_text is stopping this frame...
        if begin_test_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > begin_test_text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                begin_test_text.tStop = t  # not accounting for scr refresh
                begin_test_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'begin_test_text.stopped')
                # update status
                begin_test_text.status = FINISHED
                begin_test_text.setAutoDraw(False)
        
        # *begin_test_resp* updates
        waitOnFlip = False
        
        # if begin_test_resp is starting this frame...
        if begin_test_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            begin_test_resp.frameNStart = frameN  # exact frame index
            begin_test_resp.tStart = t  # local t and not account for scr refresh
            begin_test_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(begin_test_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'begin_test_resp.started')
            # update status
            begin_test_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(begin_test_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(begin_test_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if begin_test_resp.status == STARTED and not waitOnFlip:
            theseKeys = begin_test_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _begin_test_resp_allKeys.extend(theseKeys)
            if len(_begin_test_resp_allKeys):
                begin_test_resp.keys = _begin_test_resp_allKeys[-1].name  # just the last key pressed
                begin_test_resp.rt = _begin_test_resp_allKeys[-1].rt
                begin_test_resp.duration = _begin_test_resp_allKeys[-1].duration
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
        for thisComponent in begin_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "begin_test" ---
    for thisComponent in begin_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('begin_test.stopped', globalClock.getTime())
    # check responses
    if begin_test_resp.keys in ['', [], None]:  # No response was made
        begin_test_resp.keys = None
    thisExp.addData('begin_test_resp.keys',begin_test_resp.keys)
    if begin_test_resp.keys != None:  # we had a response
        thisExp.addData('begin_test_resp.rt', begin_test_resp.rt)
        thisExp.addData('begin_test_resp.duration', begin_test_resp.duration)
    thisExp.nextEntry()
    # the Routine "begin_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_test = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stroop_condition_file_test.xlsx'),
        seed=None, name='trials_test')
    thisExp.addLoop(trials_test)  # add the loop to the experiment
    thisTrials_test = trials_test.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_test.rgb)
    if thisTrials_test != None:
        for paramName in thisTrials_test:
            globals()[paramName] = thisTrials_test[paramName]
    
    for thisTrials_test in trials_test:
        currentLoop = trials_test
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_test.rgb)
        if thisTrials_test != None:
            for paramName in thisTrials_test:
                globals()[paramName] = thisTrials_test[paramName]
        
        # --- Prepare to start Routine "ITI" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('ITI.started', globalClock.getTime())
        # Run 'Begin Routine' code from pre_fixcross
        # Before the fixation cross (the one before the cue) is displayed, randomly
        # choose a duration for it. Since we are using seconds as time unit, these
        # numbers correspond to 100ms, 350ms, 800ms and 1200ms.
        pre_fixcross = randchoice([0.1, 0.35, 0.8, 1.2])
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
            if fixcross.status == NOT_STARTED and tThisFlip >= pre_fixcross-frameTolerance:
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
        
        # --- Prepare to start Routine "test_run" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('test_run.started', globalClock.getTime())
        text.setColor(color, colorSpace='rgb')
        text.setText(word)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        test_runComponents = [text, key_resp]
        for thisComponent in test_runComponents:
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
        
        # --- Run Routine "test_run" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['r', 'g', 'b'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # was this correct?
                    if (key_resp.keys == str(corrAns)) or (key_resp.keys == corrAns):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
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
            for thisComponent in test_runComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test_run" ---
        for thisComponent in test_runComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('test_run.stopped', globalClock.getTime())
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_test (TrialHandler)
        trials_test.addData('key_resp.keys',key_resp.keys)
        trials_test.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            trials_test.addData('key_resp.rt', key_resp.rt)
            trials_test.addData('key_resp.duration', key_resp.duration)
        # the Routine "test_run" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 5.0 repeats of 'trials_test'
    
    
    # --- Prepare to start Routine "goodbye" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('goodbye.started', globalClock.getTime())
    # keep track of which components have finished
    goodbyeComponents = [textGoodbye]
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
        
        # *textGoodbye* updates
        
        # if textGoodbye is starting this frame...
        if textGoodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textGoodbye.frameNStart = frameN  # exact frame index
            textGoodbye.tStart = t  # local t and not account for scr refresh
            textGoodbye.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textGoodbye, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textGoodbye.started')
            # update status
            textGoodbye.status = STARTED
            textGoodbye.setAutoDraw(True)
        
        # if textGoodbye is active this frame...
        if textGoodbye.status == STARTED:
            # update params
            pass
        
        # if textGoodbye is stopping this frame...
        if textGoodbye.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textGoodbye.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                textGoodbye.tStop = t  # not accounting for scr refresh
                textGoodbye.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textGoodbye.stopped')
                # update status
                textGoodbye.status = FINISHED
                textGoodbye.setAutoDraw(False)
        
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

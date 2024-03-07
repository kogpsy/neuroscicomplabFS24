/******************* 
 * Random_Dot *
 *******************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.2.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'random_dot';  // from the Builder filename that created this script
let expInfo = {
    'participant': ("sub-" + `${util.pad(Number.parseFloat(util.randint(0, 99999)).toFixed(0), 6)}`),
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionRoutineBegin());
flowScheduler.add(instructionRoutineEachFrame());
flowScheduler.add(instructionRoutineEnd());
const practice_run_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practice_run_loopLoopBegin(practice_run_loopLoopScheduler));
flowScheduler.add(practice_run_loopLoopScheduler);
flowScheduler.add(practice_run_loopLoopEnd);




flowScheduler.add(instruction_1RoutineBegin());
flowScheduler.add(instruction_1RoutineEachFrame());
flowScheduler.add(instruction_1RoutineEnd());
const first_run_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(first_run_loopLoopBegin(first_run_loopLoopScheduler));
flowScheduler.add(first_run_loopLoopScheduler);
flowScheduler.add(first_run_loopLoopEnd);



flowScheduler.add(instruction_2RoutineBegin());
flowScheduler.add(instruction_2RoutineEachFrame());
flowScheduler.add(instruction_2RoutineEnd());
const second_run_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(second_run_loopLoopBegin(second_run_loopLoopScheduler));
flowScheduler.add(second_run_loopLoopScheduler);
flowScheduler.add(second_run_loopLoopEnd);



flowScheduler.add(goodbyeRoutineBegin());
flowScheduler.add(goodbyeRoutineEachFrame());
flowScheduler.add(goodbyeRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'random_dot_conditions.csv', 'path': 'random_dot_conditions.csv'},
    {'name': 'random_dot_conditions.csv', 'path': 'random_dot_conditions.csv'},
    {'name': 'random_dot_conditions.csv', 'path': 'random_dot_conditions.csv'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "instruction"
  instructionClock = new util.Clock();
  textInstr = new visual.TextStim({
    win: psychoJS.window,
    name: 'textInstr',
    text: 'Willkommen zum Experiment.\n\nIm Folgenden werden Sie eine Reihe von Aufgaben lösen. Ihnen wird ein Kreis voller Punkte präsentiert. Einige dieser Punkte bewegen sich entweder nach links oder nach rechts. Ihre Aufgabe ist es, zu entscheiden, in welche Richtung sie sich bewegen.\n\nDrücken Sie die linke Pfeiltaste, wenn Sie glauben, dass sich die Punkte nach links bewegen, oder die rechte Pfeiltaste, wenn Sie glauben, dass sie sich nach rechts bewegen.\n\nBitte konzentrieren Sie sich immer auf das kleine Kreuz auf dem Bildschirm, wenn nichts anderes angezeigt wird.\n\nDrücken Sie [ Leertaste ], um mit dem Übungsdurchgang zu beginnen, wenn Sie bereit sind.\n\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Run 'Begin Experiment' code from codeInstr
  psychoJS.window.color = "black";
  
  respInstr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ITI"
  ITIClock = new util.Clock();
  fixcross = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixcross',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "dots"
  dotsClock = new util.Clock();
  backgroundDots = new visual.Polygon({
    win: psychoJS.window, name: 'backgroundDots', 
    edges: 100, size:[0.75, 0.75],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('black'),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  respDots = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  textFeedback = new visual.TextStim({
    win: psychoJS.window,
    name: 'textFeedback',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "instruction_1"
  instruction_1Clock = new util.Clock();
  textSpeedInst = new visual.TextStim({
    win: psychoJS.window,
    name: 'textSpeedInst',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  respSpeedInstr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction_2"
  instruction_2Clock = new util.Clock();
  textAccuracyInstr = new visual.TextStim({
    win: psychoJS.window,
    name: 'textAccuracyInstr',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  respAccuracyInstr = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "goodbye"
  goodbyeClock = new util.Clock();
  goodbye_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'goodbye_text',
    text: 'Sie sind am Ende angelangt. \n\nVielen Dank, dass sie an diesem Experiment teilgenommen haben. :)',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function instructionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction' ---
    t = 0;
    instructionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instruction.started', globalClock.getTime());
    respInstr.keys = undefined;
    respInstr.rt = undefined;
    _respInstr_allKeys = [];
    // keep track of which components have finished
    instructionComponents = [];
    instructionComponents.push(textInstr);
    instructionComponents.push(respInstr);
    
    for (const thisComponent of instructionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function instructionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction' ---
    // get current time
    t = instructionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textInstr* updates
    if (t >= 0.0 && textInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textInstr.tStart = t;  // (not accounting for frame time here)
      textInstr.frameNStart = frameN;  // exact frame index
      
      textInstr.setAutoDraw(true);
    }
    
    
    // *respInstr* updates
    if (t >= 0.0 && respInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respInstr.tStart = t;  // (not accounting for frame time here)
      respInstr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respInstr.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respInstr.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respInstr.clearEvents(); });
    }
    
    if (respInstr.status === PsychoJS.Status.STARTED) {
      let theseKeys = respInstr.getKeys({keyList: ['space'], waitRelease: false});
      _respInstr_allKeys = _respInstr_allKeys.concat(theseKeys);
      if (_respInstr_allKeys.length > 0) {
        respInstr.keys = _respInstr_allKeys[_respInstr_allKeys.length - 1].name;  // just the last key pressed
        respInstr.rt = _respInstr_allKeys[_respInstr_allKeys.length - 1].rt;
        respInstr.duration = _respInstr_allKeys[_respInstr_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function instructionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction' ---
    for (const thisComponent of instructionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instruction.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(respInstr.corr, level);
    }
    psychoJS.experiment.addData('respInstr.keys', respInstr.keys);
    if (typeof respInstr.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('respInstr.rt', respInstr.rt);
        psychoJS.experiment.addData('respInstr.duration', respInstr.duration);
        routineTimer.reset();
        }
    
    respInstr.stop();
    // the Routine "instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function practice_run_loopLoopBegin(practice_run_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practice_run_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 10, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'random_dot_conditions.csv',
      seed: undefined, name: 'practice_run_loop'
    });
    psychoJS.experiment.addLoop(practice_run_loop); // add the loop to the experiment
    currentLoop = practice_run_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPractice_run_loop of practice_run_loop) {
      snapshot = practice_run_loop.getSnapshot();
      practice_run_loopLoopScheduler.add(importConditions(snapshot));
      practice_run_loopLoopScheduler.add(ITIRoutineBegin(snapshot));
      practice_run_loopLoopScheduler.add(ITIRoutineEachFrame());
      practice_run_loopLoopScheduler.add(ITIRoutineEnd(snapshot));
      practice_run_loopLoopScheduler.add(dotsRoutineBegin(snapshot));
      practice_run_loopLoopScheduler.add(dotsRoutineEachFrame());
      practice_run_loopLoopScheduler.add(dotsRoutineEnd(snapshot));
      practice_run_loopLoopScheduler.add(feedbackRoutineBegin(snapshot));
      practice_run_loopLoopScheduler.add(feedbackRoutineEachFrame());
      practice_run_loopLoopScheduler.add(feedbackRoutineEnd(snapshot));
      practice_run_loopLoopScheduler.add(practice_run_loopLoopEndIteration(practice_run_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function practice_run_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practice_run_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function practice_run_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function first_run_loopLoopBegin(first_run_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    first_run_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 20, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'random_dot_conditions.csv',
      seed: undefined, name: 'first_run_loop'
    });
    psychoJS.experiment.addLoop(first_run_loop); // add the loop to the experiment
    currentLoop = first_run_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisFirst_run_loop of first_run_loop) {
      snapshot = first_run_loop.getSnapshot();
      first_run_loopLoopScheduler.add(importConditions(snapshot));
      first_run_loopLoopScheduler.add(ITIRoutineBegin(snapshot));
      first_run_loopLoopScheduler.add(ITIRoutineEachFrame());
      first_run_loopLoopScheduler.add(ITIRoutineEnd(snapshot));
      first_run_loopLoopScheduler.add(dotsRoutineBegin(snapshot));
      first_run_loopLoopScheduler.add(dotsRoutineEachFrame());
      first_run_loopLoopScheduler.add(dotsRoutineEnd(snapshot));
      first_run_loopLoopScheduler.add(first_run_loopLoopEndIteration(first_run_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function first_run_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(first_run_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function first_run_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function second_run_loopLoopBegin(second_run_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    second_run_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 20, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'random_dot_conditions.csv',
      seed: undefined, name: 'second_run_loop'
    });
    psychoJS.experiment.addLoop(second_run_loop); // add the loop to the experiment
    currentLoop = second_run_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisSecond_run_loop of second_run_loop) {
      snapshot = second_run_loop.getSnapshot();
      second_run_loopLoopScheduler.add(importConditions(snapshot));
      second_run_loopLoopScheduler.add(ITIRoutineBegin(snapshot));
      second_run_loopLoopScheduler.add(ITIRoutineEachFrame());
      second_run_loopLoopScheduler.add(ITIRoutineEnd(snapshot));
      second_run_loopLoopScheduler.add(dotsRoutineBegin(snapshot));
      second_run_loopLoopScheduler.add(dotsRoutineEachFrame());
      second_run_loopLoopScheduler.add(dotsRoutineEnd(snapshot));
      second_run_loopLoopScheduler.add(second_run_loopLoopEndIteration(second_run_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function second_run_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(second_run_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function second_run_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function ITIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ITI' ---
    t = 0;
    ITIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('ITI.started', globalClock.getTime());
    // Run 'Begin Routine' code from preFixcross
    fixation_pre = randchoice([0.1, 0.35, 0.8, 1.2]);
    
    // keep track of which components have finished
    ITIComponents = [];
    ITIComponents.push(fixcross);
    
    for (const thisComponent of ITIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function ITIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ITI' ---
    // get current time
    t = ITIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixcross* updates
    if (t >= fixation_pre && fixcross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixcross.tStart = t;  // (not accounting for frame time here)
      fixcross.frameNStart = frameN;  // exact frame index
      
      fixcross.setAutoDraw(true);
    }
    
    frameRemains = fixation_pre + 0.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixcross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixcross.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ITIComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function ITIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ITI' ---
    for (const thisComponent of ITIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ITI.stopped', globalClock.getTime());
    // the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function dotsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'dots' ---
    t = 0;
    dotsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('dots.started', globalClock.getTime());
    // Run 'Begin Routine' code from codeDots
    if ((direction === "right")) {
        dots_direction = 0;
    } else {
        if ((direction === "left")) {
            dots_direction = 180;
        }
    }
    
    respDots.keys = undefined;
    respDots.rt = undefined;
    _respDots_allKeys = [];
    // keep track of which components have finished
    dotsComponents = [];
    dotsComponents.push(backgroundDots);
    dotsComponents.push(respDots);
    
    for (const thisComponent of dotsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function dotsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'dots' ---
    // get current time
    t = dotsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *backgroundDots* updates
    if (frameN >= 0 && backgroundDots.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      backgroundDots.tStart = t;  // (not accounting for frame time here)
      backgroundDots.frameNStart = frameN;  // exact frame index
      
      backgroundDots.setAutoDraw(true);
    }
    
    if (backgroundDots.status === PsychoJS.Status.STARTED && frameN >= (backgroundDots.frameNStart + 90)) {
      backgroundDots.setAutoDraw(false);
    }
    
    // *respDots* updates
    if (t >= 0.1 && respDots.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respDots.tStart = t;  // (not accounting for frame time here)
      respDots.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respDots.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respDots.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respDots.clearEvents(); });
    }
    
    if (respDots.status === PsychoJS.Status.STARTED) {
      let theseKeys = respDots.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _respDots_allKeys = _respDots_allKeys.concat(theseKeys);
      if (_respDots_allKeys.length > 0) {
        respDots.keys = _respDots_allKeys[_respDots_allKeys.length - 1].name;  // just the last key pressed
        respDots.rt = _respDots_allKeys[_respDots_allKeys.length - 1].rt;
        respDots.duration = _respDots_allKeys[_respDots_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of dotsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function dotsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'dots' ---
    for (const thisComponent of dotsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('dots.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(respDots.corr, level);
    }
    psychoJS.experiment.addData('respDots.keys', respDots.keys);
    if (typeof respDots.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('respDots.rt', respDots.rt);
        psychoJS.experiment.addData('respDots.duration', respDots.duration);
        routineTimer.reset();
        }
    
    respDots.stop();
    // the Routine "dots" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('feedback.started', globalClock.getTime());
    textFeedback.setText(response_text);
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(textFeedback);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textFeedback* updates
    if (t >= 0.0 && textFeedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textFeedback.tStart = t;  // (not accounting for frame time here)
      textFeedback.frameNStart = frameN;  // exact frame index
      
      textFeedback.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (textFeedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      textFeedback.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function instruction_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction_1' ---
    t = 0;
    instruction_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instruction_1.started', globalClock.getTime());
    // Run 'Begin Routine' code from codeInstr_2
    import {core, event, visual} from 'psychopy';
    import * as random from 'random';
    instructions = ["Anweisung 1", "Anweisung 2"];
    Math.random.shuffle(instructions);
    instruction_text = new visual.TextStim({"win": psychoJS.window, "text": "", "color": "white", "height": 30});
    for (var instruction, _pj_c = 0, _pj_a = instructions, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        instruction = _pj_a[_pj_c];
        instruction_text.text = instruction;
        instruction_text.draw();
        psychoJS.window.flip();
        psychoJS.eventManager.waitKeys({"keyList": ["space"]});
    }
    psychoJS.window.close();
    
    textSpeedInst.setText(instruction_text);
    respSpeedInstr.keys = undefined;
    respSpeedInstr.rt = undefined;
    _respSpeedInstr_allKeys = [];
    // keep track of which components have finished
    instruction_1Components = [];
    instruction_1Components.push(textSpeedInst);
    instruction_1Components.push(respSpeedInstr);
    
    for (const thisComponent of instruction_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function instruction_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction_1' ---
    // get current time
    t = instruction_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textSpeedInst* updates
    if (t >= 0.0 && textSpeedInst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textSpeedInst.tStart = t;  // (not accounting for frame time here)
      textSpeedInst.frameNStart = frameN;  // exact frame index
      
      textSpeedInst.setAutoDraw(true);
    }
    
    
    // *respSpeedInstr* updates
    if (t >= 0.0 && respSpeedInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respSpeedInstr.tStart = t;  // (not accounting for frame time here)
      respSpeedInstr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respSpeedInstr.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respSpeedInstr.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respSpeedInstr.clearEvents(); });
    }
    
    if (respSpeedInstr.status === PsychoJS.Status.STARTED) {
      let theseKeys = respSpeedInstr.getKeys({keyList: ['space'], waitRelease: false});
      _respSpeedInstr_allKeys = _respSpeedInstr_allKeys.concat(theseKeys);
      if (_respSpeedInstr_allKeys.length > 0) {
        respSpeedInstr.keys = _respSpeedInstr_allKeys[_respSpeedInstr_allKeys.length - 1].name;  // just the last key pressed
        respSpeedInstr.rt = _respSpeedInstr_allKeys[_respSpeedInstr_allKeys.length - 1].rt;
        respSpeedInstr.duration = _respSpeedInstr_allKeys[_respSpeedInstr_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instruction_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function instruction_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction_1' ---
    for (const thisComponent of instruction_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instruction_1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(respSpeedInstr.corr, level);
    }
    psychoJS.experiment.addData('respSpeedInstr.keys', respSpeedInstr.keys);
    if (typeof respSpeedInstr.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('respSpeedInstr.rt', respSpeedInstr.rt);
        psychoJS.experiment.addData('respSpeedInstr.duration', respSpeedInstr.duration);
        routineTimer.reset();
        }
    
    respSpeedInstr.stop();
    // the Routine "instruction_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function instruction_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction_2' ---
    t = 0;
    instruction_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instruction_2.started', globalClock.getTime());
    // Run 'Begin Routine' code from codeInstr_3
    import * as random from 'random';
    if ((selected_instruction === "accuracy")) {
        instruction_text_2 = "Wir sind nun mit dem ersten Hauptexperiment fertig und werden zum zweiten Hauptexperiment \u00fcbergehen. Bitte versuchen Sie dieses Mal so schnell wie m\u00f6glich zu antworten. Dr\u00fccken Sie [Leertaste], um das Hauptexperiment zu starten.";
    } else {
        if ((selected_instruction === "speed")) {
            instruction_text_2 = "Wir sind nun mit dem ersten Hauptexperiment fertig und werden zum zweiten Hauptexperiment \u00fcbergehen. Bitte versuchen Sie dieses Mal so genau wie m\u00f6glich zu antworten. Dr\u00fccken Sie [Leertaste], um das zweite Hauptexperiment zu starten.";
        }
    }
    
    textAccuracyInstr.setText(instruction_text_2);
    respAccuracyInstr.keys = undefined;
    respAccuracyInstr.rt = undefined;
    _respAccuracyInstr_allKeys = [];
    // keep track of which components have finished
    instruction_2Components = [];
    instruction_2Components.push(textAccuracyInstr);
    instruction_2Components.push(respAccuracyInstr);
    
    for (const thisComponent of instruction_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function instruction_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction_2' ---
    // get current time
    t = instruction_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textAccuracyInstr* updates
    if (t >= 0.0 && textAccuracyInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textAccuracyInstr.tStart = t;  // (not accounting for frame time here)
      textAccuracyInstr.frameNStart = frameN;  // exact frame index
      
      textAccuracyInstr.setAutoDraw(true);
    }
    
    
    // *respAccuracyInstr* updates
    if (t >= 0.0 && respAccuracyInstr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respAccuracyInstr.tStart = t;  // (not accounting for frame time here)
      respAccuracyInstr.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respAccuracyInstr.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respAccuracyInstr.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respAccuracyInstr.clearEvents(); });
    }
    
    if (respAccuracyInstr.status === PsychoJS.Status.STARTED) {
      let theseKeys = respAccuracyInstr.getKeys({keyList: ['space'], waitRelease: false});
      _respAccuracyInstr_allKeys = _respAccuracyInstr_allKeys.concat(theseKeys);
      if (_respAccuracyInstr_allKeys.length > 0) {
        respAccuracyInstr.keys = _respAccuracyInstr_allKeys[_respAccuracyInstr_allKeys.length - 1].name;  // just the last key pressed
        respAccuracyInstr.rt = _respAccuracyInstr_allKeys[_respAccuracyInstr_allKeys.length - 1].rt;
        respAccuracyInstr.duration = _respAccuracyInstr_allKeys[_respAccuracyInstr_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instruction_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function instruction_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction_2' ---
    for (const thisComponent of instruction_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instruction_2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(respAccuracyInstr.corr, level);
    }
    psychoJS.experiment.addData('respAccuracyInstr.keys', respAccuracyInstr.keys);
    if (typeof respAccuracyInstr.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('respAccuracyInstr.rt', respAccuracyInstr.rt);
        psychoJS.experiment.addData('respAccuracyInstr.duration', respAccuracyInstr.duration);
        routineTimer.reset();
        }
    
    respAccuracyInstr.stop();
    // the Routine "instruction_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function goodbyeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'goodbye' ---
    t = 0;
    goodbyeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('goodbye.started', globalClock.getTime());
    // keep track of which components have finished
    goodbyeComponents = [];
    goodbyeComponents.push(goodbye_text);
    
    for (const thisComponent of goodbyeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function goodbyeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'goodbye' ---
    // get current time
    t = goodbyeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *goodbye_text* updates
    if (t >= 0.0 && goodbye_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      goodbye_text.tStart = t;  // (not accounting for frame time here)
      goodbye_text.frameNStart = frameN;  // exact frame index
      
      goodbye_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (goodbye_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      goodbye_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of goodbyeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function goodbyeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'goodbye' ---
    for (const thisComponent of goodbyeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('goodbye.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}

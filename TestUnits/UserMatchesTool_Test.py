import pyautogui as p
import ExceptionWrappedTools as tool
import time

from paths_and_messages import *


def guiTest():
    #import path from paths_and_messages
    testFolder = PM_testFolder
    #Implement a failsafe pause
    p.PAUSE = 0.25

    # print('SCREEN COORDINATES ARE', p.locateCenterOnScreen('C:\\Users\\twr_000\\Desktop\\Horizon_Tool.png'))

    screenSize = p.size()


    '''


		Find the objects locations on screen


	'''

    cameraSolverLocation = tool.locateCenterOnScreen('CameraSolver', testFolder + 'C_CameraSolver.png')

    if (cameraSolverLocation == None):
        raise Exception('Cannot find C_CameraSolver from image recognition')

    #Tuple returns numpy.int32 which is not an int so we need to cast as int for pixelmatching.
    csX = int(cameraSolverLocation[0])
    csY = int(cameraSolverLocation[1])
    # print(p.pixel(csX, (csY + 7)))
    #Check C_CameraSolver's pixel colour is in the script on the specified location - Note this needs to be changed to image recognition
    if p.pixelMatchesColor(csX, (csY + 7),  (102, 0, 0)):
        #Click on the C_CameraSolver to open it's UI
	    p.click(cameraSolverLocation[0], cameraSolverLocation[1], clicks=2, interval=0.1, button='left')
    else:
        raise Exception('Failed to Find C_CameraSolver')


    #click on the cameraSolver Match tool
    cameraSolverMatchButtonLocation = tool.locateCenterOnScreen('Match Button' ,testFolder + 'match.png')
    p.click(cameraSolverMatchButtonLocation[0], cameraSolverMatchButtonLocation[1], clicks=1, interval=0, button='left')
    time.sleep(5)

    # click on the cameraSolver solve button
    cameraSolverSolveButtonLocation = tool.locateCenterOnScreen('Solve Button', testFolder + 'solve.png')
    p.click(cameraSolverSolveButtonLocation[0], cameraSolverSolveButtonLocation[1], clicks=1, interval=0, button='left')
    time.sleep(3)

    # click on the popup for not enough matches OK button
    notEnoughMatchesOKButtonLocation = tool.locateCenterOnScreen('Not Enough Matches Button', testFolder + 'notEnoughMatches_OK.png')
    p.click(notEnoughMatchesOKButtonLocation[0], notEnoughMatchesOKButtonLocation[1], clicks=1, interval=0, button='left')
    time.sleep(1)

    # click on the setupRig Button Location
    setupRigButtonLocation = tool.locateCenterOnScreen('Setup Rig Button', testFolder + 'setupRig.png')
    p.click(setupRigButtonLocation[0], setupRigButtonLocation[1], clicks=1, interval=0, button='left')
    time.sleep(1)

    #click on the userMatches tool
    userMatchesButtonLocation = tool.locateCenterOnScreen('User Match Button' ,testFolder + 'userMatches_icon.png')

    #check to see if we are roughly in the correct area to click on.
    if ((screenSize[0] * 0.03) <= userMatchesButtonLocation[0] <= (screenSize[0]*0.035)):
        p.click(userMatchesButtonLocation[0], userMatchesButtonLocation[1], clicks=1, interval=0, button='left')
    else:
        print('Cannot click on the userMatch tool, maybe it has already been clicked on?')


    ''' 


		Keyboard and mouse moves.


	'''
    ''' Move the the viewer'''

    #Hold down Ctrl + Alt
    p.keyDown('ctrl')
    p.keyDown('alt')


    #Move mouse to an overlapping point + click
    p.click((screenSize[0] * 0.3), (screenSize[1] * 0.21))

    #Release Ctrl + Alt
    p.keyUp('ctrl')
    p.keyUp('alt')




import pyautogui as p
import ExceptionWrappedTools as tool
import Evaluation as EV
import Utilities as UT

import time


def guiTest():
    testFolder = 'C:\\Users\\thomas.rice\\PycharmProjects\\GUI_Tester\\Test_Images\\'
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


    #click on the horizon tool
	#NOTE -  there are two symbols with the same icon here. Usually the first returned one is the one we want but we need some way of checking this.
    horizonToolButtonLocation = tool.locateCenterOnScreen('Horizon Tool' ,testFolder + 'icon.png')

    if (horizonToolButtonLocation == None):
        raise Exception('Cannot Find Horizon Tool')

    #Find the horizon button by image recognition then check the specified pixel is correct
	#As there are two buttons for this icon, check to see if we are roughly in the correct area to click on.
    if ((screenSize[0] * 0.03) <= horizonToolButtonLocation[0] <= (screenSize[0]*0.035)):
        p.click(horizonToolButtonLocation[0], horizonToolButtonLocation[1], clicks=1, interval=0, button='left')
    else:
        print('Cannot click on the horizon tool, maybe it has already been clicked on?')


    ''' 


		Keyboard and mouse moves.


	'''
    ''' Move the C_CameraSolver_UI'''
    #Move mouse to center
    p.moveTo((screenSize[0] * 0.4), (screenSize[1] * 0.3))


    #Hold down Ctrl + Alt
    p.keyDown('ctrl')
    p.keyDown('alt')

    #Drag to the left
    p.dragTo((screenSize[0] * 0.1), (screenSize[1] * 0.3), 3.0)

    #Drag up
    p.dragTo((screenSize[0] * 0.35), (screenSize[1] * 0.2), 3.0)

    #Drag to the left
    p.dragTo((screenSize[0] * 0.35), (screenSize[1] * 0.4), 3.0)

    #Release Ctrl + Alt
    p.keyUp('ctrl')
    p.keyUp('alt')






UT.openApplication()
UT.time.sleep(10)
UT.checkApplicationIsOpen()
UT.openFile()

time.sleep(5)
guiTest()

EV.captureViewer()
bbox = EV.getFinalImageBBOX('HorizonTool')
EV.evaluate(bbox, (414, 139, 514, 390),'HorizonTool Drag Move')

UT.closeApplication()
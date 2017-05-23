import time
import pyautogui as p

import Evaluation as EV
import Utilities as UT
from paths_and_messages import *
import ExceptionWrappedTools as tool


class baseTest(object):
    def __init__(self):
        #import path from paths_and_messages
        self.testFolder = PM_testFolder
        #Implement a failsafe pause
        p.PAUSE = 0.25
        # print('SCREEN COORDINATES ARE', p.locateCenterOnScreen('C:\\Users\\twr_000\\Desktop\\Horizon_Tool.png'))
        self.screenSize = p.size()

    def setup(self):
        UT.openApplication()
        time.sleep(15)
        UT.checkApplicationIsOpen()


    def openFile(self, fileToOpen):
        UT.openFile(fileToOpen)
        time.sleep(5)


    def evaluate(self, test, refBBOX):
        EV.captureViewer()
        bbox = EV.getFinalImageBBOX(test)
        # print(bbox)
        EV.evaluate(bbox, refBBOX, test)
        # (328, 162, 689, 345)

    def tearDown(self):
        UT.closeApplication()

    def clickCameraSolver(self):
        cameraSolverLocation = tool.locateCenterOnScreen('CameraSolver', self.testFolder + 'C_CameraSolver.png')

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

    def clickAndDrag(self):
        ''' 
            Keyboard and mouse moves.
        '''
        ''' Move the C_CameraSolver_UI'''
        #Move mouse to center
        p.moveTo((self.screenSize[0] * 0.4), (self.screenSize[1] * 0.3))


        #Hold down Ctrl + Alt
        p.keyDown('ctrl')
        p.keyDown('alt')

        #Drag to the left
        p.dragTo((self.screenSize[0] * 0.1), (self.screenSize[1] * 0.3), 3.0)

        #Drag up
        p.dragTo((self.screenSize[0] * 0.35), (self.screenSize[1] * 0.2), 3.0)

        #Drag to the left
        p.dragTo((self.screenSize[0] * 0.35), (self.screenSize[1] * 0.4), 3.0)

        #Release Ctrl + Alt
        p.keyUp('ctrl')
        p.keyUp('alt')



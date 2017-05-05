import pyautogui as p
import ExceptionWrappedTools as tool
from paths_and_messages import *

testFolder = PM_testFolder

def captureViewer():
    try:

        #screenshot the result image
        p.screenshot(testFolder + 'test.png', region=(414,139, 514, 390))
    except Exception as e:
        print('Error Screenshotting', e)


def getFinalImageBBOX(imageName):
       bbox = tool.locateOnScreen(imageName , testFolder + 'HorizonTool.png')

       return bbox



def evaluate(result, reference, testName):
    if reference != result:
        message = ('Image not the same as reference \n' + testName)
        # p.alert(message, 'Test Result', button='OK')
        return (False, message)
    else:
        message = ('Test Passed!!! - ' + testName)
        print(message)
        # p.alert(message, 'Test Result', button='OK')
        return (True, message)

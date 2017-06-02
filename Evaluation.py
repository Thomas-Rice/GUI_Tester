import pyautogui as p

import ExceptionWrappedTools as tool
from paths_and_messages import *

testFolder = PM_testFolder

def captureViewer(testName, captureRegion):
    try:
        #screenshot the result image
        p.screenshot(testFolder + testName + '_Result_Image.png', region=captureRegion )
    except Exception as e:
        print('Error Screenshotting', e)


def getFinalImageBBOX(imageName):
       bbox = tool.locateOnScreen(imageName , testFolder + imageName + '.png')
       return bbox



def evaluate(result, reference, testName):
    if reference != result:
        message = ('Test Failed :( -- Image not the same as reference \n' + testName)
        print(message)
        raise Exception('Image Comparison Failed - Result image is not the same as the Ref')
        return (False, message)
    else:
        message = ('Test Passed!!! - ' + testName)
        print(message)
        # p.alert(message, 'Test Result', button='OK')
        return (True, message)

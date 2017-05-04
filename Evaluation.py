import pyautogui as p
import ExceptionWrappedTools as tool

'TO DO - pass in region and filename'
testFolder = 'C:\\Users\\thomas.rice\\PycharmProjects\\GUI_Tester\\Test_Images\\'

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
        message = ('Test Failed - Image not the same as reference \n' + testName)
        p.alert(message, 'Test Result', button='OK')
        raise Exception(message)
    else:
        message = ('Test Passed!!! - ' + testName)
        print(message)
        p.alert(message, 'Test Result', button='OK')

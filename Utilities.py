import pyautogui as p
import ExceptionWrappedTools as tool
from paths_and_messages import *

import time


testFolder = PM_testFolder
screenSize = p.size()


# X = 641, Y = 1066
def openApplication(X = 960, Y = 1420):
    # TODO  check all the locations of the Nuke symbol - if there is more than one then require corods. If not then use the locateCenter func
    p.click(X, Y, 2, 0.1)

# X = 1887, Y = 8
def closeApplication(X = 3408, Y = 18):
    #Click the Close Button
    p.click(X, Y)

    # Sleep to wait for the window to open
    time.sleep(3)

    #Check if a save before close window is there
    isWarningPopupOpen(True)


def checkApplicationIsOpen():
    appIsOpen = tool.locateCenterOnScreen('NukeFileMenu', testFolder + 'File_Menus_Open_Check.png')


def openFile():
    # click in the script editor
    p.click(screenSize[0], screenSize[1] - 100)
    #open the hotkey window
    p.hotkey('ctrl', 'o')

    # Dont need to click on the filePath box as it's already selected
    # 850, 660
    # Click on the file path input box
    # filePathBox = tool.locateCenterOnScreen('filePath Box', testFolder + 'filePath_box.png')
    # p.click(filePathBox[0], filePathBox[1])

    #Enter the path to the file
    p.typewrite('GUI_Automation1.nk')
    p.press('enter')

    #Sleep to wait for the window to open
    time.sleep(3)

    # 999, 564
    #check if popup is there and click corods if so.
    isWarningPopupOpen(True)


def isWarningPopupOpen(no = None):
    # TODO add in a click on the yes option too
    isWindowOpen = tool.locateCenterOnScreen('Popup Window', testFolder + 'autoSave_Check.png', True)
    noButton = tool.locateCenterOnScreen('No Button', testFolder + 'popup_No.png', True)
    if isWindowOpen is not None:
        if no:
            p.click(noButton[0], noButton[1])
        # if yes:
        #     p.click(yesButton[0], yesButton[1])
    else:
        print('No Popup window detected - this is likely fine')



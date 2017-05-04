import pyautogui as p
import ExceptionWrappedTools as tool
import time

testFolder = 'C:\\Users\\thomas.rice\\PycharmProjects\\GUI_Tester\\Test_Images\\'

def openApplication(X = 641, Y = 1066):
    p.click(X, Y, 2, 0.1)


def closeApplication(X = 1887, Y = 8):
    #Click the Close Button
    p.click(X, Y,)

    # Sleep to wait for the window to open
    time.sleep(3)

    #Check if a save before close window is there
    isWarningPopupOpen(961, 548)


def checkApplicationIsOpen():
    appIsOpen = tool.locateCenterOnScreen('NukeFileMenu', testFolder + 'File_Menus_Open_Check.png')


def openFile():
    # click in the script editor
    p.click(162, 949)
    #open the hotkey window
    p.hotkey('ctrl', 'o')
    # Click on the file path input box
    p.click(850, 660)
    #Enter the path to the file
    p.typewrite('test_Script.nk')
    p.press('enter')

    #Sleep to wait for the window to open
    time.sleep(3)

    #check if popup is there and click corods if so.
    isWarningPopupOpen(999, 564)


def isWarningPopupOpen(X, Y):
    isWindowOpen = tool.locateCenterOnScreen('Popup Window', testFolder + 'autoSave_Check.png')
    if isWindowOpen is not None:
        p.click(X, Y)
    else:
        print('No Popup window detected - this is likely fine')


# openApplication()
# time.sleep(10)
# checkApplicationIsOpen()
# openFile()
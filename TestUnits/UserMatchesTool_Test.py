from  baseTest import *



class UserMatchesTool_Test(baseTest):
    # Inherits the baseClass
    def __init__(self):
        super(UserMatchesTool_Test, self).__init__()

    def matchAndSolveSetupRig(self):

        #click on the cameraSolver Match tool
        cameraSolverMatchButtonLocation = tool.locateCenterOnScreen('Match Button' ,self.testFolder + 'match.png')
        p.click(cameraSolverMatchButtonLocation[0], cameraSolverMatchButtonLocation[1], clicks=1, interval=0, button='left')
        time.sleep(5)

        # click on the cameraSolver solve button
        cameraSolverSolveButtonLocation = tool.locateCenterOnScreen('Solve Button', self.testFolder + 'solve.png')
        p.click(cameraSolverSolveButtonLocation[0], cameraSolverSolveButtonLocation[1], clicks=1, interval=0, button='left')
        time.sleep(3)

        # click on the popup for not enough matches OK button
        notEnoughMatchesOKButtonLocation = tool.locateCenterOnScreen('Not Enough Matches Button', self.testFolder + 'notEnoughMatches_OK.png')
        p.click(notEnoughMatchesOKButtonLocation[0], notEnoughMatchesOKButtonLocation[1], clicks=1, interval=0, button='left')
        time.sleep(1)

        # click on the setupRig Button Location
        setupRigButtonLocation = tool.locateCenterOnScreen('Setup Rig Button', self.testFolder + 'setupRig.png')
        p.click(setupRigButtonLocation[0], setupRigButtonLocation[1], clicks=1, interval=0, button='left')
        time.sleep(1)
        
    def clickUserMatchesTool(self):

        #click on the userMatches tool
        userMatchesButtonLocation = tool.locateCenterOnScreen('User Match Button' ,self.testFolder + 'userMatches_icon.png')

        #check to see if we are roughly in the correct area to click on.
        if ((self.screenSize[0] * 0.03) <= userMatchesButtonLocation[0] <= (self.screenSize[0]*0.035)):
            p.click(userMatchesButtonLocation[0], userMatchesButtonLocation[1], clicks=1, interval=0, button='left')
        else:
            print('Cannot click on the userMatch tool, maybe it has already been clicked on?')

    def clickAndDrag(self):
        #Hold down Ctrl + Alt
        p.keyDown('ctrl')
        p.keyDown('alt')


        #Move mouse to an overlapping point + click
        p.click((self.screenSize[0] * 0.3), (self.screenSize[1] * 0.21))

        #Release Ctrl + Alt
        p.keyUp('ctrl')
        p.keyUp('alt')




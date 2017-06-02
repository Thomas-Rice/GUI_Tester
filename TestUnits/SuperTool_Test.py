from UserMatchesTool_Test import *


class SuperTool_Test(UserMatchesTool_Test):
    def __init__(self):
        super(SuperTool_Test, self).__init__()
        pass


    def ctrlAltCam1(self):
        ''' Move the C_CameraSolver_UI'''
        # Click on the camera 1
        p.click((self.screenSize[0] * 0.491), (self.screenSize[1] * 0.3))
        #Click on the camera outline to move the camera
        p.moveTo((self.screenSize[0] * 0.48), (self.screenSize[1] * 0.3))

        # Hold down Ctrl + Alt
        p.keyDown('ctrl')
        p.keyDown('alt')

        # Drag to the left
        p.dragTo((self.screenSize[0] * 0.1), (self.screenSize[1] * 0.3), 3.0)

        # Drag up
        p.dragTo((self.screenSize[0] * 0.35), (self.screenSize[1] * 0.2), 3.0)

        # Drag to the left
        p.dragTo((self.screenSize[0] * 0.35), (self.screenSize[1] * 0.4), 3.0)

        # Release Ctrl + Alt
        p.keyUp('ctrl')
        p.keyUp('alt')

        #Click off screen to deselect the camera for the next step
        p.click((self.screenSize[0] * 0.1), (self.screenSize[1] * 0.3))
        #Click on the camera outline to move the camera
        p.click((self.screenSize[0] * 0.5), (self.screenSize[1] * 0.3))



    def clickUserMatch(self):

        #Move mouse to an overlapping point + click
        p.click((self.screenSize[0] * 0.267), (self.screenSize[1] * 0.225))

    def clickAndDrag(self):

        ''' Move the C_CameraSolver_UI'''
        #Move mouse to center + a bit left to hit the camera
        p.click((self.screenSize[0] * 0.45), (self.screenSize[1] * 0.3))


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
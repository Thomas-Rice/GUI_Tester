from  baseTest import *




class CamerasTool_Test(baseTest):
    # Inherits the baseClass
    def __init__(self):
        super(CamerasTool_Test, self).__init__()



    def clickCamerasTool(self):

        #click on the cameras tool
        #NOTE -  there are two symbols with the same icon here. Usually the first returned one is the one we want but we need some way of checking this.
        camerasToolButtonLocation = tool.locateCenterOnScreen('Cameras Tool' ,self.testFolder + 'cameras_icon.png')

        if (camerasToolButtonLocation == None):
            raise Exception('Cannot Find the Tool')

        #Find the cameras button by image recognition then check the specified pixel is correct
        p.click(camerasToolButtonLocation[0], camerasToolButtonLocation[1], clicks=1, interval=0, button='left')

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
from  baseTest import *



class HorizonTool_Test(baseTest):
    # Inherits the baseClass
    def __init__(self):
        super(HorizonTool_Test, self).__init__()
        pass


    def clickHorizonTool(self):
        #click on the horizon tool
        #NOTE -  there are two symbols with the same icon here. Usually the first returned one is the one we want but we need some way of checking this.
        horizonToolButtonLocation = tool.locateCenterOnScreen('Horizon Tool' ,self.testFolder + 'icon.png')

        if (horizonToolButtonLocation == None):
            raise Exception('Cannot Find Horizon Tool')

        #Find the horizon button by image recognition then check the specified pixel is correct
        #As there are two buttons for this icon, check to see if we are roughly in the correct area to click on.
        if ((self.screenSize[0] * 0.03) <= horizonToolButtonLocation[0] <= (self.screenSize[0]*0.035)):
            p.click(horizonToolButtonLocation[0], horizonToolButtonLocation[1], clicks=1, interval=0, button='left')
        else:
            print('Cannot click on the horizon tool, maybe it has already been clicked on?')




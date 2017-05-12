from  baseTest import *

from CamerasTool_Test import *
from HorizonTool_Test import *
from UserMatchesTool_Test import *


class SuperTool_Test(baseTest):
    def __init__(self):
        super(SuperTool_Test, self).__init__()
        self.CT = CamerasTool_Test()
        self.HT = HorizonTool_Test()
        self.UMT = UserMatchesTool_Test()

    def execute(self):
        #TODO  - Issue here is that C_CameraSolver is selected. So it will not recognise it.
        self.CT.execute()
        print('Run CT')
        self.HT.execute()
        print('Run HT')
        self.UMT.execute()
        print('Run UMT')


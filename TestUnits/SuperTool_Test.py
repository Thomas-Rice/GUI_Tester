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
        self.CT.execute()
        self.HT.execute()
        self.UMT.execute()


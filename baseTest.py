import Evaluation as EV
import Utilities as UT

import time


class baseTest():
    def __init__(self, testCommands):
        self.testCommands = testCommands

    def setup(self):
        UT.openApplication()
        time.sleep(15)
        UT.checkApplicationIsOpen()
        UT.openFile()
        time.sleep(5)

    def execute(self):
        self.testCommands.guiTest()

    def evaluate(self):
        EV.captureViewer()
        bbox = EV.getFinalImageBBOX('HorizonTool')
        EV.evaluate(bbox, (328, 162, 689, 345),'HorizonTool Drag Move')

    def tearDown(self):
        UT.closeApplication()




if __name__ == '__main__':
    # Needs to be changed so we import all tests in the future.
    import HorizonTool_Test as Test_1
    t = baseTest(Test_1)
    t.setup()
    t.execute()
    t.evaluate()
    t.tearDown()


import time

import Evaluation as EV
import Utilities as UT


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

    def evaluate(self, test, refBBOX):
        EV.captureViewer()
        bbox = EV.getFinalImageBBOX(test)
        # print(bbox)
        EV.evaluate(bbox, refBBOX, test)
        # (328, 162, 689, 345)

    def tearDown(self):
        UT.closeApplication()




if __name__ == '__main__':
    # Needs to be changed so we import all tests in the future.
    from TestUnits import HorizonTool_Test as Test_1

    t = baseTest(Test_1)
    t.setup()
    t.execute()
    t.evaluate()
    t.tearDown()


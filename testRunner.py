import importlib
from paths_and_messages import *

import sys
import os
import glob
import time


tests = []
importedTests = {}

sys.path.append(PM_testUnits)



#get a list of all test files
for filename in glob.glob(PM_testUnits + "*_Test.py"):
    #Strip the py then take the basename / filename
    tests.append(os.path.basename(os.path.splitext(filename)[0]))

#import all test files
for file in tests:
    module = getattr(importlib.import_module(file), file)
    importedTests[file]= module()




#Stack of functions to call from baseTest
def runExecutionStack(testObject, testName):
    testObject.setup()
    testObject.execute()
    testObject.evaluate(testName, PM_bboxes[testName])
    testObject.tearDown()


def reportTestRun():
    #TODO - Report the results of all the tests
    pass

def run():
    #Run all the tests in the sequence
    for i in tests:
        print(importedTests[i])
        testToRun = importedTests[i]
        runExecutionStack(testToRun, i)
        time.sleep(5)


def returnTestObjects():
    return importedTests

if __name__== '__main__':
    run()
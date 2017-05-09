import baseTest
import importlib
from paths_and_messages import *

import sys
import os
import glob

# TODO - Run through a list of tests and execute them

tests = []
importedTests = []

sys.path.append(PM_testUnits)



#get a list of all test files
for filename in glob.glob(PM_testUnits + "*_Test.py"):
    #Strip the py then take the basename / filename
    tests.append(os.path.basename(os.path.splitext(filename)[0]))

#import all test files
for file in tests:
    module = importlib.import_module(file)
    importedTests.append(module)




#Stack of functions to call from baseTest
def runExecutionStack(t):
    t.setup()
    t.execute()
    t.evaluate()
    t.tearDown()


def reportTestRun():
    #TODO - Report the results of all the tests
    pass


# #Run all the tests in the sequence
for i in range(0, len(tests)):
    testToRun = baseTest.baseTest(importedTests[i])
    runExecutionStack(testToRun)
#
#

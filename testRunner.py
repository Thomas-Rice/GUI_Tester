import baseTest

# TODO - Run through a list of tests and execute them
import HorizonTool_Test as Test_1
tests = ['HorizonTool_Test']


import importlib
for file in tests:
    importlib.import_module(file)






# #Stack of functions to call from baseTest
# def runExecutionStack(t):
#     t.setup()
#     t.execute()
#     t.evaluate()
#     t.tearDown()
#
#
# def reportTestRun():
#     #TODO - Report the results of all the tests
#     pass
#
#
# #Run all the tests in the sequence
# for test in tests:
#     testToRun = baseTest.baseTest(test)
#     runExecutionStack(testToRun)
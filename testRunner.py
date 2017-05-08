import baseTest
import importlib


# TODO - Run through a list of tests and execute them

tests = ['HorizonTool_Test']

listOfTests = []


for file in tests:
    i = importlib.import_module(file)
    listOfTests.append(i)




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
    testToRun = baseTest.baseTest(listOfTests[i])
    runExecutionStack(testToRun)



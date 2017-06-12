# UI automation using pyautogui and opencv and BDD.

# Installation:
To get started, we'll need to ensure that pyautogui is installed. The easiest means of doing so is with Pip:

```
pip install pyautogui
```
I'd recommend taking a good look at the install instuctions listed here:
https://pyautogui.readthedocs.io/en/latest/install.html


Next I'd suggest getting opencv as this will enhance the feature detection of pyautogui:
```
pip install opencv-python
```

And Numpy:
```
pip install numpy
```

Finally lets get behave which is a python implementation of Cucumber, a Behavioural Driven Development approach.

```
pip install behave
```

Alternatively you can read [installation documenation](http://pythonhosted.org/behave/install.html) on the Behave website. 




# Running

TO RUN:
In terminal / cmd
```
cd into GUI_Tester/features
behave
```



# BDD Example and test writing
Using BDD allow us to create user stories/ scenarios which describe the steps a test will take in execution order.

Tests start with writing "Feature" files that use plain english to describe the steps of your test. Features use keywords to form the actual steps being taken in the test:

* **Given** we put the system in a known state before the user (or external system) starts interacting with the system (in the When steps). Avoid talking about user interaction in givens.

* **When** we take key actions the user (or external system) performs. This is the interaction with your system which should (or perhaps should not) cause some state to change.

* **Then** we observe outcomes.

Within the 'Feature_Files' directory are all of the feature scenarios used for testing. They describe interactions with the website and map directly to functions to perform the actions.

These feature files are name the same as the python files located in the 'Steps' directory.
The python files are where the functions to perform website operations are stored.
 These files call on factory classes with a generic base set of functions are located which aid with wrapping common functions in one place, the factory files are found in Page_Objects.
 There is current a base class -> basePage which then is inherited by two other classes to extend functionality specific to that page:

            '''
            basePage   --> bag (bag operations)
                       --> savedItem (saved item operations)
            '''

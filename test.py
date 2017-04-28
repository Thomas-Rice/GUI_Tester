import pyautogui as p

#Implement a failsafe pause
p.PAUSE = 0.25

# print('SCREEN COORDINATES ARE', p.locateCenterOnScreen('C:\\Users\\twr_000\\Desktop\\Horizon_Tool.png'))

screenSize = p.size()


#Check C_CameraSolver's pixel colour is in the script on the specified location - Note this needs to be changed to image recognition
if p.pixelMatchesColor(802, 1209,  (163, 0, 0)):
    #Click on the C_CameraSolver to open it's UI
    p.click(x=802, y=1209, clicks=2, interval=0.1, button='left')
else:
    raise Exception('Failed to Find C_ColourMatcher')


#click on the horizon tool
horizonToolButtonLocation = p.locateCenterOnScreen('C:\\Users\\twr_000\\Desktop\\Horizon_Tool.png')

print(p.pixel(int(horizonToolButtonLocation[0]), int(horizonToolButtonLocation[1])))

#Find the horizon button by image recognition then check the specified pixel is correct
if horizonToolButtonLocation != None and p.pixelMatchesColor(int(horizonToolButtonLocation[0]), int(horizonToolButtonLocation[1]), (156, 156, 156)):
    p.click(x=horizonToolButtonLocation[0], y=horizonToolButtonLocation[1], clicks=1, interval=0, button='left')
else:
    raise Exception('Cannot Find Horizon Tool')





''' Move the C_CameraSolver_UI'''
#Move mouse to center
p.moveTo(1230, 438)



#Hold down Ctrl + Alt
p.keyDown('ctrl')
p.keyDown('alt')

#Drag to the left
p.dragTo((screenSize[0] * 0.1), (screenSize[1] * 0.3), 3.0)

#Drag up
p.dragTo((screenSize[0] * 0.35), (screenSize[1] * 0.1), 3.0)

#Drag to the left
p.dragTo((screenSize[0] * 0.35), (screenSize[1] * 0.4), 3.0)

#Release Ctrl + Alt
p.keyUp('ctrl')
p.keyUp('alt')
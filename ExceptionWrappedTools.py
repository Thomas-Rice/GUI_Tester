import pyautogui as p


def locateCenterOnScreen(imageName, imagePath, ):
    result = p.locateCenterOnScreen(imagePath)

    coord = analyseResult(result, imageName)
    return coord


def locateOnScreen(imageName, imagePath):
    result = p.locateOnScreen(imagePath)

    coord = analyseResult(result, imageName)
    return coord


'''this function might not be needed '''
def analyseResult(result, imageName):
    if result is None:
        print('locateOnScreen returned None therefore could not match the reference')
    else:
        assert isinstance(result, object)
        return result
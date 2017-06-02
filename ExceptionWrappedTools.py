import pyautogui as p


def locateCenterOnScreen(imageName, imagePath, popup = False):
    result = p.locateCenterOnScreen(imagePath)

    coord = analyseResult(result, imageName, popup)
    return coord


def locateOnScreen(imageName, imagePath, popup = False):
    result = p.locateOnScreen(imagePath)

    coord = analyseResult(result, imageName, popup)
    return coord


'''this function might not be needed '''
def analyseResult(result, imageName, isPopup = False):
    if result is None and not isPopup:
        raise Exception('Final Image Comparison Failed')
    else:
        assert isinstance(result, object)
        return result
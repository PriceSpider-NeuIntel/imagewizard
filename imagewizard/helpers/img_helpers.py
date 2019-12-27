import cv2 as cv

def imread(file_name):
    try:
        return cv.imread(file_name)
    except Exception as inst:
        return inst
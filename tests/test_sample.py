# Sample Test passing with nose and pytest
import sys
import cv2 as cv
sys.path.append("..")

import imagewizard
from PIL import Image

def test_pass():
    # assert True, "dummy sample test"
    a_hash = imagewizard.ahash(Image.open('data/test.png'))
    d_hash = imagewizard.dhash(Image.open('data/test.png'))
    print(a_hash, "\n", d_hash)

def test_hamming():
    a_hex, b_hex = 0x4bd1, 5 #, '0x4bd1', '5', '0b1001']
    # a_int, b_int = '4bd1', ['5bd2', 0x4bd1]
    # a_bin_list, b_bin_list = [1,0,0,0,1], [0,1,1,0,1]

    print("cosine distance: ", imagewizard.similarity(a_hex, b_hex, "cosine"))
    print("hamming distance: ", imagewizard.similarity(a_hex, b_hex, "hamming"))
    print("euclidean distance: ", imagewizard.similarity(a_hex, b_hex, "euclidean"))
    print("manhattan distance: ", imagewizard.similarity(a_hex, b_hex, "manhattan"))
    print("jaccard distance: ", imagewizard.similarity(a_hex, b_hex, "jaccard"))
    print("minkowski distance: ", imagewizard.similarity(a_hex, b_hex, "minkowski"))

def test_colorspaces():
    pro = imagewizard.image_processsing.Processing()
    res = pro.bgr_to_gray('data/test.png')
    img = cv.imread('data/test.png')
    cv.imshow('original', img)
    cv.imshow('new1', res[0])
    cv.imshow('new2', res[1])
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite('new1.png', res[0])
    cv.imwrite('new2.png', res[1])

if __name__=="__main__":
    # test_hamming()
    test_colorspaces()


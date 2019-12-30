# Sample Test passing with nose and pytest
import sys
import cv2 as cv
sys.path.append("..")

import imagewizard
from PIL import Image

def test_hashing():
    # assert True, "dummy sample test"
    ihash = imagewizard.Hashing()
    a_hash = ihash.ahash(Image.open('data/test.png'))
    d_hash = ihash.dhash(Image.open('data/test.png'))
    p_hash = ihash.phash(Image.open('data/test.png'))
    w_hash = ihash.whash(Image.open('data/test.png'))
    print("a hash: ", a_hash, "\nd hash: ", d_hash, "\nphash: ", p_hash, "\nwhash: ", w_hash)

def test_hamming():
    a_hex, b_hex = 0x4bd1, 5 #, '0x4bd1', '5', '0b1001']
    # a_int, b_int = '4bd1', ['5bd2', 0x4bd1]
    # a_bin_list, b_bin_list = [1,0,0,0,1], [0,1,1,0,1]
    isim = imagewizard.Similarity()
    print("cosine distance: ", isim.similarity(a_hex, b_hex, "cosine"))
    print("hamming distance: ", isim.similarity(a_hex, b_hex, "hamming"))
    print("euclidean distance: ", isim.similarity(a_hex, b_hex, "euclidean"))
    print("manhattan distance: ", isim.similarity(a_hex, b_hex, "manhattan"))
    print("jaccard distance: ", isim.similarity(a_hex, b_hex, "jaccard"))
    print("minkowski distance: ", isim.similarity(a_hex, b_hex, "minkowski"))

def test_colorspaces():
    img = cv.imread('data/test.png')
    improcess = imagewizard.Processing()
    res = improcess.img2grayscale(img, True)

    cv.imshow('original', img)
    cv.imshow('processed', res)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__=="__main__":
    # test_hamming()
    # test_colorspaces()
    test_hashing()


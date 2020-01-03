# Sample Test passing with nose and pytest
import sys
import cv2 as cv
sys.path.append("..")

import imagewizard
from PIL import Image

def test_hashing():
    # assert True, "dummy sample test"
    ihash = imagewizard.Hashing()
    a_hash = ihash.ahash(image = Image.open('data/test.png'))
    d_hash = ihash.dhash(Image.open('data/test.png'))
    p_hash = ihash.phash(Image.open('data/test.png'))
    # w_hash = ihash.whash(Image.open('data/test.png'))
    w_hash = ihash.whash(cv.imread('data/test.png'))
    print("a hash: {}".format(a_hash))
    print("a hash: ", str(a_hash), "\nd hash: ", d_hash, "\nphash: ", p_hash, "\nwhash: ", w_hash)
    print("PIL a-hash: {}".format(a_hash))

def test_similarity():
    a_hex, b_hex = [0, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0, 0]# 0x4bd1, 5 #, '0x4bd1', '5', '0b1001']
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

def test_hash_and_similarity():

    iw_similarity = imagewizard.Similarity()
    iw_hash = imagewizard.Hashing()
    
    image1 = cv.imread('data/test.png')
    hash1_str = str(iw_hash.dhash(image1, order = 'BGR'))
    
    image2 = cv.imread('data/test2.png')
    hash2_str = str(iw_hash.dhash(image2, order = 'BGR'))

    print("cosine : {}".format(iw_similarity.similarity(hash1_str, hash2_str, 'cosine')))
    print("hamming : {}".format(iw_similarity.similarity(hash1_str, hash2_str, 'hamming')))
    print("euclidean : {}".format(iw_similarity.similarity(hash1_str, hash2_str, 'euclidean')))
    print("manhattan : {}".format(iw_similarity.similarity(hash1_str, hash2_str, 'manhattan')))
    print("jaccard : {}".format(iw_similarity.similarity(hash1_str, hash2_str, 'jaccard')))
    print("minkowski : {}".format(iw_similarity.similarity(hash1_str, hash2_str, 'minkowski')))

if __name__=="__main__":
    # test_colorspaces()
    # test_hashing()
    test_hash_and_similarity()
    # TODO: test image processing 
    # TODO: add coverage
    # TODO: add travis build

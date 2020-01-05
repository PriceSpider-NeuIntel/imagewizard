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

def test_lum():
    img = cv.imread('data/original_images/lenna.png')
    ip = imagewizard.Processing()

    lum_100 = ip.luminosity(img, 100, 'bgr')
    lum_150 = ip.luminosity(img, 150, 'bgr')
    lum_255 = ip.luminosity(img, 255, 'bgr')

    lum_neg_100 = ip.luminosity(img, -100, 'bgr')
    lum_neg_255 = ip.luminosity(img, -255, 'bgr')

    # cv.imshow("original image", img)
    # cv.imshow('lum 100', lum_100)
    # cv.imshow('lum 150', lum_150)
    # cv.imshow('lum -100', lum_neg_100)

    # cv.imshow('lum 255', lum_255)
    # cv.imshow('lum -255', lum_neg_255)

    cv.imwrite('lum_100.png', lum_100)
    cv.imwrite('lum_neg_100.png', lum_neg_100)
    

    cv.waitKey(0)
    cv.destroyAllWindows()

def test_blur():
    img = cv.imread('data/original_images/street.png')
    ip = imagewizard.Processing()

    blur5 = ip.blur(img, blur_level=5, order='bgr')
    blur25 = ip.blur(img, blur_level=25, order='bgr')
    blur50 = ip.blur(img, blur_level=50, order='bgr')

    cv.imshow("original image", img)
    cv.imshow('blur 5', blur5)
    cv.imshow('blur 25', blur25)
    cv.imshow('blur 50', blur50)

    cv.imwrite('blur5.png', blur5)
    cv.imwrite('blur25.png', blur25)
    cv.imwrite('blur50.png', blur50)

    cv.waitKey(0)
    cv.destroyAllWindows()


def test_mirror():
    img = cv.imread('data/original_images/lenna.png')
    ip = imagewizard.Processing()

    mir_x = ip.mirror(img, flip_code=1, order='bgr')
    mir_y = ip.mirror(img, flip_code=0, order='bgr')
    mir_xy = ip.mirror(img, flip_code=-1, order='bgr')

    cv.imshow('flip image around X axis', mir_x)
    cv.imshow('flip image around Y axis', mir_y)
    cv.imshow('flip image around both X & Y axis', mir_xy)
    
    cv.imwrite('flip_x.png', mir_x)
    cv.imwrite('flip_y.png', mir_y)
    cv.imwrite('flip_xy.png', mir_xy)

    cv.waitKey(0)
    cv.destroyAllWindows()

def test_crop():
    img = cv.imread('data/original_images/street.png')
    ip = imagewizard.Processing()
    crop1 = ip.crop(img, start_x = 50, end_x = 100, start_y = 50, end_y = 100, is_percentage=True, order='bgr')
    crop2 = ip.crop(img, 400, 1000, 0, 500, is_percentage=False, order='bgr')
    
    # cv.imshow('original', img)
    # cv.imshow('cropped 1', crop1)
    # cv.imshow('cropped 2', crop2)

    cv.imwrite('crop1.png', crop1)
    cv.imwrite('crop2.png', crop2)

    cv.waitKey(0)
    cv.destroyAllWindows()


def test_rotate():
    img = cv.imread('data/original_images/lenna.png')
    ip = imagewizard.Processing()

    # res1 = ip.rotate(img, 90, order='bgr')
    # res2 = ip.rotate(img, 180, order='bgr')
    # res3 = ip.rotate(img, 270, order='bgr')
    # res4 = ip.rotate(img, 315, scaling_factor=0.5, order='bgr')
    # res5 = ip.rotate(img, 45, scaling_factor=2, order='bgr')
    
    # cv.imshow('original', img)
    # cv.imshow('res1', res1)
    # cv.imshow('res2', res2)
    # cv.imshow('res3', res3)
    # cv.imshow('res4', res4)
    # cv.imshow('res5', res5)

    # cv.imwrite('rotate-90deg.png', res1)
    # cv.imwrite('rotate-180deg.png', res2)
    # cv.imwrite('rotate-270deg.png', res3)
    # cv.imwrite('rotate-315deg-scale.png', res4)
    # cv.imwrite('rotate-45deg-scale.png', res5)

    cv.waitKey(0)
    cv.destroyAllWindows()

def test_resize_zoom():
    img = cv.imread('data/test.png')
    ip = imagewizard.Processing()
    
    # res = ip.resize(img, resize_percentage = 50, order = 'bgr')
    res = ip.resize(img, resize_width=300, resize_height=300, order = 'bgr')
    # dim = (2000, 2000)
    # interpolation = cv.INTER_LINEAR
    # res = cv.resize(img, dim, interpolation=interpolation)

    # cv.imshow('Original Image', img)
    # cv.imshow('Resized Image (zoom)', res)
    cv.imwrite('shrink-300px-300px.png', res)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

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

def test_binarize():
    image = cv.imread('data/original_images/lenna.png')
    # cv.imshow("Original Image", image)
    # cv.imwrite('org_lenna.png', image)

    ip = imagewizard.Processing()
    # cv.imshow("inverted Image", cv.bitwise_not(image))

    """
    inv_img = ip.img2grayscale(image, inverted=True, is_gray=False, order = 'bgr')
    cv.imshow("inverted Image", cv.bitwise_not(image))
    cv.imwrite('clr_inverted.png', inv_img)

    gray_image = ip.img2grayscale(image, inverted=True, order = 'bgr')
    cv.imshow("Gray Inverted", gray_image)
    cv.imwrite('gray_inverted.png', gray_image)

    trunc_inv_image = ip.img2grayscale(image, trunc=True, inverted=True, order = 'bgr')
    cv.imshow("Trunc Inverted", trunc_inv_image)
    cv.imwrite('trunc_inverted.png', trunc_inv_image)

    gray_image = ip.img2grayscale(image, order = 'bgr')
    cv.imshow("Gray", gray_image)
    cv.imwrite('gray.png', gray_image)
    
    binary_image = ip.img2grayscale(image, to_binary=True, order = 'bgr')
    cv.imshow("Binary Threshold", binary_image)
    cv.imwrite('binary_img.png', binary_image)

    binary_inv_image = ip.img2grayscale(image, to_binary=True, inverted=True, order = 'bgr')
    cv.imshow("Binary Threshold Inverted Image", binary_inv_image)
    cv.imwrite('binary_inv_image.png', binary_inv_image)

    trunc_image = ip.img2grayscale(image, trunc=True, order = 'bgr')
    cv.imshow("Trucated Threshold Image", trunc_image)
    cv.imwrite('trunc_image.png', trunc_image)

    to_zero_image = ip.img2grayscale(image, to_zero=True, order = 'bgr')
    cv.imshow("To Zero Image", to_zero_image)
    cv.imwrite('to_zero_image.png', to_zero_image)

    to_zero_inverted = ip.img2grayscale(image, to_zero=True, inverted = True, order = 'bgr')
    cv.imshow("To Zero Inverted Image", to_zero_inverted)
    cv.imwrite('to_zero_inverted.png', to_zero_inverted)
    """

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__=="__main__":
    # test_colorspaces()
    # test_hashing()
    # test_hash_and_similarity()
    # test_resize_zoom()
    # test_rotate()
    # test_crop()
    # test_mirror()
    # test_blur()
    test_lum()
    # test_binarize()
    # TODO: test image processing 
    # TODO: add coverage
    # TODO: needles in hay stack testing
    # TODO: add travis build


# Sample Test passing with nose and pytest
import sys
import cv2 as cv
sys.path.append("..")
import numpy as np

import imagewizard
from PIL import Image

def crop_color_border(in_img: np.ndarray = None) -> np.ndarray:
    in_img = cv.imread('data/original_images/quiet_flow10.png')  
    """Determine if image has uniform color padding and crop if so"""
    # Check number of dims of input img
    dims = len(in_img.shape)
    # Convert to grey if dims > 2, assume BGR input
    if dims > 2:
        img = cv.cvtColor(in_img, cv.COLOR_BGR2GRAY)
        # img = ImageCompare.to_gray(in_img)
    else:
        img = np.copy(in_img)
    upperLeftVal = img[0, 0]
    # We need to check for left and right cols that uniformly match upperLeftValue
    borderCols = [all(img[:, i] == upperLeftVal) for i in range(img.shape[1])]
    if not any(borderCols):  # Should only happen if no column is uniform
        leftCol = 0
        rightCol = img.shape[1]
    else:
        leftCol = min(
            [
                img.shape[1] + 1 if borderCols[j] else j
                for j in range(len(borderCols))
            ]
        )
        rightCol = max([0 if borderCols[j] else j for j in range(len(borderCols))])
    # Repeat process for rows
    borderRows = [all(img[:, i] == upperLeftVal) for i in range(img.shape[0])]
    if not any(borderRows):  # Should only happen if no Rowumn is uniform
        leftRow = 0
        rightRow = img.shape[0]
    else:
        leftRow = min(
            [
                img.shape[0] + 1 if borderRows[j] else j
                for j in range(len(borderRows))
            ]
        )
        rightRow = max([0 if borderRows[j] else j for j in range(len(borderRows))])

    res = in_img[leftCol:rightCol, leftRow:rightRow, ...]

    cv.imshow('original', in_img)
    cv.imshow('processed', res)

    cv.waitKey(0)
    cv.destroyAllWindows()

    return in_img[leftCol:rightCol, leftRow:rightRow, ...]

def test_dominant_color():
    img_pil = Image.open("data/original_images/lenna.png")
    img_cv = cv.imread("data/original_images/lenna.png")
    imanalysis = imagewizard.Analysis()
    import time
    start = time.time()
    res = imanalysis.dominant_colors(img_pil, 3, 'rgb')
    end = time.time()
    res1 = imanalysis.dominant_colors(img_cv, 3, 'bgr')
    print("PIL immage - dominant color (RGB) :\n", res)
    print("CV immage - dominant color (RGB) :\n", res1)
    print("Time taken: ", end-start)

def test_mode_color():
    img_pil = Image.open("data/original_images/lenna.png")
    img_cv = cv.imread("data/original_images/lenna.png")
    imanalysis = imagewizard.Analysis()
    res = imanalysis.frequent_color(img_pil, 'rgb')
    res1 = imanalysis.frequent_color(img_cv, 'bgr')
    print("PIL immage - frequent color (RGB) :", res)
    print("CV immage - frequent color (RGB) :", res1)

def test_analysis_mean_color():
    img_pil = Image.open("data/original_images/lenna.png")
    img_cv = cv.imread("data/original_images/lenna.png")
    imanalysis = imagewizard.Analysis()
    res = imanalysis.mean_color(img_pil, 'rgb')
    res1 = imanalysis.mean_color(img_cv, 'bgr')
    print("PIL immage - mean color (RGB) :", res)
    print("CV immage - mean color (RGB) :", res1)

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

def test_skew_affine():
    img = cv.imread('data/original_images/skew_aff_org.png')
    ip = imagewizard.Processing()
    
    ip_aff = np.float32([[50,50],[200,50],[50,200]])
    op_aff = np.float32([[10,100],[200,50],[100,250]])

    skew_aff = ip.skew_affine(img, ip_aff, op_aff, order='bgr')

    cv.imshow("original", img)
    cv.imshow("skew affine image", skew_aff)
    cv.imwrite('skew_aff.png', skew_aff)
    cv.waitKey(0)
    cv.destroyAllWindows()

def test_skew():
    img = cv.imread('data/original_images/skew.png')
    ip = imagewizard.Processing()
    
    # # input_points: three points on input image, ex: np.float32([[50,50],[200,50],[50,200]])
    # ip_points = np.float32([[50,50],[200,50],[50,200]])
    # # output_points: three points on output location correspoinding to input_points' to be transformed, np.float32([[10,100],[200,50],[100,250]])
    # op_points = np.float32([[10,100],[200,50],[100,250]])

    # skew_affine = ip.skew_affine(img, ip_points, op_points, 'bgr')
    
    # input_points: four points on input image, ex: np.float32([[56,65],[368,52],[28,387],[389,390]])
    # [(73, 239), (356, 117), (475, 265), (187, 443)]
    # ip_per = np.float32([(250, 165), (631, 405), (98, 428), (474, 596)])
    
    # ip_per = np.float32([(100, 320), (475, 160), (640, 340), (250, 580)])
    # # output_points: four points on output location correspoinding to input_points' to be transformed, ex: np.float32([[0,0],[300,0],[0,300],[300,300]])
    # op_per = np.float32([[0,0], [300,0], [300,300], [0,300]])

    ip_per = np.float32([(100, 320), (472, 156), (250, 580), (630, 345)])
    op_per = np.float32([[0,0], [500,0], [0,350], [500,350]])

    skew_per = ip.skew_perspective(img, ip_per, op_per, 'bgr')

    cv.imshow("original", img)
    # cv.imshow("skew affine image", skew_affine)
    cv.imshow("skew perspective image", skew_per)

    cv.imwrite('skew_per.png', skew_per)
    

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
    # crop1 = ip.crop(img, start_x = 50, end_x = 100, start_y = 50, end_y = 100, is_percentage=True, order='bgr')
    # crop2 = ip.crop(img, 400, 1000, 0, 500, is_percentage=False, order='bgr')
    crop3 = ip.crop(img, 0, 50, 0, 50, is_percentage=True, order='bgr')
    # cv.imshow('original', img)
    # cv.imshow('cropped 1', crop1)
    # cv.imshow('cropped 2', crop2)
    cv.imshow('cropped 3', crop3)
    # cv.imwrite('crop1.png', crop1)
    # cv.imwrite('crop2.png', crop2)
    cv.imwrite('crop3.png', crop3)

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
    
    image2 = cv.imread('data/original_images/test2.png')
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

def trim_to_content():
    # filename_in = "data/original_images/san_disk_white_pad.png"
    filename_in = "data/original_images/quiet_flow10.png"
    iw_analysis = imagewizard.Analysis()

    pil_im = Image.open(filename_in)
    pil_im = iw_analysis.trim_to_content(pil_im)

    or_im  = cv.imread(filename_in)
    cv_im = iw_analysis.trim_to_content(or_im, 'bgr')

    # cv.imshow("original", or_im)
    # cv.imshow("trimmed cv image", cv_im)
    # pil_im.show()
    # cv.imshow("trimmed pil image", pil_im)
    cv.imwrite('crop_to_content_image.png', cv_im)

    cv.waitKey(0)
    cv.destroyAllWindows()

def test_quite_flow():
    im_hash = imagewizard.Hashing()
    sim = imagewizard.Similarity()

    im1 = cv.imread("data/original_images/quiet_flow10.png")
    im2 = cv.imread("data/original_images/quiet_flow20.png")

    im1_dhash = im_hash.dhash(im1)
    im2_dhash = im_hash.dhash(im2)

    print("im1 hash", (im1_dhash))
    print("im2 hash", (im2_dhash))

    sim_score = sim.similarity(str(im1_dhash), str(im2_dhash), 'hamming')

    print(im1_dhash - im2_dhash)
    print(sim_score)

def test_segmentation():
    img = cv.imread('data/original_images/lenna.png')
    img1 = Image.open('data/original_images/lenna.png')

    colors = [[224, 166, 147], [110, 34, 71], [195, 98, 100]]

    ip = imagewizard.Processing()

    cv_res = ip.segmentation(img, colors, 'bgr')
    pil_res = ip.segmentation(img1, colors, 'rgb')

    pil_res_im = Image.fromarray(pil_res)

    cv.imshow("original image", img)
    cv.imshow('cv result', cv_res)
    pil_res_im.show()
    pil_res_im.save("segmented_image.png")
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__=="__main__":
    test_segmentation()
    # test_quite_flow()
    # test_colorspaces()
    # test_hashing()
    # test_hash_and_similarity()
    # test_resize_zoom()
    # test_rotate()
    # test_crop()
    # test_skew()
    # test_skew_affine()
    # test_mode_color()
    # test_dominant_color()
    # crop_color_border()
    # trim_to_content()
    # test_analysis_mean_color()
    # test_mirror()
    # test_blur()
    # test_lum()
    # test_binarize()
    # TODO: test image processing 
    # TODO: add coverage
    # TODO: needles in hay stack testing
    # TODO: add travis build
    # TODO: check the hashes for the images Ben sent
    # TODO: Graphana
    # TODO: BM25 vector search
    # TODO: add clustered image processing
    # k.showImage()
    # k.showCentroidColours()
    # k.showClustering()

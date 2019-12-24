# Sample Test passing with nose and pytest
import sys
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

if __name__=="__main__":
    test_hamming()


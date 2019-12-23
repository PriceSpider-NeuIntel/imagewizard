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
    a_hex, b_hex = '0x4bd1', ['0x5bd2', '0x4bd1', '5', '0b1001']
    a_int, b_int = '4bd1', ['5bd2', 0x4bd1]

    print(imagewizard.similarity(a_hex, b_hex))
    print(imagewizard.similarity(a_int, b_int, metric="hamming"))

if __name__=="__main__":
    test_hamming()


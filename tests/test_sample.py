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

if __name__=="__main__":
    test_pass()


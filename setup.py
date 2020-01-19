import io
import os
import re

from setuptools import find_packages
from setuptools import setup
from pip.req import parse_requirements

REQ_GEN = parse_requirements('requirements.txt', session='hack')
INSTALL_REQS = [str(ir.req) for ir in REQ_GEN]


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="imagewizard",
    version="0.1.0",
    url="https://github.com/Swaroop-p/imagewizard",
    license='MIT',

    author="Swaroop Padala",
    author_email="soupspring47@gmail.com",

    description="imagewizard is a python based library for performing various image manipulations and operations",
    long_description=read("README.rst"),

    keywords = ['imagewizard', 'image hashing', 'hash', 'similarity', 'segmentation', 'image segmentation', 'image processing'],

    packages=find_packages(exclude=('tests','demo',)),

    install_requires=INSTALL_REQS,

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

#!/usr/bin/python

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from pynt import task

from path import Path
import glob

from src.data.download import pydownload_file
from src.data.preprocess import pypreprocess

iris_file = 'data/raw/iris.csv'
processed_file = 'data/processed/processed.pickle'

@task()
def rawdata():
  '''Download IRIS dataset'''
  pydownload_file('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', iris_file)

@task()
def clean():
    '''Clean all build artifacts'''
    patterns = ['data/raw/*.csv', 'data/processed/*.pickle',
            'data/processed/*.xlsx', 'reports/figures/*.png']
    for pat in patterns:
        for fl in glob.glob(pat):
            Path(fl).remove()

@task(rawdata)
def preprocess():
    '''Preprocess IRIS dataset'''
    pypreprocess(iris_file, processed_file)
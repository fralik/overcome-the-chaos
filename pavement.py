import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from paver.easy import *
from paver.setuputils import setup

from src.data.download import pydownload_file
from src.data.preprocess import pypreprocess
from src.visualization.exploratory import pyexploratory

iris_file = path('data/raw/iris.csv')
preprocessed_file = path('data/processed/preprocessed.pickle')
graph_file = path('reports/figures/exploratory.png')

@task
def rawdata():
    """Download IRIS dataset"""
    pydownload_file('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
            iris_file)

@task
def clean():
    """Clean the build"""
    iris_file.remove()
    preprocessed_file.remove()
    graph_file.remove()

@task
@needs('rawdata')
def preprocess():
    """Preprocess IRIS dataset"""
    pypreprocess(iris_file, preprocessed_file)

@task
@needs('preprocess')
def exploratory():
    '''Make an image with pairwise distribution'''
    pyexploratory(preprocessed_file, graph_file)

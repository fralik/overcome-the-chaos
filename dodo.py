from src.data.download import doit_download_file
from src.data.preprocess import doit_pypreprocess
from src.visualization.exploratory import pyexploratory

DOIT_CONFIG = {
    'verbosity': 2, # set default verbosity for all targets.
                 # Display both stdout and stderr.
}

def task_rawdata():
    """Download IRIS dataset"""
    iris_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    target_file = 'data/raw/iris.csv'
    return {
        'file_dep': ['src/data/download.py'], # rebuild target if file_dep have been changed
        'targets': [target_file], # outcome of the task

        # run python function doit_download_file, argument url will be set to iris_url
        # note that doit_download_file takes a second argument targets, which
        # will be automatically provided by doit.
        'actions': [(doit_download_file, (), {'url': iris_url})],

        # delete target files during cleaning
        'clean': True,
    }

def task_preprocess():
    """Preprocess IRIS dataset"""
    pickle_file = 'data/processed/processed.pickle'
    excel_file = 'data/processed/processed.xlsx'
    return {
        'file_dep': ['src/data/preprocess.py'],
        'targets': [pickle_file, excel_file],
        'actions': [doit_pypreprocess],
        # input argument input_file of doit_pypreprocess is set to the result of task rawdata
        'getargs': {'input_file': ('rawdata', 'filename')},
        'clean': True,
    }

def task_exploratory():
    """Make exploratory data analysis image"""
    target_file = 'reports/figures/exploratory.png'
    return {
        'file_dep': ['src/visualization/exploratory.py', 'data/processed/processed.pickle'],
        'targets': [target_file],
        'actions': [(pyexploratory, (), {'output_file': target_file})],
        'getargs': {'input_file': ('preprocess', 'processed')},
        'clean': True,
    }

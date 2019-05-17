import luigi
import logging

from src.data.download import pydownload_file
from src.data.preprocess import pypreprocess
from src.visualization.exploratory import pyexploratory

class RawData(luigi.Task):
    iris_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    target_file = 'data/raw/iris.csv'

    def requires(self):
        return None

    def output(self):
        # It might be better to always wrap the output in a list.
        # The motivation behind it is that if you have Task C that depends on Task A and Task B,
        # then by having all outputs of dependent tasks as lists one can process them
        # in a similar manner in Task C. See TaskC later in this file.
        return [luigi.LocalTarget(self.target_file)]

    def run(self):
        pydownload_file(self.iris_url, self.output()[0].path)

class Preprocess(luigi.Task):
    pickle_file = 'data/processed/processed.pickle'
    excel_file = 'data/processed/processed.xlsx'

    def requires(self):
        return RawData()
    def output(self):
        return [luigi.LocalTarget(self.pickle_file), luigi.LocalTarget(self.excel_file)]
    def run(self):
        pypreprocess(self.input()[0].path, self.pickle_file, self.excel_file)

class Exploratory(luigi.Task):
    def requires(self):
        return Preprocess()
    def output(self):
        return [luigi.LocalTarget('reports/figures/exploratory.png')]
    def run(self):
        pyexploratory(self.input()[0].path, self.output()[0].path)

class TaskC(luigi.Task):
    def requires(self):
        return [RawData(), Preprocess()]

    def output(self):
        return None
    def run(self):
        logging.debug('TaskC has {} dependencies'.format(len(self.input())))

        for i, inp in enumerate(self.input()):
            for file in inp:
                print('\tDependency #{}, file {}'.format(i, file.path))

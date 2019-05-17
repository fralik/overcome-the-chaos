import click
import matplotlib

matplotlib.use('agg')
import seaborn as sns

import sys

sys.path.append('src')

from data import read_processed_data


def exploratory_visualization(dframe):
    return sns.pairplot(dframe, diag_kind='kde', vars=['x0', 'x1', 'x2', 'x3'], hue='y')


@click.command()
@click.argument('input_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('output_file', type=click.Path(writable=True, dir_okay=False))
def main(input_file, output_file):
    pyexploratory(input_file, output_file)

def pyexploratory(input_file, output_file):
    print('Plotting pairwise distribution...')

    dframe = read_processed_data(input_file)
    plot = exploratory_visualization(dframe)
    plot.savefig(output_file)


if __name__ == '__main__':
    main()

import requests
import click

@click.command()
@click.argument('url')
@click.argument('filename', type=click.Path())
def download_file(url, filename):
    pydownload_file(url, filename)

def pydownload_file(url, filename):
    print('Downloading from {} to {}'.format(url, filename))
    response = requests.get(url)
    with open(filename,  'wb') as ofile:
        ofile.write(response.content)

def doit_download_file(url, targets):
    # targets is a set, let's take the last element
    filename = targets.pop()
    pydownload_file(url, filename)

    # return a dictionary, so that other tasks in doit can use it.
    return {'filename': filename}

if __name__ == '__main__':
    download_file()

from setuptools import setup, find_packages
from os.path import join as path_join

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='flask-session',
    version='0.1',
    url='https://gitlab.com/rgcalsaverini/flask-sesion',
    author='Rui Calsaverini',
    author_email='rui.calsaverini',
    description='Decode/encode flask sessions',
    packages=find_packages(),
    install_requires=required,
    scripts=[path_join('bin', 'flask-session')],
)

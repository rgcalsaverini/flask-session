from setuptools import setup, find_packages

from flask_sec.api import VERSION

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='flask-session',
    version=VERSION,
    url='https://gitlab.com/rgcalsaverini/flask-sesion',
    author='Rui Calsaverini',
    author_email='rui.calsaverini',
    description='Decode/encode flask sessions',
    packages=find_packages(),
    install_requires=required,
    scripts=['flask_session'],
)

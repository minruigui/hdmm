from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='hdmm',
    version='0.0.1',
    description='Source code for HDMM: The High-Dimensional Matrix Mechanism, which first appeared in VLDB 2018.',
    url='git@github.com:minruigui/hdmm.git',
    author='ryan112358 ',
    author_email='?',
    license='AGPL-3.0 license',
    packages=['hdmm'],
    package_dir={'': 'src'},
    install_requires=requirements,
)

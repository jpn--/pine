"""
A toolkit for various purposes.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pines',
    version='2.94',

    description='A toolkit for various purposes',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/jpn--/pines',

    # Author details
    author='Jeffrey Newman',
    author_email='jeff@newman.me',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
    ],

    # What does your project relate to?
    keywords='reusable code',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html

    install_requires=[
        'distributed>=1.17.1',
        'dask>=0.15',
        'egnyte>=0.5.3',
        'pandas>=0.20.1',
        'dbf>=0.96',
        'numpy>=1.13.1',
        'scipy>=0.19.0',
        'tables>=3.4.2',
        'psycopg2',
        # conda install mysql-connector-python
    ],

    entry_points={
            'console_scripts': [
                'pines_config = pines.configure:print_config',
                'pines_cluster_worker_v = pines.daskworker:new_worker',
                'cluster_v = pines.daskworker:new_worker_with_egnyte',
                'pines_pip_rebuild = pines.private_pip:pip_rebuild',
                'pines_pip = pines.private_pip:_pip_install_entry',
                'pines-pip = pines.private_pip:_pip_install_entry',
                'omx-cube-convert = pines.omx_cube_converter:convert',
            ],

            'gui_scripts': [
                'pines_cluster_worker = pines.daskworker:new_worker',
                'cluster_q = pines.daskworker:new_worker_with_egnyte',
            ]
    },

    package_data={
        '': ['*.exe',],
    }
)
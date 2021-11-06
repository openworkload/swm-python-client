#========================================================================
# setup.py
#========================================================================
# See also: https://github.com/pypa/sampleproject/blob/master/setup.py
#########################################################################

from setuptools import setup, find_packages
from codecs     import open   # to use a consistent encoding
from os         import path
from subprocess import check_output


def get_version():
    cmd = "git describe --dirty"
    try:
        result = check_output( cmd.split(),  ).strip()
    except:
        result = "?"
    return result


def get_long_description():
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()


setup(
    name='swmclient',
    version=get_version(),
    description='Sky Workload Manager core daemon python interface',
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords='hpc highperformancecomputing workload cloud computing jupyter',
    url='https://github.com/skyworkflows/swm-core/python',
    author='Taras Shapovalov',
    author_email='taras@iclouds.net',
    packages=['swmclient'],
    license='BSD',
    include_package_data=True,
    install_requires=['pytest'],
    python_requires='>=3.9, <4',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/skyworkflows/swm-core/issues',
        'Source': 'https://github.com/skyworkflows/swm-core/python',
    },
)

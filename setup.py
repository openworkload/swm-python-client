# ========================================================================
# setup.py
# ========================================================================
# See also: https://github.com/pypa/sampleproject/blob/master/setup.py
#########################################################################

from codecs import open  # to use a consistent encoding
from os import path
from subprocess import check_output

from setuptools import setup, find_packages


def get_version():
    cmd = "git describe"
    try:
        result = check_output(
            cmd.split(),
        ).decode('utf-8').strip()
    except:
        result = "?"
    return result


def get_long_description():
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
    return long_description


setup(
    name="swmclient",
    version=get_version(),
    description="Python bindings for swm-core user REST API",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="hpc highperformancecomputing workload cloudcomputing jupyter swm skyworkloadmanager",
    url="https://github.com/skyworkflows/swm-python-client",
    author="Taras Shapovalov",
    author_email="taras@iclouds.net",
    packages=find_packages(),
    license="BSD",
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.9, <4",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    project_urls={
        "Bug Reports": "https://github.com/skyworkflows/swm-python-client/issues",
        "Source": "https://github.com/skyworkflows/swm-python-client",
    },
)

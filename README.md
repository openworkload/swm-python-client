Python bindings for swm-core client REST API
============================================

# Description

Sky Port is an universal bus between user software and compute resources.
It can also be considered as a transportation layer between workload producers
and compute resource providers. Sky Port makes it easy to connect user software
to different cloud resources.

The current python package represents a wrapper around client REST API of the core
component of Sky Port -- [core daemon](https://github.com/skyworkflows/swm-core).
The package provides classes and data structures that can be used in python programs 
in order to communicate with swm-core. Such communication is useful when Sky Port
terminals are built (see [JupyterLab terminal](https://github.com/skyworkflows/swm-jupyter-term)
as an example).

# Build

## Requirements:

1) Use swm-core dev container or install manually:
```bash
sudo apt-get install python3-all-dev
sudo apt install python3-pip

pip3 install pip-tools
pip3 install virtualenv
```

Note: python >= 3.9 is required.

2) Install the project dependencies with virtualenv
```bash
make prepare-venv
```

## Run code autoformatting and validation tools:
```bash
make format
make check
```

## Run unit tests:
```bash
make test
```

## Build pip package and upload to pypi.org:

```bash
make clean
make package
make upload
```


# Setup

## Installation from PyPi:
```bash
python3 -m pip install --user swmclient
```

## Remove installed package:
```bash
python3 -m pip uninstall swmclient
```


# Contributing

We appreciate all contributions. If you are planning to contribute back bug-fixes, please do so
without any further discussion. If you plan to contribute new features, utility functions or extensions,
please first open an issue and discuss the feature with us.

# Lincese

We use a shared copyright model that enables all contributors to maintain the copyright on their contributions.

This software is licensed under the BSD-3-Clause license.

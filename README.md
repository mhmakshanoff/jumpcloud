# JumpCloud Assessment from Miriam Makshanoff

## System Specifications

- MacOS Big Sur Version 11.3
- Homebrew *(recommended)*
  - Instructions for installing Homebrew can be found at this [link](https://brew.sh/)
- Python :snake:
  - *(recommended)* Latest Python can be installed via Homebrew as a formula (brew install python)
  - Python binaries can be downloaded at this [link](https://www.python.org/downloads/)

## Installation

- After the above is installed, clone [this repo](https://github.com/mhmakshanoff/jumpcloud)
- CD into this directory
- Run `pip install -r requirements.txt`
- To install the Password Hashing Application, run `bin/install-app.sh`

## Running Tests

- To run the whole test suite, run `pytest`
- To specify a specific file, run `pytest tests/file_name.py`
- To run tests with a specific marker, run `pytest -v -m marker`
  - Markers are set based on priority: Critical, High, Medium, Low
- To run tests without a specific marker, run `pytest -v -m 'not marker'`

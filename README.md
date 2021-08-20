# JumpCloud Assessment from Miriam Makshanoff

## System Specifications

- MacOS Big Sur Version 11.3
- Homebrew *(recommended)*
  - Instructions for installing Homebrew can be found at this [link](https://brew.sh/)
- Python :snake:
  - *(recommended)* Latest Python can be installed via Homebrew as a formula (brew install python)
  - Python binaries can be downloaded at this [link](https://www.python.org/downloads/)

## Installation

- After the above is installed, clone this repo:
- CD into this directory
- Run `pip install -r requirements.txt`

- The password hashing application can be obtained by running `wget --no-check-certificate --no-proxy ‘https://s3.amazonaws.com/qa-broken-hashserve/broken-hashserve.tgz’`

- Set a PORT environment variable by running `export PORT=8088`

## Running Tests

- To run the whole test suite, run `pytest`
- To specify a specific file, run `pytest file_name.py`

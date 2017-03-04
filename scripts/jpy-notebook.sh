#!/bin/bash

ROOT_DIR=/vagrant
export PYTHONPATH=$ROOT_DIR/python
export NOTEBOOK_DIR=/vagrant/notebooks

jupyter notebook --port=8888 --ip=192.168.33.10 --no-browser --notebook-dir=$NOTEBOOK_DIR

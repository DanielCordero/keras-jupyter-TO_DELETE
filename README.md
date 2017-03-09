# keras-jupyter

* Source code - [Github][1]
* Author - Gavin Noronha - <gnoronha@hotmail.com>

[1]: https://github.com/gavinln/keras-jupyter.git

## About

This project provides a [Ubuntu (16.04)][10] [Vagrant][20] Virtual Machine (VM)
with the [Keras][30] and [TensorFlow][40] libraries and [Jupyter][50]
(formerly known as IPython) notebooks. Keras also works with [Theano][60].

[10]: http://releases.ubuntu.com/14.04/
[20]: http://www.vagrantup.com/
[30]: http://deeplearning.net/software/theano/
[40]: http://tensorflow.org/
[50]: http://jupyter.org/
[60]: https://github.com/fchollet/keras

Follow the **Requirements** section below for a one-time setup of Virtualbox,
Vagrant and Git before running the commands below. These instructions should
work on Windows, Mac and Linux operating systems.

## Running Keras

### 1. Start the VM

1. Change to the tensorflow-ipy root directory

    ```
    cd keras-jupyter
    ```

3. Make sure you have the latest version of vagrant (1.9.1)

    ```
    vagrant -v
    ```

3. Start the Virtual machine (VM)

    ```
    vagrant up
    ```

4. Login to the VM

    ```
    vagrant ssh
    ```

5. Install Jupyter notebook extensions

    ```
    jupyter contrib nbextension install --user
    ```

6. Install vim extension (optional)

    ```
    cd $(jupyter --data-dir)/nbextensions
    git clone https://github.com/lambdalisue/jupyter-vim-binding vim_binding
    ```

### 2. Run your first TensorFlow command line program

First run section 1.

1. Change to the python directory

    ```
    cd /vagrant/python
    ```

2. Set environment variable to disable warnings

    ```
    export TF_CPP_MIN_LOG_LEVEL=2
    ```

2. Run the first program

    ```
    python3 first-tensorflow.py
    ```

3. Make sure the version printed on the first line of the output is the version
   you expect. The releases are documented on this [page][70]

[70]: https://github.com/tensorflow/tensorflow/releases

### 3. Start the Jupyter notebooks

First run section 1.

1. Change to the notebooks directory

    ```
    cd /vagrant/scripts
    ```

2. Run the IPython notebook server

    ```
    chmod +x jpy-notebook.sh
    ./jpy-notebook.sh
    ```

3. Open your browser to http://192.168.33.10:8888/ to view the notebooks

## Requirements

The following software is needed to get the software from github and run
Vagrant. The Git environment also provides an [SSH client][100] for Windows.

* [Oracle VM VirtualBox][110]
* [Vagrant][120] version 1.9.1 or higher
* [Git][130]

[100]: http://en.wikipedia.org/wiki/Secure_Shell
[110]: https://www.virtualbox.org/
[120]: http://vagrantup.com/
[130]: http://git-scm.com/

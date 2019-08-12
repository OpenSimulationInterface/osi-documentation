Linux
=====
1. Install ``cmake`` (minimum required version 3.7):

- Download cmake 3.7.2
- Unzip it and navigate to the unzipped folder.
- Run the following commands:

.. code-block:: shell

    ./bootstrap
    make
    sudo make install 

2. Install Protobuf 2.6.1: ``sudo apt-get install libprotobuf-dev protobuf-compiler``
3. Clone open simulation interface from GitHub and navigate to this directory using a terminal.
4. Create a new directory build and navigate into it using the following command:

.. code-block:: shell

    mkdir build
    cd build 

5. Run the following commands to build and install OSI (v2.1.1 or higher required):

.. code-block:: shell

    cmake .. [-DCMAKE_INSTALL_PREFIX=/usr/local]
    make
    sudo make install

P.S.: To build a 32-bit target under 64-bit linux, please add ``-DCMAKE_CXX_FLAGS="-m32"`` to the ``cmake`` command. In this case, please make sure that ``protobuf`` is in a 32-bit mode too.

Python
-----------

1. Get protobuf compiler 2.6.1: ``sudo apt-get install libprotobuf-dev protobuf-compiler``
2. Install the missing python packages: ``sudo apt-get install python-setuptools``
3. Clone `open simulation interface <https://github.com/OpenSimulationInterface/open-simulation-interface>`_  and navigate to this directory using a terminal.
4. Run the following command: ``sudo python setup.py install``

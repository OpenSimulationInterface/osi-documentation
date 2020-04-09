Installation Guide
====================
The OSI Validator is being developed with Python 3.6 within a virtual environment. It is recommended to use the same python version for validation tasks.

Setup for linux users
----------------------
This setup guide is for users who want to just use the validator.

Clone the repository osi-validation:

.. code-block:: bash

    git clone https://github.com/OpenSimulationInterface/osi-validation.git

Change directory to osi-validation:

.. code-block:: bash

    cd osi-validation

Clone the submodules:

.. code-block:: bash

    git submodule update --init

Install the open-simulation-interface:

.. code-block:: bash

    cd open-simulation-interface
    pip install .

Install osi-validation into the global root directory:

.. code-block:: bash

    cd ..; sudo pip3 install .

Now you can run the validator on an example trace file (``trace.osi``) by calling:

.. code-block:: bash

    osivalidator -d trace.osi

OSI Validator Binary
~~~~~~~~~~~~~~~~~~~~~
After the installation of all the dependencies it is possible to compile the osi-validator into one binary file (size ~ 9.1 Mb) for easier distribution and usage.
For that we use `pyinstaller <https://www.pyinstaller.org/>`_:

.. code-block:: bash

    pip install pyinstaller
    pyinstaller osivalidator/osi_general_validator.py --onefile

After the compilation you can find the binary in the ``dist`` directory. You can use the binary the normal way you would use the command line interface:

.. code-block:: bash

    ./dist/osi_general_validator -h

Make sure to provide the path to the rules when validating trace files to avoid path errors:

.. code-block:: bash

    python rules2yml.py # Parse and generate rules folder
    ./dist/osi_general_validator -r rules data/small_test.txt.lzma

Setup for linux developers
----------------------------
This setup guide is for developers who want to contribute to the OSI Validator.

Clone repository osi-validation:

.. code-block:: bash

    git clone https://github.com/OpenSimulationInterface/osi-validation.git

Change directory:

.. code-block:: bash

    cd osi-validation

Clone the submodules:

.. code-block:: bash

    git submodule update --init

It is best practice to use a virtual environment in python. It has various advantages such as the ability to install modules locally, export a working environment, and execute a Python program in that environment so that you don't mess around with your global python environment. 
Install virtual environment:

.. code-block:: bash

    sudo apt-get install virtualenv

Create virtual environment:

.. code-block:: bash

    virtualenv -p /usr/bin/python3 venv

Activate your virtual environment:

.. code-block:: bash

    source venv/bin/activate

Install open-simulation-interface:

.. code-block:: bash

    cd open-simulation-interface
    pip install .

Now you can run the validator on an example trace file (``trace.osi``) by calling:

.. code-block:: bash

    python osivalidator/osi_general_validator.py -d trace.osi

The advantage to call the osi-validator this way for developers is that you do not need to reinstall the application when you made changes to the code.


Setup for windows users
-------------------------
In Progress ...

Setup for windows developers
-----------------------------
In Progress ...

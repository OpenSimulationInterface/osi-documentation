Installation Guide
====================
The OSI Validator is being developed with Python 3.6 within a virtual environment. It is recommended to use the same python version for validation tasks.

Setup for linux users
----------------------
This setup guide is for users who want to just use the validator.

Clone the repository osi-validation:

``git clone https://github.com/OpenSimulationInterface/osi-validation.git``

Change directory to osi-validation:

``cd osi-validation``

Clone the submodules:

``git submodule update --init``

Install the open-simulation-interface:

``cd open-simulation-interface; pip install .``

Install osi-validation into the global root directory:

``cd ..; sudo pip3 install .``

Now you can run the validator on an example trace file (``trace.osi``) by calling:

``osivalidator -d trace.osi``


Setup for linux developers
----------------------------
This setup guide is for developers who want to contribute to the OSI Validator.

Clone repository osi-validation:

``git clone https://github.com/OpenSimulationInterface/osi-validation.git``

Change directory:

``cd osi-validation``

Clone the submodules:

``git submodule update --init``

It is best practice to use a virtual environment in python. It has various advantages such as the ability to install modules locally, export a working environment, and execute a Python program in that environment so that you don't mess around with your global python environment. 
Install virtual environment:

``sudo apt-get install virtualenv``

Create virtual environment:

``virtualenv -p /usr/bin/python3 vpython``

Activate your virtual environment:

``source vpython/bin/activate``

Install open-simulation-interface:

``cd open-simulation-interface; pip install .``

Now you can run the validator on an example trace file (``trace.osi``) by calling:

``python osivalidator/osi_general_validator.py -d trace.osi``

The advantage to call the osi-validator this way for developers is that you do not need to reinstall the application when you made changes to the code.


Setup for windows users
-------------------------
In Progress ...

Setup for windows developers
-----------------------------
In Progress ...

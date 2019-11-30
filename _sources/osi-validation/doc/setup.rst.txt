Installation Guide
====================
The *OSI Validator* has been developed with **Python 3.6** with virtual environment. It is the only version of Python that is supported now. *OSI Validator* should only be used with **Python 3.6**.

Setup for linux users
----------------------
This setup guide is for users who want to just use the validator.

Clone repository osi-validation:

``git clone https://github.com/OpenSimulationInterface/osi-validation.git``

Change directory to osi-validation:

``cd osi-validation``

Clone the repository open-simulation-interface:

``git clone https://github.com/OpenSimulationInterface/open-simulation-interface.git``

Clone repository proto2cpp:

``git clone https://github.com/OpenSimulationInterface/proto2cpp.git``

Install osi-validation into the global root directory:

``sudo pip3 install .``


Setup for linux developers
----------------------------
This setup guide is for developers who want to contribute to the OSI Validator.

Clone repository osi-validation:

``git clone https://github.com/OpenSimulationInterface/osi-validation.git``

Change directory:

``cd osi-validation``

Clone repository open-simulation-interface:

``git clone https://github.com/OpenSimulationInterface/open-simulation-interface.git``

Clone repository proto2cpp:

``git clone https://github.com/OpenSimulationInterface/proto2cpp.git``

It is best practice to use a virtual environment in python. It has various advantages such as the ability to install modules locally, export a working environment, and execute a Python program in that environment so that you don't mess around with your global python environment. 
Install virtual environment:

``sudo apt-get install virtualenv``

Create virtual environment:

``virtualenv -p /usr/bin/python3 vpython``

Activate your virtual environment:

``source vpython/bin/activate``

Install open-simulation-interface:

``cd open-simulation-interface; pip install .``

Install osi-validator:

``cd ..; pip install .``


Setup for windows users
-------------------------
In Progress ...

Setup for windows developers
-----------------------------
In Progress ...

Installation Guide
====================
The *OSI Validator* has been developed with **Python 3.6** with virtual environment. It is the only version of Python that is supported now. *OSI Validator* should only be used with **Python 3.6**.

Setup for linux users
----------------------
This setup guide is for users who want to 

Clone repository osi-validation:

``git clone https://github.com/OpenSimulationInterface/osi-validation.git``

Install osi-validation into the global root directory:

``sudo python3 setup.py install``


Setup for linux developers
----------------------------
This setup guide is for developers who want to contribute to osi-validation.

Clone repository osi-validation:

``git clone https://github.com/OpenSimulationInterface/osi-validation.git``

Change directory:

``cd osi-validation``

Change the branch to development:

``git checkout development``

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

Install last requirements:

``pip install -r requirements.txt``

Install osi-validator:

``cd ..; pip install .``

Last step copy ``requirements-osi-3`` to ``vpython/lib/python3.6/site-packages``

``cp -R requirements-osi-3 vpython/lib/python3.6/site-packages/``

or **install with virtual environment via script**

Just run the script:

``sudo bash installation.sh``


Setup for windows users
-------------------------
In Progress ...

Setup for windows developers
-----------------------------
In Progress ...

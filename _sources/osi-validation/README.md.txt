# OSI Validator
[![Travis Build Status](https://travis-ci.org/OpenSimulationInterface/osi-validation.svg?branch=master)](https://travis-ci.org/OpenSimulationInterface/osi-validation)

OSI Validator checks the compliance of OSI messages with predefined [rules](https://opensimulationinterface.github.io/osi-documentation/osi-validator/osivalidator.html#module-osivalidator.osi_rules_implementations). The full documentation on usage and customization of the rules is available [here](https://opensimulationinterface.github.io/osi-documentation/osi-validator/osivalidator-module.html).

## Usage

```
usage: osivalidator [-h] [--rules RULES] --data DATA
                    [--type {SensorView,GroundTruth,SensorData}]
                    [--output OUTPUT] [--timesteps TIMESTEPS] [--debug]
                    [--verbose]

Validate data defined at the input

optional arguments:
--help, -h                                      Show this help message and exit.
--rules RULES, -r RULES                         Directory with text files containig rules.
--data DATA, -d DATA                            Path to the file with OSI-serialized data.
--type {SensorView,GroundTruth,SensorData},     Name of the message type used to serialize data.
    -t {SensorView,GroundTruth,SensorData}
--output OUTPUT, -o OUTPUT                      Output folder of the log files.
--timesteps TIMESTEPS                           Number of timesteps to analyze. If -1, all.
--debug                                         Set the debug mode to ON.
--verbose                                       Set the verbose mode to ON (display in console).
```

## Installation

OSI Validator has been developed with Python 3.6 within a virtual environment on Ubuntu 18.04.

#### Local (recommended)

Clone repository osi-validation:

```git clone https://github.com/OpenSimulationInterface/osi-validation.git```

Change directory:

```cd osi-validation```

Clone repository open-simulation-interface:

```git clone https://github.com/OpenSimulationInterface/open-simulation-interface.git```

Clone repository proto2cpp:

```git clone https://github.com/OpenSimulationInterface/proto2cpp.git```

Install virtual environment:

```sudo apt-get install virtualenv```

Create virtual environment:

```virtualenv -p /usr/bin/python3 vpython```

Activate your virtual environment:

```source vpython/bin/activate```

Install open-simulation-interface:

```cd open-simulation-interface; pip install .```

Install osi-validator:

```cd ..; pip install .```

Last step copy `requirements-osi-3` to `vpython/lib/python3.6/site-packages`

```cp -R requirements-osi-3 vpython/lib/python3.6/site-packages/```


#### Global
Clone repository osi-validation:

```git clone https://github.com/OpenSimulationInterface/osi-validation.git```

Change directory:

```cd osi-validation```

Clone repository open-simulation-interface:

```git clone https://github.com/OpenSimulationInterface/open-simulation-interface.git```

Clone repository proto2cpp:

```git clone https://github.com/OpenSimulationInterface/proto2cpp.git```

Install:

```sudo pip3 install .```

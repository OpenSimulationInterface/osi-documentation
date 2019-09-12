# OSI Validator
[![Travis Build Status](https://travis-ci.org/OpenSimulationInterface/osi-validation.svg?branch=master)](https://travis-ci.org/OpenSimulationInterface/osi-validation)
## Presentation

The *OSI Validator* checks the compliance of the OSI messages with the KPI
rules.

The full documentation on usage and customization of the rules is available
[here](https://ainar.github.io/osi-validation/).

## Requirements

The *OSI Validator* has been developed with **Python 3.6** with virtual environment
environment. It is the only version of Python that is supported now. *OSI
Validator* should only be used with **Python 3.6**.

## Installation
### Install with virtual environment (step-by-step) (**recommended**)

Clone repository osi-validation

```git clone https://github.com/OpenSimulationInterface/osi-validation.git```

Change directory

```cd osi-validation```

Change the branch to development

```git checkout development```

Clone repository open-simulation-interface

```git clone https://github.com/OpenSimulationInterface/open-simulation-interface.git```

Clone repository proto2cpp

```git clone https://github.com/OpenSimulationInterface/proto2cpp.git```

Install virutal environment

```sudo apt-get install virtualenv```

Create virtual environment

```virtualenv -p /usr/bin/python3 vpython```

Activate your virtual environment

```source vpython/bin/activate```

Install open-simulation-interface

```cd open-simulation-interface; pip install .```

Install last requirements

```pip install -r requirements.txt```

Install osi-validator

```cd ..; pip install .```

Last step copy `requirements-osi-3` to `vpython/lib/python3.6/site-packages`

```cp -R requirements-osi-3 vpython/lib/python3.6/site-packages/```


### In the root directory 

```sudo python3 setup.py install```


## Usage
```
usage: osivalidator [-h] [--rules RULES]
                    [--type {SensorView,GroundTruth,SensorData}]
                    [--output OUTPUT] [--timesteps TIMESTEPS] [--debug]
                    [--verbose]
                    data

Validate data defined at the input

positional arguments:
data                  Path to the file with OSI-serialized data.

optional arguments:
-h, --help            show this help message and exit
--rules RULES, -r RULES
                        Directory with text files containig rules.
--type {SensorView,GroundTruth,SensorData}, -t {SensorView,GroundTruth,SensorData}
                        Name of the type used to serialize data.
--output OUTPUT, -o OUTPUT
                        Output folder of the log files.
--timesteps TIMESTEPS
                        Number of timesteps to analyze. If -1, all.
--debug               Set the debug mode to ON.
--verbose             Set the verbose mode to ON.
```

## Usecase
To validate a recorded osi-message you run 

```osivalidator osi_message_data/osi_message_test.txt```

The `osi_message_test.txt` was recorded with osi-visualizer for the scenario `astas_turn_long.txt`.
After running the validator you get the following output:

```
Instanciate logger
Read data
Retrieving message offsets in scenario file until inf...
 |################################| 172098454/172098454
262 messages has been discovered in 0.05367231369018555 s
Collect validation rules
Caching...
Importing messages from scenario file...
 |################################| 262/262
Caching done!
 |################################| 262/262 [0:00:11]

Errors (27) 
Ranges of timestamps    Message
----------------------  ------------------------------------------------------------------------------------------------------------------------------------------------------------
[0, 261]                SensorView.sensor_id.is_set(None) does not comply in SensorView
[0, 260]                Identifier.value.is_set(None) does not comply in SensorView.sensor_id
[0, 261]                SensorView.global_ground_truth.is_set(None) does not comply in SensorView
[0, 260]                GroundTruth.host_vehicle_id.is_set(None) does not comply in SensorView.global_ground_truth
[0, 260]                Identifier.value.is_set(None) does not comply in SensorView.global_ground_truth.host_vehicle_id
[0, 260]                GroundTruth.country_code.is_set(None) does not comply in SensorView.global_ground_truth
[0, 260]                GroundTruth.version.is_set(None) does not comply in SensorView.global_ground_truth
[0, 260]                InterfaceVersion.version_major.is_set(None) does not comply in SensorView.global_ground_truth.version
[0, 260]                InterfaceVersion.version_minor.is_set(None) does not comply in SensorView.global_ground_truth.version
[0, 260]                InterfaceVersion.version_patch.is_set(None) does not comply in SensorView.global_ground_truth.version
[0, 260]                GroundTruth.timestamp.is_set(None) does not comply in SensorView.global_ground_truth
[0, 260]                Timestamp.seconds.is_set(None) does not comply in SensorView.global_ground_truth.timestamp
[0, 260]                Timestamp.nanos.is_set(None) does not comply in SensorView.global_ground_truth.timestamp
[0, 260]                GroundTruth.stationary_object.is_set(None) does not comply in SensorView.global_ground_truth
[0, 260]                GroundTruth.moving_object.is_set(None) does not comply in SensorView.global_ground_truth
[0, 260]                GroundTruth.lane_boundary.is_set(None) does not comply in SensorView.global_ground_truth
[0, 260]                GroundTruth.lane.is_set(None) does not comply in SensorView.global_ground_truth
[0, 260]                GroundTruth.environmental_conditions.is_set(None) does not comply in SensorView.global_ground_truth
[0, 260]                EnvironmentalConditions.atmospheric_pressure.is_set(None) does not comply in SensorView.global_ground_truth.environmental_conditions
[0, 260]                EnvironmentalConditions.temperature.is_set(None) does not comply in SensorView.global_ground_truth.environmental_conditions
[0, 260]                EnvironmentalConditions.relative_humidity.is_set(None) does not comply in SensorView.global_ground_truth.environmental_conditions
[0, 260]                EnvironmentalConditions.ambient_illumination.is_set(None) does not comply in SensorView.global_ground_truth.environmental_conditions
[0, 260]                EnvironmentalConditions.time_of_day.is_set(None) does not comply in SensorView.global_ground_truth.environmental_conditions
[0, 260]                EnvironmentalConditions.TimeOfDay.seconds_since_midnight.is_set(None) does not comply in SensorView.global_ground_truth.environmental_conditions.time_of_day
[0, 260]                EnvironmentalConditions.precipitation.is_set(None) does not comply in SensorView.global_ground_truth.environmental_conditions
[0, 260]                EnvironmentalConditions.fog.is_set(None) does not comply in SensorView.global_ground_truth.environmental_conditions
[0, 260]                Reference unresolved: GroundTruth to MovingObject (ID: 0)

Warnings (5) 
Ranges of timestamps    Message
----------------------  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
[0, 260]                GroundTruth.country_code.is_iso_country_code(None) does not comply in SensorView.global_ground_truth.country_code
[0, 260]                EnvironmentalConditions.atmospheric_pressure.is_greater_than_or_equal_to(80000) does not comply in SensorView.global_ground_truth.environmental_conditions.atmospheric_pressure
[0, 260]                EnvironmentalConditions.temperature.is_greater_than_or_equal_to(170) does not comply in SensorView.global_ground_truth.environmental_conditions.temperature
[0, 260]                GroundTruth.environmental_conditions.is_valid(None) does not comply in SensorView.global_ground_truth.environmental_conditions
[0, 260]                SensorView.global_ground_truth.is_valid(None) does not comply in SensorView.global_ground_truth
```


## Deployment of the documentation

### Install Doxygen

```sudo apt-get install doxygen doxygen-doc doxygen-gui graphviz ```

### Deployment of all the documentation

All documentation is generated under *docs* directory.

*This will erase the formerly generated documentation.* This will also deploy
the KPIs documentation at the same time.

In the folder *docs*: `make gh-pages`

To push the documentation on Git, run in root directory:
```git push origin `git subtree split --prefix docs/html master`:gh-pages```

### Deployment of the documentation of KPIs

In the folder KPIs: `make "KPISDOCDIR=../docs/html/KPIs"`

The newly generated KPIs are in the directory *docs/html/KPIs*.
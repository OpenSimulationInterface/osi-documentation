Usage
=======

Example
----------------
After installation you can call the command ``osivalidator`` in your terminal which has the following usage:

.. code-block:: text

    usage: osivalidator [-h] [--rules RULES] --data DATA
                        [--type {SensorView,GroundTruth,SensorData}]
                        [--output OUTPUT] [--timesteps TIMESTEPS] [--debug]
                        [--verbose]

    Validate data defined at the input

    optional arguments:
    --help, -h                                      Show this help message and exit
    --rules RULES, -r RULES                         Directory with text files containig rules.
    --data DATA, -d DATA                            Path to the file with OSI-serialized data.
    --type {SensorView,GroundTruth,SensorData},     Name of the message type used to serialize data.
        -t {SensorView,GroundTruth,SensorData}  
    --output OUTPUT, -o OUTPUT                      Output folder of the log files.
    --timesteps TIMESTEPS                           Number of timesteps to analyze. If -1, all.
    --debug                                         Set the debug mode to ON.
    --verbose                                       Set the verbose mode to ON (display in console).

To run the validation first you need to record an osi-message. Here we already have an osi-message which is called ``osi_message_test.txt``. To validate the osi-message you simply call ``osivalidator`` and provide the path to the stored osi-message which is here in the folder ``osi_message_data``:

.. code-block:: text

    osivalidator --data osi_message_data/osi_message_test.txt

After successfully running the validation the following output is generated:

.. code-block:: text

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

The Output is a report of how many errors (here 27) and warnings (here 5) were found in the osi-message according to the defined rules. The rules can be found under the tag ``\rules`` in the \*.proto files from the `osi github <https://github.com/OpenSimulationInterface/open-simulation-interface>`_ or in the `requirements folder <https://github.com/OpenSimulationInterface/osi-validation/tree/master/requirements-osi-3>`_ from osi-validation as \*.yml files (for more information see :ref:`commenting`).  Currently an error is thrown when a field is not set. A warning is thrown when a field is set but do not comply with the defined rules. For each error and warning there is a description on which timestamp it was found, the path to the rule and the path to the osi-message. The general format is:

.. code-block:: text

    Errors (NUMBER_ERRORS) 
    Ranges of timestamps                Message
    --------------------------------    --------------------------------------------------------
    [START_TIMESTAMP, END_TIMESTAMP]    PATH_TO_RULE(VALUE) does not comply in PATH_TO_OSI_FIELD

    Warnings (NUMBER_WARNINGS) 
    Ranges of timestamps    Message
    --------------------------------    --------------------------------------------------------
    [START_TIMESTAMP, END_TIMESTAMP]    PATH_TO_RULE(VALUE) does not comply in PATH_TO_OSI_FIELD

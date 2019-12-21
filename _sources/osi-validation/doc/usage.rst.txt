Usage
=======

Example
----------------
After installation you can call the command ``osivalidator`` in your terminal which has the following usage:

.. code-block:: bash

    usage: osivalidator [-h] [--rules RULES]
                        [--type {SensorView,GroundTruth,SensorData}]
                        [--output OUTPUT] [--timesteps TIMESTEPS] [--debug]
                        [--verbose] [--parallel] [--format {separated,None}]
                        [--blast BLAST] [--buffer BUFFER]
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
    --verbose, -v         Set the verbose mode to ON.
    --parallel, -p        Set parallel mode to ON.
    --format {separated,None}, -f {separated,None}
                            Set the format type of the trace.
    --blast BLAST, -bl BLAST
                            Set the in-memory storage count of OSI messages during
                            validation.
    --buffer BUFFER, -bu BUFFER
                            Set the buffer size to retrieve OSI messages from
                            trace file. Set it to 0 if you do not want to use
                            buffering at all.

To run the validation first you need an OSI trace file which consists of multiple OSI messages. 
In the directory ``data`` we already have two OSI trace files provided which are called ``small_test.osi.lzma`` (a `lzma <https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm>`_ compressed trace file with length separation of OSI messages) and a ``small_test.txt.lzma`` (a `lzma <https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm>`_ compressed trace file with the ``$$__$$`` separator which in future will be depracted. Use the ``txt2osi.py`` of the OSI repo in the format directory to convert from ``*.txt`` to ``*.osi`` files or from ``*.txt.lzma`` to ``*.osi.lzma``). See usage below:

.. code-block:: bash

    usage: txt2osi converter [-h] [--file FILE]
                            [--type {SensorView,GroundTruth,SensorData}]
                            [--output OUTPUT] [--compress]

    Convert txt trace file to osi trace files.

    optional arguments:
    -h, --help            show this help message and exit
    --file FILE, -f FILE  Path to the file with serialized data.
    --type {SensorView,GroundTruth,SensorData}, -t {SensorView,GroundTruth,SensorData}
                            Name of the type used to serialize data.
    --output OUTPUT, -o OUTPUT
                            Output name of the file.
    --compress, -c        Compress the output to a lzma file.

To validate the trace files you simply call ``osivalidator`` and provide the path to the trace:

.. code-block:: bash

    osivalidator --data data/small_test.osi.lzma
    osivalidator --data data/small_test.txt.lzma -f separated

You can also validate the traces in parallel to increase the speed of the validation by providing ``-p`` flag:

.. code-block:: bash

    osivalidator --data data/small_test.osi.lzma -p
    osivalidator --data data/small_test.txt.lzma -f separated -p


After successfully running the validation the following output is generated:

.. code-block:: bash

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

.. code-block:: bash

    Errors (NUMBER_ERRORS) 
    Ranges of timestamps                Message
    --------------------------------    --------------------------------------------------------
    [START_TIMESTAMP, END_TIMESTAMP]    PATH_TO_RULE(VALUE) does not comply in PATH_TO_OSI_FIELD

    Warnings (NUMBER_WARNINGS) 
    Ranges of timestamps    Message
    --------------------------------    --------------------------------------------------------
    [START_TIMESTAMP, END_TIMESTAMP]    PATH_TO_RULE(VALUE) does not comply in PATH_TO_OSI_FIELD

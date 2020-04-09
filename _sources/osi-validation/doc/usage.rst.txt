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
In the directory ``data`` of the repository we already provide an example trace file which is called ``small_test.txt.lzma`` (a `lzma <https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm>`_ compressed trace file with the ``$$__$$`` separator which can/should be converted into an ``*.osi`` file). For decompressing lzma compressed files on linux machines run ``lzma -d data/small_test.txt.lzma``. 
Use the `txt2osi.py <https://github.com/OpenSimulationInterface/open-simulation-interface/blob/master/format/txt2osi.py>`_ of the OSI repo in the format directory to convert from ``*.txt`` to ``*.osi`` files or from ``*.txt.lzma`` to ``*.osi.lzma``). See usage below:

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
    osivalidator --data data/small_test.txt.lzma

You can also validate the traces in parallel to increase the speed of the validation by providing ``-p`` flag:

.. code-block:: bash

    osivalidator --data data/small_test.osi.lzma -p
    osivalidator --data data/small_test.txt.lzma -p

To validate trace files with rules defined in the comments of ``*.proto`` files in the open-simulation-interface repository first you need to generate them and then specify them:

.. code-block:: bash

    python rules2yml.py # Generates the rule directory
    osivalidator -r rules data/small_test.txt.lzma -p


After successfully running the validation the following output is generated:

.. note::

    For demonstration purposes a more complex trace file with 2718 OSI message was used in this example.

.. code-block:: bash

    Instantiate logger ...
    Reading data ...
    Retrieving messages in osi trace file until 1314997975 ...
    |################################| 1314997975/1314997975
    2718 messages has been discovered in 0.8990724086761475 s
    Collect validation rules ...

    Caching ...
    Importing messages from trace file ...
    |################################| 500/500
    Caching done!
    |#####                           | 500/2718 [0:04:07]
    Closed pool!

    Caching ...
    Importing messages from trace file ...
    |################################| 500/500
    Caching done!
    |###########                     | 1000/2718 [0:07:06]
    Closed pool!

    Caching ...
    Importing messages from trace file ...
    |################################| 500/500
    Caching done!
    |#################               | 1500/2718 [0:09:09]
    Closed pool!

    Caching ...
    Importing messages from trace file ...
    |################################| 500/500
    Caching done!
    |#######################         | 2000/2718 [0:12:34]
    Closed pool!

    Caching ...
    Importing messages from trace file ...
    |################################| 500/500
    Caching done!
    |#############################   | 2500/2718 [0:17:05]
    Closed pool!

    Caching ...
    Importing messages from trace file ...
    |################################| 218/218
    Caching done!
    |################################| 2718/2718 [0:17:54]
    Closed pool!


    Errors (55) 
    Ranges of timestamps                      Message
    ----------------------------------------  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    [0, 2717]                                 SensorView.host_vehicle_id.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.version.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.timestamp.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.mounting_position.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.mounting_position_rmse.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.host_vehicle_data.is_set(None) does not comply in SensorView
    [0, 498], [500, 998], [1000, 1498],       GroundTruth.country_code.is_set(None) does not comply in SensorView.global_ground_truth
    [1500, 1998], [2000, 2498], [2500, 2716]
    [0, 2717]                                 BaseStationary.base_polygon.is_set(None) does not comply in SensorView.global_ground_truth.stationary_object.base
    [0, 2717]                                 StationaryObject.base.is_valid(None) does not comply in SensorView.global_ground_truth.stationary_object.base
    [0, 2717]                                 StationaryObject.model_reference.is_set(None) does not comply in SensorView.global_ground_truth.stationary_object
    [0, 2717]                                 GroundTruth.stationary_object.is_valid(None) does not comply in SensorView.global_ground_truth.stationary_object
    [0, 2717]                                 MovingObject.VehicleAttributes.number_wheels.is_greater_than_or_equal_to(1) does not comply in SensorView.global_ground_truth.moving_object.vehicle_attributes.number_wheels
    [0, 2717]                                 MovingObject.vehicle_attributes.is_valid(None) does not comply in SensorView.global_ground_truth.moving_object.vehicle_attributes
    [0, 2717]                                 MovingObject.VehicleClassification.LightState.emergency_vehicle_illumination.is_set(None) does not comply in SensorView.global_ground_truth.moving_object.vehicle_classification.light_state
    [0, 2717]                                 MovingObject.VehicleClassification.LightState.service_vehicle_illumination.is_set(None) does not comply in SensorView.global_ground_truth.moving_object.vehicle_classification.light_state
    [0, 2717]                                 MovingObject.VehicleClassification.light_state.is_valid(None) does not comply in SensorView.global_ground_truth.moving_object.vehicle_classification.light_state
    [0, 2717]                                 MovingObject.vehicle_classification.is_valid(None) does not comply in SensorView.global_ground_truth.moving_object.vehicle_classification
    [0, 2717]                                 BaseMoving.orientation_acceleration.is_set(None) does not comply in SensorView.global_ground_truth.moving_object.base
    [0, 2717]                                 BaseMoving.base_polygon.is_set(None) does not comply in SensorView.global_ground_truth.moving_object.base
    [0, 2717]                                 MovingObject.base.is_valid(None) does not comply in SensorView.global_ground_truth.moving_object.base
    [0, 2717]                                 MovingObject.model_reference.is_set(None) does not comply in SensorView.global_ground_truth.moving_object
    [0, 2717]                                 GroundTruth.moving_object.is_valid(None) does not comply in SensorView.global_ground_truth.moving_object
    [0, 2717]                                 GroundTruth.traffic_sign.is_set(None) does not comply in SensorView.global_ground_truth
    [0, 2717]                                 GroundTruth.traffic_light.is_set(None) does not comply in SensorView.global_ground_truth
    [0, 2717]                                 GroundTruth.road_marking.is_set(None) does not comply in SensorView.global_ground_truth
    [0, 2717]                                 LaneBoundary.Classification.limiting_structure_id.is_set(None) does not comply in SensorView.global_ground_truth.lane_boundary.classification
    [0, 2717]                                 LaneBoundary.classification.is_valid(None) does not comply in SensorView.global_ground_truth.lane_boundary.classification
    [0, 2717]                                 GroundTruth.lane_boundary.is_valid(None) does not comply in SensorView.global_ground_truth.lane_boundary
    [0, 2717]                                 Lane.Classification.right_adjacent_lane_id.check_if.is_set(None) does not comply in SensorView.global_ground_truth.lane.classification
    [0, 2717]                                 Lane.Classification.right_adjacent_lane_id.check_if([{'is_different_to': 4, 'target': 'this.type'}]) does not comply in SensorView.global_ground_truth.lane.classification
    [0, 2717]                                 Lane.Classification.right_adjacent_lane_id.is_set(None) does not comply in SensorView.global_ground_truth.lane.classification
    [0, 2717]                                 Lane.Classification.free_lane_boundary_id.check_if.is_set(None) does not comply in SensorView.global_ground_truth.lane.classification
    [0, 2717]                                 Lane.Classification.free_lane_boundary_id.check_if([{'is_different_to': 4, 'target': 'this.type'}]) does not comply in SensorView.global_ground_truth.lane.classification
    [0, 2717]                                 Lane.Classification.free_lane_boundary_id.is_set(None) does not comply in SensorView.global_ground_truth.lane.classification
    [0, 2717]                                 Lane.Classification.lane_pairing.is_set(None) does not comply in SensorView.global_ground_truth.lane.classification
    [0, 2717]                                 Lane.classification.is_valid(None) does not comply in SensorView.global_ground_truth.lane.classification
    [0, 2717]                                 Lane.Classification.left_adjacent_lane_id.check_if.is_set(None) does not comply in SensorView.global_ground_truth.lane.classification
    [0, 2717]                                 Lane.Classification.left_adjacent_lane_id.check_if([{'is_different_to': 4, 'target': 'this.type'}]) does not comply in SensorView.global_ground_truth.lane.classification
    [0, 2717]                                 Lane.Classification.left_adjacent_lane_id.is_set(None) does not comply in SensorView.global_ground_truth.lane.classification
    [0, 2717]                                 GroundTruth.lane.is_valid(None) does not comply in SensorView.global_ground_truth.lane
    [0, 2717]                                 GroundTruth.occupant.is_set(None) does not comply in SensorView.global_ground_truth
    [0, 2717]                                 EnvironmentalConditions.atmospheric_pressure.is_greater_than_or_equal_to(80000) does not comply in SensorView.global_ground_truth.environmental_conditions.atmospheric_pressure
    [0, 2717]                                 EnvironmentalConditions.temperature.is_greater_than_or_equal_to(170) does not comply in SensorView.global_ground_truth.environmental_conditions.temperature
    [0, 2717]                                 EnvironmentalConditions.unix_timestamp.is_set(None) does not comply in SensorView.global_ground_truth.environmental_conditions
    [0, 498], [500, 998], [1000, 1498],       EnvironmentalConditions.fog.is_set(None) does not comply in SensorView.global_ground_truth.environmental_conditions
    [1500, 1998], [2000, 2498], [2500, 2716]
    [0, 2717]                                 GroundTruth.environmental_conditions.is_valid(None) does not comply in SensorView.global_ground_truth.environmental_conditions
    [0, 2717]                                 GroundTruth.proj_string.is_set(None) does not comply in SensorView.global_ground_truth
    [0, 2717]                                 GroundTruth.map_reference.is_set(None) does not comply in SensorView.global_ground_truth
    [0, 2717]                                 SensorView.global_ground_truth.is_valid(None) does not comply in SensorView.global_ground_truth
    [0, 2717]                                 SensorView.generic_sensor_view.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.radar_sensor_view.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.lidar_sensor_view.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.camera_sensor_view.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.ultrasonic_sensor_view.is_set(None) does not comply in SensorView
    499, 999, 1499, 1999, 2499, 2717          GroundTruth.country_code.is_iso_country_code(None) does not comply in SensorView.global_ground_truth.country_code

    Warnings (7) 
    Ranges of timestamps    Message
    ----------------------  ----------------------------------------------------------------------
    [0, 2717]               Several objects of type SensorView, MovingObject have the ID 0
    [513, 641]              Several objects of type StationaryObject, MovingObject have the ID 555
    513, [571, 641]         Several objects of type StationaryObject, MovingObject have the ID 454
    [504, 512]              Several objects of type StationaryObject, MovingObject have the ID 444
    [642, 770]              Several objects of type StationaryObject, MovingObject have the ID 666
    [643, 749]              Several objects of type StationaryObject, MovingObject have the ID 667
    [642, 770]              Several objects of type StationaryObject, MovingObject have the ID 668



The Output is a report of how many errors (here 55) and warnings (here 7) were found in the osi-message according to the defined rules in your specified rules directory. The rules can be found under the tag ``\rules`` in the \*.proto files from the `osi github <https://github.com/OpenSimulationInterface/open-simulation-interface>`_ or in the `requirements folder <https://github.com/OpenSimulationInterface/osi-validation/tree/master/requirements-osi-3>`_ from osi-validation as \*.yml files (for more information see :ref:`commenting`).

Currently an error is thrown when a message is not valid or the fields inside the message are not set. A warning is thrown everything concerning ids. For each error and warning there is a description on which timestamp it was found, the path to the rule and the path to the osi-message is provided. The general format is:

.. code-block:: bash

    Errors (NUMBER_ERRORS) 
    Ranges of timestamps                Message
    --------------------------------    --------------------------------------------------------
    [START_TIMESTAMP, END_TIMESTAMP]    PATH_TO_RULE(VALUE) does not comply in PATH_TO_OSI_FIELD

    Warnings (NUMBER_WARNINGS) 
    Ranges of timestamps    Message
    --------------------------------    --------------------------------------------------------
    [START_TIMESTAMP, END_TIMESTAMP]    PATH_TO_RULE(VALUE) does not comply in PATH_TO_OSI_FIELD

Understanding Validation Ouput
-------------------------------
For easier understanding of the validation output let us use the example above and describe the meaning of the lines.
First of all one should know that the rules to the fields are checked in a `depth-first-search <https://en.wikipedia.org/wiki/Depth-first_search>`_ (DFS) traversal manner. 
The validation starts with the ``SensorView`` Node and goes in depth if the message is set. For example the messages below are checked but do not go further in depth because they are not set (indicated by ``is_set(None)``):

.. code-block:: bash

    [0, 2717]                                 SensorView.host_vehicle_id.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.version.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.timestamp.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.mounting_position.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.mounting_position_rmse.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.host_vehicle_data.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.generic_sensor_view.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.radar_sensor_view.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.lidar_sensor_view.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.camera_sensor_view.is_set(None) does not comply in SensorView
    [0, 2717]                                 SensorView.ultrasonic_sensor_view.is_set(None) does not comply in SensorView

Since the ``GlobalGroundTruth`` in ``SensorView`` is set (``SensorView.global_ground_truth``) the next check is a test if it is valid. 
A message is valid when all the fields in all the submessages comply to the rules. Hence the check for valid fields is performed recursively.
The validation output prints a non valid message (indicated by ``is_valid(None)``):

.. code-block:: bash

    [0, 2717]                                 SensorView.global_ground_truth.is_valid(None) does not comply in SensorView.global_ground_truth

This is because at least one message field does not comply to the rules like:

.. code-block:: bash

    [0, 498], [500, 998], [1000, 1498],       GroundTruth.country_code.is_set(None) does not comply in SensorView.global_ground_truth
    [1500, 1998], [2000, 2498], [2500, 2716]
    499, 999, 1499, 1999, 2499, 2717          GroundTruth.country_code.is_iso_country_code(None) does not comply in SensorView.global_ground_truth.country_code

In the rules (``osi_groundtruth.yml``) we defined (\*.yml files follow the same structure as \*.proto file in OSI):

.. code-block:: yaml

    GroundTruth:
        country_code:
            - is_iso_country_code:

This means if the field is not in the `ISO country code <https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes>`_ format an error will be thrown making ``SensorView.global_ground_truth`` invalid because ``SensorView.global_ground_truth.country_code`` is not set. 
The incorrectness is appearing in the intervals between message frame 0 and message frame 498 but not in message frame 499. In the message frame 499 the ``GroundTruth.country_code`` is set but do not comply to the ``is_iso_country_code`` rule. 
That is why you see split frame messages like this [0, 498], [500, 998] for not set and 499 for is not ISO country code.
Note that ``GroundTruth.country_code`` refers to the same path as ``SensorView.global_ground_truth.country_code``. 
The SensorView part is cut due to better readability.

In the output there are more message fields which are not set on the ``GroundTruth`` level making it invalid:

.. code-block:: bash

    [0, 2717]                                 GroundTruth.proj_string.is_set(None) does not comply in SensorView.global_ground_truth
    [0, 2717]                                 GroundTruth.map_reference.is_set(None) does not comply in SensorView.global_ground_truth
    [0, 2717]                                 GroundTruth.occupant.is_set(None) does not comply in SensorView.global_ground_truth
    [0, 2717]                                 GroundTruth.traffic_sign.is_set(None) does not comply in SensorView.global_ground_truth
    [0, 2717]                                 GroundTruth.traffic_light.is_set(None) does not comply in SensorView.global_ground_truth
    [0, 2717]                                 GroundTruth.road_marking.is_set(None) does not comply in SensorView.global_ground_truth

Next the path ``GroundTruth.environmental_conditions`` is set but not valid leading to the output below (Note that the indentation demonstrates the hierarchy of the message fields):

.. code-block:: bash

    [0, 2717]                                 GroundTruth.environmental_conditions.is_valid(None) does not comply in SensorView.
        [0, 2717]                                 EnvironmentalConditions.atmospheric_pressure.is_greater_than_or_equal_to(80000) does not comply in SensorView.global_ground_truth.environmental_conditions.atmospheric_pressure
        [0, 2717]                                 EnvironmentalConditions.temperature.is_greater_than_or_equal_to(170) does not comply in SensorView.global_ground_truth.environmental_conditions.temperature
        [0, 2717]                                 EnvironmentalConditions.unix_timestamp.is_set(None) does not comply in SensorView.global_ground_truth.environmental_conditions
        [0, 498], [500, 998], [1000, 1498],       EnvironmentalConditions.fog.is_set(None) does not comply in SensorView.global_ground_truth.environmental_conditions
        [1500, 1998], [2000, 2498], [2500, 2716]

The output is generate because of the rules defined in ``osi_environment.yml``:

.. code-block:: yaml

    EnvironmentalConditions:
        ambient_illumination:
        time_of_day:
        unix_timestamp:
        atmospheric_pressure:
            - is_greater_than_or_equal_to: 80000
            - is_less_than_or_equal_to: 120000
        temperature:
            - is_greater_than_or_equal_to: 170
            - is_less_than_or_equal_to: 340
        relative_humidity:
            - is_greater_than_or_equal_to: 0
            - is_less_than_or_equal_to: 100
        precipitation:
        fog:
        TimeOfDay:
            seconds_since_midnight:
            - is_greater_than_or_equal_to: 0
            - is_less_than: 86400

The rules state that the ``EnvironmentalConditions.atmospheric_pressure`` should be between 80000 Pa and 120000 Pa which is not the case for the trace (the used trace atmospheric_pressure is set to zero). 
The same goes for the temprature.

The validation output reads for the other fields the same way as for the example above (indentation and ordering was added manually for readability):

.. code-block:: bash

    [0, 2717]                                 GroundTruth.lane_boundary.is_valid(None) does not comply in SensorView.global_ground_truth.lane_boundary
        [0, 2717]                                 LaneBoundary.classification.is_valid(None) does not comply in SensorView.global_ground_truth.lane_boundary.classification
            [0, 2717]                                 LaneBoundary.Classification.limiting_structure_id.is_set(None) does not comply in SensorView.global_ground_truth.lane_boundary.classification
    [0, 2717]                                 GroundTruth.lane.is_valid(None) does not comply in SensorView.global_ground_truth.lane
        [0, 2717]                                 Lane.classification.is_valid(None) does not comply in SensorView.global_ground_truth.lane.classification
            [0, 2717]                                 Lane.Classification.right_adjacent_lane_id.check_if.is_set(None) does not comply in SensorView.global_ground_truth.lane.classification
            [0, 2717]                                 Lane.Classification.right_adjacent_lane_id.check_if([{'is_different_to': 4, 'target': 'this.type'}]) does not comply in SensorView.global_ground_truth.lane.classification
            [0, 2717]                                 Lane.Classification.right_adjacent_lane_id.is_set(None) does not comply in SensorView.global_ground_truth.lane.classification
            [0, 2717]                                 Lane.Classification.free_lane_boundary_id.check_if.is_set(None) does not comply in SensorView.global_ground_truth.lane.classification
            [0, 2717]                                 Lane.Classification.free_lane_boundary_id.check_if([{'is_different_to': 4, 'target': 'this.type'}]) does not comply in SensorView.global_ground_truth.lane.classification
            [0, 2717]                                 Lane.Classification.free_lane_boundary_id.is_set(None) does not comply in SensorView.global_ground_truth.lane.classification
            [0, 2717]                                 Lane.Classification.lane_pairing.is_set(None) does not comply in SensorView.global_ground_truth.lane.classification
            [0, 2717]                                 Lane.Classification.left_adjacent_lane_id.check_if.is_set(None) does not comply in SensorView.global_ground_truth.lane.classification
            [0, 2717]                                 Lane.Classification.left_adjacent_lane_id.check_if([{'is_different_to': 4, 'target': 'this.type'}]) does not comply in SensorView.global_ground_truth.lane.classification
            [0, 2717]                                 Lane.Classification.left_adjacent_lane_id.is_set(None) does not comply in SensorView.global_ground_truth.lane.classification
    [0, 2717]                                 GroundTruth.moving_object.is_valid(None) does not comply in SensorView.global_ground_truth.moving_object
        [0, 2717]                                 MovingObject.vehicle_attributes.is_valid(None) does not comply in SensorView.global_ground_truth.moving_object.vehicle_attributes
            [0, 2717]                                 MovingObject.VehicleAttributes.number_wheels.is_greater_than_or_equal_to(1) does not comply in SensorView.global_ground_truth.moving_object.vehicle_attributes.number_wheels
        [0, 2717]                                 MovingObject.base.is_valid(None) does not comply in SensorView.global_ground_truth.moving_object.base
            [0, 2717]                                 BaseMoving.orientation_acceleration.is_set(None) does not comply in SensorView.global_ground_truth.moving_object.base
            [0, 2717]                                 BaseMoving.base_polygon.is_set(None) does not comply in SensorView.global_ground_truth.moving_object.base
        [0, 2717]                                 MovingObject.vehicle_classification.is_valid(None) does not comply in SensorView.global_ground_truth.moving_object.vehicle_classification
            [0, 2717]                                 MovingObject.VehicleClassification.LightState.emergency_vehicle_illumination.is_set(None) does not comply in SensorView.global_ground_truth.moving_object.vehicle_classification.light_state
            [0, 2717]                                 MovingObject.VehicleClassification.light_state.is_valid(None) does not comply in SensorView.global_ground_truth.moving_object.vehicle_classification.light_state
                [0, 2717]                                 MovingObject.VehicleClassification.LightState.service_vehicle_illumination.is_set(None) does not comply in SensorView.global_ground_truth.moving_object.vehicle_classification.light_state
        [0, 2717]                                 MovingObject.model_reference.is_set(None) does not comply in SensorView.global_ground_truth.moving_object
    [0, 2717]                                 GroundTruth.stationary_object.is_valid(None) does not comply in SensorView.global_ground_truth.stationary_object
        [0, 2717]                                 StationaryObject.model_reference.is_set(None) does not comply in SensorView.global_ground_truth.stationary_object
        [0, 2717]                                 StationaryObject.base.is_valid(None) does not comply in SensorView.global_ground_truth.stationary_object.base
            [0, 2717]                                 BaseStationary.base_polygon.is_set(None) does not comply in SensorView.global_ground_truth.stationary_object.base

Custom Rules
--------------

Currently the following rules exist:

.. code-block:: python
    
    is_greater_than: 1
    is_greater_than_or_equal_to: 1
    is_less_than_or_equal_to: 10
    is_less_than: 2
    is_equal: 1
    is_different: 2
    is_globally_unique
    refers_to: MovingObject
    is_iso_country_code:
    first_element: {is_equal: 0.13, is_greater_than: 0.13}
    last_element: {is_equal: 0.13, is_greater_than: 0.13}
    check_if: [{is_equal: 2, is_greater_than: 3, target: this.y}, {do_check: {is_equal: 1, is_less_than: 3}}]

These rules can be added manually to the rules \*.yml files like in the example of the environmental conditions below (see :ref:`how-to-write-rules` for more): 

.. code-block:: yaml

    EnvironmentalConditions:
        ambient_illumination:
        time_of_day:
        unix_timestamp:
        atmospheric_pressure:
            - is_greater_than_or_equal_to: 80000
            - is_less_than_or_equal_to: 120000
        temperature:
            - is_greater_than_or_equal_to: 170
            - is_less_than_or_equal_to: 340
        relative_humidity:
            - is_greater_than_or_equal_to: 0
            - is_less_than_or_equal_to: 100
        precipitation:
        fog:
        TimeOfDay:
            seconds_since_midnight:
            - is_greater_than_or_equal_to: 0
            - is_less_than: 86400

Further custom rules can be implemented into the osi-validator (see `rules implementation <https://opensimulationinterface.github.io/osi-documentation/osi-validation/doc/osivalidator.html#module-osivalidator.osi_rules_implementations>`_ for more).
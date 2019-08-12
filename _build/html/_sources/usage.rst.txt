Usage
=====

Using this command will check each time step of data independently for all the
rules.

.. code-block:: text

    usage: osivalidator [-h] [--rules RULES] --data DATA
                        [--type {SensorView,GroundTruth,SensorData}]
                        [--output OUTPUT] [--timesteps TIMESTEPS] [--debug]
                        [--verbose]

    Validate data defined at the input

    optional arguments:
    -h, --help            show this help message and exit
    --rules RULES, -r RULES
                            Directory with text files containig rules.
    --data DATA, -d DATA  Path to the file with OSI-serialized data.
    --type {SensorView,GroundTruth,SensorData}, -t {SensorView,GroundTruth,SensorData}
                            Name of the message type used to serialize data.
    --output OUTPUT, -o OUTPUT
                            Output folder of the log files.
    --timesteps TIMESTEPS
                            Number of timesteps to analyze. If -1, all.
    --debug               Set the debug mode to ON.
    --verbose             Set the verbose mode to ON (display in console).


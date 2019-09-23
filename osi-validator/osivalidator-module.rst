.. _osi-validation:

OSI Validation
===============

.. image:: https://travis-ci.org/OpenSimulationInterface/osi-validation.svg?branch=master
    :target: https://travis-ci.org/OpenSimulationInterface/osi-validation

The OSI Validator is a validation framework for the field values of OSI messages. It recursively checks the compliance of an OSI message of type ``SensorData``, ``SensorView`` or ``GroundTruth`` according to predefined rules. It was developed due to the need of validation of a huge amount of incoming OSI messages which cannot be validated by hand. 



.. toctree::
   :maxdepth: 2

   setup
   usage
   writing-rules
   osivalidator
   

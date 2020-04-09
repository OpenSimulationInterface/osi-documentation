.. _how-to-write-rules:

How to write rules
===================

Folder structure
-----------------

Currently the rules are contained in ``*.yml`` files in the folder `requirements-osi-3 <https://github.com/OpenSimulationInterface/osi-validation/tree/master/requirements-osi-3>`_. 
The organization of the files in this folder follows the architecture of OSI for consistency. In the future the rules will be ported directly into the ``*.proto`` files of `OSI <https://github.com/OpenSimulationInterface/open-simulation-interface>`_.

File structure
---------------

Below you can see an example of the `osi_detectedlane.yml <https://github.com/OpenSimulationInterface/osi-validation/blob/master/requirements-osi-3/osi_detectedlane.yml>`_ rule file for `osi_detectedlane.proto <https://github.com/OpenSimulationInterface/open-simulation-interface/blob/master/osi_detectedlane.proto>`_:

.. code-block:: YAML

  DetectedLane:
    header:
    CandidateLane:
      probability:
        - is_greater_than_or_equal_to: 0
        - is_less_than_or_equal_to: 1
      classification:

  DetectedLaneBoundary:
    header:
    boundary_line:
      position:

Each root at the top level represent a root message type ``DetectedLane`` or ``DetectedLaneBoundary``. The children of each root message represent its fields if they are
not camel-case. For example ``header`` is a field of ``DetectedLane`` or ``header`` and ``boundary_line`` are fields of ``DetectedLaneBoundary``. ``CandidateLane`` is a submessage of the message ``DetectedLane``. Each field has a ``sequence`` (starting with an hyphen ``-``) of rules that apply to that specific field. For example the probability of the message ``CandidateLane`` is between 0 and 1.


Rules
------

The rules can either be with or without any parameters.

::

  is_greater_than_or_equal_to: 0.0
  is_equal: 1

In the case a rule has a parameter, it is written as a `mapping` ( a `scalar`
followed by a colon ":"). What comes after the colon depends on the rule used. For instance, the rule ``is_greater_than_or_equal_to`` accept a double.

The available rules and their usage are explained in the osi-validator class `osi_rules_implementations <https://opensimulationinterface.github.io/osi-documentation/osi-validation/doc/osivalidator.html#module-osivalidator.osi_rules_implementations>`_. See also examples for available rules which can be defined in ``*.yml`` files below:

.. code-block:: python
    
    is_greater_than: 1
    is_greater_than_or_equal_to: 1
    is_less_than_or_equal_to: 10
    is_less_than: 2
    is_equal: 1
    is_different: 2
    is_globally_unique
    refers_to: Lane
    is_iso_country_code:
    first_element: {is_equal: 0.13, is_greater_than: 0.13}
    last_element: {is_equal: 0.13, is_greater_than: 0.13}
    check_if: [{is_equal: 2, is_greater_than: 3, target: this.y}, {do_check: {is_equal: 1, is_less_than: 3}}]


Severity
--------

When an attribute does not comply with a rule, a Warning is throw. An Error
will be throw if an exclamation mark is written at the end of the verb of a
rule.

Example
^^^^^^^
::

  is_greater_than!: 0

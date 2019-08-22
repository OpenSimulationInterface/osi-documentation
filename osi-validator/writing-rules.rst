.. _how-to-write-rules:

How to write rules
===================

Folder structure
-----------------

The rules are contained into YAML files into one folder. The organization of
the files in this folder follows the architecture of OSI for consistency.

File structure
---------------

We will take this example of the `osi_detectedlane.yml` file:

.. code-block:: YAML

  DetectedLane:
    header:
      - is_set
    CandidateLane:
      probability:
        - in_range: [0, 1]
      classification:
        - is_set

  DetectedLaneBoundary:
    header:
      - is_set
    boundary_line:
      - each:
          position:
            - is_set

According to the Python module used, YAML **version 1.1** is used. In this
document, we will try to make associations between the `YAML` vocabulary
according to its specifications and the `Protocol Buffers` one.

Each root (at the top level) `scalar` represent a root message type (ex:
``DetectedLane``, ``DetectedLaneBoundary``).

The children `scalars` of each `root scalar` represent its fields if they are
not camel-case (ex: ``header`` is a field of ``DetectedLane`` ; ``header`` and
``boundary_line`` are fields of ``DetectedLaneBoundary``). See `Child message
type`_ for the camel-case scalars.

Each field has a `sequence` (starting with an hyphen ``-``) of scalar
representing the `rules`_ that apply on.

Child message type
------------------

A message type can have included message type. For example ``DetectedLane`` has
a ``CandidateLane`` included message type. They first seem similar has field
but they are not: they contain, exactly like top-level message type, fields
with rules.

Rules
------

The rules can either be without any parameter (ex: ``is_set``) or with a
parameter.

Example
^^^^^^^
::

  in_range: [0, 1]

In the case a rule has a parameter, it is written as a `mapping` (a `scalar`
followed by a column ":"). What comes after the column is totally free and
depends on the rule used. For instance, the rule ``in_range`` accept a sequence
of double ; the rule ``each`` ask for mappings. Other rules accept string,
number, etc.

The available rule and their usage are explained here: :doc:`rules`.

Severity
--------

When an attribute does not comply with a rule, a Warning is throw. An Error
will be throw if an exclamation mark is written at the end of the verb of a
rule.

Example
^^^^^^^
::

  in_range!: [0, 1]

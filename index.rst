.. Open Simulation Interface documentation master file, created by
   sphinx-quickstart on Sat Aug 10 20:49:55 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Open Simulation Interface's documentation!
=====================================================

The Vision
-----------

The Open Simulation Interface (OSI) is a generic interface for the environmental perception of automated driving functions in virtual scenarios.

As the complexity of automated driving functions rapidly increases, the requirements for test and development methods are growing.
Testing in virtual environments offers the advantage of completely controlled and reproducible environment conditions.

In order to achieve widespread use of driving simulators for function developers, the connection between the function development framework and the simulation environment has to rely on generic and standardized interfaces.
An easy and straight-forward compatibility between automated driving functions and the variety of available driving simulation frameworks is made possible by OSI.
OSI was developed exactly for this purpose and addresses the emerging standard ISO 23150 for real sensors' standardized communication interface.
In this context, OSI defines generic interfaces to ensure modularity, integrability, and interchangeability of the individual components:
The following figure shows the interfaces and models involved in modeling a sensor.

.. image:: _static/images/osi-context.png
   :align: center
   :alt: Open Simulation Interface overview

OSI also defines interfaces for traffic participant models.
These interfaces allow to send commands to traffic participant models and to receive their updated state.
The following figure shows the interfaces of a generic traffic participant.

.. image:: _static/images/osi-traffic-participant-principle.png
   :align: center
   :alt: Traffic participant interfaces

Traffic participant models may use other OSI interfaces internally, for example, to model autonomous vehicles.
The following figure shows a more advanced use case for traffic participants.

.. image:: _static/images/osi-traffic-participant-use-case-3.png
   :align: center
   :alt: Traffic participant with sensor models, AD function, and dynamic model

OSI currently provides only limited support for data structures describing measured internal states of the traffic participant.
Actuator intentions are currently not covered by OSI and must be handled with a different data description format.

Interfaces
----------

OSI contains an object-based environment description using the message format of the `protocol buffer <https://github.com/protocolbuffers/protobuf/wiki>`_ library developed and maintained by Google. OSI defines top-level messages that are used to exchange between separate models. Top-level messages defines the ``GroundTruth`` interface, the SensorData interface and, since OSI version 3.0.0, the ``SensorView`` / ``SensorView`` configuration interfaces and the ``FeatureData`` interface.

The ``GroundTruth`` interface provides an exact view on the simulated objects in a global coordinate system, the ground truth world coordinate system. This message is populated using the data available internally and then published to external subscribers by a plugin within the driving simulation framework. Depending on the external subscriber, the ``GroundTruth`` message may be individually restricted to reduce the data to be exchanged to the necessary level (e.g. ``SensorView``).

The ``FeatureData`` interface provides a list of simple features in the reference frame of the respective sensor of a vehicle for environmental perception. It is generated from a ``GroundTruth`` message and may serve as input for a sensor model that simulates object detection or feature fusion of multiple sensors.

The ``SensorData`` interface describes the objects in the reference frame of a vehicle for environmental perception. It is generated from a ``GroundTruth`` message or from one or several ``FeatureData`` messages and can either be used to directly connect to an automated driving function using ideal simulated data, or may serve as input for a sensor model simulating limited perception as a replication of real world sensor behaviour.

The ``SensorView`` Configuration interface is the configuration setting for the ``SensorView`` to be provided by the environment simulation. This message can be provided by the sensor model to the environment simulation, in which case it describes the input configuration that is desired by the sensor model. In response the environment simulation will configure the input and provide a new message of this type, which describes the actual configuration that it is going to employ. The two can and will differ, when either the environment simulation does not support a given requested configuration, and/or when the requested configuration allowed for multiple alternatives, in which case the set configuration will only contain the alternative chosen. It should be noted that this message is not intended to provide for parameterization of a generic sensor model, but rather for the automatic configuration of an environment simulation in order to supply the necessary input to it, depending on its actual configuration.

The ``SensorView`` interface is derived from ``GroundTruth`` and used as input to sensor models. The ``SensorView`` information is supposed to provide input to sensor models for simulation of actual real sensors. All information regarding the environment is given with respect to the virtual sensor coordinate system, except for the individual physical technology-specific data, which is given with respect to the physical sensor coordinate system specified in the corresponding physical sensor's mounting position, and the global ground truth, which is given in global coordinates.

The ```TrafficCommand`` interface provides control commands from the scenario engine to traffic participant models.

The ``TrafficUpdate`` interface is provided by traffic participant models to provide updates of their position, state and future trajectory back to the simulation environment.

The authors' vision is to be able to connect any automated driving function to any driving simulator and emerging new hardware sensor generations with a standardized ISO 23150 interface. This will simplify integration and thus significantly strengthen the accessibility and usefulness of virtual testing.


.. toctree::
   :maxdepth: 1
   :caption: Open Simulation Interface:

   open-simulation-interface/README
   open-simulation-interface/doc/description
   open-simulation-interface/doc/installation
   open-simulation-interface/doc/fileformat
   open-simulation-interface/doc/coordinatesystem
   osi-documentation/traffic-participants
   open-simulation-interface/doc/interfaceconventions
   open-simulation-interface/doc/commenting
   open-simulation-interface/doc/versioning
   open-simulation-interface/doc/releases
   open-simulation-interface/doc/howtocontribute
   open-simulation-interface/library_root

.. toctree::
    :maxdepth: 2
    :caption: OSI Validator:

    osi-validation/README
    osi-validation/doc/description
    osi-validation/doc/howtocontribute
    osi-validation/doc/osivalidator


.. toctree::
    :maxdepth: 2
    :caption: OSI Visualizer:

    osi-visualizer/README
    osi-visualizer/doc/panels
    osi-visualizer/doc/nvidia-docker
    osi-visualizer/doc/howtocontribute


.. toctree::
    :maxdepth: 2
    :caption: OSI Sensor Model Packaging:

    osi-sensor-model-packaging/README
    osi-sensor-model-packaging/doc/specification
    osi-sensor-model-packaging/doc/examples

.. toctree::
    :maxdepth: 2
    :caption: Proto2Cpp:

    proto2cpp/README


API Reference
-------------
Visit the `doxygen documentation <https://opensimulationinterface.github.io/open-simulation-interface/>`_ of the actual `open-simulation-interface <https://github.com/OpenSimulationInterface/open-simulation-interface>`_ master branch.


Indices and tables
-------------------
* :ref:`genindex`
* :ref:`search`

Modeling traffic participants
==============================

Traffic participants
--------------------

A traffic participant is an element of the simulated world, which can change its position and orientation during simulation time.
A traffic participant represents one of the following:

- A living being.
- A means of transportation for living beings.
- A means of transportation for goods.
- Any other movable object that may travel the road network.

Pedestrians and animals are examples of traffic participants that are living objects.
Vehicles are examples of traffic participants that are means of transportation.
Therefore, the ego vehicle is also a traffic participant.

The following figure shows the interface of a traffic participant.

.. image:: _static/images/osi-traffic-participant-principle.png
   :align: center
   :alt: Traffic participant interface.

With every simulation step, an OSI traffic participant model receives ground truth data from the environment around itself, the sensor view.
A traffic participant can output its own perceivable state, the traffic update.
Traffic commands influence the behavior of the traffic participant model.
This channel allows event-based communication towards the traffic participant, for example, at certain simulation steps.
OSI only specifies the interface of the traffic participant.
OSI is agnostic to the architecture of both, the simulation environment and the traffic participant.


Use cases for traffic participants
----------------------------------

Different models are involved in modeling a traffic participant.
In all the examples, a simulator loads and interprets a scenario and a map prior to execution.
The scenario is, for example, provided by OpenSCENARIO.
The map data is, for example, provided by OpenDRIVE.
During runtime the simulator interacts with the traffic participants via OSI messages.
There can be multiple instances of a traffic participant.
The traffic participants are co-simulated.

The following figure shows a very simple use case.

.. image:: _static/images/osi-traffic-participant-use-case-1.png
   :align: center
   :alt: Simple traffic participant

The traffic participant bases its behavior only on an idealized view of the area around it.
The traffic participant’s dynamics are included in the model, if they exist.
The map, the simulated world state, the sensor view, and the traffic updates represent the ground truth, meaning objective statements about the world.
The scenario and the traffic commands on the other hand represent the intentions of the traffic participants.

The following figure shows a traffic participant with a separately modeled behavior and dynamics.

.. image:: _static/images/osi-traffic-participant-use-case-2.png
   :align: center
   :alt: Traffic participants with separate dynamics.

Separating dynamics from behavior introduces 2 more types of channels:

* Measured data, meaning ground truth as interpreted by the traffic participant
* Actuator-intention data, providing information on what actuators are supposed to do

In this example, host vehicle data describes how the vehicle interprets its own states.
OSI currently provides only limited support for data structures describing measured internal states of the traffic participant.
Actuator intentions are currently not covered by OSI and must be handled with a different data description format.

The following figure shows a more complex traffic participant.

.. image:: _static/images/osi-traffic-participant-use-case-3.png
   :align: center
   :alt: Traffic participant with sensor models, AD-function, and dynamic model.

This use case will probably be relevant for modeling the ego vehicle, which includes the SUT.
The traffic participant includes an arbitrary number of sensor models, which provide sensor data.
Sensor data is another example of measured data as an interpretation of ground truth by the traffic participant.
In contrast to host vehicle data, sensor data describes how sensors interpret the surroundings, for example, with lidar, camera, radar, or ultrasonic technology.
The AD-function consumes measured data and outputs actuator-intention data.
As with the prior example, OSI currently does not support actuator-intention data.

The following figure shows a cooperative use case with both an AD-function and a human driver.

.. image:: _static/images/osi-traffic-participant-use-case-4.png
   :align: center
   :alt: Traffic participant with both an AD-function and a human driver.

It is possible to model a traffic participant with an AD-function in the loop, but a human driver can still override the actuation command.
Such a cooperative use case is, for example, relevant to studies on human-machine interaction.
OSI's limitations regarding dynamic-model input apply in this example as well.

The following figure shows a similiar example with the difference that there is only a human driver in control.

.. image:: _static/images/osi-traffic-participant-use-case-5.png
   :align: center
   :alt: Driver in the loop.

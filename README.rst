`OSI-Documentation <https://opensimulationinterface.github.io/osi-documentation/>`_
======================================================================================

.. image:: https://github.com/OpenSimulationInterface/osi-documentation/actions/workflows/asciidoc-build.yml/badge.svg?branch=master
    :target: https://github.com/OpenSimulationInterface/osi-documentation/actions/workflows/asciidoc-build.yml

This is the main repository for the whole documentation of the osi-project. 
The documentation is based on `asciidoc <https://asciidoc.org/>`_. See the documentation `here <https://opensimulationinterface.github.io/osi-documentation/>`_.

Organization Build Overview
----------------------------
|osi_build| - `Open Simulation Interface`_

Pipeline is broken - `OSI Validation`_

|osi_visualizer_build| - `OSI Visualizer`_

|osi_sensor_model_packaging_build| - `OSI Model Packaging`_

How To build and change Documentation locally on Windows
--------------------------------------------------------
- Install Docker Desktop
- Clone this repository with submodules
- Clone OSI and OSMP with submodules into this folder
- Check file ``docker-compose.yml`` with the following content:

.. code-block:: yaml

  version: "2"
  
  services: 
  asciidoctor:
      image: asciidoctor/docker-asciidoctor:1
      volumes: 
      - .:/documents
      working_dir: /documents
      entrypoint: asciidoctor -D . --failure-level WARN -r asciidoctor-bibtex -r asciidoctor-diagram -a mathjax --trace --backend=html5 index.adoc -o open-simulation-interface_localbuild.html

.. _Open Simulation Interface: https://opensimulationinterface.github.io/osi-documentation/open-simulation-interface/README.html
.. _OSI Validation: https://opensimulationinterface.github.io/osi-documentation/osi-validation/README.html
.. _OSI Visualizer: https://opensimulationinterface.github.io/osi-documentation/osi-visualizer/README.html
.. _OSI Model Packaging: https://opensimulationinterface.github.io/osi-documentation/osi-sensor-model-packaging/README.html

.. |osi_build| image:: https://github.com/OpenSimulationInterface/open-simulation-interface/actions/workflows/protobuf.yml/badge.svg
    :target: https://github.com/OpenSimulationInterface/open-simulation-interface/actions/workflows/protobuf.yml

.. |osi_validation_build| image:: ..
    :target: ..

.. |osi_visualizer_build| image:: https://github.com/OpenSimulationInterface/osi-visualizer/actions/workflows/ci-build.yml/badge.svg
    :target: https://github.com/OpenSimulationInterface/osi-visualizer/actions/workflows/ci-build.yml

.. |osi_sensor_model_packaging_build| image:: https://github.com/OpenSimulationInterface/osi-sensor-model-packaging/actions/workflows/protobuf.yml/badge.svg
    :target: https://github.com/OpenSimulationInterface/osi-sensor-model-packaging/actions/workflows/protobuf.yml

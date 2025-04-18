==============
|nipy| NiPyApi
==============

.. |nipy| image:: https://image.ibb.co/f0FRs0/nipy.png
    :height: 28px

Nifi-Python-Api: A rich Apache NiFi Python Client SDK

.. image:: https://img.shields.io/pypi/v/nipyapi.svg
        :target: https://pypi.python.org/pypi/nipyapi
        :alt: Release Status

.. image:: https://readthedocs.org/projects/nipyapi/badge/?version=latest
        :target: https://nipyapi.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/Chaffelson/nipyapi/shield.svg
     :target: https://pyup.io/repos/github/Chaffelson/nipyapi/
     :alt: Python Updates

.. image:: https://coveralls.io/repos/github/Chaffelson/nipyapi/badge.svg?branch=main
    :target: https://coveralls.io/github/Chaffelson/nipyapi?branch=main&service=github
    :alt: test coverage

.. image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: License


Features
--------

**Three layers of Python support for working with Apache NiFi:**
 - High-level Demos and example scripts
 - Mid-level Client SDK for typical complex tasks
 - Low-level Client SDKs for the full API implementation of NiFi and selected sub-projects

**Functionality Highlights:**
 - Detailed documentation of the full SDK at all levels
 - CRUD wrappers for common task areas like Processor Groups, Processors, Templates, Registry Clients, Registry Buckets, Registry Flows, etc.
 - Convenience functions for inventory tasks, such as recursively retrieving the entire canvas, or a flat list of all Process Groups
 - Support for scheduling and purging flows, controller services, and connections
 - Support for fetching and updating Variable Registries
 - Support for import/export of Versioned Flows from NiFi-Registry
 - Docker Compose configurations for testing and deployment
 - A scripted deployment of an interactive environment, and a secured configuration, for testing and demonstration purposes


Please see the `issue <https://github.com/Chaffelson/nipyapi/issues>`_ register for more information on current development.

Quick Start
-----------

| There are several scripts to produce demo environments in *nipyapi.demo.**
| The mid-level functionality is in *nipyapi.canvas / nipyapi.security / nipyapi.templates / nipyapi.versioning*
| You can access the entire API using the low-level SDKs in *nipyapi.nifi / nipyapi.registry*

The easiest way to install NiPyApi is with pip::

    # in bash
    pip install nipyapi
    
    # or with docker support for demos
    pip install nipyapi[demo]

You can set the config for your endpoints in the central config file::

    # in python
    import nipyapi
    nipyapi.config.nifi_config.host = 'https://localhost:8080/nifi-api'
    nipyapi.config.registry_config.host = 'http://localhost:18080/nifi-registry-api'

Then import a module and execute tasks::


    nipyapi.canvas.get_root_pg_id()
    >'4d5dcf9a-015e-1000-097e-e505ed0f7fd2'

You can use the Docker demos to create a secured interactive console showing many features::

    from nipyapi.demo.secured_console import *
    from nipyapi.demo.console import *

You can also explore the scripts to get ideas for how NiPyAPi can be used to automate your environment.

Please check out the `Contribution Guide <https://github.com/Chaffelson/nipyapi/blob/master/docs/contributing.rst>`_ if you are interested in contributing to the feature set.

Background and Documentation
----------------------------

| For more information on Apache NiFi, please visit `https://nifi.apache.org <https://nifi.apache.org>`_
| For Documentation on this package please visit `https://nipyapi.readthedocs.io. <https://nipyapi.readthedocs.io/en/latest>`_


NiFi Version Support
--------------------

| Currently we are testing against NiFi versions 1.9.2 - 1.28.1, and NiFi-Registry versions 0.3.0 - 1.28.1.

| We have also tested against the latest NiFi-2.2.0 release using the 1.x SDK and have found that basic functionality works as expected.
| Apache NiFi offers no compatibility guarantees between major versions, and while many functions may work the same, you should test carefully for your specific use case.
| In future we will create a specific branch of NiPyAPI for NiFi 2.x SDKs, and maintain separate NiFi 1.x and NiFi 2.x clients.

| If you find a version compatibility problem please raise an `issue <https://github.com/Chaffelson/nipyapi/issues>`_

Python Support
--------------

| Python 3.9-12 supported, though other versions may work. 
| Python2 is no longer supported as of the 1.0 release, please use the 0.x branch for Python2 projects.
| OSX M1 chips have had various issues with Requests and Certificates.

| Tested on AL2023, developed on OSX 14+ and Windows 10 with Docker Desktop.
| Outside of the standard Python modules, we make use of lxml, DeepDiff, ruamel.yaml and xmltodict in processing, and Docker for demo/tests.

Welcome to pyCreate2's documentation!
=====================================

pyCreate2 is a package to control an iRobot Create2 robot.
It supports seamless integration with the V-REP robotics simulator.
Scripts can be run without any changes in simulation and on the physical robot.
The iCreate2 robot is extended with an embedded computer, allowing fully autonomous operation.

Getting Starting
----------------

Simulation
^^^^^^^^^^

#. Download pyCreate2 from the github repository
#. Download `V-REP <http://www.coppeliarobotics.com/>`_
#. Open example1.ttt in V-REP
#. Execute::

    python3 run.py example1 --sim

Physical Robot
^^^^^^^^^^^^^^

#. Modify your robot by following this section :ref:`hardware`
#. Install Ubuntu on the ODROID
#. Copy the python files to the ODROID
#. Execute::

    python3 run.py example1

Contents:

.. toctree::
   software
   hardware
   :maxdepth: 2


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


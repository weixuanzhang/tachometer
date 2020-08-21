# tachometer
A rosnode to get measurement data from UNI-T UT372 Tachometer

# system & software requirement
Ubuntu 18.04

Ros melodic

sigrok: https://sigrok.org/wiki/Main_Page

Sigrok implemented a driver for this specific tachometer. This node calls its commandline tool sigrok-cli to get the measurement.
TO run the node: rosrun tachometer tachometer_node.py

This could get a update rate of 1 Hz.

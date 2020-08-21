# tachometer
A rosnode to get measurement data from UNI-T UT372 Tachometer

# system & software requirement
Ubuntu 18.04

Ros melodic

sigrok: https://sigrok.org/wiki/Main_Page Specifically, you need to run sudo apt install libsigrok.

Sigrok implemented a driver for this specific tachometer. This node calls its commandline tool sigrok-cli to get the measurement.
TO run the node: rosrun tachometer tachometer_node.py

This could get a update rate of 4 Hz.

To operate the tachometer, turn on the tachometer, connect it to the laptop using the usb cable. Long press the R/C to enter setup mode. Set usb mode to 1. Aslo ensure that the tachometer is at RPM mode.

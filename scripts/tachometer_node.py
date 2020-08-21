#!/usr/bin/env python
'''
This script reads measurements from Uni-T UT372 tachometer and publish it as ros topic.
It requires sigrok to be installed: "https://sigrok.org/wiki/Main_Page", which implemented a driver
for the tachometer. This node calls the commandline tool sigrok-cli to get the measurement.
Author: Weixuan Zhang (wzhang@ethz.ch) 2020
'''


import rospy
from std_msgs.msg import String
from tachometer.msg import TachometerReading
import subprocess 
def get_tachometer_reading():
	rospy.init_node('tachometer_node', anonymous=True)
	pub = rospy.Publisher('tachometer_reading', TachometerReading)
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		results = subprocess.Popen(["sigrok-cli","--driver=uni-t-ut372:conn=1a86.e008", "--samples=1"], stdout=subprocess.PIPE)
		out, err = results.communicate()
		rpm_number = float(out.split(' ')[1])
		msg = TachometerReading()
		msg.header.stamp = rospy.Time.now()
		msg.reading = rpm_number
		pub.publish(msg)
		print('rpm_number ', rpm_number)
		print('time_stamp ', msg.header.stamp)
		rate.sleep()


if __name__ == '__main__':
	try:
		get_tachometer_reading()
	except rospy.ROSInterruptException:
		pass

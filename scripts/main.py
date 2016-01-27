#!/usr/bin/env python

import rospy as rp
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist as Twi
import math

rp.init_node('main')

velPub = rp.Publisher('turtle1/cmd_vel', Twi, queue_size=1)
velSum = Twi()
direction = 0


while not rp.is_shutdown():
	velPar = Twi()
	commnad = raw_input('0:strait, 1:right, 2:left')
	
	if '0' in commnad:
		velPar.linear.x = 1.0
		velPub.publish(velPar)
			

	if '1' in commnad:
		for angle in range(360):
			velPar.angular.z = 90 * math.pi / 180
			velPar.linear.x = 1.0
			velPub.publish(velPar)

	if '2' in commnad:
		for angle in range(360):
			velPar.angular.z = -90 * math.pi / 180
			velPar.linear.x = 1.0
			velPub.publish(velPar)

	

	print(velPar)
	velSum.linear.x += velPar.linear.x
	velSum.linear.y += velPar.linear.y
	velSum.linear.x += velPar.linear.z
	print(velSum)
	rp.sleep(1)


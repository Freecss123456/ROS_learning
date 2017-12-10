#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import rospy
import json
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from get_msgs.msg import acc_odom
ser = serial.Serial(port='/dev/ttyUSB0',baudrate=115200,timeout=1)

def callback(data):
    #rospy.loginfo("twist:"+str(data))
    ser.write(str(data)+'\r')
    

def my_serial():
    rospy.init_node("serial_node")
    rospy.Subscriber('cmd_vel_mux/input/teleop', Twist, callback,queue_size=10)
    read_pub=rospy.Publisher('odom_data', acc_odom, queue_size=10)
    
    if(ser.isOpen()):
        rospy.loginfo('Serial Port initialized')
    else:
        return -1
    result=acc_odom()
    rate=rospy.Rate(10)   
    while not rospy.is_shutdown():
        ser_get=ser.readline()		
        #print ser_get
	if ser_get:
            json_get=json.loads(ser_get)
            #print json_get
	    result.right=float(json_get[u'right'])
            print result.right
	    result.left=float(json_get[u'left'])
            read_pub.publish(result)
        rate.sleep()
    rospy.spin()
if __name__ == '__main__':
    my_serial()       
ser.close()

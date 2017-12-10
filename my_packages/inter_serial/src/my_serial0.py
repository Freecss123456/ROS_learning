#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

ser = serial.Serial(port='/dev/ttyUSB0',baudrate=115200,timeout=1)

def callback(data):
    #rospy.loginfo("twist:"+str(data))
    ser.write(str(data)+'\r')
    

def my_serial():
    rospy.init_node("serial_node")
    rospy.Subscriber('cmd_vel_mux/input/teleop', Twist, callback,queue_size=10)
    read_pub=rospy.Publisher('odom_data', String, queue_size=10)
    result=String()
    
    if(ser.isOpen()):
        rospy.loginfo('Serial Port initialized')
    else:
        return -1
    
    rate=rospy.Rate(10)   
    while not rospy.is_shutdown():
        result.data=ser.read()
        read_pub.publish(result)
        rate.sleep()
    rospy.spin()
if __name__ == '__main__':
    my_serial()       
ser.close()

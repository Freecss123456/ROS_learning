#include <ros/ros.h> 
#include <serial/serial.h>   
#include <std_msgs/String.h> 
#include <std_msgs/Empty.h> 
#include <geometry_msgs/Twist.h>
serial::Serial ser;  

//callback
void write_callback(const geometry_msgs::Twist::ConstPtr& msg)//(const std_msgs::String::ConstPtr& msg)
{
	ROS_INFO_STREAM("Writing to serial port" << msg->linear);
	//ser.write(msg->linear);  
}

int main(int argc, char** argv)
{
	
	ros::init(argc, argv, "serial_node");	
	ros::NodeHandle nh;
	 
	ros::Subscriber write_sub = nh.subscribe("cmd_vel_mux/input/teleop", 10, write_callback);
	
	ros::Publisher read_pub = nh.advertise<std_msgs::String>("odom_data", 10);

	try
	{
		ser.setPort("/dev/ttyUSB0");
		ser.setBaudrate(115200);
		serial::Timeout to = serial::Timeout::simpleTimeout(1000);
		ser.setTimeout(to);
		ser.open();
	}
	catch (serial::IOException& e)
	{
		ROS_ERROR_STREAM("Unable to open port ");
		return -1;
	}
 
	if (ser.isOpen())
	{
		ROS_INFO_STREAM("Serial Port initialized");
	}
	else
	{
		return -1;
	}

	ros::Rate loop_rate(10);
	while (ros::ok())
	{

		if (ser.available()) {
			ROS_INFO_STREAM("Reading from serial port\n");
			std_msgs::String result;
			result.data = ser.read(ser.available());
			ROS_INFO_STREAM("Read: " << result.data);
			read_pub.publish(result);
		}
	
		ros::spinOnce();
		loop_rate.sleep();

	}
}

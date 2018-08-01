#*****ROS文件系统*****# \
rospack find roscpp \
roscd roscpp  \
roscd log \
rosls roscpp_tutorials  \
rospack depends1 rospy  \
echo $ROS_PACKAGE_PATH  

#*****创建ROS程序包*****# \
cd ~/catkin_ws/src  \
catkin_create_pkg beginner_tutorials std_msgs rospy roscpp  \
rospack depends1 beginner_tutorials 

roscd beginner_tutorials  \
cat package.xml 

rospack depends1 rospy  

#*****编译ROS程序包*****#   
//在catkin工作空间下  \
$ catkin_make [make_targets] [-DCMAKE_VARIABLES=...]  \
//rebuilding 单一的 catkin Package \
$ cd ~/catkin_ws  \
$ catkin_make –pkg package-name 

参考：http://blog.csdn.net/baidu_18189515/article/details/52401329

#*****日志文件*****#   
查询当前的run_id \
rosparam get /run_id \

查看当前账户中被ROS日志消耗的硬盘空间 \
rosclean check \

删除所有已经存在的日志 \
rosclean purge \

通过图形界面设置日志级别 \
rqt_logger_level

#*****计算图源*****#  
Export ROS_NAMESPACE=default-namespace

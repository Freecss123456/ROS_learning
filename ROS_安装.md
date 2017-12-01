1 首先打开软件和更新对话框,
打开后按照下图进行配置（确保你的"restricted"， "universe，" 和 "multiverse."前是打上勾的）

2 
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

3 设置秘钥:
$ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 0xB01FA116

4 安装 ROS
首先确保系统软件处于最新版
$ sudo apt-get update
$ sudo apt-get install ros-indigo-desktop-full

5 初始化rosdep（ROS的软件包依赖项）
$ sudo rosdep init
$ rosdep update

6 设置环境变量
$ echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
$ source ~/.bashrc

7 获得rosinstall
$ sudo apt-get install python-rosinstall

8 创建一个catkin_ws工作空间
$ mkdir -p ~/catkin_ws/src/
$ cd ~/catkin_ws/src/
$ catkin_init_workspace

$ cd ~/catkin_ws/
$ catkin_make

$ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc

9 为了确认你的工作空间已经被至于最顶层，确认环境变量ROS_PACKAGE_PATH包含了你所在的目录：
$ echo $ROS_PACKAGE_PATH

10 进入src创建相应包
$ catkin_create_pkg inter_camera std_msgs rospy roscpp





 

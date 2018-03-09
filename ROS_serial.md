#-*-ROS串口-*-
#-*-C++版-*-
通过sudo apt-get install ros-<distro>-serial下载ROS对应版本的工具包
  
  
#-*-python版-*-
通过pip install serial 安装serial模块

需要增加/dev/ttyUSB0读写权限，否则报错：could not open port /dev/ttyUSB0: [Errno 13] Permission denied \
增加权限：$ sudo chmod 666 /dev/ttyUSB0

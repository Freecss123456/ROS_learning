# ROS_learning
配置ROS，实现导航
#-*-树莓派的配置-*-
1、sudo apt-get install xrdp #实现远程桌面
#注意：我用的是镜像raspberrypi，不要配置中文输入，否则会影响远程桌面连接

2、sudo apt-get update #更新软件列表

3、sudo apt-get install python-vlc #安装语音识别模块

4、$sudo pip install --upgrade pip，报错：python-Not uninstalling at /usr/lib/python2.7/dist-packages, owned by OS
原因：ubuntu 的pip 采用的是apt-get install python-pip 方法安装的
更新pip应该
$sudo apt-get autoremove python-pip
$sudo apt-get install python-pip

5、树莓派无法从U盘复制文件，无法删除本地文件，报错：No space left on device
  查看一下系统的磁盘情况： df -h
  解决办法：raspi-config,选择第一项Expand Filesystem，选择ok重启即可
  

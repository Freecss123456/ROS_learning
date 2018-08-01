#*****ubuntu安装gmapping*****# \
apt-get install ros-indigo-slam-gmapping

#*****ubuntu安装cartographer*****# \
参考网址：http://www.cnblogs.com/hitcm/p/5939507.html
一、安装所有依赖项
sudo apt-get install -y google-mock libboost-all-dev  libeigen3-dev libgflags-dev libgoogle-glog-dev liblua5.2-dev libprotobuf-dev  libsuitesparse-dev libwebp-dev ninja-build protobuf-compiler python-sphinx  ros-indigo-tf2-eigen libatlas-base-dev libsuitesparse-dev liblapack-dev

二、首先安装ceres solver，选择的版本是1.11,路径随意
1.     git clone https://github.com/hitcm/ceres-solver-1.11.0.git
2.      cd ceres-solver-1.11.0/build
3.      cmake ..
4.      make –j4 （一般取-j4，同时跑四个进程，取数越大，编译越快，但过大电脑会卡死）
5.      sudo make install

三、然后安装 cartographer,路径随意
1.      git clone https://github.com/hitcm/cartographer.git
2 .     cd cartographer/build 
3.       cmake .. -G Ninja 
4.       ninja 
5.       ninja test 
6.       sudo ninja install 

四、安装cartographer_ros。
谷歌官方提供的安装方法比较繁琐，我对原来的文件进行了少许的修改，核心代码不变，只是修改了编译文件 
下载到catkin_ws下面的src文件夹下面 
git clone https://github.com/hitcm/cartographer_ros.git 
然后到catkin_ws下面运行catkin_make即可。 

五、数据下载测试 
2d数据，大概500M，用迅雷下载
https://storage.googleapis.com/cartographer-public-data/bags/backpack_2d/cartographer_paper_deutsches_museum.bag

3d数据，8G左右，同样用迅雷下载
https://storage.googleapis.com/cartographer-public-data/bags/backpack_3d/cartographer_3d_deutsches_museum.bag
 
然后运行launch文件即可。
roslaunch cartographer_ros demo_backpack_2d.launch bag_filename:=${HOME}/Downloads/cartographer_paper_deutsches_museum.bag
roslaunch cartographer_ros demo_backpack_3d.launch bag_filename:=${HOME}/Downloads/cartographer_3d_deutsches_museum.bag
RViz学习

六、补充
cartographer 算法主要有三个文件夹 
1、cartographer_ros （该文件件里的代码是cartographer 在 ros平台中的接口） 
2、cartographer （核心slam算法） 
3、ceres-solver （google 的开源 优化库）
安装步骤：http://www.jianshu.com/p/9922a51ce38f


#*****使用rplidar和cartographer建图*****# \
参考网址：http://blog.csdn.net/ywj447/article/details/52922487  \
把cartographer_ros—cartographer_ros--configuration_files--revo_lds.lua改一下 \
之后运行: \
roslaunch rplidar_ros rplidar.launch \
roslaunch cartographer_ros demo_revo_lds.launch \
rosrun rviz rviz cartographer_ros/configuration_files/demo_2d.rviz \
在rviz里通过By topic 添加PointCloud2 

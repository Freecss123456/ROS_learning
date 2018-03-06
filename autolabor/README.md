/****************关于autolabor开源模拟机器人的相关笔记******************/ \
官方微信号：机器人干货 \
官方网站：http://autolabor.cn/ 

//源码包介绍 \
1)simulation目录下包括： 

1.1 autolabor_faker.cpp 这个包是获得autolabor小车的位置，以及静态地图中传感器的数据。发布小车的里程计的相关消息。 

1.2 autolabor_description 提供autolabor小车的3D模型。 

1.3 lidar_simulation提供单线激光雷达的模拟数据，这里主要包括雷达模拟数据、雷达模拟静态地图的数据，雷达模拟障碍物的数据。

2)simulation_launch目录主要包括三个launch文件，包括小车地图创建的create_map_simulation.launch、小车自动规划的move_base_simulation.launch以及用键盘或手柄控制模拟小车运动的sim_move_simulation.launch。 

3)move_base_sim 小车自主规划的算法，以及navigation组件，这个主要是基于ROS官网上navigation包加以修改适应模拟器来的。

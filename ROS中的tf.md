参考网址： \
#-*-tf原理与代码解读-*- \
http://blog.csdn.net/hcx25909/article/details/50154225 \
http://blog.csdn.net/hcx25909/article/details/9255001 \
#简单tf变换，将一点从一坐标系变换到另一坐标系 \
http://blog.csdn.net/xuehuafeiwu123/article/details/68060377 

#-*-tf命令-*- \
1、#在当前目录生成描述tf树的pdf文件
    rosrun tf view_frames
  #查看创建的pdf
   evince frames.pdf

2、#在rqt中显示tf树
    rosrun rqt_tf_tree rqt_tf_tree
   或 rqt & +回车+TAB
    
3、#输出B 相对于 A 的坐标
    rosrun tf tf_echo frameA freameB

4、#打印tf树中的所有参考系信息 \
    rosrun tf tf_monitor [source_frame] [target_target] 如 rosrun tf tf_monitor /base_footprint /odom
    
#-*-tf——API-*- \
static_transform_publisher工具的功能是发布两个参考系之间的静态坐标变换，两个参考系一般不发生相对位置变化。 \
命令的格式如下： \
    static_transform_publisher x y z yaw pitch roll frame_id child_frame_id period_in_ms \
    static_transform_publisher x y z qx qy qz qw frame_id child_frame_id  period_in_ms 
    
#-*-ROS中map,odom,base_link,base_laser 坐标系的理解-*- \
map:\
    地图坐标系，一般设该坐标系为固定坐标系（fixed frame），与机器人所在的世界坐标系一致。 \
base_link:\
    机器人本体坐标系，与机器人中心重合，有些机器人中(PR 2)是base_footprint,其实是一个意思。 \
odom：\
    里程计坐标系，这里要区分开odom topic，这是两个概念，一个是坐标系，一个是根据编码器（或者视觉等）计算的里程计。但是两者也有关系，odom topic 转化得位姿矩阵是odom-->base_link的tf关系。这时可有会有疑问，odom和map坐标系是不是重合的？可以很肯定的告诉你，机器人运动开始是重合的。但是，随着时间的推移是不重合的，而出现的偏差就是里程计的累积误差。那map-->odom的tf怎么得到?就是在一些校正传感器合作校正的package比如gmapping会给出一个位置估计（localization），这可以得到map-->base_link的tf，所以估计位置和里程计位置的偏差也就是odom与map的坐标系偏差。所以，如果你的odom计算没有错误，那么map-->odom的tf就是0。\
base_laser:\
    激光雷达的坐标系，与激光雷达的安装点有关，其与base_link的tf为固定的。

参考网址：
#-*-tf原理与代码解读-*-
http://blog.csdn.net/hcx25909/article/details/50154225
http://blog.csdn.net/hcx25909/article/details/9255001

#-*-tf——API-*-
static_transform_publisher工具的功能是发布两个参考系之间的静态坐标变换，两个参考系一般不发生相对位置变化。
命令的格式如下：
    static_transform_publisher x y z yaw pitch roll frame_id child_frame_id period_in_ms
    static_transform_publisher x y z qx qy qz qw frame_id child_frame_id  period_in_ms

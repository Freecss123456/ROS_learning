参考网址：http://blog.csdn.net/heyijia0327/article/details/42065293
#-*-ROS 教程之 network：多台计算机之间网络通信（以两个终端为例）-*-
1、查看两台电脑各自的ip信息和主机名hostname：
$ifconfig 
$hostname

2、修改/etc文件夹下的hosts文件，实现解析对方主机名：
$sudo gedit /etc/hosts [or $sudo chmod a+w /etc/hosts $vim /etc/hosts]
打开hosts后,在行尾插入[your_ip   your_hostname]
#注意：中间用tab键隔开，不是空格

3、修改完以后，在两台电脑上都输入下列命令重启以下网络：
$sudo /etc/init.d/networking restart

4、选择一个终端作为master,在两个终端上分别输入相同如下指令：
$export ROS_MASTER_URI=http://master_hostname:11311 

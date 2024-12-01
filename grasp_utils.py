import rospy
import time
from geometry_msgs.msg import Twist
import rospy



def move_to_grasp_pose(self):
    pass
    



def move_to_detect_pose(self):
    pass



def move_forward():

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(10) 
    time.sleep(1)
    
    print("forward...")
    move_cmd = Twist()
    # 设置前进速度，单位是m/s
    move_cmd.linear.x = 0.15
    # 计算前进所需时间
    duration = 20
    # 记录开始时间
    start_time = time.time()
    # 发布消息，持续移动直到达到所需的时间
    while time.time() - start_time < duration:
        pub.publish(move_cmd)
        rate.sleep()  # 维持一定频率发布速度命令
    # 发布零速度，停止移动
    print("forword finished")
    move_cmd.linear.x = 0
    pub.publish(move_cmd)

def move_backward():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(10) 
    time.sleep(1)


    move_cmd = Twist()
    # 设置前进速度，单位是m/s
    move_cmd.linear.x = -0.12
    # 计算前进所需时间
    duration = 20


    print("backward...")
    

    start_time = time.time()
    while time.time() - start_time < duration+2:
        pub.publish(move_cmd)
        rate.sleep()  # 维持一定频率发布速度命令

    # 发布零速度，停止移动
    move_cmd.linear.x = 0
    pub.publish(move_cmd)
    

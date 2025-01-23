#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def emg_publisher():
    # ROS 노드 초기화
    rospy.init_node('emg_publisher', anonymous=True)
    
    # 퍼블리셔 생성
    pub = rospy.Publisher('emg_msg', Int32, queue_size=10)
    
    # 루프 속도 설정 (10Hz)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        try:
            # 사용자 입력 받기
            user_input = input("Enter 0 or 1 to publish (1 to start): ")
            
            # 0 또는 1인지 확인
            if user_input in ['0', '1']:
                message = Int32()
                message.data = int(user_input)
                
                # 메시지 퍼블리시
                pub.publish(message)
                rospy.loginfo(f"Published: {message.data}")
            else:
                rospy.logwarn("Invalid input. Please enter 0 or 1.")
        except Exception as e:
            rospy.logerr(f"An error occurred: {e}")

        # 루프 대기
        rate.sleep()

if __name__ == '__main__':
    try:
        emg_publisher()
    except rospy.ROSInterruptException:
        pass


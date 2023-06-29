#! /usr/bin/env python
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def callback(data):
    bridge = CvBridge()
    try:
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
        cv2.imshow("Image window", cv_image)
        cv2.waitKey(1)
    except CvBridgeError as e:
        print(e)

if __name__ == '__main__':
    rospy.init_node('image_converter', anonymous=True)
    rospy.Subscriber("bridge/image_filtered", Image, callback, queue_size=1)
    rospy.spin()
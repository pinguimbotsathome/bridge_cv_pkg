#! /usr/bin/env python
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def image_callback(data):
    filtered_image_pub = rospy.Publisher("bridge/image_filtered", Image, queue_size=1)

    bridge = CvBridge()
    try:
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
        blurred_image = cv2.Canny(cv_image,100,200)
        filtered_image_msg = bridge.cv2_to_imgmsg(blurred_image, "mono8")
        filtered_image_pub.publish(filtered_image_msg)
        
    except CvBridgeError as e:
        print(e)


rospy.init_node('image_filter_node', anonymous=True)

bridge = CvBridge()
filtered_image_msg = None
rospy.Subscriber("camera/rgb/image_raw", Image, image_callback,queue_size=1)


rospy.spin()

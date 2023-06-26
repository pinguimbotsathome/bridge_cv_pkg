#! /usr/bin/env python
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def image_callback(data):
    bridge = CvBridge()
    try:
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
        blurred_image = cv2.blur(cv_image, (5, 5))
        filtered_image_msg = bridge.cv2_to_imgmsg(blurred_image, "bgr8")
        filtered_image_pub.publish(filtered_image_msg)
        cv2.imshow("Image window", blurred_image)
        cv2.waitKey(1)
        
    except CvBridgeError as e:
        print(e)

if __name__ == '__main__':
    rospy.init_node('image_filter_node', anonymous=True)
    
    bridge = CvBridge()
    filtered_image_pub = rospy.Publisher("camera/rgb/image_filtered", Image, queue_size=1)
    rospy.Subscriber("camera/rgb/image_raw", Image, image_callback, queue_size=1)
    
    rospy.spin()

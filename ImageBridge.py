#!/usr/bin/env python
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

if __name__ == "__main__":
	cv_image = cv2.imread("cat.jpg")
	bridge = CvBridge()
	imgmsg = bridge.cv2_to_imgmsg(cv_image, "bgr8")
	cv_image2 = bridge.imgmsg_to_csv2(imgmsg, "bgr8")
	cv2.imshow("Image window", cv_image2)
	cv2.waitKey(0)
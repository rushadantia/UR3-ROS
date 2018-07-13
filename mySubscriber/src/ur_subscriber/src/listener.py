#!/usr/bin/env python
import rospy
from geometry_msgs.msg import WrenchStamped, TransformStamped
import tf2_msgs.msg

def eth_callback(msg):
	rospy.loginfo("%u Fx:%.2f Fy:%.2f Fz:%.2f Tx:%.2f Ty:%.2f Tz:%.2f \r\n", msg.header.seq, msg.wrench.force.x, msg.wrench.force.y, msg.wrench.force.z, msg.wrench.torque.x, msg.wrench.torque.y, msg.wrench.torque.z)

def ur_callback(msg):
	for t in msg.transforms:
		rospy.loginfo("X:%.2f  Y:%.2f  Z:%.2f Rx:%.2f Ry:%.2f Rz:%.2f \r\n", t.transform.translation.x, t.transform.translation.y,  t.transform.translation.z, t.transform.rotation.x, t.transform.rotation.y, t.transform.rotation.z)

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber('ethdaq_data', WrenchStamped , eth_callback)
	rospy.Subscriber('tf', tf2_msgs.msg.TFMessage, ur_callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
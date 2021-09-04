#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def function(msg):
    
    veri = str(msg)

    if veri[7] == 'A' and veri[32] == 'B':
    
        rospy.loginfo("position_robotic_arm: ")
        
        anaveri = veri[8:32]

        grup1 = anaveri[:4]
        grup2 = anaveri[4:8]
        grup3 = anaveri[8:12]
        grup4 = anaveri[12:16]
        grup5 = anaveri[16:20]
        grup6 = anaveri[20:]

        if int(grup1[1:]) > 255:
            grup1 = grup1[:1] + '255'
        if int(grup2[1:]) > 255:
            grup2 = grup2[:1] + '255'
        if int(grup3[1:]) > 255:
            grup3 = grup3[:1] + '255'
        if int(grup4[1:]) > 255:
            grup4 = grup4[:1] + '255'
        if int(grup5[1:]) > 255:
            grup5 = grup5[:1] + '255'
        if int(grup6[1:]) > 255:
            grup6 = grup6[:1] + '255'
        
            
        if int(grup1) > 999 :
            grup1 = "+" + grup1[1:]
        else:
            grup1 = "-" + grup1[1:]
        if int(grup2) > 999 :
            grup2 = "+" + grup2[1:]
        else:
            grup2 = "-" + grup2[1:]
        if int(grup3) > 999 :
            grup3 = "+" + grup3[1:]
        else:
            grup3 = "-" + grup3[1:]
        if int(grup4) > 999 :
            grup4 = "+" + grup4[1:]
        else:
            grup4 = "-" + grup4[1:]
        if int(grup5) > 999 :
            grup5 = "+" + grup5[1:]
        else:
            grup5 = "-" + grup5[1:]
        if int(grup6) > 999 :
            grup6 = "+" + grup6[1:]
        else:
            grup6 = "-" + grup6[1:]

            
        islenmis_robotic_arm_veri = grup1 + " " + grup2 + " " + grup3 + " " + grup4 + " " + grup5 + " " + grup6
        rospy.loginfo(msg)
        print(islenmis_robotic_arm_veri)

        publisher.publish(islenmis_robotic_arm_veri)
        


rospy.init_node('encoder_sub2_node',anonymous=True)
sub = rospy.Subscriber("/serial/robotic_arm",String,function)
publisher = rospy.Publisher("/position_robotic_arm",String,queue_size=10)

rospy.spin()

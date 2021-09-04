#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

#roslaunch komutu hata verdi, bu yüzden roslaunch kullanamadım

# veri almak için fonksiyon yazilir
def function(msg):
    
    # alinan mesaj islenebilmesi için veri değişkenine atanir
    veri = str(msg)

    # terminalden gorulebilecegi gibi alinan veri "data: "alinan veri""" kalibi ile gelir
    # bize ulasan verinin ilk elemani 7. sirada son elemani 24.siradadir. 
    if veri[7] == 'A' and veri[24] == 'B':

        #terminale yazdirma komutu
        rospy.loginfo("position_drive: ")

        
        # data: "AsayilarB" seklinde gelen verinin data:"A B" kismindan kurtulma:
        anaveri = veri[8:24]

        # eldeki 16 sayıyı 4'lu gruplara ayirma:
        grup1 = anaveri[:4]
        grup2 = anaveri[4:8]
        grup3 = anaveri[8:12]
        grup4 = anaveri[12:]

        # 4 elemanlı grupların son 3 elemanlarının 255'i asan degerlerini 255'e cekme :
        if int(grup1[1:]) > 255:
            grup1 = grup1[:1] + '255'
        if int(grup2[1:]) > 255:
            grup2 = grup2[:1] + '255'
        if int(grup3[1:]) > 255:
            grup3 = grup3[:1] + '255'
        if int(grup4[1:]) > 255:
            grup4 = grup4[:1] + '255'

        # pozitif-negatif degerini belirlemek için grup 4 basamakli sayi olarak degerlendirilir:
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

        # 4'lu gruplari birlestirme:    
        islenmis_drive_veri = grup1 + " " + grup2 + " " + grup3 + " " + grup4
        # terminale alinan veiriyi yazdirma:
        rospy.loginfo(msg)
        # islenen verinin son halini terminale yazdirma:
        print(islenmis_drive_veri)

        publisher.publish(islenmis_drive_veri)
        

# node olusturma:
rospy.init_node('encoder_sub1_node',anonymous=True)
# topic olusturma:
sub = rospy.Subscriber("/serial/drive",String,function)
publisher = rospy.Publisher("position/drive",String,queue_size=10)

# kapatilana kadar calismasi icin:
rospy.spin()

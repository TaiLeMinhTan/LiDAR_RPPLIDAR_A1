# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:47:35 2019

@author: LeTai-FCU
"""
#!/usr/bin/env python3
#gksudo kate /usr/local/lib/python3.5/dist-packages/rplidar.py

from rplidar import RPLidar
import time

lidar = RPLidar('/dev/ttyUSB1')
info = lidar.get_info()
print(info)
health = lidar.get_health()
print(health)

def GetDataScanLiDAR():
    #Get Data Scan LiDAR function 
    oldTime = None
    dataSpeed = []
    #scan2 = []

    try:
        #List of Scan Data 
        # This FOR help get every emlement in Big Scaned Data
        #String valueScan (quality, angle, distance)
        for i, scan in enumerate(lidar.iter_scans()):# Scan list of (quality, angle, distance)
            #print('%d: Got %d measurments' % (i, len(scan))) 
            #len(scan) help me get data everytime scan.
            now = time.time()
            if oldTime is None:
                oldTime = now
                continue
            #Time for every scan
            deltaTime = now - oldTime
            #print(deltaTime)
            #print('%.2f Hz, %.2f RPM' % (1/deltaTime, 60/deltaTime))
            dataSpeed.append(deltaTime)
            oldTime = now
            for valueScan in scan:
                #Split data in scan list 
                strInValueScan = valueScan
                #Convert List to String 3 data 
                valueQuality = strInValueScan[0]
                valueAngle = strInValueScan[1]
                valueDistance = strInValueScan[2]  
                #print('Quality: ', valueQuality)
                print('Angle: ', valueAngle)
                print('Distance: ', valueDistance)
                #print('-------------------------------------------------------------')
                #scan2.append((valueAngle,valueDistance))
            #print(scan)
    except KeyboardInterrupt:
        # Press Ctrl + C to STOP
        print('Stop')
        lidar.stop()
        lidar.stop_motor()
        lidar.disconnect()
        deltaTime = sum(dataSpeed)/len(dataSpeed)
        print('Average: %.2f Hz, %.2f RPM' % (1/deltaTime, 60/deltaTime))
def Check



if __name__ == '__main__':
    GetDataScanLiDAR()
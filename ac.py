from ac_class import AirCondition
import os
import sys
import json



print("Welcome to AC controller through WiFi")
print("This script supports ac units that  are already supported by TFIAC application")
useSettings = False
if os.path.isfile('./settings.json') == True:
    x = open('settings.json','r')
    print ("Following settings have been found")
    setting = open("settings.json", "r")
    settings = json.load(x)
    ip2 = str((settings['info']['IP']))
    port2 = int((settings['info']['PORT']))
    print ("IP address: ", ip2)
    print ("Port: ", port2)
    while True:
        x = str(input("Do you want to use this settings? [Y/n]"))
        if (x=="Y" ) or (x=="y" ):
            useSettings = True
            break
        elif (x =="N") or (x =="n"):
            useSettings = False
            break
if useSettings == False:
    
    ip = str(input("Please enter the AC's IP address: "))
    port = int (input("Please enter the AC's UDP port  [ex. 7777]"))

    while True:
        save = str(input("Do you want to save settings? [Y/N] \n"))
        if (save =="Y") or (save =="y"):
            settings =  {}
            settings['info'] ={
                'IP' : ip,
                'PORT': port
            }
            with open('settings.json','w') as x :
                json.dump(settings,x)
            break
        elif (save =="N") or (save =="n"):
            
            break
else:
    #settings = open("settings.txt","r")
    ip =  ip2
    port = port2

ac = AirCondition(ip,port)
print ("========= Please choose a function from the menu =========")
    print ("[0] Exit ")
    print("[1] Turn ON AC")
    print ("[2] Turn OFF AC")
    print ("[3] Adjust Temperature")
    #print ("[4] Change wind direction")
while True:
    try:
            z = input("Please select: ")
            break
        except NameError:
            print ("Error. Please input only numbers")
        except:
            print ('Error')
    if z == 0:
        
        break
    elif (z ==1):
        ac.TurnOn()
    elif (z ==2):
        ac.TurnOff
    elif(z ==3):
        ac.setTemp()
    else:
        print ("Error.Please choose from 0 - 3")
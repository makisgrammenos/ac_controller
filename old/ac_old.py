import socket
import os
import sys
import json

def log(IP,MSG,PORT):
    file_save = open('log.json','w')
    log_output = {}
    log_output['Activity'] = {
        'IP Address': IP,
        'PORT':  PORT,
        'COMMAND':MSG
    }
    with open('log.json','w') as x:
        json.dump(log_output,x)
def broadcast(IP,PORT,MSG):
    
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(MSG,(IP,PORT))
def turnOn(IP,PORT):
    MSG = '<msg msgid="SetMessage" type="Control" seq="1"><SetMessage><TurnOn>on</TurnOn></SetMessage></msg>'
    broadcast(IP,PORT,MSG) 
    log(IP,MSG,PORT)   
def turnOff(IP,PORT):
    MSG = '<msg msgid="SetMessage" type="Control" seq="12345"><SetMessage><TurnOn>off</TurnOn></SetMessage></msg>'
    broadcast(IP,PORT,MSG)
#def lowTemp(IP,PORT):
#    MSG = '<msg msgid="SetMessage" type="Control" seq="1"><SetMessage><SetTemp>74</SetTemp></SetMessage></msg'
def setTemp(IP,PORT):
    temp = CtoF() # convert Celsius degrees to F degrees
    if temp ==0:
        return None
    MSG ='<msg msgid="SetMessage" type="Control" seq="12345"><SetMessage><SetTemp>{}</SetTemp></SetMessage></msg>'.format(str(temp))
    broadcast(IP,PORT,MSG)
def setWindirection(IP,PORT):
    print "Please select WindSpeed"
    print "[1] Low"
    print "[2] Medium"
    print "[3] High"
    print "To return to main menu  press [0]"
    while True:
        try:
            speed = input("Select [1-3]: ")
        except NameError:
            print "Error"
        if speed == 0 :
            return None
        if (speed>=1) and (speed<=3):
            if speed == 1:
                speed = 'Low'
                break
            elif speed == 2:
                speed = 'Medium'
                break
            else:
                speed = 'High'
                break
        else:
            print "Allowed values from 1-3"
        
    MSG = '<msg msgid="SetMessage" type="Control" seq="12345"><SetMessage><WindSpeed>{}</WindSpeed></SetMessage></msg>'.format(str(speed))
    broadcast(IP,PORT,MSG)

#convert Celsius to Fahrenheit
def CtoF():
    while True:
        try:
            print "To return to main menu pres [0]"
            temp_x = input('Select Temperature (16 - 31 C): ')
            if temp_x == 0:
                return 0
            if (temp_x>=16) and (temp_x<=31):
                break 
            else:
                print "Allowed temperatures from 16C to 31C"
        except NameError:
            print "Error.Please make sure you typed only numbers"
    tempF = [61,63,65,66,68,70,72,74,76,78,80,81,83,84,86,88]
    tempC =[]
    for i in range(0,16):
        tempC.append(16+i)
    

    temp = tempF[tempC.index(temp_x)]
    return temp
def SetMode(IP,PORT):
    while True:
        try:
            print "To return to main menu press [0]"
            select = input('Select mode \n [1] Cool \n [2] Heat\n [3] Fan')
            if select ==  1 :
                mode = 'cool'
            elif select == 2 :
               mode = 'heat'
            elif select == 3 :
                mode = 'fan'
            else :
                NameError
            #MSG = '<msg msgid="SetMessage" type="Control" seq="1355"><SetMessage><BaseMode>{}</BaseMode></SetMessage></msg>'.format(str(mode))
            #broadcast(IP,PORT,MSG)
            #break
        except NameError:
            print "Error .Allowed inputs [1-3]"  


# main code
print "Welcome to Morric AC controler "
useSettings = False
if os.path.isfile('./settings.json') == True:
    x = open('settings.json','r')
    print "Following settings have been found"
    setting = open("settings.json", "r")
    settings = json.load(x)
    ip2 = str((settings['info']['IP']))
    port2 = int((settings['info']['PORT']))
    print "IP address: ", ip2
    print "Port: ", port2
    while True:
        x = raw_input("Do you want to use this settings? [Y/n]")
        if (x=="Y" ) or (x=="y" ):
            useSettings = True
            break
        elif (x =="N") or (x =="n"):
            useSettings = False
            break
if useSettings == False:
    
    IP = raw_input("Please enter the AC's IP address: ")
    PORT = input("Please enter the AC's UDP port ")

    while True:
        save = raw_input("Do you want to save settings? [Y/N] \n")
        if (save =="Y") or (save =="y"):
            settings =  {}
            settings['info'] ={
                'IP' : IP,
                'PORT': PORT
            }
            with open('settings.json','w') as x :
                json.dump(settings,x)
            break
        elif (save =="N") or (save =="n"):
            
            break
else:
    #settings = open("settings.txt","r")
    IP =  ip2
    PORT = port2
while True:
    
    print "========= Please choose a function from the menu ========="
    print "[0] Exit "
    print "[1] Turn ON AC"
    print "[2] Turn OFF AC"
    print "[3] Adjust Temperature"
    print "[4] Change wind direction"
    while True:
        try:
            x = input("Please select: ")
            break
        except NameError:
            print "Error. Please input only numbers"
        except:
            print 'Error'
    if x == 1:
        turnOn(IP,PORT)
    elif x ==2:
        turnOff(IP,PORT)
    elif x == 3 :
        setTemp(IP,PORT)
    elif x == 0:
        sys.exit()
    elif x ==4:
        setWindirection(IP,PORT)
    elif x == 5 :
        SetMode(IP,PORT)  
    else:
        print "Error.Please choose from 0 - 3"

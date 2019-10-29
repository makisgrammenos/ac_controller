import socket
import os
import sys

def broadcast(IP,PORT,MSG):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(MSG,(IP,PORT))
def turnOn(IP,PORT):
    MSG = '<msg msgid="SetMessage" type="Control" seq="1"><SetMessage><TurnOn>on</TurnOn></SetMessage></msg>'
    broadcast(IP,PORT,MSG)
    
def turnOff(IP,PORT):
    MSG = '<msg msgid="SetMessage" type="Control" seq="12345"><SetMessage><TurnOn>off</TurnOn></SetMessage></msg>'
    broadcast(IP,PORT,MSG)
#def lowTemp(IP,PORT):
#    MSG = '<msg msgid="SetMessage" type="Control" seq="1"><SetMessage><SetTemp>74</SetTemp></SetMessage></msg'
def setTemp(IP,PORT):
    temp = CtoF() # convert Celsius degrees to F degrees
    MSG ='<msg msgid="SetMessage" type="Control" seq="12345"><SetMessage><SetTemp>{}</SetTemp></SetMessage></msg>'.format(str(temp))
    broadcast(IP,PORT,MSG)

#convert Celsius to Fahrenheit
def CtoF():
    while True:
        try:
            temp_x = input('Select Temperature (16 - 31 C): ')
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







# main code
print "Welcome to Morric AC controler "
useSettings = False
if os.path.isfile('./settings.txt') == True:
    print "Following settings have been found"
    settings = open("settings.txt", "r")
    print "IP address: ", settings.readline()
    print "Port: ", settings.readline()
    settings = settings.close()
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
            settings = open("settings.txt","w+")
            settings.write(IP)
            settings.write('\n')
            settings.write(str(PORT))
            settings.close()
            
            break
        elif (save =="N") or (save =="n"):
            
            break
else:
    settings = open("settings.txt","r")
    IP = settings.readline()
    PORT = int(settings.readline())
while True:
    
    print "========= Please choose a function from the menu ========="
    print "[0] Exit "
    print "[1] Turn ON AC"
    print "[2] Turn OFF AC"
    print "[3] Adjust Temperature"
    while True:
        try:
            x = input("Please select: ")
            break
        except NameError:
            print "Error. Please input only numbers"
    if x == 1:
        turnOn(IP,PORT)
    elif x ==2:
        turnOff(IP,PORT)
    elif x == 3 :
        setTemp(IP,PORT)
    elif x == 0:
        sys.exit()  
    else:
        print "Error.Please choose from 0 - 3"

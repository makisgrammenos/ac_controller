import socket
import os

def turnOn(IP,PORT):
    MSG = '<msg msgid="SetMessage" type="Control" seq="1"><SetMessage><TurnOn>on</TurnOn></SetMessage></msg>'



    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(MSG,(IP,PORT))
def turnOff(IP,PORT):
    MSG = '<msg msgid="SetMessage" type="Control" seq="12345"><SetMessage><TurnOn>off</TurnOn></SetMessage></msg>'



    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(MSG,(IP,PORT))

print "Welcome to Morric AC controler"
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
    print "[1] Turn ON AC"
    print "[2] Turn OFF AC"
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
    elif x == 0:
        break   
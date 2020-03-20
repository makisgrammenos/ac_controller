import socket


class AirCondition:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        
    
    def broadcast(ip,port,msg):
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        #sock.sendto(msg,(ip,port))
        sock.sendto(msg.encode(),(ip, port))
    def TurnOn(self):
        msg = '<msg msgid="SetMessage" type="Control" seq="1"><SetMessage><TurnOn>on</TurnOn></SetMessage></msg>'
        AirCondition.broadcast(self.ip,self.port,msg)
    def TurnOff(self):
        msg = '<msg msgid="SetMessage" type="Control" seq="12345"><SetMessage><TurnOn>off</TurnOn></SetMessage></msg>'
        AirCondition.broadcast(self.ip,self.port,msg)
    #convert Celsius to Fahrenheit
    def CtoF(self):
        while True:
            try:
                print ("To return to main menu pres [0]")
                temp_x = int(input('Select Temperature (16 - 31 C): '))
                if temp_x == 0:
                    return 0
                if (temp_x>=16) and (temp_x<=31):
                    break 
                else:
                    print ("Allowed temperatures from 16C to 31C")
            except NameError:
                print ("Error.Please make sure you typed only numbers")
        tempF = [61,63,65,66,68,70,72,74,76,78,80,81,83,84,86,88]
        tempC =[]
        for i in range(0,16):
            tempC.append(16+i)
        

        temp = tempF[tempC.index(temp_x)]
        return temp

    def setTemp(self):
        temp = self.CtoF() # convert Celsius degrees to F degrees
        if temp ==0:
            return None
        
        msg ='<msg msgid="SetMessage" type="Control" seq="12345"><SetMessage><SetTemp>{}</SetTemp></SetMessage></msg>'.format(str(temp))
        AirCondition.broadcast(self.ip,self.port,msg)
    def setWindirection(self):
        print ("Please select WindSpeed")
        print ("[1] Low")
        print( "[2] Medium")
        print ("[3] High")
        print ("To return to main menu  press [0]")
        while True:
            try:
                speed = int(input("Select [1-3]: "))
            except NameError:
                print ("Error")
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
                print ("Allowed values from 1-3")
            
        msg = '<msg msgid="SetMessage" type="Control" seq="12345"><SetMessage><WindSpeed>{}</WindSpeed></SetMessage></msg>'.format(str(speed))
        AirCondition.broadcast(self.ip,self.port,msg)
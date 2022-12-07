import os

class Server:
    

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip
        self.ping()

    def ping(self):
       
        print("The Server IP is", self.server_ip)
       
        filepath = os.path.dirname(os.path.abspath(__file__))
       
        os.chdir(filepath)        

        pingresult = "pingResults__.txt"
        pingText = 'ping ' + (self.server_ip) + ' > ' + pingresult         
        print("Command sent to the OS system for the ping is: ", pingText)
        response = os.system(pingText) 
        
        f = open(pingresult, "r")
        if (response == 0):            
            print("Ping Successfull for the server", self.server_ip)            
            print(f.read())
        else:
            print("Check the server - Unsuccessfull ping response for ", self.server_ip)
            print(f.read())

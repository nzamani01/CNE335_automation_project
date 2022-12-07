import os
import paramiko

class Server:
    

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip
        self.ping()

    def ping(self):
        # TODO - Use os module to ping the server
        print("The Server IP is", self.server_ip)

        filepath = os.path.dirname(os.path.abspath(__file__))
        #Set the working directory to the path where the python source code is
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
            


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='172.31.11.187', username='ubuntu', key_filename='/home/ubuntu/.ssh/newkey.pem')

stdin, stdout, stderr = ssh.exec_command('lsb_release -a')

for line in stdout.read().splitlines():
    print(line)

ssh.close()

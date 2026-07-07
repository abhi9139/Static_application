import subprocess
import shutil
import os



def run (cmd):
    subprocess.run(cmd,shell=True, check=True)
    
    
    
if shutil.which("nginx"):
    print("Nginx is installed")    
else:
    command = "sudo-apt-get update && sudo -apt-get install -y nginx "    
    run(command)
    

    
    
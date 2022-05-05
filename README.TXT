This is a simple powershell python script that will help you dump lsass without an GUI access . should be used for CTF's and educational purposes only !
this script uses 2 libraries , subprocess and psutil

Please note ! the script edits the local execution policy " Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force "
to reverse the effect used this command - " Set-ExecutionPolicy Restricted -Scope CurrentUser -Force "
the current policy can be viewed with this command - " Get-ExecutionPolicy "

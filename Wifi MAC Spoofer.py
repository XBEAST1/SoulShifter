import os

print ('''
██     ██ ██ ███████ ██     ███    ███  █████   ██████     ███████ ██████   ██████   ██████  ███████ ███████ ██████  
██     ██ ██ ██      ██     ████  ████ ██   ██ ██          ██      ██   ██ ██    ██ ██    ██ ██      ██      ██   ██ 
██  █  ██ ██ █████   ██     ██ ████ ██ ███████ ██          ███████ ██████  ██    ██ ██    ██ █████   █████   ██████  
██ ███ ██ ██ ██      ██     ██  ██  ██ ██   ██ ██               ██ ██      ██    ██ ██    ██ ██      ██      ██   ██ 
 ███ ███  ██ ██      ██     ██      ██ ██   ██  ██████     ███████ ██       ██████   ██████  ██      ███████ ██   ██ 
                                                                                                                     
                                                                                                                     
''')
iface = input ('Enter Your Interface Name : ')
choice = input ('\nDo You Want To Reset Your MAC Address\n\nYes or No\n\nAnswer : ')
choice = (choice.upper())
if choice == ('YES') or choice == ('Y'):
    os.system (f'ifconfig {iface} down')
    os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
    os.system (f'ifconfig {iface} down')
    os.system (f'ifconfig {iface} down')
    os.system (f'screen -d -m macchanger -p {iface}\n'*100)
    os.system (f'ifconfig {iface} up')
    os.system (f'macchanger -s {iface}')
    exit ()
else:
    pass
macspoof = input ('\nEnter MAC Address That You Want To Spoof : ')
os.system (f'ifconfig {iface} down')
os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
os.system (f'screen -d -m macchanger -m {macspoof} {iface}\n'*100)
os.system (f'ifconfig {iface} up')
os.system ('service NetworkManager restart')
os.system (f'macchanger -s {iface}')

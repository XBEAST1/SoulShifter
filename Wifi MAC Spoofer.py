import os

print ('''
██     ██ ██ ███████ ██     ███    ███  █████   ██████     ███████ ██████   ██████   ██████  ███████ ███████ ██████  
██     ██ ██ ██      ██     ████  ████ ██   ██ ██          ██      ██   ██ ██    ██ ██    ██ ██      ██      ██   ██ 
██  █  ██ ██ █████   ██     ██ ████ ██ ███████ ██          ███████ ██████  ██    ██ ██    ██ █████   █████   ██████  
██ ███ ██ ██ ██      ██     ██  ██  ██ ██   ██ ██               ██ ██      ██    ██ ██    ██ ██      ██      ██   ██ 
 ███ ███  ██ ██      ██     ██      ██ ██   ██  ██████     ███████ ██       ██████   ██████  ██      ███████ ██   ██ 
                                                                                                                     
                                                                                                                     
''')
iface = input ('Enter Your Interface Name : ')
def loop ():
    choices = input ('\n\n1.Reset MAC Address\n\n2.Random MAC Address\n\n3.Specific MAC Address\n\n4.Show Current MAC Address\n\n\nYour Choice : ')
    choice = (choices.upper())
    if choice == ('1') or choice == ('RESET') or choice ==  ('RESETADDRESS') or choice ==  ('RESET ADDRESS') or choice == ('RESET MAC ADDRESS') or choice == ('RESETMACADDRESS'):
        os.system (f'ifconfig {iface} down')
        os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
        os.system (f'ifconfig {iface} down')
        os.system (f'ifconfig {iface} down')
        os.system (f'screen -d -m macchanger -p {iface}\n'*100)
        os.system (f'ifconfig {iface} up')
        print ('\n')
        os.system (f'macchanger -s {iface}')
        exit ()
    elif choice == ('2') or choice == ('RANDOM') or choice == ('RANDOMADDRESS') or choice == ('RANDOM ADDRESS') or choice == ('RANDOM MAC ADDRESS') or choice == ('RANDOMMACADDRESS'):
        os.system (f'ifconfig {iface} down')
        os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
        os.system (f'ifconfig {iface} down')
        os.system (f'ifconfig {iface} down')
        os.system (f'screen -d -m macchanger -r {iface}\n'*100)
        os.system (f'ifconfig {iface} up')
        print ('\n')
        os.system (f'macchanger -s {iface}')
        exit ()
    elif choice == ('3') or choice == ('SPECIFIC') or choice ==  ('SPECIFIC MAC ADDRESS') or choice ==  ('SPECIFICADDRESS') or choice == ('SPECIFIC ADDRESS') or choice == ('SPECIFICMACADDRESS'):
        macspoof = input ('\nEnter MAC Address That You Want To Spoof : ')
        os.system (f'ifconfig {iface} down')
        os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
        os.system (f'screen -d -m macchanger -m {macspoof} {iface}\n'*100)
        os.system (f'ifconfig {iface} up')
        os.system ('service NetworkManager restart')
        print ('\n')
        os.system (f'macchanger -s {iface}')
        exit ()
    elif choice == ('4') or choice == ('SHOW') or choice == ('SHOW CURRENT MAC ADDRESS') or choice == ('SHOWADDRESS') or choice ==  ('SHOW ADDRESS') or choice == ('SHOW MAC ADDRESS') or choice == ('SHOWCURRENTMACADDRESS') or choice == ('SHOWMACADDRESS'):
        print ('\n')
        os.system (f'macchanger -s {iface}')
    else:
        print ('\nPlease Chose Number or Name From Given Options\n')
        loop ()
loop ()

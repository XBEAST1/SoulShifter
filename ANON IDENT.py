import os
import subprocess
import random

print ('''
 ▄▄▄       ███▄    █  ▒█████   ███▄    █     ██▓▓█████▄ ▓█████  ███▄    █ ▄▄▄█████▓
▒████▄     ██ ▀█   █ ▒██▒  ██▒ ██ ▀█   █    ▓██▒▒██▀ ██▌▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒
▒██  ▀█▄  ▓██  ▀█ ██▒▒██░  ██▒▓██  ▀█ ██▒   ▒██▒░██   █▌▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░
░██▄▄▄▄██ ▓██▒  ▐▌██▒▒██   ██░▓██▒  ▐▌██▒   ░██░░▓█▄   ▌▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
 ▓█   ▓██▒▒██░   ▓██░░ ████▓▒░▒██░   ▓██░   ░██░░▒████▓ ░▒████▒▒██░   ▓██░  ▒██▒ ░ 
 ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ░▓   ▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   
  ▒   ▒▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░    ▒ ░ ░ ▒  ▒  ░ ░  ░░ ░░   ░ ▒░    ░    
  ░   ▒      ░   ░ ░ ░ ░ ░ ▒     ░   ░ ░     ▒ ░ ░ ░  ░    ░      ░   ░ ░   ░      
      ░  ░         ░     ░ ░           ░     ░     ░       ░  ░         ░          
                                                 ░                                                                                                                                                   
''')
# Function to retrieve the Wi-Fi adapters available
def get_network_adapters():
    try:
        # Executes the 'ip link show' command and captures the output
        output = subprocess.check_output(['ip', 'link', 'show'], stderr=subprocess.STDOUT, universal_newlines=True)
        # Split the output into lines
        lines = output.split('\n')
        adapters = []

        # Iterate over the lines and find the network adapters
        for line in lines:
            if 'state UP' in line:
                # Extract the adapter name
                adapter = line.split(':')[1].strip()
                adapters.append(adapter)

        return adapters
    except subprocess.CalledProcessError as e:
        # If the command execution fails, print the error
        print(f"Command execution failed with error: {e.output}")

# Retrieve the available network adapters
network_adapters = get_network_adapters()

# If there are network adapters available
if len(network_adapters) > 0:
    print("Available network adapters:\n")
    # Print the list of available adapters with their corresponding numbers
    for index, adapter in enumerate(network_adapters, start=1):
        print(f"{index}. {adapter}")

    while True:
        # Prompt the user to select a network adapter by entering the corresponding number
        selection = input("\nEnter the number corresponding to the network adapter you want to select: \n\nYour Choice: ")

        try:
            selection = int(selection)
            # If the selection is valid, assign the selected adapter to 'iface'
            if selection >= 1 and selection <= len(network_adapters):
                iface = network_adapters[selection - 1]
                print(f"\nSelected network adapter: {iface}")
                break
            else:
                print("\nInvalid selection.\n")
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")
else:
    print("No network adapters found.")

# Function to generate random mac addresses

def generate_random_mac():
    random_mac = [random.choice('0123456789ABCDEF') for _ in range(6)]
    return ':'.join([random_mac[i]+random_mac[i+1] for i in range(0, len(random_mac), 2)])

# Loop to execute script again and again if someone writes wrong number

def main_loop ():

    # Choices to select the options

    choices = input ('\n\n1.Reset MAC Address\n\n2.Random MAC Address\n\n3.Random Vendor MAC Address\n\n4.Specific MAC Address\n\n5.Specific Vendor MAC Address\n\n6.Show Current MAC Address\n\n\n\nYour Choice : ')
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
    elif choice == ('3') or choice == ('RANDOM VENDOR') or choice == ('RANDOMVENDORADDRESS') or choice == ('RANDOM VENDOR ADDRESS') or choice == ('RANDOM VENDOR MAC ADDRESS') or choice == ('RANDOMVENDORMACADDRESS'):
        os.system (f'ifconfig {iface} down')
        os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
        os.system (f'ifconfig {iface} down')
        os.system (f'ifconfig {iface} down')
        os.system (f'screen -d -m macchanger -A {iface}\n'*100)
        os.system (f'ifconfig {iface} up')
        print ('\n')
        os.system (f'macchanger -s {iface}')
        exit ()
    elif choice == ('4') or choice == ('SPECIFIC') or choice ==  ('SPECIFIC MAC ADDRESS') or choice ==  ('SPECIFICADDRESS') or choice == ('SPECIFIC ADDRESS') or choice == ('SPECIFICMACADDRESS'):
        macspoof = input ('\nEnter MAC Address That You Want To Spoof : ')
        os.system (f'ifconfig {iface} down')
        os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
        os.system (f'screen -d -m macchanger -m {macspoof} {iface}\n'*100)
        os.system (f'ifconfig {iface} up')
        os.system ('service NetworkManager restart')
        print ('\n')
        os.system (f'macchanger -s {iface}')
        exit ()
    elif choice == ('5') or choice == ('SPECIFIC VENDOR') or choice ==  ('SPECIFIC VENDOR MAC ADDRESS') or choice ==  ('SPECIFICVENDORADDRESS') or choice == ('SPECIFIC VENDOR ADDRESS') or choice == ('SPECIFICVENDORMACADDRESS'):
        def vendor_category_loop ():
            vendor_choice = input ('\n\n\nSelect Vendor Category\n\n1.PC Vendors\n\n2.Mobile Vendors\n\n\n\nYour Choice: ')
            vendor_choice = (vendor_choice.upper())
            if vendor_choice == ('1') or vendor_choice == ('PC VENDORS'):
                def pc_vendor_loop():
                    global first_digits
                    global last_digits
                    pc_vendor = input ('\n\n\n1.Dell\n\n2.HP\n\n3.Lenovo\n\n4.Asus\n\n5.Acer\n\n6.Intel\n\n7.Toshiba\n\n8.Sony\n\n9.Gateway\n\n10.Gigabyte\n\n11.Msi\n\n12.Asrock\n\n\n\nYour Choice: ')
                    pc_vendor = (pc_vendor.upper())
                    if pc_vendor == ('1') or pc_vendor == ('DELL'):
                        first_digits = ('00:11:43')
                        last_digits = generate_random_mac()
                    elif pc_vendor == ('2') or pc_vendor == ('HP'):
                        first_digits = ('00:04:EA')
                        last_digits = generate_random_mac()
                    elif pc_vendor == ('3') or pc_vendor == ('LENOVO'):
                        first_digits = ('A4:8C:DB')
                        last_digits = generate_random_mac()
                    elif pc_vendor == ('4') or pc_vendor == ('ASUS'):
                        first_digits = ('14:DA:E9')
                        last_digits = generate_random_mac()
                    elif pc_vendor == ('5') or pc_vendor == ('ACER'):
                        first_digits = ('C0:98:79')
                        last_digits = generate_random_mac()
                    elif pc_vendor == ('6') or pc_vendor == ('INTEL'):
                        first_digits = ('00:02:B3')
                        last_digits = generate_random_mac()
                    elif pc_vendor == ('7') or pc_vendor == ('TOSHIBA'):
                        first_digits = ('E8:3A:97')
                        last_digits = generate_random_mac()       
                    elif pc_vendor == ('8') or pc_vendor == ('SONY'):
                        first_digits = ('00:01:4A')
                        last_digits = generate_random_mac()
                    elif pc_vendor == ('9') or pc_vendor == ('GATEWAY'):
                        first_digits = ('00:1D:84')
                        last_digits = generate_random_mac()
                    elif pc_vendor == ('10') or pc_vendor == ('GIGABYTE'):
                        first_digits = ('')
                        last_digits = generate_random_mac()
                    elif pc_vendor == ('11') or pc_vendor == ('MSI'):
                        first_digits = ('00:16:17')
                        last_digits = generate_random_mac()
                    elif pc_vendor == ('12') or pc_vendor == ('ASROCK'):
                        first_digits = ('D0:50:99')
                        last_digits = generate_random_mac()
                    else:
                        print ("\n\nEnter the number corresponding to the given vendors")
                        pc_vendor_loop()
                pc_vendor_loop()

            elif vendor_choice == ('2') or vendor_choice == ('Mobile VENDORS'):

                def mobile_vendor_loop():
                    global first_digits
                    global last_digits
                    mobile_vendor = input ('\n\n\n1.Samsung\n\n2.Iphone\n\n3.Huawei\n\n4.OnePlus\n\n5.Oppo\n\n6.Vivo\n\n7.Motorola\n\n8.Xiaomi\n\n9.Realme\n\n10.Sony\n\n11.HTC\n\n12.Nokia\n\n13.Lenovo\n\n14.LG\n\n\nYour Choice: ')
                    mobile_vendor = (mobile_vendor.upper())
                    if mobile_vendor == ('1') or mobile_vendor == ('SAMSUNG'):
                        first_digits = ('D4:E8:B2')
                        last_digits = generate_random_mac()
                    elif mobile_vendor == ('2') or mobile_vendor == ('IPHONE'):
                        first_digits = ('04:26:65')
                        last_digits = generate_random_mac()
                    elif mobile_vendor == ('3') or mobile_vendor == ('HUAWEI'):
                        first_digits = ('04:9F:CA')
                        last_digits = generate_random_mac()
                    elif mobile_vendor == ('4') or mobile_vendor == ('ONEPLUS'):
                        first_digits = ('94:65:2D')
                        last_digits = generate_random_mac()
                    elif mobile_vendor == ('5') or mobile_vendor == ('OPPO'):
                        first_digits = ('B8:37:65')
                        last_digits = generate_random_mac()
                    elif mobile_vendor == ('6') or mobile_vendor == ('VIVO'):
                        first_digits = ('10:F6:81')
                        last_digits = generate_random_mac()
                    elif mobile_vendor == ('7') or mobile_vendor == ('MOTOROLA'):
                        first_digits = ('14:1A:A3')
                        last_digits = generate_random_mac()
                    elif mobile_vendor == ('8') or mobile_vendor == ('XIAOMI'):
                        first_digits = ('9C:99:A0')
                        last_digits = generate_random_mac()
                    elif mobile_vendor == ('9') or mobile_vendor == ('REALME'):
                        first_digits = ('D0:28:BA')
                        last_digits = generate_random_mac()
                    elif mobile_vendor == ('10') or mobile_vendor == ('SONY'):
                        first_digits = ('00:0E:07')
                        last_digits = generate_random_mac()
                    elif mobile_vendor == ('11') or mobile_vendor == ('HTC'):
                        first_digits = ('D8:B3:77')
                        last_digits = generate_random_mac()
                    elif mobile_vendor == ('12') or mobile_vendor == ('NOKIA'):
                        first_digits = ('14:3E:60')
                        last_digits = generate_random_mac()
                    elif mobile_vendor == ('13') or mobile_vendor == ('LENOVO'):
                        first_digits = ('14:9F:E8')
                        last_digits = generate_random_mac()
                    elif mobile_vendor == ('14') or mobile_vendor == ('LG'):
                        first_digits = ('98:D6:F7')
                        last_digits = generate_random_mac()
                    else:
                        print ("\n\nEnter the number corresponding to the given vendors")
                        mobile_vendor_loop()
                mobile_vendor_loop()
            else:
                print ("\n\nEnter the number corresponding to the given vendor categories")
                vendor_category_loop ()

        vendor_category_loop ()

        os.system (f'ifconfig {iface} down')

        os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
        os.system (f'screen -d -m macchanger -m {first_digits}:{last_digits} {iface}\n'*100)
        os.system (f'ifconfig {iface} up')
        os.system ('service NetworkManager restart')
        print ('\n')
        os.system (f'macchanger -s {iface}')
        exit ()
    elif choice == ('6') or choice == ('SHOW') or choice == ('SHOW CURRENT MAC ADDRESS') or choice == ('SHOWADDRESS') or choice ==  ('SHOW ADDRESS') or choice == ('SHOW MAC ADDRESS') or choice == ('SHOWCURRENTMACADDRESS') or choice == ('SHOWMACADDRESS'):
        print ('\n')
        os.system (f'macchanger -s {iface}')
    else:
        print ('\nPlease Chose Number or Name From Given Options\n')
        main_loop ()
main_loop ()
import os
import subprocess
import random
import time
import argparse
import sys
import tkinter as tk
from tkinter import messagebox
from termcolor import colored

def install_dependencies():
    import os
    import shutil

    def is_installed(binary):
        return shutil.which(binary) is not None

    def has_python_module(module_name):
        try:
            __import__(module_name)
            return True
        except ImportError:
            return False

    # Determine distro
    distro = ""
    if os.path.exists("/etc/os-release"):
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("ID="):
                    distro = line.strip().split("=")[1].strip('"').lower()
                    break

    to_install = []

    # Check required dependencies
    need_tk = not has_python_module("tkinter")
    need_termcolor = not has_python_module("termcolor")
    need_macchanger = not is_installed("macchanger")
    need_screen = not is_installed("screen")

    if distro in ["arch", "manjaro"] and shutil.which("pacman"):
        if need_tk:
            to_install.append("tk")
        if need_termcolor:
            to_install.append("python-termcolor")
        if need_macchanger:
            to_install.append("macchanger")
        if need_screen:
            to_install.append("screen")

        if to_install:
            install_cmd = f"sudo pacman -Sy --noconfirm {' '.join(to_install)}"
            print(f"[INFO] Installing missing packages: {install_cmd}")
            os.system(install_cmd)

    elif distro in ["ubuntu", "debian", "pop", "linuxmint"] and shutil.which("apt"):
        if need_tk:
            to_install.append("python3-tk")
        if need_termcolor:
            to_install.append("python3-termcolor")
        if need_macchanger:
            to_install.append("macchanger")
        if need_screen:
            to_install.append("screen")

        if to_install:
            install_cmd = f"sudo apt update && sudo apt install -y {' '.join(to_install)}"
            print(f"[INFO] Installing missing packages: {install_cmd}")
            os.system(install_cmd)

    elif distro in ["fedora", "rhel", "centos"] and shutil.which("dnf"):
        if need_tk:
            to_install.append("python3-tkinter")
        if need_termcolor:
            to_install.append("python3-termcolor")
        if need_macchanger:
            to_install.append("macchanger")
        if need_screen:
            to_install.append("screen")

        if to_install:
            install_cmd = f"sudo dnf install -y {' '.join(to_install)}"
            print(f"[INFO] Installing missing packages: {install_cmd}")
            os.system(install_cmd)

    elif distro in ["opensuse", "suse", "sles"] and shutil.which("zypper"):
        if need_tk:
            to_install.append("python3-tk")
        if need_termcolor:
            to_install.append("python3-termcolor")
        if need_macchanger:
            to_install.append("macchanger")
        if need_screen:
            to_install.append("screen")

        if to_install:
            install_cmd = f"sudo zypper install -y {' '.join(to_install)}"
            print(f"[INFO] Installing missing packages: {install_cmd}")
            os.system(install_cmd)

    elif distro == "void" and shutil.which("xbps-install"):
        if need_tk:
            to_install.append("python3-tkinter")
        if need_termcolor:
            to_install.append("python3-termcolor")
        if need_macchanger:
            to_install.append("macchanger")
        if need_screen:
            to_install.append("screen")

        if to_install:
            install_cmd = f"sudo xbps-install -y {' '.join(to_install)}"
            print(f"[INFO] Installing missing packages: {install_cmd}")
            os.system(install_cmd)

    else:
        print(f"[WARN] Unsupported distro '{distro}' or missing package manager.")
        print("[INFO] Please install these packages manually if missing:")
        if need_tk:
            print("- tkinter")
        if need_termcolor:
            print("- termcolor")
        if need_macchanger:
            print("- macchanger")
        if need_screen:
            print("- screen")


def run_command_line():
    
    print("\n")
    title = (
        '  ██████  ▒█████   █    ██  ██▓         ██████  ██░ ██  ██▓  █████▒▄▄▄█████▓▓█████  ██▀███  \n'
        '▒██    ▒ ▒██▒  ██▒ ██  ▓██▒▓██▒       ▒██    ▒ ▓██░ ██▒▓██▒▓██   ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒\n'
        '░ ▓██▄   ▒██░  ██▒▓██  ▒██░▒██░       ░ ▓██▄   ▒██▀▀██░▒██▒▒████ ░ ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒\n'
        '  ▒   ██▒▒██   ██░▓▓█  ░██░▒██░         ▒   ██▒░▓█ ░██ ░██░░▓█▒  ░ ░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  \n'
        '▒██████▒▒░ ████▓▒░▒▒█████▓ ░██████▒   ▒██████▒▒░▓█▒░██▓░██░░▒█░      ▒██▒ ░ ░▒████▒░██▓ ▒██▒\n'
        '▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░   ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓   ▒ ░      ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░\n'
        '░ ░▒  ░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░ ▒  ░   ░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░ ░          ░     ░ ░  ░  ░▒ ░ ▒░\n'
        '░  ░  ░  ░ ░ ░ ▒   ░░░ ░ ░   ░ ░      ░  ░  ░   ░  ░░ ░ ▒ ░ ░ ░      ░         ░     ░░   ░ \n'
        '      ░      ░ ░     ░         ░  ░         ░   ░  ░  ░ ░                      ░  ░   ░     \n'
        '                                                                                            \n'
        '                  by XBEAST  ~  Discover the world through a different lens! <3             \n'
        '                                           v6.0                                             \n'
        '                           Github Link: https://github.com/XBEAST1                          \n'
    )

    colored_text = colored(title, 'red')
    print(colored_text)
    
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

        # Reset MAC Address

        if choice == ('1') or choice == ('RESET') or choice ==  ('RESETADDRESS') or choice ==  ('RESET ADDRESS') or choice == ('RESET MAC ADDRESS') or choice == ('RESETMACADDRESS'):
            os.system (f'ifconfig {iface} down')
            time.sleep(1)
            os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
            time.sleep(1)
            os.system (f'screen -d -m macchanger -p {iface}\n'*100)
            time.sleep(1)
            os.system (f'ifconfig {iface} up')
            time.sleep(1)
            os.system ('screen -d -m systemctl restart NetworkManager')
            print ('\n')
            os.system (f'macchanger -s {iface}')
            exit ()

        # Random MAC Address

        elif choice == ('2') or choice == ('RANDOM') or choice == ('RANDOMADDRESS') or choice == ('RANDOM ADDRESS') or choice == ('RANDOM MAC ADDRESS') or choice == ('RANDOMMACADDRESS'):
            os.system (f'ifconfig {iface} down')
            time.sleep(1)
            os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
            time.sleep(1)
            os.system (f'screen -d -m macchanger -r {iface}\n'*100)
            time.sleep(1)
            os.system (f'ifconfig {iface} up')
            time.sleep(1)
            os.system ('screen -d -m systemctl restart NetworkManager')
            print ('\n')
            os.system (f'macchanger -s {iface}')
            exit ()

        # Random Vendor MAC Address

        elif choice == ('3') or choice == ('RANDOM VENDOR') or choice == ('RANDOMVENDORADDRESS') or choice == ('RANDOM VENDOR ADDRESS') or choice == ('RANDOM VENDOR MAC ADDRESS') or choice == ('RANDOMVENDORMACADDRESS'):
            os.system (f'ifconfig {iface} down')
            time.sleep(1)
            os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
            time.sleep(1)
            os.system (f'screen -d -m macchanger -A {iface}\n'*100)
            time.sleep(1)
            os.system (f'ifconfig {iface} up')
            time.sleep(1)
            os.system ('screen -d -m systemctl restart NetworkManager')
            print ('\n')
            os.system (f'macchanger -s {iface}')
            exit ()

        # Specific MAC Address

        elif choice == ('4') or choice == ('SPECIFIC') or choice ==  ('SPECIFIC MAC ADDRESS') or choice ==  ('SPECIFICADDRESS') or choice == ('SPECIFIC ADDRESS') or choice == ('SPECIFICMACADDRESS'):
            macspoof = input ('\nEnter MAC Address That You Want To Spoof : ')
            os.system (f'ifconfig {iface} down')
            time.sleep(1)
            os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
            time.sleep(1)
            os.system (f'screen -d -m macchanger -m {macspoof} {iface}\n'*100)
            time.sleep(1)
            os.system (f'ifconfig {iface} up')
            time.sleep(1)
            os.system ('screen -d -m systemctl restart NetworkManager')
            print ('\n')
            os.system (f'macchanger -s {iface}')
            exit ()
        elif choice == ('5') or choice == ('SPECIFIC VENDOR') or choice ==  ('SPECIFIC VENDOR MAC ADDRESS') or choice ==  ('SPECIFICVENDORADDRESS') or choice == ('SPECIFIC VENDOR ADDRESS') or choice == ('SPECIFICVENDORMACADDRESS'):
            def vendor_category_loop ():

                # Vendor category selection menu

                vendor_choice = input ('\n\n\nSelect Vendor Category\n\n1.PC Vendors\n\n2.Mobile Vendors\n\n\n\nYour Choice: ')
                vendor_choice = (vendor_choice.upper())
                if vendor_choice == ('1') or vendor_choice == ('PC VENDORS'):

                    # Loop if someone type wrong number

                    def pc_vendor_loop():
                        global first_digits
                        global last_digits

                        # PC Vendor selection menu

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
                            first_digits = ('FC:AA:14')
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

                    # Loop if someone type wrong number

                    def mobile_vendor_loop():
                        global first_digits
                        global last_digits

                        # Mobile Vendor selection menu

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
            time.sleep(1)
            os.system (f'screen -d -m iwconfig {iface} mode auto\n')
            time.sleep(1)
            os.system (f'screen -d -m macchanger -m {first_digits}:{last_digits} {iface}\n')
            time.sleep(1)
            os.system (f'ifconfig {iface} up')
            time.sleep(1)
            os.system ('screen -d -m systemctl restart NetworkManager')
            print ('\n')
            os.system (f'macchanger -s {iface}')
            exit ()

        # Show Current MAC Address

        elif choice == ('6') or choice == ('SHOW') or choice == ('SHOW CURRENT MAC ADDRESS') or choice == ('SHOWADDRESS') or choice ==  ('SHOW ADDRESS') or choice == ('SHOW MAC ADDRESS') or choice == ('SHOWCURRENTMACADDRESS') or choice == ('SHOWMACADDRESS'):
            print ('\n')
            os.system (f'macchanger -s {iface}')
        else:
            print ('\nPlease Chose Number or Name From Given Options\n')
            main_loop ()
    main_loop ()

def run_gui():

    if os.geteuid() == 0:
        try:
            import tkinter as tk
            tk.Tk().destroy()  # Try to access display
        except tk.TclError:
            print("\n❌ GUI can't be launched directly as root.")
            print("✅ Run this instead:")
            print("   xhost +SI:localuser:root && sudo python3 SOUL-SHIFTER.py -G")
            sys.exit(1)
    
    def get_network_adapters():
        try:
            # Execute the command 'ip link show' and capture the output
            output = subprocess.check_output(['ip', 'link', 'show'], stderr=subprocess.STDOUT, universal_newlines=True)

            # Split the output into lines
            lines = output.split('\n')

            adapters = []

            # Iterate through each line
            for line in lines:
                # Check if the line contains the word 'state'
                if 'state' in line:
                    # Split the line by ':' and get the second element, which contains the adapter name
                    adapter = line.split(':')[1].strip()

                    # Exclude loopback ('lo') and Docker interfaces
                    if 'lo' not in adapter and 'docker' not in adapter:
                        adapters.append(adapter)

            # Return the list of adapters
            return adapters
        except subprocess.CalledProcessError as e:
            print(f"Command execution failed with error: {e.output}")

    # Function to select available wifi adapters

    def check_adapter_selected():
        if not hasattr(sys.modules[__name__], 'iface') or not iface:
            messagebox.showwarning("Warning", "Please select a network adapter first.")
            return False
        return True

    # Function to generate random MAC address

    def generate_random_mac():
        random_mac = [random.choice('0123456789ABCDEF') for _ in range(6)]
        return ':'.join([random_mac[i]+random_mac[i+1] for i in range(0, len(random_mac), 2)])

    # Function to reset mac address

    def reset_mac_address():
        os.system(f'ifconfig {iface} down')
        time.sleep(1)
        os.system(f'screen -d -m iwconfig {iface} mode auto\n')
        time.sleep(1)
        os.system(f'screen -d -m macchanger -p {iface}\n')
        time.sleep(1)
        os.system(f'ifconfig {iface} up')
        time.sleep(1)
        os.system ('screen -d -m systemctl restart NetworkManager')
        output_var.set(os.popen(f'macchanger -s {iface}').read())

    # Function for random mac address

    def random_mac_address():
        os.system(f'ifconfig {iface} down')
        time.sleep(1)
        os.system(f'screen -d -m iwconfig {iface} mode auto\n')
        time.sleep(1)
        os.system(f'screen -d -m macchanger -r {iface}\n')
        time.sleep(1)
        os.system(f'ifconfig {iface} up')
        time.sleep(1)
        os.system ('screen -d -m systemctl restart NetworkManager')
        output_var.set(os.popen(f'macchanger -s {iface}').read())

    # Function for random vendor mac address

    def random_vendor_mac_address():
        os.system(f'ifconfig {iface} down')
        time.sleep(1)
        os.system(f'screen -d -m iwconfig {iface} mode auto\n')
        time.sleep(1)
        os.system(f'screen -d -m macchanger -A {iface}\n')
        time.sleep(1)
        os.system(f'ifconfig {iface} up')
        time.sleep(1)
        os.system ('screen -d -m systemctl restart NetworkManager')
        output_var.set(os.popen(f'macchanger -s {iface}').read())

    # Function for specific mac address

    def show_specific_mac_address_input():
        specific_window = tk.Toplevel(window)
        specific_window.title("Enter Specific MAC Address")

        specific_label = tk.Label(specific_window, text="Enter Specific MAC Address:")
        specific_label.pack()

        input_var_specific = tk.StringVar(specific_window)
        specific_entry = tk.Entry(specific_window, textvariable=input_var_specific)
        specific_entry.pack()

        def confirm_button_click():
            mac_address = input_var_specific.get()
            if mac_address:
                set_specific_mac_address(mac_address, specific_window)
            else:
                message_label.config(text="Please enter a MAC address.\n XX:XX:XX:XX:XX:XX")

        confirm_button = tk.Button(specific_window, text="Confirm", command=confirm_button_click)
        confirm_button.pack()

        message_label = tk.Label(specific_window, text="")
        message_label.pack()

    def set_specific_mac_address(mac_address, specific_window):
        specific_window.destroy()

        os.system(f'ifconfig {iface} down')
        time.sleep(1)
        os.system(f'screen -d -m iwconfig {iface} mode auto\n')
        time.sleep(1)
        os.system(f'screen -d -m macchanger -m {mac_address} {iface}\n')
        time.sleep(1)
        os.system(f'ifconfig {iface} up')
        time.sleep(1)
        os.system ('screen -d -m systemctl restart NetworkManager')
        output_var.set(os.popen(f'macchanger -s {iface}').read())

    # Function for specific vendor mac addresses

    def specific_vendor_address():
        global first_digits
        global last_digits
        vendor_choice = vendor_choice_var.get()
        if vendor_choice == '1' or vendor_choice == 'PC VENDORS':
            pc_vendor = pc_vendor_var.get()
            if pc_vendor == ('1') or pc_vendor == ('Dell'):
                first_digits = ('00:11:43')
                last_digits = generate_random_mac()
            elif pc_vendor == ('2') or pc_vendor == ('HP'):
                first_digits = ('00:04:EA')
                last_digits = generate_random_mac()
            elif pc_vendor == ('3') or pc_vendor == ('Lenovo'):
                first_digits = ('A4:8C:DB')
                last_digits = generate_random_mac()
            elif pc_vendor == ('4') or pc_vendor == ('Asus'):
                first_digits = ('14:DA:E9')
                last_digits = generate_random_mac()
            elif pc_vendor == ('5') or pc_vendor == ('Acer'):
                first_digits = ('C0:98:79')
                last_digits = generate_random_mac()
            elif pc_vendor == ('6') or pc_vendor == ('Intel'):
                first_digits = ('00:02:B3')
                last_digits = generate_random_mac()
            elif pc_vendor == ('7') or pc_vendor == ('Toshiba'):
                first_digits = ('E8:3A:97')
                last_digits = generate_random_mac()       
            elif pc_vendor == ('8') or pc_vendor == ('Sony'):
                first_digits = ('00:01:4A')
                last_digits = generate_random_mac()
            elif pc_vendor == ('9') or pc_vendor == ('Gateway'):
                first_digits = ('00:1D:84')
                last_digits = generate_random_mac()
            elif pc_vendor == ('10') or pc_vendor == ('Gigabyte'):
                first_digits = ('FC:AA:14')
                last_digits = generate_random_mac()
            elif pc_vendor == ('11') or pc_vendor == ('Msi'):
                first_digits = ('00:16:17')
                last_digits = generate_random_mac()
            elif pc_vendor == ('12') or pc_vendor == ('Asrock'):
                first_digits = ('D0:50:99')
                last_digits = generate_random_mac()
        elif vendor_choice == '2' or vendor_choice == 'Mobile VENDORS':
            mobile_vendor = mobile_vendor_var.get()
            if mobile_vendor == ('1') or mobile_vendor == ('Samsung'):
                first_digits = ('D4:E8:B2')
                last_digits = generate_random_mac()
            elif mobile_vendor == ('2') or mobile_vendor == ('iPhone'):
                first_digits = ('04:26:65')
                last_digits = generate_random_mac()
            elif mobile_vendor == ('3') or mobile_vendor == ('Huawei'):
                first_digits = ('04:9F:CA')
                last_digits = generate_random_mac()
            elif mobile_vendor == ('4') or mobile_vendor == ('Oneplus'):
                first_digits = ('94:65:2D')
                last_digits = generate_random_mac()
            elif mobile_vendor == ('5') or mobile_vendor == ('Oppo'):
                first_digits = ('B8:37:65')
                last_digits = generate_random_mac()
            elif mobile_vendor == ('6') or mobile_vendor == ('Vivo'):
                first_digits = ('10:F6:81')
                last_digits = generate_random_mac()
            elif mobile_vendor == ('7') or mobile_vendor == ('Motorola'):
                first_digits = ('14:1A:A3')
                last_digits = generate_random_mac()
            elif mobile_vendor == ('8') or mobile_vendor == ('Xiaomi'):
                first_digits = ('9C:99:A0')
                last_digits = generate_random_mac()
            elif mobile_vendor == ('9') or mobile_vendor == ('Realme'):
                first_digits = ('D0:28:BA')
                last_digits = generate_random_mac()
            elif mobile_vendor == ('10') or mobile_vendor == ('Sony'):
                first_digits = ('00:0E:07')
                last_digits = generate_random_mac()
            elif mobile_vendor == ('11') or mobile_vendor == ('HTC'):
                first_digits = ('D8:B3:77')
                last_digits = generate_random_mac()
            elif mobile_vendor == ('12') or mobile_vendor == ('Nokia'):
                first_digits = ('14:3E:60')
                last_digits = generate_random_mac()
            elif mobile_vendor == ('13') or mobile_vendor == ('Lenovo'):
                first_digits = ('14:9F:E8')
                last_digits = generate_random_mac()
            elif mobile_vendor == ('14') or mobile_vendor == ('LG'):
                first_digits = ('98:D6:F7')
                last_digits = generate_random_mac()
        else:
            output_var.set("\n\nEnter the number corresponding to the given vendor categories")
            return

        last_digits = generate_random_mac()
        os.system(f'ifconfig {iface} down')
        time.sleep(1)
        os.system(f'screen -d -m iwconfig {iface} mode auto\n')
        time.sleep(1)
        os.system(f'screen -d -m macchanger -m {first_digits}:{last_digits} {iface}\n')
        time.sleep(1)
        os.system(f'ifconfig {iface} up')
        time.sleep(1)
        os.system ('screen -d -m systemctl restart NetworkManager')
        output_var.set(os.popen(f'macchanger -s {iface}').read())

    # Function for specific vendor mac address buttons
    def specific_vendor_mac_address_buttons():
        vendor_category_label.pack()
        vendor_category_dropdown.pack()
        output_var.set("")

    # Function to remove specific vendor mac address buttons
    def remove_specific_vendor_mac_button():
        vendor_category_label.pack_forget()
        vendor_category_dropdown.pack_forget()
        pc_vendor_label.pack_forget()
        pc_vendor_dropdown.pack_forget()
        mobile_vendor_label.pack_forget()
        mobile_vendor_dropdown.pack_forget()

    # Automatically update UI on option select
    def on_option_change(*args):
        selected = input_var.get()
        if selected == '5':
            specific_vendor_mac_address_buttons()
        else:
            remove_specific_vendor_mac_button()

    def on_vendor_category_change(*args):
        category = vendor_choice_var.get().lower()

        # Hide both first
        pc_vendor_label.pack_forget()
        pc_vendor_dropdown.pack_forget()
        mobile_vendor_label.pack_forget()
        mobile_vendor_dropdown.pack_forget()

        if category == 'pc vendors':
            pc_vendor_label.pack()
            pc_vendor_dropdown.pack()
        elif category == 'mobile vendors':
            mobile_vendor_label.pack()
            mobile_vendor_dropdown.pack()

    # Main execution function
    def main_loop():
        if not check_adapter_selected():
            return
            
        choices = input_var.get().upper()

        if choices in ['1', 'RESET MAC ADDRESS']:
            reset_mac_address()
        elif choices in ['2', 'RANDOM MAC ADDRESS']:
            random_mac_address()
        elif choices in ['3', 'RANDOM VENDOR MAC ADDRESS']:
            random_vendor_mac_address()
        elif choices in ['4', 'SPECIFIC MAC ADDRESS']:
            show_specific_mac_address_input()
        elif choices in ['5', 'SPECIFIC VENDOR MAC ADDRESS']:
            specific_vendor_address()
        else:
            output_var.set("Invalid option")

    # Create the Tkinter window
    window = tk.Tk()
    window.title("SOUL SHIFTER")
    window.geometry("1100x800")
    window.resizable(False, False)

    text = '███████╗ ██████╗ ██╗   ██╗██╗         ███████╗██╗  ██╗██╗███████╗████████╗███████╗██████╗\n' \
        '██╔════╝██╔═══██╗██║   ██║██║         ██╔════╝██║  ██║██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗\n' \
        '███████╗██║   ██║██║   ██║██║         ███████╗███████║██║█████╗     ██║   █████╗  ██████╔╝\n' \
        '╚════██║██║   ██║██║   ██║██║         ╚════██║██╔══██║██║██╔══╝     ██║   ██╔══╝  ██╔══██╗\n' \
        '███████║╚██████╔╝╚██████╔╝███████╗    ███████║██║  ██║██║██║        ██║   ███████╗██║  ██║\n' \
        '╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝\n' \
        '                                                                                          \n' \
        '                  by XBEAST  ~  Discover the world through a different lens! <3           \n' \
        '                                           v6.0                                           \n' \
        '                           Github Link: https://github.com/XBEAST1                        \n'

    label = tk.Label(window, text=text, font=("Courier", 12))
    label.pack(anchor=tk.NW)

    # Get the list of network adapters
    network_adapters = get_network_adapters()
    adapter_var = tk.StringVar(window)
    if network_adapters:
        adapter_var.set("Select Network adapter")
        adapter_dropdown = tk.OptionMenu(window, adapter_var, *network_adapters)
        adapter_dropdown.pack()
    else:
        adapter_var.set("No adapters found")
        adapter_dropdown = tk.OptionMenu(window, adapter_var, ["No adapters found"])
        adapter_dropdown.pack()
    
    # Label to show selected adapter
    selected_adapter_label = tk.Label(window, text="Selected Adapter: None")
    selected_adapter_label.pack(pady=(0,10))
    
    # Function to update selected adapter
    def on_adapter_change(*args):
        global iface
        selected = adapter_var.get()
        if selected and selected != "Select Network adapter" and selected != "No adapters found":
            iface = selected
            selected_adapter_label.config(text=f"Selected Adapter: {selected}")
        else:
            selected_adapter_label.config(text="Selected Adapter: None")
    
    adapter_var.trace_add('write', on_adapter_change)

    # Operation selection
    operation_label = tk.Label(window, text="Select Operation:")
    operation_label.pack()

    # Vendor Category Selection
    vendor_category_label = tk.Label(window, text="Vendor Category:")
    vendor_choice_var = tk.StringVar()
    vendor_category_choices = ['PC VENDORS', 'Mobile VENDORS']
    vendor_category_dropdown = tk.OptionMenu(window, vendor_choice_var, *vendor_category_choices)
    vendor_choice_var.trace_add('write', on_vendor_category_change)

    # PC Vendor Selection
    pc_vendor_label = tk.Label(window, text="PC Vendor:")
    pc_vendor_var = tk.StringVar()
    pc_vendor_choices = ['Dell', 'HP', 'Lenovo', 'Asus', 'Acer', 'Intel', 'Toshiba', 'Sony', 'Gateway', 'Gigabyte', 'Msi', 'Asrock']
    pc_vendor_dropdown = tk.OptionMenu(window, pc_vendor_var, *pc_vendor_choices)

    # Mobile Vendor Selection
    mobile_vendor_label = tk.Label(window, text="Mobile Vendor:")
    mobile_vendor_var = tk.StringVar()
    mobile_vendor_choices = ['Samsung', 'iPhone', 'Huawei', 'OnePlus', 'Oppo', 'Vivo', 'Motorola', 'Xiaomi', 'Realme', 'Sony', 'HTC', 'Nokia', 'Lenovo', 'LG']
    mobile_vendor_dropdown = tk.OptionMenu(window, mobile_vendor_var, *mobile_vendor_choices)

    # Output Label
    output_var = tk.StringVar()
    output_label = tk.Label(window, textvariable=output_var)
    output_label.pack()

    # Operation input and radio buttons
    input_var = tk.StringVar(window)
    operations = [
        "1. Reset to Original MAC Address",
        "2. Set to Random MAC Address",
        "3. Set to Random Vendor MAC Address",
        "4. Set to Specific MAC Address",
        "5. Set to Specific Vendor MAC Address"
    ]
    for operation in operations:
        rb = tk.Radiobutton(window, text=operation, variable=input_var, value=operation.split('.')[0])
        rb.pack(anchor=tk.W)

    # Watch for changes in the selected operation
    input_var.trace_add('write', on_option_change)
    
    # Place the Execute button at the bottom, after all other controls
    button = tk.Button(window, text="Execute", command=main_loop)
    button.pack(pady=10)  # Add some padding for better spacing

    # Final output label
    output_var = tk.StringVar(window)
    output_label = tk.Label(window, textvariable=output_var)
    output_label.pack()

    # Start GUI loop
    window.mainloop()


def main():
    install_dependencies()
    parser = argparse.ArgumentParser()
    parser.add_argument('-G', '--gui', action='store_true')
    args = parser.parse_args()

    if args.gui:
        run_gui()
    else:
        run_command_line()

if __name__ == '__main__':
    main()

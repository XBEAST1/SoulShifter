import os
import subprocess
import random
import argparse
import tkinter as tk
from tkinter import messagebox
from termcolor import colored

def run_command_line():
    
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
        '                                           v5.0                                             \n'
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
            os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
            os.system (f'screen -d -m macchanger -p {iface}\n'*100)
            os.system (f'ifconfig {iface} up')
            os.system ('service NetworkManager restart')
            print ('\n')
            os.system (f'macchanger -s {iface}')
            exit ()

        # Random MAC Address

        elif choice == ('2') or choice == ('RANDOM') or choice == ('RANDOMADDRESS') or choice == ('RANDOM ADDRESS') or choice == ('RANDOM MAC ADDRESS') or choice == ('RANDOMMACADDRESS'):
            os.system (f'ifconfig {iface} down')
            os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
            os.system (f'screen -d -m macchanger -r {iface}\n'*100)
            os.system (f'ifconfig {iface} up')
            os.system ('service NetworkManager restart')
            print ('\n')
            os.system (f'macchanger -s {iface}')
            exit ()

        # Random Vendor MAC Address

        elif choice == ('3') or choice == ('RANDOM VENDOR') or choice == ('RANDOMVENDORADDRESS') or choice == ('RANDOM VENDOR ADDRESS') or choice == ('RANDOM VENDOR MAC ADDRESS') or choice == ('RANDOMVENDORMACADDRESS'):
            os.system (f'ifconfig {iface} down')
            os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
            os.system (f'screen -d -m macchanger -A {iface}\n'*100)
            os.system (f'ifconfig {iface} up')
            os.system ('service NetworkManager restart')
            print ('\n')
            os.system (f'macchanger -s {iface}')
            exit ()

        # Specific MAC Address

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
            os.system (f'screen -d -m iwconfig {iface} mode auto\n'*10)
            os.system (f'screen -d -m macchanger -m {first_digits}:{last_digits} {iface}\n'*100)
            os.system (f'ifconfig {iface} up')
            os.system ('service NetworkManager restart')
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

    def select_adapter():
        # Get the list of available Wi-Fi adapters
        network_adapters = get_network_adapters()

        if len(network_adapters) > 0:
            # Create a new window for selecting the adapter
            adapter_window = tk.Toplevel(window)
            adapter_window.title("Select Wi-Fi Adapter")

            # Function to confirm the selected adapter
            def confirm_selection():
                global iface
                # Get the index of the selected adapter from the listbox
                selection = adapter_listbox.curselection()

                if selection:
                    # Retrieve the selected adapter from the list of adapters
                    iface = network_adapters[selection[0]]
                    messagebox.showinfo("Selection", f"Selected Wi-Fi adapter: {iface}")
                    adapter_window.destroy()
                else:
                    messagebox.showwarning("Warning", "No adapter selected.")

            # Create a listbox to display the available adapters
            adapter_listbox = tk.Listbox(adapter_window)
            adapter_listbox.pack(pady=10)

            # Populate the listbox with the available adapters
            for adapter in network_adapters:
                adapter_listbox.insert(tk.END, adapter)

            # Create a button to confirm the adapter selection
            confirm_button = tk.Button(adapter_window, text="Confirm", command=confirm_selection)
            confirm_button.pack(pady=10)
        else:
            messagebox.showinfo("No Wi-Fi Adapters", "No Wi-Fi adapters found.")

    # Function to generate random MAC address

    def generate_random_mac():
        random_mac = [random.choice('0123456789ABCDEF') for _ in range(6)]
        return ':'.join([random_mac[i]+random_mac[i+1] for i in range(0, len(random_mac), 2)])

    # Function to reset mac address

    def reset_mac_address():
        os.system(f'ifconfig {iface} down')
        os.system(f'screen -d -m iwconfig {iface} mode auto\n'*10)
        os.system(f'screen -d -m macchanger -p {iface}\n'*100)
        os.system(f'ifconfig {iface} up')
        os.system('service NetworkManager restart')
        output_var.set(os.popen(f'macchanger -s {iface}').read())

    # Function for random mac address

    def random_mac_address():
        os.system(f'ifconfig {iface} down')
        os.system(f'screen -d -m iwconfig {iface} mode auto\n'*10)
        os.system(f'screen -d -m macchanger -r {iface}\n'*100)
        os.system(f'ifconfig {iface} up')
        os.system('service NetworkManager restart')
        output_var.set(os.popen(f'macchanger -s {iface}').read())

    # Function for random vendor mac address

    def random_vendor_mac_address():
        os.system(f'ifconfig {iface} down')
        os.system(f'screen -d -m iwconfig {iface} mode auto\n'*10)
        os.system(f'screen -d -m macchanger -A {iface}\n'*100)
        os.system(f'ifconfig {iface} up')
        os.system('service NetworkManager restart')
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
        os.system(f'screen -d -m iwconfig {iface} mode auto\n'*10)
        os.system(f'screen -d -m macchanger -m {mac_address} {iface}\n'*100)
        os.system(f'ifconfig {iface} up')
        os.system('service NetworkManager restart')
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
        os.system(f'screen -d -m iwconfig {iface} mode auto\n'*10)
        os.system(f'screen -d -m macchanger -m {first_digits}:{last_digits} {iface}\n'*100)
        os.system(f'ifconfig {iface} up')
        os.system('service NetworkManager restart')
        output_var.set(os.popen(f'macchanger -s {iface}').read())

    # Function for specific vendor mac address buttons

    def specific_vendor_mac_address_buttons():
        vendor_category_label.pack()
        vendor_category_dropdown.pack()
        pc_vendor_label.pack()
        pc_vendor_dropdown.pack()
        mobile_vendor_label.pack()
        mobile_vendor_dropdown.pack()
        run_button.pack()
        output_var.set("")

    # Function to remove specific vendor mac address buttons

    def remove_specific_vendor_mac_button():
        vendor_category_label.pack_forget()
        vendor_category_dropdown.pack_forget()
        pc_vendor_label.pack_forget()
        pc_vendor_dropdown.pack_forget()
        mobile_vendor_label.pack_forget()
        mobile_vendor_dropdown.pack_forget()
        run_button.pack_forget()

    def main_loop():
        choices = input_var.get().upper()

        if choices in ['1', 'RESET MAC ADDRESS']:
            reset_mac_address()
            remove_specific_vendor_mac_button()
        elif choices in ['2', 'RANDOM MAC ADDRESS']:
            random_mac_address()
            remove_specific_vendor_mac_button()
        elif choices in ['3', 'RANDOM VENDOR MAC ADDRESS']:
            random_vendor_mac_address()
            remove_specific_vendor_mac_button()
        elif choices in ['4', 'SPECIFIC MAC ADDRESS']:
            show_specific_mac_address_input()
            remove_specific_vendor_mac_button()
        elif choices in ['5', 'SPECIFIC VENDOR MAC ADDRESS']:
            specific_vendor_mac_address_buttons()
        else:
            remove_specific_vendor_mac_button()
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
            '                                           v5.0                                           \n' \
            '                           Github Link: https://github.com/XBEAST1                        \n'


    label = tk.Label(window, text=text, font=("Courier", 12))
    label.pack(anchor=tk.CENTER)

    # Place the label at the top of the window
    label.pack(anchor=tk.NW)

    # Execute wifi adapter select function
    select_adapter_button = tk.Button(window, text="Select Network Adapter", command=select_adapter)
    select_adapter_button.pack(pady=10)

    # Create a label and entry for selecting the operation
    operation_label = tk.Label(window, text="Select Operation:")
    operation_label.pack()

    # Vendor Category Selection
    vendor_category_label = tk.Label(window, text="Vendor Category:")
    vendor_choice_var = tk.StringVar()
    vendor_category_choices = ['PC VENDORS', 'Mobile VENDORS']
    vendor_category_dropdown = tk.OptionMenu(window, vendor_choice_var, *vendor_category_choices)

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

    # Output Text
    output_var = tk.StringVar()
    output_label = tk.Label(window, textvariable=output_var)
    output_label.pack()

    # Run Button
    run_button = tk.Button(window, text="Run", command=specific_vendor_address)

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

    # Create a button to execute the operation
    button = tk.Button(window, text="Execute", command=main_loop)
    button.pack()

    # Create a label to display the output
    output_var = tk.StringVar(window)
    output_label = tk.Label(window, textvariable=output_var)
    output_label.pack()

    # Run the Tkinter event loop
    window.mainloop()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-G', '--gui', action='store_true')
    args = parser.parse_args()

    if args.gui:
        run_gui()
    else:
        run_command_line()

if __name__ == '__main__':
    main()

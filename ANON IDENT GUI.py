import os
import subprocess
import random
import tkinter as tk
from tkinter import messagebox

# Function to retrieve available wifi adapters

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

# Specific MAC Address functions

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

def main_loop():
    choices = input_var.get().upper()

    if choices in ['1', 'RESET', 'RESETADDRESS', 'RESET ADDRESS', 'RESET MAC ADDRESS', 'RESETMACADDRESS']:
        os.system(f'ifconfig {iface} down')
        os.system(f'screen -d -m iwconfig {iface} mode auto\n'*10)
        os.system(f'screen -d -m macchanger -p {iface}\n'*100)
        os.system(f'ifconfig {iface} up')
        os.system('service NetworkManager restart')
        output_var.set(os.popen(f'macchanger -s {iface}').read())
        vendor_category_label.pack_forget()
        vendor_category_dropdown.pack_forget()
        pc_vendor_label.pack_forget()
        pc_vendor_dropdown.pack_forget()
        mobile_vendor_label.pack_forget()
        mobile_vendor_dropdown.pack_forget()
        run_button.pack_forget()
    elif choices in ['2', 'RANDOM', 'RANDOMADDRESS', 'RANDOM ADDRESS', 'RANDOM MAC ADDRESS', 'RANDOMMACADDRESS']:
        os.system(f'ifconfig {iface} down')
        os.system(f'screen -d -m iwconfig {iface} mode auto\n'*10)
        os.system(f'screen -d -m macchanger -r {iface}\n'*100)
        os.system(f'ifconfig {iface} up')
        os.system('service NetworkManager restart')
        output_var.set(os.popen(f'macchanger -s {iface}').read())
        vendor_category_label.pack_forget()
        vendor_category_dropdown.pack_forget()
        pc_vendor_label.pack_forget()
        pc_vendor_dropdown.pack_forget()
        mobile_vendor_label.pack_forget()
        mobile_vendor_dropdown.pack_forget()
        run_button.pack_forget()
    elif choices in ['3', 'RANDOM VENDOR', 'RANDOMVENDORADDRESS', 'RANDOM VENDOR ADDRESS', 'RANDOM VENDOR MAC ADDRESS', 'RANDOMVENDORMACADDRESS']:
        os.system(f'ifconfig {iface} down')
        os.system(f'screen -d -m iwconfig {iface} mode auto\n'*10)
        os.system(f'screen -d -m macchanger -A {iface}\n'*100)
        os.system(f'ifconfig {iface} up')
        os.system('service NetworkManager restart')
        output_var.set(os.popen(f'macchanger -s {iface}').read())
        vendor_category_label.pack_forget()
        vendor_category_dropdown.pack_forget()
        pc_vendor_label.pack_forget()
        pc_vendor_dropdown.pack_forget()
        mobile_vendor_label.pack_forget()
        mobile_vendor_dropdown.pack_forget()
        run_button.pack_forget()
    elif choices in ['4', 'SPECIFIC', 'SPECIFIC MAC ADDRESS', 'SPECIFICADDRESS', 'SPECIFIC ADDRESS', 'SPECIFICMACADDRESS']:
        show_specific_mac_address_input()
        vendor_category_label.pack_forget()
        vendor_category_dropdown.pack_forget()
        pc_vendor_label.pack_forget()
        pc_vendor_dropdown.pack_forget()
        mobile_vendor_label.pack_forget()
        mobile_vendor_dropdown.pack_forget()
        run_button.pack_forget()
    elif choices in ['5', 'SPECIFIC VENDOR', 'SPECIFIC VENDOR MAC ADDRESS', 'SPECIFICVENDORADDRESS', 'SPECIFIC VENDOR ADDRESS', 'SPECIFICVENDORMACADDRESS']:
        vendor_category_label.pack()
        vendor_category_dropdown.pack()
        pc_vendor_label.pack()
        pc_vendor_dropdown.pack()
        mobile_vendor_label.pack()
        mobile_vendor_dropdown.pack()
        run_button.pack()
        output_var.set("")
    else:
        vendor_category_label.pack_forget()
        vendor_category_dropdown.pack_forget()
        pc_vendor_label.pack_forget()
        pc_vendor_dropdown.pack_forget()
        mobile_vendor_label.pack_forget()
        mobile_vendor_dropdown.pack_forget()
        run_button.pack_forget()
        output_var.set("Invalid option")

# Create the Tkinter window
window = tk.Tk()
window.title("ANON IDENT")
window.geometry("950x750")
window.resizable(False, False)

text = " █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗    ██╗██████╗ ███████╗███╗   ██╗████████╗\n" \
       "██╔══██╗████╗  ██║██╔═══██╗████╗  ██║    ██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝\n" \
       "███████║██╔██╗ ██║██║   ██║██╔██╗ ██║    ██║██║  ██║█████╗  ██╔██╗ ██║   ██║   \n" \
       "██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║    ██║██║  ██║██╔══╝  ██║╚██╗██║   ██║   \n" \
       "██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║    ██║██████╔╝███████╗██║ ╚████║   ██║   \n" \
       "╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   \n"

label = tk.Label(window, text=text, font=("Courier", 12))
label.pack(anchor=tk.CENTER)

# Place the label at the top of the window
label.pack(anchor=tk.NW)

# Execute wifi adapter select function
select_adapter_button = tk.Button(window, text="Select Wi-Fi Adapter", command=select_adapter)
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
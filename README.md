# Soul Shifter

Soul Shifter is a powerful tool designed to manage and manipulate MAC addresses for your network adapters. It provides both a Command-Line Interface (CLI) and a Graphical User Interface (GUI) for ease of use. Whether you want to reset your MAC address, generate a random one, or set a specific vendor MAC address, Soul Shifter has you covered.

---

## Features

- **Reset MAC Address**: Revert your network adapter's MAC address to its original state.
- **Random MAC Address**: Generate and assign a completely random MAC address.
- **Random Vendor MAC Address**: Generate a random MAC address based on a specific vendor.
- **Specific MAC Address**: Set a custom MAC address of your choice.
- **Specific Vendor MAC Address**: Choose a MAC address from a list of predefined vendors (e.g., Dell, Samsung, Lenovo, etc.).
- **Cross-Platform Support**: Works on various Linux distributions.
- **Dependency Management**: Automatically installs required dependencies based on your Linux distribution.

---

## Installation

Before using Soul Shifter, ensure you have Python 3 installed on your system. The tool will handle the installation of additional dependencies automatically.

---

## Usage

### Command-Line Interface (CLI)

Run the following command to use the CLI mode:

```bash
sudo python3 SOUL-SHIFTER.py
```

### Graphical User Interface (GUI)

Run the following command to use the GUI mode:

```bash
sudo python3 SOUL-SHIFTER.py -G
```

---

## Screenshots

### CLI Mode

![soulshifter](https://github.com/XBEAST1/Soul-Shifter/assets/81472131/62193196-ada2-4433-a53d-07cbee5d8525)

### GUI Mode

![soulshiftergui](https://github.com/XBEAST1/Soul-Shifter/assets/81472131/76aad229-386e-4ea4-88bb-5cb235e18fd3)

---

## Supported Linux Distributions

Soul Shifter supports the following Linux distributions and their package managers:

- **Arch/Manjaro**: `pacman`
- **Ubuntu/Debian/Pop/Linux Mint**: `apt`
- **Fedora/RHEL/CentOS**: `dnf`
- **OpenSUSE/SUSE/SLES**: `zypper`
- **Void Linux**: `xbps-install`

If your distribution is not listed, you may need to install the required dependencies manually.

---

## Dependencies

The following dependencies are required for Soul Shifter to function:

- `tkinter` (for GUI support)
- `termcolor` (for colored CLI output)
- `macchanger` (for MAC address manipulation)
- `screen` (for terminal multiplexing)

The tool will automatically detect and install these dependencies based on your Linux distribution.

---

## Author

Developed by **XBEAST**

- GitHub: [XBEAST1](https://github.com/XBEAST1)
- GitHub: [Email](mailto:xbeast1@proton.me)
- Version: 6.0

---

## License

This project is licensed under the [GPL-3.0 license](LICENSE).
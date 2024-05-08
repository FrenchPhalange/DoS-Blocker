# 🛡️ Python DoS Blocker

Welcome to the Python DoS (Denial of Service) Blocker project! This repository contains two main scripts: one for blocking excessive traffic (a simple DoS attack prevention tool) and another for testing the effectiveness of the DoS blocker by simulating traffic.

## 🌟 Features

- **DoS Blocking**: Automatically blocks IP addresses that exceed a specified packet rate threshold, helping to protect your network against potential DoS attacks.
- **Traffic Simulation**: A script to simulate high traffic from an IP address to test the effectiveness of the DoS blocker.
- **Logging and Monitoring**: Both scripts provide essential feedback about their operation, including logging blocked IPs and traffic rates.

## 🛠 Installation

To run these scripts, you will need Python and Scapy. Here's how to set them up:

1. **Python**: Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **Scapy**: Install Scapy using pip:
```bash
   pip install scapy
```
## 🚀 Usage

### DoS Blocker

Run the DoS blocker script with root privileges:

```bash
sudo python dos_blocker.py
`````
This script will monitor network traffic and block IPs that exceed the threshold of 40 packets per second

Traffic Simulator

Run the traffic simulation script to test the DoS blocker:

```bash
python dos_blocker_tester.py
````

Make sure to update the TARGET_IP and INTERFACE variables in the script to match your target and network interface.

🔧 Configuration

    DoS Blocker: Set the THRESHOLD variable in dos_blocker.py to change the packet rate threshold.
    Traffic Simulator: Adjust TARGET_IP, INTERFACE, NUM_PACKETS, and DURATION in dos_blocker_tester.py to configure the simulation parameters.

🤝 Contributing

Feel free to fork this repo and contribute back by submitting a pull request. We love your input on:

    Enhancing the detection logic
    Expanding the script capabilities
    Improving efficiency

😄 A Little Dev Joke

    How many programmers does it take to change a light bulb? 🤔

    None, that's a hardware problem! 💡😂

📜 License

This project is released under the MIT license. Feel free to use it, modify it, and distribute it as you see fit!

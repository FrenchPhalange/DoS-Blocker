import os
import sys
import time
from collections import defaultdict
from scapy.all import sniff, IP

THRESHOLD = 40  # Packets per second
print(f"THRESHOLD: {THRESHOLD}")

def packet_callback(packet):
    src_ip = packet[IP].src
    packet_count[src_ip] += 1

    current_time = time.time()
    if current_time - start_time[0] >= 1:  # Check every second
        for ip, count in list(packet_count.items()):
            packet_rate = count / (current_time - start_time[0])
            if packet_rate > THRESHOLD and ip not in blocked_ips:
                print(f"Blocking IP: {ip}, packet rate: {packet_rate}")
                os.system(f"iptables -A INPUT -s {ip} -j DROP")
                blocked_ips.add(ip)
        packet_count.clear()
        start_time[0] = current_time

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("This script requires root privileges.")
        sys.exit(1)

    packet_count = defaultdict(int)
    start_time = [time.time()]  # Use list to allow modifications inside callback
    blocked_ips = set()

    print("Monitoring network traffic...")
    sniff(filter="ip", prn=packet_callback)

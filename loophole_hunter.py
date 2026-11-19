import socket

# Your mapped IPs from the nmap scan
targets = {
    "Hisense TV": "192.168.40.52",
    "Smart Plug": "192.168.40.111",
    "Smart Bulb": "192.168.40.138",
    "PS5": "192.168.40.149",
    "Watch": "192.168.40.157",
    "iPhone": "192.168.40.50",
    "MacBook": "192.168.40.32"
}

# Key "loopholes" to check: Telnet, HTTP, ADB, Discovery
ports_to_check = [23, 80, 443, 5555, 6667, 8080, 9000]

print("--- Starting Phase 2: Active Loophole Discovery ---")

for name, ip in targets.items():
    print(f"Scanning {name} ({ip})...")
    for port in ports_to_check:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"  [!] ALERT: Port {port} is OPEN on {name}!")
        s.close()

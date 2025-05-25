import socket
from datetime import datetime

# Banner
print("-" * 50)
print("🔍 Simple Port Scanner")
print("-" * 50)

# User input
target = input("Enter target IP or domain: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\nScanning target: {target}")
print(f"Port range: {start_port}-{end_port}")
print("Scan started at:", datetime.now())
print("-" * 50)

try:
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"🟢 Port {port} is OPEN")
        s.close()

except KeyboardInterrupt:
    print("\nScan cancelled by user.")
except socket.gaierror:
    print("Hostname could not be resolved.")
except socket.error:
    print("Couldn't connect to server.")

print("-" * 50)
print("Scan completed at:", datetime.now())

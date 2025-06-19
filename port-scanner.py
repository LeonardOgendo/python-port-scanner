import socket
import sys

def scan_ports(target_ip, ports_to_scan, timeout=1):
    print(f"[+] Starting scan on {target_ip}")

    for port in ports_to_scan:
        try:
            # Create a TCP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)

            # Try to connect to the port
            result =sock.connect_ex((target_ip, port))
           
            if result == 0:
                print(f"[+] Port {port:<5} is OPEN")
            else:
                print(f"[-] Port {port:<5} is CLOSED")
            
            socket.close()

        except socket.error as err:
            print(f"[!] Error connecting to port {port}: {err}")
        except KeyboardInterrupt:
            print(f"\n[!] Scan interrupted by user")
            sys.exit()

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    ports_to_scan = [int(port) for port in input("Enter the ports to scan (comma-separated): ").split(",")]
    
    scan_ports(target_ip, ports_to_scan)
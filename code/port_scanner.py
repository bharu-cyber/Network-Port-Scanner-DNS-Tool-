"""
port_scanner.py
Basic TCP port scanner.

Tries to open a TCP connection to each port in a given range on a target
IP address. If the connection succeeds, the port is reported as open.
"""

import socket


def scan_port(target, port, timeout=1):
    """
    Attempt a TCP connection to a single port on the target.

    Returns True if the port is open, False otherwise.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)

    result = s.connect_ex((target, port))  # 0 = success (open)
    s.close()

    return result == 0


def scan_range(target, start_port, end_port, timeout=1):
    """
    Scan every port in [start_port, end_port] on the target.

    Returns a list of open ports.
    """
    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target, port, timeout):
            print(f"Port {port} is OPEN")
            open_ports.append(port)

    return open_ports


def run_port_scanner():
    """Interactive entry point used by the menu in main.py."""
    target = input("Enter IP Address: ").strip()
    start_port = int(input("Start Port: "))
    end_port = int(input("End Port: "))

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
    open_ports = scan_range(target, start_port, end_port)

    print("\n--- Scan Complete ---")
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found in this range.")


if __name__ == "__main__":
    run_port_scanner()

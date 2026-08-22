"""
main.py
Entry point for the Network Tool: a simple menu that routes to the
port scanner or the DNS lookup module.
"""

from port_scanner import run_port_scanner
from dns_lookup import run_dns_lookup


def show_menu():
    print("\n===== Network Tool =====")
    print("1. Port Scanner")
    print("2. DNS Lookup")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            run_port_scanner()
        elif choice == "2":
            run_dns_lookup()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

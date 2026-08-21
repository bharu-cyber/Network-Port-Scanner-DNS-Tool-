"""
dns_lookup.py
Basic DNS lookup tool.

Resolves a domain name to an IP address and pulls A, MX, and NS records
using dnspython. Install dnspython first:

    pip install dnspython
"""

import socket

try:
    import dns.resolver
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False


def get_ip_address(domain):
    """Resolve a domain name to its IP address."""
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None


def get_records(domain, record_type):
    """
    Query a specific DNS record type (A, MX, NS) for a domain.

    Returns a list of record strings, or an empty list if none are found
    or dnspython isn't installed.
    """
    if not DNS_AVAILABLE:
        return []

    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(rdata) for rdata in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return []


def run_dns_lookup():
    """Interactive entry point used by the menu in main.py."""
    domain = input("Enter domain: ").strip()

    ip = get_ip_address(domain)
    if ip is None:
        print(f"Could not resolve {domain}. Check the domain name and try again.")
        return

    print(f"\nDomain:      {domain}")
    print(f"IP Address:  {ip}")

    if not DNS_AVAILABLE:
        print("\n(Install dnspython with 'pip install dnspython' to see A/MX/NS records.)")
        return

    a_records = get_records(domain, "A")
    mx_records = get_records(domain, "MX")
    ns_records = get_records(domain, "NS")

    print(f"A records:   {a_records if a_records else 'none found'}")
    print(f"MX records:  {mx_records if mx_records else 'none found'}")
    print(f"NS records:  {ns_records if ns_records else 'none found'}")


if __name__ == "__main__":
    run_dns_lookup()
  

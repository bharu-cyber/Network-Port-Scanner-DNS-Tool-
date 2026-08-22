# 🌳 Night Tree — Network Reconnaissance Toolkit

A network toolkit with two parts: a Python CLI for real TCP port scanning and DNS lookups, and a 3D web visualization that turns those same ideas into a living tree — roots that resolve DNS records, fruit that represents open ports.

## Live Demo

Enable GitHub Pages on this repo (see below) to get a live link, then visit:

`https://bharu-cyber.github.io/Network-Port-Scanner-DNS-Tool-/`

## What it does

**🌐 The Tree (`docs/index.html`)**
- A 3D tree, rendered in-browser with Three.js
- **Roots = DNS records.** Enter a domain and real, live DNS records (A, MX, NS, TXT) resolve via a public DNS-over-HTTPS API and grow as glowing roots beneath the tree
- **Fruit = ports.** Enter a target IP and port range; each port becomes a piece of fruit. Open ports glow and **fall to the ground**; closed ones stay on the branch
- Scroll to orbit 360° around the tree — one continuous camera path through both tools
- **Tap any fruit or root** to zoom in and see full details: port number, service name, a plain-English description, and live status — or the resolved DNS value and what that record type means
- Two independent tool cards (DNS lookup, port scan) — no need to run both together

**🖥️ The CLI (`code/`)**
- `port_scanner.py` — real TCP port scanning using Python's `socket` and `connect_ex()`
- `dns_lookup.py` — real DNS resolution using `socket` and `dnspython` (A / MX / NS records)
- `main.py` — simple menu tying both together

## Setup (CLI)

```bash
pip install dnspython
cd code
python3 main.py

===== Network Tool =====
1. Port Scanner
2. DNS Lookup
3. Exit

Enter choice: 1
Enter IP Address: 127.0.0.1
Start Port: 20
End Port: 100

Port 22 is OPEN
Port 80 is OPEN
⚠️ Responsible use
Only scan systems you own or have explicit permission to test — 127.0.0.1, localhost, or a machine in your own lab. Scanning systems without authorization may be illegal.
Note: the web tree's port scan is a labeled simulation — browsers can't open raw TCP sockets, so no real network probing happens there. The DNS lookups in the tree, however, are real and live.
Project structure
Network-Port-Scanner-DNS-Tool-/
├── README.md
├── code/
│   ├── main.py            # menu / entry point
│   ├── port_scanner.py    # real TCP port scanning (connect_ex)
│   └── dns_lookup.py      # real DNS resolution (socket + dnspython)
└── docs/
    └── index.html         # the 3D Night Tree visualization
Tech stack
Python 3 — socket, dnspython
Three.js (r128) — 3D rendering, procedural branch generation
Cloudflare DNS-over-HTTPS API — live DNS records in the browser
Enable GitHub Pages (free live link)
Repo → Settings → Pages
Source: Deploy from a branch
Branch: main, folder: /docs
Save — live in a minute or two
Roadmap
[ ] Map more well-known ports to service descriptions
[ ] Save scan/lookup history
[ ] Colored terminal output for the CLI
[ ] Simple Tkinter GUI for the CLI
Built by Bharu, B.E. CSE (Cyber Security), as part of a cybersecurity portfolio.

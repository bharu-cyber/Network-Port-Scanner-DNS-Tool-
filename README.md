# Network Port Scanner & DNS Lookup Tool

A simple, menu-driven Python tool for learning core networking and
cybersecurity concepts: TCP ports, sockets, and DNS resolution. Includes
a companion website with an interactive demo and a 3D scan visualization.

## Live demo

- [`docs/index.html`](docs/index.html) — project showcase
- [`docs/interactive.html`](docs/interactive.html) — live DNS lookup + simulated port scanner
- [`docs/3d-visualization.html`](docs/3d-visualization.html) — 3D scan visualization

(Enable GitHub Pages on this repo to get a live link — see the bottom of this file.)

## Features

- **Port Scanner** — checks a range of TCP ports on a target IP and
  reports which ones are open.
- **DNS Lookup** — resolves a domain name to an IP address and pulls
  A, MX, and NS records.

## Setup

```bash
pip install dnspython
```

## Usage

```bash
cd code
python3 main.py
```

```
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
```

## ⚠️ Responsible use

Only scan systems you own or have explicit permission to test —
`127.0.0.1`, `localhost`, or a machine in your own lab. Scanning
systems without authorization may be illegal.

## Project structure

```
Network-Port-Scanner-DNS-Tool/
├── README.md
├── code/
│   ├── main.py            # menu / entry point
│   ├── port_scanner.py    # TCP port scanning logic
│   └── dns_lookup.py      # DNS resolution logic
└── docs/
    ├── index.html              # showcase page
    ├── interactive.html        # live DNS lookup + simulated scanner
    └── 3d-visualization.html   # 3D scan visualization
```

## Enable GitHub Pages (optional, free live link)

1. Go to your repo's **Settings → Pages**
2. Under **Build and deployment**, set **Source** to "Deploy from a branch"
3. Set **Branch** to `main` and folder to `/docs`
4. Save — your site will be live at `https://your-username.github.io/Network-Port-Scanner-DNS-Tool/`

## Roadmap

- [ ] Multithreaded scanning for faster sweeps
- [ ] Map open ports to known service names (22 = SSH, 80 = HTTP, ...)
- [ ] Colored terminal output
- [ ] Save results to a file
- [ ] Simple Tkinter GUI

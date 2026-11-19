# Quiet Devices, Loud Metadata — Testbed Scripts & Sample Captures

This anonymized repository accompanies the submission *"Quiet Devices, Loud Metadata: A Testbed Measurement of Idle Traffic and Local Control Exposure in a Seven-Device Smart Home."*

## Contents
- `loophole_hunter.py` — Python TCP connect scanner used in Phase 2 to probe target ports across the seven testbed devices (0.5 s timeout).
- `pcap_dump_1.txt` — Sample decrypted IP/UDP/ARP/ICMP packet dump from the isolated `/24` testbed subnet.
- `pcap_dump_2.txt` — Sample 802.11 monitor-mode wireless capture (testbed SSID anonymized to `Testbed_AP` for double-blind review).
- `Data_7Smartwatch.png` — Wireshark I/O graph illustrating per-device idle packet rates and volumetric bursts.

## Requirements
- Python 3.8+ (standard library `socket` module; no external dependencies required for `loophole_hunter.py`).
- Wireshark / `tshark` and Zeek for PCAP inspection and flow summarization.

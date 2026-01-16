import subprocess
import xml.etree.ElementTree as ET
import sys

print("=========================================")
print("Welcome to Nmap Auto Parser")
print("=========================================\n")

def nmap(target):
    subprocess.run(["nmap", "-sV", "-oX", "output.xml", target])

def xmlparse():
    tree = ET.parse("output.xml")
    root = tree.getroot()

    for port in root.findall(".//port"):
        port_id = port.get("portid")
        state = port.find("state").get("state")
        service = port.find("service").get("name")
        print(f"Port {port_id} → {state} ({service})")

if len(sys.argv) < 2:
    print("Usage: python nmap_xmlparser.py <IP>")
    print("\n=========================================")
    print("Developed by sudo_0xksh")
    print("=========================================")
    sys.exit()

target = sys.argv[1]

nmap(target)
xmlparse()

print("\n=========================================")
print("Scan Completed")
print("Developed by sudo_0xksh")
print("=========================================")

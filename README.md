# 🗺️🔥 Nmap Auto Parser 🔥🗺️

Nmap Auto Parser is a Python CLI tool that runs an Nmap service scan,
stores the output in XML,
and instantly parses it into clean, readable results 🧠⚙️

No manual XML.
No extra commands.
Just scan and understand.

---

## 👀 Overview

Nmap scans are powerful.
Nmap XML files are not fun 😵‍💫

This tool automates the full process:
first it runs an Nmap scan with service detection,
then it parses the generated XML file
and prints useful port information directly to the terminal.

One command.
Full clarity.

---

## 🚀 Features

- Runs Nmap with service detection (-sV) 🛰️  
- Automatically saves output in XML format 📄  
- Parses XML without user interaction 🧠  
- Displays port number, state, and service name 🔍  
- Fast, simple, and beginner-friendly ⚡  

---

## ⚙️ How It Works

The tool runs Nmap using a subprocess call
and saves the scan output as output.xml.

Once the scan finishes,
the XML file is parsed using Python’s XML parser,
and all ports with their state and service names
are printed in a clean, readable format.

Scan → Parse → Understand.

---

## 🧪 Usage

Run the tool exactly like this  
python nmap_xmlparser.py <IP>

Example  
python nmap_xmlparser.py 192.168.1.1

The scan will run automatically
and results will appear as soon as parsing completes 😎

---

## 📤 Example Output

Port 22 → open (ssh)  
Port 80 → open (http)  
Port 443 → open (https)  

No XML tags.
No scrolling.
Just results.

---

## 📦 Requirements

- Python 3.x  
- Nmap installed on the system  

Make sure Nmap is available in your PATH.

---

## 🧠 What You Learn From This Project

- Automating external tools with Python  
- How Nmap service detection works  
- XML parsing basics  
- Turning raw scan data into readable output  
- Why automation saves time in recon  

---

## 🗿 Final Words

Scanning is step one.
Understanding is step two.

This tool does both — automatically 🔥

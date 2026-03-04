# 🚀 Kali Linux Quick Start Guide

## Installation (3 Steps)

### Step 1: Clone Repository

```bash
cd ~/tools
git clone https://github.com/rudraksha-avatara/ddos-load.git
cd ddos-load
```

### Step 2: Run Installer

```bash
chmod +x install-kali.sh
./install-kali.sh
```

### Step 3: Verify Installation

```bash
chmod +x test-installation.sh
./test-installation.sh
```

---

## Quick Commands

### Basic Testing

```bash
# Simple test
python3 main-kali-linux.py http://target.com -n 1000 -c 50

# With cache busting (recommended)
python3 main-kali-linux.py http://target.com -n 1000 -c 50 --no-cache
```

### Security Testing

```bash
# Test login endpoint
python3 main-kali-linux.py http://target.com/login \
  -n 500 -c 25 -m POST \
  --body "username=admin&password=test" \
  --no-cache

# Test API with authorization
python3 main-kali-linux.py http://target.com/api \
  -n 2000 -c 100 \
  -H "Authorization: Bearer token123" \
  --no-cache

# Stealth test (low and slow)
python3 main-kali-linux.py http://target.com \
  -n 500 -c 10 \
  --rate-limit 20 \
  --random-ua
```

### Advanced Features

```bash
# Test with Burp Suite proxy
python3 main-kali-linux.py http://target.com \
  -n 500 -c 25 \
  --proxy http://127.0.0.1:8080 \
  --no-verify-ssl

# Save responses for analysis
python3 main-kali-linux.py http://target.com \
  -n 100 -c 10 \
  --save-responses

# Save results to file
python3 main-kali-linux.py http://target.com \
  -n 1000 -c 50 \
  --no-cache \
  -o results.txt
```

---

## Integration with Kali Tools

### After Nmap Scan

```bash
# Scan first
nmap -sV -p 80,443,8080 target.com

# Then test discovered services
python3 main-kali-linux.py http://target.com:8080 -n 1000 -c 50 --no-cache
```

### After Nikto Scan

```bash
# Scan first
nikto -h http://target.com

# Test discovered endpoints
python3 main-kali-linux.py http://target.com/admin -n 500 -c 25 --no-cache
```

### With Burp Suite

```bash
# Configure Burp proxy, then test
python3 main-kali-linux.py http://target.com \
  -n 500 -c 25 \
  --proxy http://127.0.0.1:8080 \
  -H "Cookie: session=from_burp" \
  --no-verify-ssl
```

---

## Common Options

| Option         | Description         | Example                         |
| -------------- | ------------------- | ------------------------------- |
| `-n`           | Number of requests  | `-n 1000`                       |
| `-c`           | Concurrency         | `-c 50`                         |
| `-d`           | Duration (seconds)  | `-d 60`                         |
| `-m`           | HTTP method         | `-m POST`                       |
| `-H`           | Custom header       | `-H "Auth: token"`              |
| `--body`       | Request body        | `--body '{"key":"val"}'`        |
| `--no-cache`   | Cache busting       | `--no-cache`                    |
| `--random-ua`  | Random user agents  | `--random-ua`                   |
| `--rate-limit` | Requests per second | `--rate-limit 100`              |
| `--proxy`      | Proxy URL           | `--proxy http://127.0.0.1:8080` |
| `-o`           | Output file         | `-o results.txt`                |

---

## Troubleshooting

### "Too many open files"

```bash
ulimit -n 10000
```

### Permission errors

```bash
pip3 install --user -r requirements-kali-linux.txt
```

### Module not found

```bash
pip3 install aiohttp requests aiodns
```

### SSL errors

```bash
# Use --no-verify-ssl flag
python3 main-kali-linux.py https://target.com --no-verify-ssl
```

---

## ⚠️ Legal Notice

**Only test systems you own or have explicit written authorization to test.**

Unauthorized testing is:

- ❌ Illegal
- ❌ Unethical
- ❌ Prosecutable

Always get written permission before testing!

---

## 📚 Documentation

- `README.md` - General documentation
- `README-KALI-LINUX.md` - Detailed Kali guide
- `--help` - Command help

---

## 🆘 Getting Help

```bash
# Show all options
python3 main-kali-linux.py --help

# Test installation
./test-installation.sh

# Check Python version
python3 --version

# Check installed packages
pip3 list | grep aiohttp
```

---

**Developed by Team Supreme X**

Use Responsibly | Test Ethically | Stay Legal

# 🚀 DDoS Load Tool

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-production--ready-brightgreen)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen)

**A professional-grade, high-performance DDoS Load Tool for stress to attack powerful servers and web applications.**

Developed by **Team Supreme X**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation) • [Examples](#-examples)

</div>

---

## � Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Guide](#-usage-guide)
- [Command Reference](#-command-reference)
- [Examples](#-examples)
- [Understanding Results](#-understanding-results)
- [Best Practices](#-best-practices)
- [Troubleshooting](#-troubleshooting)
- [Performance Tuning](#-performance-tuning)
- [Legal & Ethics](#-legal--ethics)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

This DDoS Load Tool is built with Python's async I/O capabilities to deliver maximum performance with minimal resource usage. It's designed to help developers and DevOps teams test their applications under heavy load conditions, identify bottlenecks, and ensure their systems can handle production traffic.

### Why This Tool?

- ⚡ **Blazing Fast** - Async I/O handles 1000+ concurrent connections
- 🎯 **Accurate to attack** - Cache busting ensures real server performance to attack
- 📊 **Detailed Analytics** - Comprehensive metrics and percentile analysis
- 🛠️ **Production Ready** - Stable, tested, and battle-hardened
- 🔧 **Highly Configurable** - Extensive options for any to attack scenario
- 💻 **Easy to Use** - Simple CLI interface with sensible defaults

---

## ✨ Features

### Core Capabilities

- ⚡ **Asynchronous I/O** - Handle 1000+ concurrent connections efficiently
- 🎯 **Multiple Test Modes** - Request-based or duration-based to attack
- 📊 **Comprehensive Analytics** - Detailed performance metrics and statistics
- 🔄 **Cache Busting** - Bypass all caching layers (CDN, browser, server)
- 🎭 **User-Agent Rotation** - Simulate traffic from different browsers
- 🔒 **SSL/TLS Support** - Test HTTPS endpoints with optional verification
- ⚙️ **Rate Limiting** - Control request rate for gradual load increase
- 🌐 **All HTTP Methods** - GET, POST, PUT, DELETE, PATCH, etc.

### Advanced Features

- **HTTP Keep-Alive** - Connection pooling for better performance
- **Custom Headers** - Add any HTTP headers to requests
- **Request Body Support** - Send JSON, XML, or any payload
- **Percentile Analysis** - 50th, 75th, 90th, 95th, 99th percentiles
- **Data Throughput** - Measure bandwidth usage (MB/s)
- **Error Categorization** - Detailed error tracking and reporting
- **Graceful Interrupts** - Ctrl+C shows partial results
- **Visual Progress** - Real-time statistics with progress bars

### Statistics Provided

- Total requests and duration
- Requests per second (throughput)
- Success/failure rates
- Response time statistics (avg, median, min, max, std dev)
- Percentile distribution
- Status code breakdown
- Data transfer metrics
- Error analysis

---

## 📋 Requirements

- **Python**: 3.7 or higher
- **pip**: Python package manager
- **Operating System**: Windows, Linux, macOS
- **Network**: Stable internet connection for remote to attack

---

## 🔧 Installation

### Method 1: Clone from GitHub (Recommended)

```bash
# Clone the repository
git clone https://github.com/rudraksha-avatara/ddos-load.git

# Navigate to directory
cd ddos-load

# Install dependencies
pip install -r requirements.txt
```

### Method 2: Direct Download

1. Download the repository as ZIP
2. Extract to your desired location
3. Open terminal in the extracted folder
4. Run: `pip install -r requirements.txt`

### Verify Installation

```bash
# Check if tool is working
python main.py --help

# You should see the help menu with all options
```

### Dependencies

The tool requires these Python packages:

- `aiohttp` - Async HTTP client (core)
- `requests` - HTTP library for basic tester
- `aiodns` - Async DNS resolver (optional, for performance)
- `cchardet` - Fast character encoding (optional, for performance)
- `Brotli` - Compression support (optional, for performance)

All dependencies are listed in `requirements.txt` and installed automatically.

---

## 🚀 Quick Start

### Basic Test

```bash
# Test with default settings (1000 requests, 50 concurrent)
python main.py http://localhost:8000
```

### With Cache Busting (Recommended)

```bash
# Bypass all caches for accurate server to attack
python main.py http://localhost:8000 --no-cache
```

### High Load Test

```bash
# 10,000 requests with 100 concurrent connections
python main.py http://localhost:8000 -n 10000 -c 100 --no-cache
```

### Duration-Based Test

```bash
# Run for 60 seconds with 200 concurrent connections
python main.py http://localhost:8000 -d 60 -c 200 --no-cache
```

---

## 📚 Usage Guide

### Command Structure

```bash
python main.py <URL> [OPTIONS]
```

### Essential Options

| Option              | Description              | Example                    |
| ------------------- | ------------------------ | -------------------------- |
| `-n, --requests`    | Total number of requests | `-n 10000`                 |
| `-c, --concurrency` | Concurrent connections   | `-c 100`                   |
| `-d, --duration`    | Test duration in seconds | `-d 60`                    |
| `--no-cache`        | Enable cache busting     | `--no-cache`               |
| `-m, --method`      | HTTP method              | `-m POST`                  |
| `-H, --header`      | Custom header            | `-H "Auth: token"`         |
| `--body`            | Request body             | `--body '{"key":"value"}'` |

### Cache Busting Explained

When you use `--no-cache`, the tool:

1. Adds random parameters to each URL (`?_nocache=xyz&_t=timestamp`)
2. Sends cache-control headers (`Cache-Control: no-cache`)
3. Ensures you're to attack actual server performance, not cached responses

**Always use `--no-cache` when to attack server capacity!**

### to attack Modes

#### 1. Request-Based to attack

```bash
# Send exactly 5000 requests
python main.py http://localhost:8000 -n 5000 -c 100
```

#### 2. Duration-Based to attack

```bash
# Run for 120 seconds (2 minutes)
python main.py http://localhost:8000 -d 120 -c 150
```

---

## 🎮 Command Reference

### All Available Options

```
positional arguments:
  url                      Target URL to test (required)

Load Configuration:
  -n, --requests N         Total number of requests (default: 1000)
  -c, --concurrency N      Number of concurrent connections (default: 50)
  -d, --duration N         Test duration in seconds (overrides -n)
  --rate-limit N           Limit requests per second

HTTP Configuration:
  -m, --method METHOD      HTTP method: GET, POST, PUT, DELETE, etc. (default: GET)
  -H, --header HEADER      Custom header "Key: Value" (can be used multiple times)
  --body BODY              Request body for POST/PUT requests
  --timeout N              Request timeout in seconds (default: 30)

Performance Options:
  --no-cache               Enable cache busting (adds random params + headers)
  --random-ua              Use random User-Agent headers
  --no-keep-alive          Disable HTTP keep-alive connections
  --no-verify-ssl          Disable SSL certificate verification

Other:
  -h, --help               Show help message and exit
```

### Examples for Each Option

```bash
# Number of requests
python main.py http://localhost:8000 -n 5000

# Concurrency level
python main.py http://localhost:8000 -c 200

# Duration-based
python main.py http://localhost:8000 -d 300

# HTTP method
python main.py http://localhost:8000 -m POST

# Custom headers (multiple)
python main.py http://localhost:8000 \
  -H "Authorization: Bearer token123" \
  -H "Content-Type: application/json"

# Request body
python main.py http://localhost:8000 -m POST \
  --body '{"username":"test","password":"test123"}'

# Timeout
python main.py http://localhost:8000 --timeout 60

# Cache busting
python main.py http://localhost:8000 --no-cache

# Random user agents
python main.py http://localhost:8000 --random-ua

# Disable keep-alive
python main.py http://localhost:8000 --no-keep-alive

# Skip SSL verification (for self-signed certs)
python main.py https://localhost:8443 --no-verify-ssl

# Rate limiting
python main.py http://localhost:8000 --rate-limit 100
```

---

## 💡 Examples

### Basic to attack

```bash
# Simple GET request test
python main.py http://localhost:8000 -n 1000 -c 50

# Test with cache busting
python main.py http://localhost:8000 -n 5000 -c 100 --no-cache

# Test specific endpoint
python main.py http://localhost:8000/api/users -n 3000 -c 75 --no-cache
```

### API to attack

```bash
# Test GET API endpoint
python main.py http://localhost:8000/api/products -n 5000 -c 100 \
  -H "Authorization: Bearer your_token_here" \
  --no-cache

# Test POST API (JSON)
python main.py http://localhost:8000/api/users -n 2000 -c 50 \
  -m POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer token123" \
  --body '{"name":"John Doe","email":"john@example.com"}' \
  --no-cache

# Test PUT API
python main.py http://localhost:8000/api/users/123 -n 1000 -c 30 \
  -m PUT \
  -H "Content-Type: application/json" \
  --body '{"status":"active"}' \
  --no-cache

# Test DELETE API
python main.py http://localhost:8000/api/users/123 -n 500 -c 20 \
  -m DELETE \
  -H "Authorization: Bearer token123"
```

### Stress to attack Powerful Servers

```bash
# Moderate load test
python main.py http://localhost:8000 -n 10000 -c 100 --no-cache

# Heavy load test
python main.py http://localhost:8000 -n 50000 -c 300 --no-cache

# Extreme stress test
python main.py http://localhost:8000 -n 100000 -c 500 --no-cache --random-ua

# Maximum capacity test
python main.py http://localhost:8000 -n 200000 -c 1000 --no-cache
```

### Duration-Based to attack

```bash
# 1 minute sustained load
python main.py http://localhost:8000 -d 60 -c 100 --no-cache

# 5 minute endurance test
python main.py http://localhost:8000 -d 300 -c 200 --no-cache

# 30 minute soak test
python main.py http://localhost:8000 -d 1800 -c 150 --no-cache
```

### Real-World Scenarios

```bash
# E-commerce: Product page
python main.py http://localhost:8000/products/laptop-123 \
  -n 15000 -c 200 --no-cache --random-ua

# E-commerce: Checkout API
python main.py http://localhost:8000/api/checkout -n 5000 -c 80 \
  -m POST \
  -H "Content-Type: application/json" \
  --body '{"cart_id":"abc123","payment_method":"card"}' \
  --no-cache

# Social Media: Feed endpoint
python main.py http://localhost:8000/api/feed -n 20000 -c 250 \
  -H "Authorization: Bearer token123" \
  --no-cache

# Search Engine: Search query
python main.py "http://localhost:8000/search?q=laptop" \
  -n 10000 -c 150 --no-cache --random-ua

# Authentication: Login endpoint
python main.py http://localhost:8000/api/auth/login -n 3000 -c 60 \
  -m POST \
  -H "Content-Type: application/json" \
  --body '{"username":"testuser","password":"testpass"}' \
  --no-cache

# File Upload Simulation
python main.py http://localhost:8000/api/upload -n 1000 -c 30 \
  -m POST \
  -H "Content-Type: multipart/form-data" \
  --timeout 60 \
  --no-cache
```

### Advanced Scenarios

```bash
# Rate-limited test (100 req/s)
python main.py http://localhost:8000 -n 10000 -c 50 \
  --rate-limit 100 --no-cache

# HTTPS with self-signed certificate
python main.py https://localhost:8443 -n 5000 -c 100 \
  --no-verify-ssl --no-cache

# Disable keep-alive (new connection each time)
python main.py http://localhost:8000 -n 2000 -c 50 \
  --no-keep-alive --no-cache

# Slow endpoint with increased timeout
python main.py http://localhost:8000/api/slow-process \
  -n 1000 -c 20 --timeout 120 --no-cache

# Combined advanced features
python main.py http://localhost:8000 -n 25000 -c 300 \
  --no-cache --random-ua --rate-limit 500 --timeout 45
```

---

## 📊 Understanding Results

### Sample Output

```
======================================================================
Advanced DDoS Load Tool - Production Ready
======================================================================
Target URL: http://localhost:8000
Method: GET
Concurrency: 100
Total Requests: 10000
Timeout: 30s
Cache Busting: Enabled
Random User-Agent: Enabled
Keep-Alive: Enabled
SSL Verification: Enabled
======================================================================

Starting test at 2024-03-15 14:30:00...

Running request-based test with 10000 requests...

======================================================================
Test Results
======================================================================
Completed in: 22.45 seconds
Total requests: 10000
Successful requests: 9850
Failed requests: 150
Requests per second: 445.43
Average concurrency: 100
Data received: 125.50 MB
Throughput: 5.59 MB/s

======================================================================
Status Code Distribution:
======================================================================
                 200:   9850 ( 98.5%) █████████████████████████████████████████████████
         timeout:    100 (  1.0%) █
  connection_error:     50 (  0.5%)

======================================================================
Response Time Statistics (milliseconds):
======================================================================
  Average:    45.23ms
  Median:     42.10ms
  Std Dev:    12.45ms
  Min:        15.30ms
  Max:       250.80ms

  Percentiles:
    50th:      42.10ms
    75th:      55.20ms
    90th:      68.50ms
    95th:      82.30ms
    99th:     120.40ms

======================================================================
Summary:
======================================================================
  Success Rate (200 OK): 98.50%
  Failed Requests: 150
  Throughput: 445.43 req/s
  Avg Response Time: 45.23ms
======================================================================
```

### Interpreting Metrics

#### Throughput (Requests per Second)

- **< 100 req/s**: Low performance, investigate bottlenecks
- **100-500 req/s**: Moderate performance, typical for small apps
- **500-2000 req/s**: Good performance, well-optimized server
- **> 2000 req/s**: Excellent performance, production-grade

#### Response Times

- **< 50ms**: Excellent - Very fast responses
- **50-200ms**: Good - Acceptable for most applications
- **200-500ms**: Fair - May need optimization
- **> 500ms**: Poor - Significant performance issues

#### Success Rate

- **> 99%**: Excellent - Server handling load well
- **95-99%**: Good - Minor issues under load
- **90-95%**: Fair - Server struggling
- **< 90%**: Poor - Server overloaded

#### Percentiles Explained

- **50th (Median)**: Half of requests are faster than this
- **75th**: 75% of requests are faster than this
- **90th**: 90% of requests are faster than this
- **95th**: 95% of requests are faster than this (important for SLA)
- **99th**: 99% of requests are faster than this (worst-case scenario)

---

## 🎯 Best Practices

### 1. Progressive Load to attack

Always start small and gradually increase load:

```bash
# Step 1: Baseline (10% of target)
python main.py http://localhost:8000 -n 100 -c 10 --no-cache

# Step 2: Light load (25% of target)
python main.py http://localhost:8000 -n 500 -c 25 --no-cache

# Step 3: Moderate load (50% of target)
python main.py http://localhost:8000 -n 2500 -c 50 --no-cache

# Step 4: Heavy load (75% of target)
python main.py http://localhost:8000 -n 7500 -c 100 --no-cache

# Step 5: Peak load (100% of target)
python main.py http://localhost:8000 -n 10000 -c 150 --no-cache

# Step 6: DDoS Attack Stress (150% of target)
python main.py http://localhost:8000 -n 15000 -c 200 --no-cache
```

### 2. Always Use Cache Busting

For accurate server performance to attack:

```bash
# ✅ CORRECT - Tests actual server
python main.py http://localhost:8000 -n 5000 -c 100 --no-cache

# ❌ WRONG - May test cached responses
python main.py http://localhost:8000 -n 5000 -c 100
```

### 3. Monitor Your Server

While to attack, monitor these metrics:

```bash
# CPU usage
top
# or
htop

# Memory usage
free -m

# Network traffic
iftop
# or
nethogs

# Disk I/O
iostat -x 1

# Application logs
tail -f /var/log/your-app.log
```

### 4. Test Different Scenarios

```bash
# Normal traffic (baseline)
python main.py http://localhost:8000 -d 60 -c 50 --no-cache

# Peak hours (2x normal)
python main.py http://localhost:8000 -d 60 -c 100 --no-cache

# Traffic spike (5x normal)
python main.py http://localhost:8000 -n 10000 -c 250 --no-cache

# Sustained heavy load (endurance)
python main.py http://localhost:8000 -d 600 -c 150 --no-cache
```

### 5. Test Critical Endpoints

```bash
# Homepage
python main.py http://localhost:8000 -n 10000 -c 150 --no-cache

# API endpoints
python main.py http://localhost:8000/api/users -n 8000 -c 120 --no-cache

# Database-heavy operations
python main.py http://localhost:8000/api/search -n 5000 -c 80 --no-cache

# Authentication
python main.py http://localhost:8000/api/login -n 3000 -c 60 --no-cache

# Static assets
python main.py http://localhost:8000/static/app.js -n 15000 -c 200
```

### 6. Document Your Results

Create a to attack log:

```bash
# Save results to file
python main.py http://localhost:8000 -n 10000 -c 100 --no-cache > results_$(date +%Y%m%d_%H%M%S).txt

# Or use tee to see and save
python main.py http://localhost:8000 -n 10000 -c 100 --no-cache | tee results.txt
```

### 7. Test Before Deployment

```bash
# Pre-deployment checklist
# 1. Test current production load
python main.py http://staging.example.com -d 300 -c 100 --no-cache

# 2. Test 2x expected load
python main.py http://staging.example.com -d 300 -c 200 --no-cache

# 3. Test spike scenario
python main.py http://staging.example.com -n 50000 -c 500 --no-cache

# 4. Test sustained load
python main.py http://staging.example.com -d 1800 -c 150 --no-cache
```

### 8. Optimize Based on Results

If you see poor performance:

1. **High response times**: Check database queries, add caching
2. **Low throughput**: Increase server resources, optimize code
3. **Many timeouts**: Increase timeout or fix slow operations
4. **Connection errors**: Check server connection limits
5. **Memory issues**: Look for memory leaks, optimize memory usage

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. "Too many open files" Error

**Problem**: System limit on open file descriptors

**Solution**:

```bash
# Linux/Mac - Temporary fix
ulimit -n 10000

# Linux - Permanent fix
# Edit /etc/security/limits.conf and add:
* soft nofile 10000
* hard nofile 10000

# Then logout and login again
```

#### 2. Connection Refused Errors

**Possible Causes**:

- Server is not running
- Wrong URL or port
- Firewall blocking connections
- Server reached connection limit

**Solutions**:

```bash
# Check if server is running
curl http://localhost:8000

# Check if port is open
netstat -an | grep 8000

# Test with lower concurrency
python main.py http://localhost:8000 -n 100 -c 10
```

#### 3. High Timeout Rate

**Possible Causes**:

- Server is overloaded
- Network issues
- Timeout value too low
- Database bottleneck

**Solutions**:

```bash
# Increase timeout
python main.py http://localhost:8000 -n 1000 -c 50 --timeout 60

# Reduce concurrency
python main.py http://localhost:8000 -n 1000 -c 20

# Check server logs for errors
tail -f /var/log/your-app.log
```

#### 4. Low Throughput

**Possible Causes**:

- Network bandwidth limitation
- Client machine too slow
- Missing optional dependencies

**Solutions**:

```bash
# Install performance boosters
pip install aiodns cchardet Brotli

# Test from a more powerful machine
# Or reduce concurrency to match client capacity
python main.py http://localhost:8000 -n 5000 -c 50

# Check network speed
speedtest-cli
```

#### 5. SSL Certificate Errors

**Problem**: SSL verification failing

**Solution**:

```bash
# For self-signed certificates
python main.py https://localhost:8443 -n 1000 -c 50 --no-verify-ssl

# For production, fix the certificate instead
```

#### 6. Memory Issues

**Problem**: Tool consuming too much memory

**Solution**:

```bash
# Reduce concurrency
python main.py http://localhost:8000 -n 10000 -c 50

# Use duration-based to attack instead
python main.py http://localhost:8000 -d 300 -c 50
```

#### 7. Module Not Found Error

**Problem**: Missing dependencies

**Solution**:

```bash
# Reinstall all dependencies
pip install -r requirements.txt

# Or install individually
pip install aiohttp requests aiodns cchardet Brotli
```

#### 8. Slow Test Execution

**Problem**: Test taking too long

**Possible Causes**:

- Rate limiting enabled
- Server is slow
- Network latency

**Solutions**:

```bash
# Remove rate limiting
python main.py http://localhost:8000 -n 5000 -c 100 --no-cache

# Increase concurrency
python main.py http://localhost:8000 -n 5000 -c 200 --no-cache

# Test locally instead of remote
python main.py http://localhost:8000 -n 5000 -c 100 --no-cache
```

### Getting Help

If you're still experiencing issues:

1. Check Python version: `python --version` (should be 3.7+)
2. Verify dependencies: `pip list | grep aiohttp`
3. Test with minimal options: `python main.py http://localhost:8000 -n 10 -c 1`
4. Check server logs for errors
5. Open an issue on GitHub with:
   - Python version
   - Operating system
   - Full command used
   - Complete error message
   - Server logs (if applicable)

---

## ⚡ Performance Tuning

### System-Level Optimization

#### Linux

```bash
# Increase connection limits
sudo sysctl -w net.core.somaxconn=4096
sudo sysctl -w net.ipv4.tcp_max_syn_backlog=4096
sudo sysctl -w net.ipv4.ip_local_port_range="1024 65535"
sudo sysctl -w net.ipv4.tcp_tw_reuse=1
sudo sysctl -w net.ipv4.tcp_fin_timeout=30

# Increase file descriptors
ulimit -n 65535

# Make permanent by adding to /etc/sysctl.conf
```

#### Windows

```powershell
# Increase dynamic port range
netsh int ipv4 set dynamicport tcp start=1025 num=64511

# Reduce TIME_WAIT duration
# Edit registry: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters
# Set TcpTimedWaitDelay to 30 (decimal)
```

#### macOS

```bash
# Increase connection limits
sudo sysctl -w kern.ipc.somaxconn=4096
sudo sysctl -w net.inet.tcp.msl=1000

# Increase file descriptors
ulimit -n 65535
```

### Application-Level Optimization

#### Install Performance Boosters

```bash
# These packages significantly improve performance
pip install aiodns      # Faster DNS resolution
pip install cchardet    # Faster character encoding
pip install Brotli      # Compression support
```

#### Optimal Concurrency

Finding the sweet spot:

```bash
# Test different concurrency levels
for c in 50 100 200 300 500; do
    echo "to attack with concurrency: $c"
    python main.py http://localhost:8000 -n 5000 -c $c --no-cache
    sleep 5
done
```

Typical optimal ranges:

- **Small servers**: 50-100 concurrent
- **Medium servers**: 100-300 concurrent
- **Large servers**: 300-500 concurrent
- **Enterprise servers**: 500-1000+ concurrent

### Network Optimization

```bash
# Test from same network as server
python main.py http://192.168.1.100:8000 -n 10000 -c 200 --no-cache

# Use keep-alive (default, but ensure it's not disabled)
python main.py http://localhost:8000 -n 10000 -c 200 --no-cache

# For local to attack, use localhost instead of 127.0.0.1
python main.py http://localhost:8000 -n 10000 -c 200 --no-cache
```

### Hardware Recommendations

#### Client Machine (Running the tool)

- **CPU**: Multi-core processor (4+ cores recommended)
- **RAM**: 4GB minimum, 8GB+ recommended
- **Network**: Gigabit Ethernet or better
- **Storage**: SSD for better I/O

#### Server Machine (Being tested)

- Monitor CPU, RAM, and network during tests
- Ensure adequate resources for expected load
- Use production-like hardware for accurate results

### Benchmarking Tips

```bash
# Warm-up run (don't count this)
python main.py http://localhost:8000 -n 100 -c 10

# Actual benchmark (run 3 times, take average)
python main.py http://localhost:8000 -n 10000 -c 100 --no-cache
python main.py http://localhost:8000 -n 10000 -c 100 --no-cache
python main.py http://localhost:8000 -n 10000 -c 100 --no-cache
```

---

## ⚖️ Legal & Ethics

### ⚠️ Important Legal Notice

**READ THIS CAREFULLY BEFORE USING THIS TOOL**

This DDoS Load Tool is a powerful instrument that can generate significant traffic to web servers. Misuse of this tool may be illegal and unethical.

### Legal Use Only

#### ✅ You MAY use this tool to:

- Test your own servers and applications
- Test systems where you have explicit written permission
- Conduct authorized penetration to attack
- Perform capacity planning for your infrastructure
- Test staging/development environments you control
- Conduct security assessments with proper authorization

#### ❌ You MUST NOT use this tool to:

- Attack or disrupt third-party websites
- Test systems without explicit permission
- Conduct unauthorized security to attack
- Overload shared hosting environments
- Violate terms of service of any platform
- Cause harm to any system or service

### Legal Consequences

Unauthorized use of this tool may result in:

- **Criminal charges** under computer fraud and abuse laws
- **Civil lawsuits** for damages
- **Service provider bans** and account termination
- **Financial penalties** and legal fees
- **Criminal record** affecting future employment

### Laws That May Apply

- **USA**: Computer Fraud and Abuse Act (CFAA)
- **UK**: Computer Misuse Act 1990
- **EU**: Directive on attacks against information systems
- **International**: Various cybercrime laws

### Ethical Guidelines

1. **Get Permission**: Always obtain written authorization before to attack
2. **Inform Stakeholders**: Notify relevant parties before to attack
3. **Test Responsibly**: Start with low loads and increase gradually
4. **Respect Resources**: Don't waste bandwidth or computing resources
5. **Document Everything**: Keep records of authorization and test results
6. **Report Issues**: Responsibly disclose any vulnerabilities found
7. **Respect Privacy**: Don't collect or expose sensitive data

### Authorization Checklist

Before running any test, ensure you have:

- [ ] Written permission from system owner
- [ ] Approval from hosting provider (if applicable)
- [ ] Notification to relevant team members
- [ ] Scheduled to attack during appropriate time window
- [ ] Backup and rollback plan ready
- [ ] Monitoring in place to detect issues
- [ ] Emergency contact information available

### Disclaimer

This tool is provided "as is" without warranty of any kind. The developers and contributors:

- Are not responsible for any misuse of this tool
- Do not endorse illegal or unethical activities
- Assume no liability for damages caused by use of this tool
- Strongly condemn unauthorized to attack or attacks

**By using this tool, you agree to use it legally and ethically, and accept full responsibility for your actions.**

### Reporting Abuse

If you become aware of someone misusing this tool:

- Report to appropriate authorities
- Contact the system owner being targeted
- Document evidence of misuse

---

## 🆚 Comparison with Other Tools

| Feature              | This Tool        | Apache Bench | JMeter       | Locust      | wrk         | Gatling      |
| -------------------- | ---------------- | ------------ | ------------ | ----------- | ----------- | ------------ |
| **Async I/O**        | ✅ Yes           | ❌ No        | ❌ No        | ✅ Yes      | ✅ Yes      | ✅ Yes       |
| **Easy Setup**       | ✅ Very Easy     | ✅ Easy      | ❌ Complex   | ⚠️ Moderate | ✅ Easy     | ❌ Complex   |
| **Cache Busting**    | ✅ Built-in      | ❌ Manual    | ✅ Yes       | ⚠️ Manual   | ❌ Manual   | ✅ Yes       |
| **High Concurrency** | ✅ 1000+         | ⚠️ Limited   | ✅ Yes       | ✅ Yes      | ✅ Yes      | ✅ Yes       |
| **Detailed Stats**   | ✅ Comprehensive | ⚠️ Basic     | ✅ Extensive | ✅ Good     | ⚠️ Basic    | ✅ Extensive |
| **No GUI Required**  | ✅ CLI Only      | ✅ CLI Only  | ❌ GUI Heavy | ⚠️ Web UI   | ✅ CLI Only | ⚠️ Web UI    |
| **Python-based**     | ✅ Yes           | ❌ C         | ❌ Java      | ✅ Yes      | ❌ C        | ❌ Scala     |
| **Custom Headers**   | ✅ Easy          | ⚠️ Limited   | ✅ Yes       | ✅ Yes      | ✅ Yes      | ✅ Yes       |
| **Request Body**     | ✅ Yes           | ⚠️ Limited   | ✅ Yes       | ✅ Yes      | ✅ Yes      | ✅ Yes       |
| **Real-time Stats**  | ✅ Yes           | ❌ No        | ✅ Yes       | ✅ Yes      | ❌ No       | ✅ Yes       |
| **Learning Curve**   | ✅ Low           | ✅ Low       | ❌ High      | ⚠️ Medium   | ⚠️ Medium   | ❌ High      |
| **Cross-platform**   | ✅ Yes           | ✅ Yes       | ✅ Yes       | ✅ Yes      | ⚠️ Limited  | ✅ Yes       |

### When to Use This Tool

**Choose this tool when you need:**

- Quick and easy load to attack
- Cache busting out of the box
- Python-based solution
- Detailed percentile analysis
- No complex setup or configuration
- Cross-platform compatibility
- High concurrency with low resource usage

**Choose other tools when you need:**

- Complex test scenarios (JMeter, Gatling)
- Distributed load to attack (Locust, Gatling)
- Maximum raw performance (wrk)
- Simple quick tests (Apache Bench)

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute

1. **Report Bugs**: Open an issue with detailed information
2. **Suggest Features**: Share your ideas for improvements
3. **Submit Pull Requests**: Fix bugs or add features
4. **Improve Documentation**: Help make docs clearer
5. **Share Examples**: Contribute real-world usage examples
6. **Write Tests**: Add unit or integration tests

### Development Setup

```bash
# Fork and clone the repository
git clone https://github.com/rudraksha-avatara/ddos-load.git
cd ddos-load

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8 mypy

# Run tests
pytest

# Format code
black *.py

# Lint code
flake8 *.py
```

### Pull Request Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your fork (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small
- Write tests for new features

### Reporting Issues

When reporting bugs, include:

- Python version
- Operating system
- Full command used
- Expected behavior
- Actual behavior
- Error messages (full traceback)
- Steps to reproduce

---

## 📚 Additional Resources

### Documentation

- [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [aiohttp Documentation](https://docs.aiohttp.org/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [Load to attack Best Practices](https://www.nginx.com/blog/ddos-load-best-practices/)

### Related Tools

- [Apache Bench](https://httpd.apache.org/docs/2.4/programs/ab.html) - Simple HTTP benchmarking
- [JMeter](https://jmeter.apache.org/) - Feature-rich load to attack
- [Locust](https://locust.io/) - Python-based distributed load to attack
- [wrk](https://github.com/wg/wrk) - Modern HTTP benchmarking tool
- [Gatling](https://gatling.io/) - Scala-based load to attack

### Learning Resources

- [Understanding Load to attack](https://www.blazemeter.com/blog/performance-to-attack-vs-ddos-load-vs-stress-to-attack)
- [HTTP Performance to attack](https://www.keycdn.com/blog/http-performance-to-attack)
- [Web Performance Optimization](https://web.dev/performance/)

---

## 📞 Support

### Getting Help

- **Issues**: [GitHub Issues](https://github.com/rudraksha-avatara/ddos-load/issues)
- **Discussions**: [GitHub Discussions](https://github.com/rudraksha-avatara/ddos-load/discussions)
- **Email**: [Contact Team Supreme X](https://sx.itisuniqueofficial.com/)

### Community

- Star ⭐ this repository if you find it useful
- Watch 👀 for updates and new features
- Fork 🍴 to create your own version
- Share 📢 with others who might benefit

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary

- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ⚠️ No warranty provided
- ⚠️ No liability accepted

---

## 🙏 Acknowledgments

### Developed By

**Team Supreme X**

### Built With

- [Python](https://www.python.org/) - Programming language
- [aiohttp](https://docs.aiohttp.org/) - Async HTTP client
- [asyncio](https://docs.python.org/3/library/asyncio.html) - Async I/O framework

### Special Thanks

- All contributors who help improve this tool
- The Python community for excellent libraries
- Users who provide feedback and suggestions

---

## 🎉 Quick Start Checklist

Ready to start? Follow these steps:

- [ ] Install Python 3.7 or higher
- [ ] Clone or download this repository
- [ ] Run `pip install -r requirements.txt`
- [ ] Verify: `python main.py --help`
- [ ] Start small: `python main.py http://localhost:8000 -n 100 -c 10`
- [ ] Enable cache busting: Add `--no-cache` flag
- [ ] Gradually increase load
- [ ] Monitor server resources
- [ ] Analyze results and optimize
- [ ] Document your findings

---

## 📈 Roadmap

### Planned Features

- [ ] JSON output format for CI/CD integration
- [ ] CSV export for results
- [ ] Real-time progress bar
- [ ] Distributed to attack support
- [ ] WebSocket to attack
- [ ] GraphQL support
- [ ] Custom plugins system
- [ ] Docker container
- [ ] Web dashboard
- [ ] Historical comparison

### Version History

**v1.0.0** (Current)

- Initial release
- Async I/O support
- Cache busting
- Comprehensive statistics
- Multiple HTTP methods
- Custom headers and body
- Rate limiting
- SSL support

---

## 🌟 Star History

If you find this tool useful, please consider giving it a star ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=rudraksha-avatara/ddos-load&type=Date)](https://star-history.com/#rudraksha-avatara/ddos-load&Date)

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/rudraksha-avatara/ddos-load?style=social)
![GitHub forks](https://img.shields.io/github/forks/rudraksha-avatara/ddos-load?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/rudraksha-avatara/ddos-load?style=social)

---

<div align="center">

**Made with ❤️ by Team Supreme X**

[⬆ Back to Top](#-ddos-load-tool)

</div>

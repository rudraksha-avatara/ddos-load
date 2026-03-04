# 🚀 Production-Ready Load Testing Tool

A professional-grade, high-performance load testing tool designed to stress test powerful servers and web applications. Built with async I/O for maximum throughput and minimal resource usage.

## ✨ Features

### Core Capabilities

- ⚡ **Asynchronous I/O** - Handle 1000+ concurrent connections efficiently
- 🎯 **Multiple Test Modes** - Request-based or duration-based testing
- 📊 **Detailed Analytics** - Comprehensive performance metrics and statistics
- 🔄 **Cache Busting** - Bypass all caching layers for true performance testing
- 🎭 **User-Agent Rotation** - Simulate traffic from different browsers
- 🔒 **SSL Support** - Test HTTPS endpoints with optional verification
- ⚙️ **Rate Limiting** - Control request rate for gradual load increase
- 📈 **Real-time Progress** - Live statistics during test execution

### Advanced Features

- HTTP Keep-Alive connection pooling
- Custom headers and request bodies
- Support for all HTTP methods (GET, POST, PUT, DELETE, etc.)
- Percentile analysis (50th, 75th, 90th, 95th, 99th)
- Data throughput measurement (MB/s)
- Error categorization and reporting
- Graceful interrupt handling (Ctrl+C)

## 📋 Requirements

- Python 3.7 or higher
- pip (Python package manager)

## 🔧 Installation

### Quick Install

```bash
# Clone or download the tool
cd load-testing-tool

# Install dependencies
pip install -r requirements.txt
```

### Manual Install

```bash
# Core dependencies
pip install aiohttp requests

# Optional performance boosters (recommended)
pip install aiodns cchardet Brotli
```

### Verify Installation

```bash
python main.py --help
```

## 🎯 Usage Guide

### Basic Usage

```bash
# Simple test with default settings (1000 requests, 50 concurrent)
python main.py http://localhost:8000

# Specify number of requests and concurrency
python main.py http://localhost:8000 -n 10000 -c 100
```

### Cache Busting (Recommended for Real Testing)

```bash
# Enable cache busting to bypass all caches
python main.py http://localhost:8000 -n 5000 -c 100 --no-cache

# This adds random parameters and cache-control headers to each request
# Example: http://localhost:8000?_nocache=abc123&_t=1234567890
```

### Duration-Based Testing

```bash
# Run for 60 seconds with 200 concurrent connections
python main.py http://localhost:8000 -d 60 -c 200

# Run for 5 minutes with cache busting
python main.py http://localhost:8000 -d 300 -c 150 --no-cache
```

### Testing Powerful Servers

```bash
# High-load test: 50,000 requests with 500 concurrent connections
python main.py http://localhost:8000 -n 50000 -c 500 --no-cache

# Maximum stress test with all features
python main.py http://localhost:8000 -n 100000 -c 1000 --no-cache --random-ua

# Sustained load test for 10 minutes
python main.py http://localhost:8000 -d 600 -c 300 --no-cache
```

### API Testing

```bash
# Test GET endpoint
python main.py http://localhost:8000/api/users -n 10000 -c 100

# Test POST endpoint with JSON body
python main.py http://localhost:8000/api/users -n 5000 -c 50 \
  -m POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer token123" \
  --body '{"name": "test", "email": "test@example.com"}' \
  --no-cache

# Test PUT endpoint
python main.py http://localhost:8000/api/users/1 -n 1000 -c 20 \
  -m PUT \
  -H "Content-Type: application/json" \
  --body '{"status": "active"}'
```

### Advanced Options

```bash
# Rate-limited test (100 requests per second)
python main.py http://localhost:8000 -n 10000 -c 50 --rate-limit 100

# Test with random user agents (simulate different browsers)
python main.py http://localhost:8000 -n 5000 -c 100 --random-ua

# Disable keep-alive (new connection each request)
python main.py http://localhost:8000 -n 1000 -c 50 --no-keep-alive

# Test HTTPS with self-signed certificate
python main.py https://localhost:8443 -n 1000 -c 50 --no-verify-ssl

# Increase timeout for slow endpoints
python main.py http://localhost:8000/slow -n 1000 -c 20 --timeout 60
```

## 📊 Understanding the Output

### Test Configuration

```
======================================================================
Advanced Load Testing Tool - Production Ready
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
```

### Results Breakdown

#### Status Code Distribution

Shows HTTP response codes with visual bars:

```
Status Code Distribution:
======================================================================
                 200:   9850 ( 98.5%) ████████████████████████████████████████████████
         timeout:    100 (  1.0%) ██
  connection_error:     50 (  0.5%) █
```

#### Response Time Statistics

```
Response Time Statistics (milliseconds):
======================================================================
  Average:    45.23ms    # Mean response time
  Median:     42.10ms    # Middle value (50th percentile)
  Std Dev:    12.45ms    # Standard deviation
  Min:        15.30ms    # Fastest response
  Max:       250.80ms    # Slowest response

  Percentiles:
    50th:      42.10ms    # 50% of requests faster than this
    75th:      55.20ms    # 75% of requests faster than this
    90th:      68.50ms    # 90% of requests faster than this
    95th:      82.30ms    # 95% of requests faster than this
    99th:     120.40ms    # 99% of requests faster than this
```

#### Summary

```
Summary:
======================================================================
  Success Rate (200 OK): 98.50%
  Failed Requests: 150
  Throughput: 450.25 req/s
  Avg Response Time: 45.23ms
  Data received: 125.50 MB
  Throughput: 5.25 MB/s
======================================================================
```

## 🎓 Best Practices

### 1. Start Small, Scale Up

```bash
# Step 1: Baseline test
python main.py http://localhost:8000 -n 100 -c 10

# Step 2: Moderate load
python main.py http://localhost:8000 -n 1000 -c 50

# Step 3: Heavy load
python main.py http://localhost:8000 -n 10000 -c 200

# Step 4: Stress test
python main.py http://localhost:8000 -n 50000 -c 500
```

### 2. Use Cache Busting for Accurate Results

Always use `--no-cache` when testing server performance (not CDN):

```bash
python main.py http://localhost:8000 -n 10000 -c 100 --no-cache
```

### 3. Monitor Your Server

While running tests, monitor:

- CPU usage: `top` or `htop`
- Memory: `free -m`
- Network: `iftop` or `nethogs`
- Application logs

### 4. Test Different Scenarios

```bash
# Scenario 1: Normal traffic
python main.py http://localhost:8000 -d 60 -c 50

# Scenario 2: Peak traffic
python main.py http://localhost:8000 -d 60 -c 200

# Scenario 3: Spike traffic
python main.py http://localhost:8000 -n 10000 -c 500

# Scenario 4: Sustained heavy load
python main.py http://localhost:8000 -d 300 -c 300
```

### 5. Test Different Endpoints

```bash
# Homepage
python main.py http://localhost:8000 -n 5000 -c 100 --no-cache

# API endpoint
python main.py http://localhost:8000/api/data -n 5000 -c 100 --no-cache

# Static assets
python main.py http://localhost:8000/static/app.js -n 10000 -c 200

# Database-heavy endpoint
python main.py http://localhost:8000/api/search -n 1000 -c 50 --no-cache
```

## 🔍 Troubleshooting

### "Too many open files" Error

Increase system limits:

```bash
# Linux/Mac
ulimit -n 10000

# Or permanently in /etc/security/limits.conf
* soft nofile 10000
* hard nofile 10000
```

### Connection Refused Errors

- Check if your server is running
- Verify the URL is correct
- Ensure firewall allows connections
- Check server connection limits

### Timeout Errors

- Increase timeout: `--timeout 60`
- Reduce concurrency: `-c 50`
- Check server performance
- Verify network connectivity

### Low Throughput

- Increase concurrency: `-c 200`
- Enable keep-alive (default)
- Install optional dependencies: `pip install aiodns cchardet`
- Check network bandwidth

## 📈 Performance Tuning

### System Optimization

```bash
# Linux: Increase connection limits
sudo sysctl -w net.core.somaxconn=4096
sudo sysctl -w net.ipv4.tcp_max_syn_backlog=4096
sudo sysctl -w net.ipv4.ip_local_port_range="1024 65535"

# Increase file descriptors
ulimit -n 65535
```

### Tool Optimization

```bash
# Install performance boosters
pip install aiodns cchardet Brotli

# Use optimal concurrency (test to find sweet spot)
# Usually: 50-200 for most servers, 500-1000 for powerful servers
python main.py http://localhost:8000 -n 10000 -c 200
```

## 📝 Command Reference

### All Available Options

```
positional arguments:
  url                   Target URL to test

optional arguments:
  -h, --help            Show help message
  -n, --requests N      Total number of requests (default: 1000)
  -c, --concurrency N   Concurrent connections (default: 50)
  -d, --duration N      Test duration in seconds (overrides -n)
  -m, --method METHOD   HTTP method: GET, POST, PUT, DELETE (default: GET)
  -H, --header HEADER   Custom header "Key: Value" (repeatable)
  --body BODY           Request body for POST/PUT
  --timeout N           Request timeout in seconds (default: 30)
  --no-cache            Enable cache busting
  --random-ua           Use random User-Agent headers
  --no-keep-alive       Disable HTTP keep-alive
  --no-verify-ssl       Disable SSL verification
  --rate-limit N        Limit requests per second
```

## 🎯 Real-World Examples

### E-commerce Site Testing

```bash
# Test product page
python main.py http://localhost:8000/products/123 -n 10000 -c 150 --no-cache

# Test checkout API
python main.py http://localhost:8000/api/checkout -n 5000 -c 100 \
  -m POST -H "Content-Type: application/json" \
  --body '{"cart_id": "abc123", "payment": "card"}' --no-cache

# Test search functionality
python main.py http://localhost:8000/search?q=laptop -n 8000 -c 120 --no-cache
```

### API Server Testing

```bash
# Test authentication endpoint
python main.py http://localhost:8000/api/auth/login -n 3000 -c 50 \
  -m POST -H "Content-Type: application/json" \
  --body '{"username": "test", "password": "test123"}' --no-cache

# Test data retrieval
python main.py http://localhost:8000/api/v1/users -n 15000 -c 200 \
  -H "Authorization: Bearer token123" --no-cache

# Test data creation
python main.py http://localhost:8000/api/v1/posts -n 5000 -c 80 \
  -m POST -H "Content-Type: application/json" -H "Authorization: Bearer token123" \
  --body '{"title": "Test", "content": "Test content"}' --no-cache
```

### Microservices Testing

```bash
# Test service A
python main.py http://localhost:8001/health -n 20000 -c 300 --no-cache

# Test service B
python main.py http://localhost:8002/api/data -n 15000 -c 250 --no-cache

# Test service C with rate limiting
python main.py http://localhost:8003/api/process -n 10000 -c 100 \
  --rate-limit 200 --no-cache
```

## ⚠️ Important Warnings

### Legal Notice

- ✅ **DO** test your own servers and applications
- ✅ **DO** get written permission before testing third-party systems
- ❌ **DON'T** test websites you don't own without authorization
- ❌ **DON'T** use this tool for malicious purposes

Unauthorized load testing may be illegal and could result in:

- Criminal charges
- Civil lawsuits
- Service provider bans
- Legal penalties

### Ethical Use

This tool is designed for:

- Performance testing your own applications
- Capacity planning
- Identifying bottlenecks
- Stress testing before production deployment
- Load testing with proper authorization

### Safety Tips

1. Start with low concurrency and gradually increase
2. Monitor your server during tests
3. Test during off-peak hours if possible
4. Have a rollback plan ready
5. Inform your team before testing
6. Check your hosting provider's terms of service

## 🆚 Comparison with Other Tools

| Feature          | This Tool  | Apache Bench | JMeter | Locust |
| ---------------- | ---------- | ------------ | ------ | ------ |
| Async I/O        | ✅         | ❌           | ❌     | ✅     |
| Easy Setup       | ✅         | ✅           | ❌     | ⚠️     |
| Cache Busting    | ✅         | ❌           | ✅     | ⚠️     |
| High Concurrency | ✅ (1000+) | ⚠️ (limited) | ✅     | ✅     |
| Detailed Stats   | ✅         | ⚠️           | ✅     | ✅     |
| No GUI Required  | ✅         | ✅           | ❌     | ⚠️     |
| Python-based     | ✅         | ❌           | ❌     | ✅     |

## 🤝 Support & Contribution

### Getting Help

If you encounter issues:

1. Check the Troubleshooting section
2. Verify your Python version: `python --version`
3. Ensure all dependencies are installed: `pip list`
4. Check server logs for errors

### Tips for Success

- Use Python 3.8+ for best performance
- Install optional dependencies for speed boost
- Run from a machine with good network connectivity
- Close other applications during testing
- Use SSD storage for better I/O performance

## 📄 License

This tool is provided for legitimate load testing purposes only. Use responsibly and ethically.

## 🎉 Quick Start Checklist

- [ ] Install Python 3.7+
- [ ] Run `pip install -r requirements.txt`
- [ ] Verify installation: `python main.py --help`
- [ ] Start with small test: `python main.py http://localhost:8000 -n 100 -c 10`
- [ ] Enable cache busting: Add `--no-cache` flag
- [ ] Gradually increase load
- [ ] Monitor server resources
- [ ] Analyze results and optimize

---

**Remember: With great power comes great responsibility. Use this tool ethically and legally!** 🚀

#!/bin/bash
#
# Test Installation Script
# Verifies that the load testing tool is properly installed
#

echo "DDoS Attack Tool Installation"
echo "======================================="
echo ""

# Test 1: Python version
echo "[1/6] Checking Python version..."
python3 --version
if [ $? -eq 0 ]; then
    echo "✓ Python is installed"
else
    echo "❌ Python not found"
    exit 1
fi
echo ""

# Test 2: Required modules
echo "[2/6] Checking required modules..."
python3 -c "import aiohttp" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✓ aiohttp is installed"
else
    echo "❌ aiohttp not found - run: pip3 install aiohttp"
    exit 1
fi

python3 -c "import requests" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✓ requests is installed"
else
    echo "❌ requests not found - run: pip3 install requests"
    exit 1
fi
echo ""

# Test 3: Optional modules
echo "[3/6] Checking optional modules..."
python3 -c "import aiodns" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✓ aiodns is installed (performance boost)"
else
    echo "⚠ aiodns not installed (optional, but recommended)"
fi

python3 -c "import chardet" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✓ chardet is installed (performance boost)"
else
    echo "⚠ chardet not installed (optional, but recommended)"
fi
echo ""

# Test 4: Script executable
echo "[4/6] Checking if script is executable..."
if [ -x "main-kali-linux.py" ]; then
    echo "✓ Script is executable"
else
    echo "⚠ Script not executable - run: chmod +x main-kali-linux.py"
fi
echo ""

# Test 5: Help command
echo "[5/6] Testing help command..."
python3 main-kali-linux.py --help > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Help command works"
else
    echo "❌ Help command failed"
    exit 1
fi
echo ""

# Test 6: Basic functionality (if user wants)
echo "[6/6] Basic functionality test"
read -p "Run a basic test against httpbin.org? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Running test with 10 requests, 2 concurrent..."
    python3 main-kali-linux.py http://httpbin.org/get -n 10 -c 2
    if [ $? -eq 0 ]; then
        echo "✓ Basic test passed"
    else
        echo "❌ Basic test failed"
        exit 1
    fi
else
    echo "⊘ Skipped basic test"
fi
echo ""

echo "======================================="
echo "✓ All tests passed!"
echo "======================================="
echo ""
echo "The tool is ready to use."
echo ""
echo "Example commands:"
echo "  python3 main-kali-linux.py http://localhost:8000 -n 1000 -c 50"
echo "  python3 main-kali-linux.py http://localhost:8000 -n 5000 -c 100 --no-cache"
echo "  python3 main-kali-linux.py http://localhost:8000 -d 60 -c 100 --no-cache --random-ua"
echo ""

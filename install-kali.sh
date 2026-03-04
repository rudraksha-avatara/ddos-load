#!/bin/bash
#
# Installation Script for Kali Linux
# Advanced Load Testing Tool - Team Supreme X
#
# Usage: ./install-kali.sh
#

set -e

echo "╔═══════════════════════════════════════════════════════════════════════╗"
echo "║                                                                       ║"
echo "║        Advanced Load Testing Tool - Kali Linux Installer             ║"
echo "║                    Developed by Team Supreme X                        ║"
echo "║                                                                       ║"
echo "╚═══════════════════════════════════════════════════════════════════════╝"
echo ""

# Check if running on Kali Linux
if [ -f /etc/os-release ]; then
    if grep -qi "kali" /etc/os-release; then
        echo "✓ Kali Linux detected"
    else
        echo "⚠ Warning: Not running on Kali Linux"
        echo "  This script is optimized for Kali, but should work on other Debian-based systems"
    fi
fi
echo ""

# Check Python version
echo "[*] Checking Python version..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -ge 3 ] && [ "$PYTHON_MINOR" -ge 7 ]; then
    echo "✓ Python $PYTHON_VERSION detected (OK)"
else
    echo "❌ Python 3.7+ required, found $PYTHON_VERSION"
    echo "   Install with: sudo apt install python3.9"
    exit 1
fi
echo ""

# Check pip3
echo "[*] Checking pip3..."
if command -v pip3 &> /dev/null; then
    echo "✓ pip3 is installed"
else
    echo "❌ pip3 not found"
    echo "   Installing pip3..."
    sudo apt update
    sudo apt install -y python3-pip
fi
echo ""

# Install system dependencies
echo "[*] Installing system dependencies..."
sudo apt update
sudo apt install -y python3-dev build-essential libffi-dev gcc
echo "✓ System dependencies installed"
echo ""

# Install Python packages
echo "[*] Installing Python packages..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Python packages installed successfully"
else
    echo "⚠ Some packages failed to install"
    echo "  Trying with --user flag..."
    pip3 install --user -r requirements.txt
fi
echo ""

# Verify installation
echo "[*] Verifying installation..."
python3 -c "import aiohttp; print('✓ aiohttp:', aiohttp.__version__)" 2>/dev/null || echo "❌ aiohttp not installed"
python3 -c "import requests; print('✓ requests:', requests.__version__)" 2>/dev/null || echo "❌ requests not installed"
python3 -c "import aiodns; print('✓ aiodns: OK')" 2>/dev/null || echo "⚠ aiodns not installed (optional)"
python3 -c "import cchardet; print('✓ cchardet: OK')" 2>/dev/null || echo "⚠ cchardet not installed (optional)"
echo ""

# Make scripts executable
echo "[*] Making scripts executable..."
chmod +x advanced_load_tester.py
chmod +x load_tester.py
echo "✓ Scripts are now executable"
echo ""

# Test basic functionality
echo "[*] Testing basic functionality..."
python3 advanced_load_tester.py --help > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ Tool is working correctly"
else
    echo "❌ Tool test failed"
    exit 1
fi
echo ""

# Optional: Create symbolic link
read -p "Create system-wide command 'loadtest'? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    SCRIPT_PATH=$(pwd)/advanced_load_tester.py
    sudo ln -sf "$SCRIPT_PATH" /usr/local/bin/loadtest
    echo "✓ Created command: loadtest"
    echo "  You can now run: loadtest http://target.com -n 1000 -c 50"
fi
echo ""

# Increase file descriptor limit
echo "[*] Checking file descriptor limit..."
CURRENT_LIMIT=$(ulimit -n)
if [ "$CURRENT_LIMIT" -lt 10000 ]; then
    echo "⚠ Current limit: $CURRENT_LIMIT (recommended: 10000+)"
    echo "  To increase temporarily: ulimit -n 10000"
    echo "  To increase permanently, add to ~/.bashrc:"
    echo "    echo 'ulimit -n 10000' >> ~/.bashrc"
else
    echo "✓ File descriptor limit: $CURRENT_LIMIT (OK)"
fi
echo ""

echo "╔═══════════════════════════════════════════════════════════════════════╗"
echo "║                    Installation Complete!                            ║"
echo "╚═══════════════════════════════════════════════════════════════════════╝"
echo ""
echo "Quick Start:"
echo "  python3 advanced_load_tester.py http://localhost:8000 -n 1000 -c 50"
echo ""
echo "With cache busting:"
echo "  python3 advanced_load_tester.py http://localhost:8000 -n 1000 -c 50 --no-cache"
echo ""
echo "For help:"
echo "  python3 advanced_load_tester.py --help"
echo ""
echo "Documentation:"
echo "  README.md - General documentation"
echo "  README-KALI-LINUX.md - Kali Linux specific guide"
echo ""
echo "⚠️  LEGAL NOTICE:"
echo "  Only test systems you own or have explicit written authorization to test."
echo "  Unauthorized testing is illegal and may result in criminal prosecution."
echo ""

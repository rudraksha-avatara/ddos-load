#!/usr/bin/env bash
#
# Kali Linux Installer Script
# DDoS Attack Tool - Team Supreme X
#
# Usage: chmod +x install-kali.sh && ./install-kali.sh
#

set -Eeuo pipefail

# --------- helpers ----------
log()  { echo -e "$*"; }
ok()   { echo -e "✓ $*"; }
warn() { echo -e "⚠ $*"; }
err()  { echo -e "❌ $*" >&2; }

die() { err "$*"; exit 1; }

cleanup() {
  # If venv is active, try to deactivate quietly
  if [[ -n "${VIRTUAL_ENV:-}" ]]; then
    deactivate >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "Missing required command: $1"
}

is_root() { [[ "${EUID:-$(id -u)}" -eq 0 ]]; }

SUDO="sudo"
if is_root; then
  SUDO=""
fi

# --------- banner ----------
log "╔═══════════════════════════════════════════════════════════════════════╗"
log "║                                                                       ║"
log "║              DDoS Attack Tool - Kali Linux Installer                  ║"
log "║                    Developed by Team Supreme X                        ║"
log "║                                                                       ║"
log "╚═══════════════════════════════════════════════════════════════════════╝"
log ""

# Run from script directory (important for relative paths)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# --------- OS check ----------
if [[ -f /etc/os-release ]]; then
  if grep -qi "kali" /etc/os-release; then
    ok "Kali Linux detected"
  else
    warn "Not running on Kali Linux"
    log "  This script is optimized for Kali, but should work on Debian-based systems"
  fi
fi
log ""

# --------- Python check ----------
log "[*] Checking Python version..."
need_cmd python3

PYTHON_VERSION="$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')"
PY_OK="$(python3 -c 'import sys; print(int(sys.version_info >= (3,7)))')"

if [[ "$PY_OK" == "1" ]]; then
  ok "Python ${PYTHON_VERSION} detected (OK)"
else
  die "Python 3.7+ required, found ${PYTHON_VERSION}. Install a newer python3 package."
fi
log ""

# --------- apt + deps ----------
# We need apt on Kali/Debian
need_cmd apt-get

log "[*] Updating apt indexes..."
$SUDO apt-get update -y

log "[*] Installing system dependencies..."
$SUDO apt-get install -y \
  python3-dev \
  python3-venv \
  python3-pip \
  build-essential \
  libffi-dev \
  gcc \
  ca-certificates \
  curl \
  git

ok "System dependencies installed"
log ""

# --------- venv ----------
VENV_DIR="${VENV_DIR:-venv}"

if [[ ! -d "$VENV_DIR" ]]; then
  log "[*] Creating virtual environment at ./${VENV_DIR} ..."
  python3 -m venv "$VENV_DIR"
  ok "Virtual environment created"
else
  ok "Virtual environment already exists"
fi
log ""

log "[*] Activating virtual environment..."
# shellcheck disable=SC1090
source "$VENV_DIR/bin/activate"
ok "venv activated"
log ""

log "[*] Upgrading pip/setuptools/wheel..."
python -m pip install --upgrade pip setuptools wheel
ok "pip upgraded"
log ""

# --------- requirements ----------
REQ_FILE="requirements-kali-linux.txt"
if [[ ! -f "$REQ_FILE" ]]; then
  die "Missing ${REQ_FILE} in ${SCRIPT_DIR}. Please place it next to install-kali.sh"
fi

log "[*] Installing Python packages from ${REQ_FILE} ..."
# Avoid user-site installs inside venv; fail clearly if something breaks.
python -m pip install -r "$REQ_FILE"
ok "Python packages installed successfully"
log ""

# --------- verify imports ----------
log "[*] Verifying installation..."
python -c "import aiohttp; print('✓ aiohttp:', aiohttp.__version__)" 2>/dev/null || warn "aiohttp not installed"
python -c "import requests; print('✓ requests:', requests.__version__)" 2>/dev/null || warn "requests not installed"
python -c "import aiodns; print('✓ aiodns: OK')" 2>/dev/null || warn "aiodns not installed (optional)"
python -c "import chardet; print('✓ chardet: OK')" 2>/dev/null || warn "chardet not installed (optional)"
log ""

# --------- scripts executable ----------
log "[*] Making scripts executable..."
MAIN_SCRIPT="main-kali-linux.py"
LOAD_SCRIPT="load_tester.py"

[[ -f "$MAIN_SCRIPT" ]] || warn "Missing ${MAIN_SCRIPT} (skip chmod)"
[[ -f "$LOAD_SCRIPT" ]] || warn "Missing ${LOAD_SCRIPT} (skip chmod)"

[[ -f "$MAIN_SCRIPT" ]] && chmod +x "$MAIN_SCRIPT" || true
[[ -f "$LOAD_SCRIPT" ]] && chmod +x "$LOAD_SCRIPT" || true
ok "Script permissions updated"
log ""

# --------- basic test ----------
if [[ -f "$MAIN_SCRIPT" ]]; then
  log "[*] Testing basic functionality..."
  python "$MAIN_SCRIPT" --help >/dev/null
  ok "Tool is working correctly"
  log ""
else
  warn "Skipping tool test because ${MAIN_SCRIPT} not found"
  log ""
fi

# --------- optional symlink ----------
if [[ -f "$MAIN_SCRIPT" ]]; then
  read -r -p "Create system-wide command 'loadtest'? (y/n) " REPLY
  if [[ "${REPLY:-n}" =~ ^[Yy]$ ]]; then
    if [[ -z "$SUDO" ]]; then
      warn "You are running as root; will create symlink directly."
    fi
    SCRIPT_PATH="${SCRIPT_DIR}/${MAIN_SCRIPT}"
    $SUDO ln -sf "$SCRIPT_PATH" /usr/local/bin/loadtest
    ok "Created command: loadtest"
    log "  You can now run: loadtest http://target.com -n 1000 -c 50"
  fi
  log ""
fi

# --------- ulimit hint ----------
log "[*] Checking file descriptor limit..."
CURRENT_LIMIT="$(ulimit -n)"
if [[ "$CURRENT_LIMIT" -lt 10000 ]]; then
  warn "Current limit: ${CURRENT_LIMIT} (recommended: 10000+ for high concurrency)"
  log "  Temporary (current shell): ulimit -n 10000"
  log "  Permanent (bash): echo 'ulimit -n 10000' >> ~/.bashrc"
else
  ok "File descriptor limit: ${CURRENT_LIMIT} (OK)"
fi
log ""

# --------- done ----------
log "╔═══════════════════════════════════════════════════════════════════════╗"
log "║                    Installation Complete!                             ║"
log "╚═══════════════════════════════════════════════════════════════════════╝"
log ""
log "Quick Start:"
log "  source ${VENV_DIR}/bin/activate"
log "  python ${MAIN_SCRIPT} http://localhost:8000 -n 1000 -c 50"
log ""
log "With cache busting:"
log "  python ${MAIN_SCRIPT} http://localhost:8000 -n 1000 -c 50 --no-cache"
log ""
log "For help:"
log "  python ${MAIN_SCRIPT} --help"
log ""
log "Documentation:"
log "  README.md - General documentation"
log "  README-KALI-LINUX.md - Kali Linux specific guide"
log ""
log "⚠️  LEGAL NOTICE:"
log "  Only test systems you own or have explicit written authorization to test."
log "  Unauthorized testing is illegal and may result in criminal prosecution."
log ""

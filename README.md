# EmBomber 

[![python](https://img.shields.io/badge/Python-3.x-green.svg?style=flat-square)](https://www.python.org/downloads/) ![version](https://img.shields.io/badge/Build-Final-blue.svg) ![license](https://img.shields.io/badge/License-GPL_3-orange.svg?style=flat-square)

Python Script for Email Bombing which supports Gmail, Yahoo, Hotmail/Outlook. For 100% educational purposes only.

## Features
- Supports Gmail, Yahoo, Hotmail/Outlook
- Optional random variations in subject/body to reduce spam detection
- Random delays between sends (0.1-3.0s)
- Secure credential storage with encryption
- Modern Python 3.x compatibility

## Dependencies

The script requires Python 3.x and the following packages:
- `cryptography` (for secure credential storage)

### Installation Instructions

#### Ubuntu/Linux Mint/Kali Linux
```bash
sudo apt update
sudo apt install python3 python3-pip python3-cryptography
```

#### Fedora
```bash
sudo dnf update
sudo dnf install python3 python3-pip python3-cryptography
```

#### Arch Linux
```bash
sudo pacman -Syu
sudo pacman -S python python-pip python-cryptography
```

Alternatively, you can install dependencies via pip on any distribution:
```bash
pip3 install cryptography
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/angrycoder12/EmBomber.git
cd EmBomber
```

2. Install dependencies (choose your distro's method above)

## Usage

Run the script:
```bash
python3 EmBomber.py
```

### Features Guide

1. **Email Service Selection**:
   - Choose between Gmail, Yahoo, or Hotmail/Outlook
   - Follow prompts to enter credentials
   - Option to save credentials securely

2. **Message Configuration**:
   - Enter recipient, subject, and message
   - Choose whether to add random variations
   - Set number of emails to send

3. **Credential Storage**:
   - Optional encrypted storage of credentials
   - Protected with a passphrase
   - Saved in `~/.embomber_creds` with secure permissions



## Note
- You need to enable less secure apps or use app passwords for Gmail and Yahoo
- For Gmail: https://myaccount.google.com/lesssecureapps
- For Yahoo: Create an app password in account security settings
- This tool is for educational purposes only

## Security Notes
- Credentials are encrypted using industry-standard PBKDF2 and Fernet encryption
- Files are stored with restricted permissions (0o600)
- Passphrases are never stored
- Salt is stored separately in `~/.embomber_salt`

## Before use
- This tool is for 100% LEGAL purposes ONLY. I am NOT responsible for any misuse or un-lawful use.
- This tool was tested on voulanteers, not victims; be responsible.


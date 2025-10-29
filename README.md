# EmBomber 

[![python](https://img.shields.io/badge/Python-3.x-green.svg?style=flat-square)](https://www.python.org/downloads/) ![version](https://img.shields.io/badge/Build-Final-blue.svg) ![license](https://img.shields.io/badge/License-GPL_3-orange.svg?style=flat-square)

Python Script for Email Bombing (spam) which supports Gmail, Yahoo, Hotmail/Outlook. For 100% educational purposes only, and I am NOT responsible for any misuse, as this is only designed to be used on people who are aware of what it can do, and approve of it. 

## Features
- supports Gmail, Yahoo, Hotmail/Outlook
- optional random variations in subject/body to reduce spam detection
- random delays between sends (0.1-3.0s)
- secure credential storage with encryption
- modern Python 3.x compatibility
## Dependencies

the script requires Python 3.x and these packages:
- `cryptography` (for secure encripted password storage)

### Install Instructions

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
```i use arch btw
sudo pacman -Syu
sudo pacman -S python python-pip python-cryptography
```

you can also install dependencies via pip on any distribution (other than arch):
```bash
pip3 install cryptography
```

## Installation

1. clone the repo:
```bash
git clone https://github.com/angrycoder12/EmBomber.git
cd EmBomber
```

2. install the dependencies (choose your distro's method above)

## Usage

Run the script:
```bash
python3 EmBomber.py
```

### Features Guide

1. **Email Service Selection**:
   - choose between Gmail, Yahoo, or Hotmail/Outlook
   - follow prompts to enter credentials
   - option to save credentials securely

2. **Message Configuration**:
   - enter recipiant, subject, and message
   - choose whether you want to add random variations to each email (harder to detect)
   - set a number of emails to send

3. **Password Storage**:
   - optional encryption for credentials
   - protected with a passphrase
   - always saved in `~/.embomber_creds`



## Note
- You need to enable less secure apps or use app passwords for Gmail and Yahoo
- For Gmail: Enable two factor authentication in settings then create an app password
- For Yahoo: Create an app password in account security settings
- This tool is for educational purposes only
- Gmail does not let you send more than 500 messages to one person

## Security Notes
- Credentials are encrypted using industry-standard PBKDF2 and Fernet encryption
- Files are stored with restricted permissions (0o600)
- Passphrases are never stored
- Salt is stored separately in `~/.embomber_salt`

## Before use
- This tool is for 100% LEGAL purposes ONLY. I am NOT responsible for any misuse or un-lawful use.
- This tool was tested on voulanteers, not victims; be responsible.


#!/usr/bin/env python3
import smtplib
import time
import os
import getpass
import sys
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    ENCRYPTION_AVAILABLE = True
except ImportError:
    ENCRYPTION_AVAILABLE = False

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def bomb():
	os.system('clear')
	print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⣠⠀⠀⠀⠀⠀⠀⣠⣴⠖⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣦⣀⡀⠀⠀⠀⢲⣄⠀⢸⡏⡇⣠⡟⠀⠀⣀⣤⣶⡿⠛⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣶⣤⣄⡹⣷⣼⡇⣿⣿⣧⣴⣿⣿⠟⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣀⣀⡀⣀⢀⠀⠀⠀⠈⠙⠻⣿⡛⠿⣿⣿⣿⣿⣿⣿⣥⣄⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠻⠿⠿⣿⣿⣟⣛⣛⣛⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡶⠆    _______       _                 _                    ______  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠤⠤⢤⣤⣀⠀⣠⣴⣿⣿⣿⣶⣦⣤⡭⢙⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣍⠉⠀⠀⠀⠀⠀   (_______)     | |               | |                  (_____ \ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣶⠀⢠⢻⣿⣷⣶⣶⡿⢫⣾⣿⣿⣿⣿⡿⠛⠋⢡⡶⠟⢻⣿⣿⣿⣿⣿⣿⣿⡟⠻⢿⣷⣦⣀⠀⠀⠀    _____   ____ | | _   ___  ____ | | _   ____  ____     ____) )
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⠿⢿⣿⣿⣿⣿⠃⢰⣿⣦⡙⢿⣿⣿⡀⣿⣿⣿⣿⠟⣱⣄⠀⠀⠀⠀⢠⣿⡿⠋⢸⣿⣿⢹⣿⣿⠀⠀⠀⠈⠉⠃⠀⠀   |  ___) |    \| || \ / _ \|    \| || \ / _  )/ ___)   /_____/ 
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⡿⠋⠀⠀⣀⣿⣿⣿⡇⢠⣿⣿⣿⣿⣦⣙⠿⣿⣮⣙⣛⣡⣾⣿⣿⣧⠀⠀⣰⣿⠏⠀⠀⢸⣿⣿⠀⢹⣿⡆⠀⠀⠀⠀⠀⠀⠀   | |_____| | | | |_) ) |_| | | | | |_) | (/ /| |       _______ 
⠀⠀⠀⠀⠀⢀⣴⣾⠿⠛⠛⢿⣧⣤⣴⣾⣿⣿⣿⣿⣇⠀⢿⣿⣿⣿⣿⣿⣷⣦⣍⣛⠻⠿⣿⣿⣿⡿⠁⣸⠟⠁⠀⠀⠀⢸⣿⣿⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀   |_______)_|_|_|____/ \___/|_|_|_|____/ \____)_|      (_______)
⠀⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⡾⢀⠈⠉⠀⠀⠀⠀⠀⢸⣿⡟⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⡟⠁⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡈⠙⠿⣿⣿⣿⣿⣿⣿⣿⡟⠀⣼⣇⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣸⡿⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣄⣈⡉⠛⠛⠛⠋⣀⣼⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢰⣿⣇⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀Author: Parker Bock
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                   ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    `--' ''')


os.system('clear')
try:
    file1 = open('Banner.txt', 'r')
    print(' ')
    print(bcolors.OKGREEN + file1.read() + bcolors.ENDC)
    file1.close()
except IOError:
    print('Banner File not found')


# Credentials file helpers
CREDS_PATH = os.path.expanduser('~/.embomber_creds')
SALT_FILE = os.path.expanduser('~/.embomber_salt')

def get_or_create_salt():
    """Get existing salt or create and save a new one"""
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, 'rb') as f:
            return f.read()
    # Generate new salt
    salt = os.urandom(16)
    # Save with restricted permissions
    umask_original = os.umask(0o177)
    try:
        with open(SALT_FILE, 'wb') as f:
            f.write(salt)
        os.chmod(SALT_FILE, 0o600)
    except Exception:
        pass
    finally:
        os.umask(umask_original)
    return salt

def get_key_from_passphrase(passphrase: str):
    """Derive an encryption key from the passphrase"""
    if not ENCRYPTION_AVAILABLE:
        return None
    salt = get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(passphrase.encode()))
    return key

def save_credentials(email: str, password: str):
    """Save credentials, encrypted if cryptography is available"""
    try:
        if ENCRYPTION_AVAILABLE:
            print(bcolors.OKGREEN + "Enter a passphrase to encrypt your credentials: " + bcolors.ENDC, end='', flush=True)
            passphrase = getpass.getpass('')
            if not passphrase:
                return False
            
            # Encrypt the password
            key = get_key_from_passphrase(passphrase)
            f = Fernet(key)
            encrypted_pwd = f.encrypt(password.encode()).decode()
            data = {'email': email, 'password': encrypted_pwd, 'encrypted': True}
        else:
            # Fallback to plaintext if cryptography not available
            data = {'email': email, 'password': password, 'encrypted': False}
            
        # write file with restricted permissions
        umask_original = os.umask(0o177)
        with open(CREDS_PATH, 'w') as f:
            json.dump(data, f)
        os.umask(umask_original)
        # ensure file is only user-readable/writable
        try:
            os.chmod(CREDS_PATH, 0o600)
        except Exception:
            pass
        return True
    except Exception as e:
        print(f"Error saving credentials: {str(e)}")
        return False

def load_credentials():
    """Load credentials, decrypting if necessary"""
    if not os.path.exists(CREDS_PATH):
        return None
    try:
        with open(CREDS_PATH, 'r') as f:
            data = json.load(f)
            
        email = data.get('email')
        password = data.get('password')
        encrypted = data.get('encrypted', False)
        
        if encrypted and ENCRYPTION_AVAILABLE:
            print(bcolors.OKGREEN + "Enter passphrase to decrypt credentials: " + bcolors.ENDC, end='', flush=True)
            passphrase = getpass.getpass('')
            if not passphrase:
                return None
                
            try:
                key = get_key_from_passphrase(passphrase)
                f = Fernet(key)
                password = f.decrypt(password.encode()).decode()
            except Exception:
                print(bcolors.FAIL + "Invalid passphrase or corrupted credentials" + bcolors.ENDC)
                return None
                
        return email, password
    except Exception as e:
        print(f"Error loading credentials: {str(e)}")
        return None

#Input
print(bcolors.WARNING + '''
Choose a Mail Service:
1) Gmail
2) Yahoo
3) Hotmail/Outlook
''' + bcolors.ENDC + '--------------------------------------------------------------')
try:
    server = input(bcolors.OKGREEN + 'Mail Server: ' + bcolors.ENDC)
    # offer to use saved credentials if available
    saved = load_credentials()
    if saved:
        use_saved = input(bcolors.OKGREEN + f'Use saved credentials for {saved[0]}? (y/n): ' + bcolors.ENDC).strip().lower()
        if use_saved == 'y':
            user, pwd = saved
        else:
            user = input(bcolors.OKGREEN + 'Your Email: ' + bcolors.ENDC)
            pwd = getpass.getpass(bcolors.OKGREEN + 'Password: ' + bcolors.ENDC)
    else:
        user = input(bcolors.OKGREEN + 'Your Email: ' + bcolors.ENDC)
        pwd = getpass.getpass(bcolors.OKGREEN + 'Password: ' + bcolors.ENDC)
    to = input(bcolors.OKGREEN + 'To: ' + bcolors.ENDC)
    subject = input(bcolors.OKGREEN + 'Subject (Optional): ' + bcolors.ENDC)
    body = input(bcolors.OKGREEN + 'Message: ' + bcolors.ENDC)
    # Ask if user wants variation added to subject and body
    variation = input(bcolors.OKGREEN + "Add variation to each email? (y/n): " + bcolors.ENDC).strip().lower()
    if variation not in ('y', 'n'):
        variation = 'n'
    nomes = int(input(bcolors.OKGREEN + 'Number of Emails to send: ' + bcolors.ENDC))
    no = 0
    
    # Prepare base values; actual MIME message will be constructed per-send so we can vary subject/body
    base_subject = subject
    base_body = body
    variation_flag = (variation == 'y')
    # After entry, if user didn't use saved creds, ask if they want to save these
    if not saved:
        try:
            save_choice = input(bcolors.OKGREEN + 'Save these credentials for next time? (y/n): ' + bcolors.ENDC).strip().lower()
            if save_choice == 'y':
                ok = save_credentials(user, pwd)
                if ok:
                    print(bcolors.OKGREEN + f'Credentials saved to {CREDS_PATH}' + bcolors.ENDC)
                else:
                    print(bcolors.FAIL + 'Failed to save credentials' + bcolors.ENDC)
        except Exception:
            pass
except KeyboardInterrupt:
    print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
    sys.exit()

#Gmail
if server == '1' or server == 'gmail' or server == 'Gmail':
    bomb()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    try:
        server.login(user, pwd)
    except smtplib.SMTPAuthenticationError:
        print(bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
        Or you need to enable less secure apps
        On Gmail: https://myaccount.google.com/lesssecureapps ''' + bcolors.ENDC)
        sys.exit()
    while no != nomes:
        try:
            # Build per-send message so we can append small random variation if requested
            msg = MIMEMultipart()
            msg['From'] = user
            msg['To'] = to

            send_subject = base_subject
            send_body = base_body
            if variation_flag:
                # add 1-3 random characters (numbers or symbols) to subject and body
                import random, string
                extras_len = random.randint(1, 3)
                # choose from digits and a set of symbols
                symbols = '0123456789!@#$%&*'
                extras = ''.join(random.choice(symbols) for _ in range(extras_len))
                send_subject = f"{base_subject} {extras}" if base_subject else extras
                send_body = f"{base_body}\n\n{extras}" if base_body else extras

            msg['Subject'] = send_subject
            msg.attach(MIMEText(send_body, 'plain'))

            # short random delay before sending to reduce detection risk (0.1 to 3.0 seconds)
            import random
            delay = random.uniform(0.1, 3.0)
            time.sleep(delay)

            server.send_message(msg)
            print(bcolors.WARNING + f'Successfully sent {no+1} emails (delay {delay:.2f}s)' + bcolors.ENDC)
            no += 1
            time.sleep(.8)
        except KeyboardInterrupt:
            print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
            sys.exit()
        except Exception as e:
            print(f"Failed to Send: {str(e)}")
    server.close()
    
#Yahoo
elif server == '2' or server == 'Yahoo' or server == 'yahoo':
    server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
    bomb()
    server.starttls()
    try:
        server.login(user, pwd)
    except smtplib.SMTPAuthenticationError:
        print(bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
        Most likely you need to enable 2 factor authentication on your account, and create a app password. (this can be found by searching "app password" in your account settings)
        On Yahoo: https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps
        ''' + bcolors.ENDC)
        sys.exit()
    while no != nomes:
        try:
            # Build per-send message
            msg = MIMEMultipart()
            msg['From'] = user
            msg['To'] = to

            send_subject = base_subject
            send_body = base_body
            if variation_flag:
                import random
                symbols = '0123456789!@#$%&*'
                extras_len = random.randint(1, 3)
                extras = ''.join(random.choice(symbols) for _ in range(extras_len))
                send_subject = f"{base_subject} {extras}" if base_subject else extras
                send_body = f"{base_body}\n\n{extras}" if base_body else extras

            msg['Subject'] = send_subject
            msg.attach(MIMEText(send_body, 'plain'))

            # short random delay before sending (0.1-3.0s)
            import random
            delay = random.uniform(0.1, 3.0)
            time.sleep(delay)

            server.send_message(msg)
            print(bcolors.WARNING + f'Successfully sent {no + 1} emails (delay {delay:.2f}s)' + bcolors.ENDC)
            no += 1
            time.sleep(.8)
        except KeyboardInterrupt:
            print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
            sys.exit()
        except Exception as e:
            print(f"Failed to Send: {str(e)}")
    server.close()
    
#Hotmail/Outlook
elif server == '3' or server == 'outlook' or server == 'Outlook' or server == 'Hotmail' or server == 'hotmail':
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    bomb()
    server.ehlo()
    server.starttls()
    try:
        server.login(user, pwd)
    except smtplib.SMTPAuthenticationError:
        print(bcolors.FAIL + 'Your Username or Password is incorrect, please try again using the correct credentials' + bcolors.ENDC)
        sys.exit()
    while no != nomes:
        try:
            # Build per-send message
            msg = MIMEMultipart()
            msg['From'] = user
            msg['To'] = to

            send_subject = base_subject
            send_body = base_body
            if variation_flag:
                import random
                symbols = '0123456789!@#$%&*'
                extras_len = random.randint(1, 3)
                extras = ''.join(random.choice(symbols) for _ in range(extras_len))
                send_subject = f"{base_subject} {extras}" if base_subject else extras
                send_body = f"{base_body}\n\n{extras}" if base_body else extras

            msg['Subject'] = send_subject
            msg.attach(MIMEText(send_body, 'plain'))

            # short random delay before sending (0.1-3.0s)
            import random
            delay = random.uniform(0.1, 3.0)
            time.sleep(delay)

            server.send_message(msg)
            print(bcolors.WARNING + f'Successfully sent {no + 1} emails (delay {delay:.2f}s)' + bcolors.ENDC)
            no += 1
            time.sleep(.8)
        except KeyboardInterrupt:
            print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
            sys.exit()
        except smtplib.SMTPAuthenticationError:
            print('\nThe username or password you entered is incorrect.')
            sys.exit()
        except Exception as e:
            print(f"Failed to Send: {str(e)}")
    server.close()
    
else:
    print('Works only with Gmail, Yahoo, Outlook and Hotmail.')
    sys.exit()

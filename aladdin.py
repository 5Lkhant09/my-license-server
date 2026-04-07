import requests, re, urllib3, time, threading, os, random, hashlib, platform, ssl, json
import subprocess
from urllib.parse import urlparse, parse_qs, urljoin
from datetime import datetime

# --- SSL Error & Warnings Bypass ---
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- CONFIGURATION (နဂိုအတိုင်း သင့် Link ကိုသာ သုံးထားသည်) ---
KEY_URL = "https://raw.githubusercontent.com/5Lkhant09/my-license-server/main/key.txt"
LICENSE_FILE = ".aladdin_v11.lic" 

def get_hwid():
    ID_STORAGE = ".device_id"
    if os.path.exists(ID_STORAGE):
        with open(ID_STORAGE, "r") as f:
            return f.read().strip()

    try:
        serial = subprocess.check_output("getprop ro.serialno", shell=True).decode().strip()
        if not serial or serial == "unknown" or "012345" in serial:
            serial = subprocess.check_output("settings get secure android_id", shell=True).decode().strip()
        if not serial:
            import uuid
            serial = str(uuid.getnode())
        raw_hash = hashlib.md5(serial.encode()).hexdigest()[:10].upper()
        new_id = f"TRB-{raw_hash}"
    except:
        new_id = f"TRB-{hashlib.md5(str(os.getlogin()).encode()).hexdigest()[:10].upper()}"

    with open(ID_STORAGE, "w") as f:
        f.write(new_id)
    return new_id

def banner():
    os.system('clear')
    print("\033[93m" + " ="*35)
    print("\033[96m" + """
      █████╗ ██╗      █████╗ ██████╗ ██████╗ ██╗███╗   ██╗
     ██╔══██╗██║     ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║
     ███████║██║     ███████║██║  ██║██║  ██║██║██╔██╗ ██║
     ██╔══██║██║     ██╔══██║██║  ██║██║  ██║██║██║╚██╗██║
     ██║  ██║███████╗██║  ██║██████╔╝██████╔╝██║██║ ╚████║
     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝
    """)
    print("\033[95m" + "        ✨ Aladdin Starlink Bypass - IMMORTAL V11 ✨")
    print("\033[93m" + " ="*35 + "\033[0m\n")

def save_license(hwid, key, expiry):
    data = {"id": hwid, "key": key, "expiry": expiry}
    with open(LICENSE_FILE, "w") as f:
        json.dump(data, f)

def load_license():
    if os.path.exists(LICENSE_FILE):
        try:
            with open(LICENSE_FILE, "r") as f:
                return json.load(f)
        except:
            return None
    return None

def check_license():
    hwid = get_hwid()
    banner()
    
    local_data = load_license()
    if local_data and local_data.get("id") == hwid:
        try:
            expiry_date = datetime.strptime(local_data["expiry"], "%d-%m-%Y")
            if datetime.now() < expiry_date:
                print(f"\033[92m[✓] AUTO-LOGIN SUCCESS! (Offline Mode)\033[0m")
                print(f"\033[94m[*] EXPIRY: {local_data['expiry']}\033[0m")
                time.sleep(1.5)
                return True
        except: pass

    print(f"\033[94m[*] YOUR DEVICE ID: {hwid}\033[0m")
    input_key = input("\033[93m[>] ENTER ACCESS KEY: \033[0m").strip()
    
    print("\033[93m[*] Verifying license online...\033[0m")
    try:
        response = requests.get(KEY_URL, timeout=10, verify=False, headers={'Cache-Control': 'no-cache'}).text
        lines = response.splitlines()
        
        for line in lines:
            if "|" in line:
                parts = line.split("|")
                if len(parts) == 3:
                    db_id, db_key, db_date = [p.strip() for p in parts]
                    if db_id == hwid and db_key == input_key:
                        expiry_date = datetime.strptime(db_date, "%d-%m-%Y")
                        if datetime.now() < expiry_date:
                            save_license(hwid, input_key, db_date)
                            print(f"\033[92m[✓] ACCESS GRANTED! EXPIRY: {db_date}\033[0m")
                            time.sleep(2)
                            return True
                        else:
                            print("\033[91m[!] KEY EXPIRED! PLEASE RENEW.\033[0m")
                            return False
        
        print("\033[91m[!] INVALID KEY OR DEVICE ID NOT REGISTERED.\033[0m")
        return False
    except Exception as e:
        print(f"\033[91m[!] CONNECTION ERROR! CHECK INTERNET.\033[0m")
        return False

# --- MAIN ---
if __name__ == "__main__":
    if check_license():
        print("\033[92m[+] Aladdin Tool is Starting...\033[0m")
    else:
        exit()

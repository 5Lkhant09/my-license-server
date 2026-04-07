import os, requests, time, subprocess
from datetime import datetime
from ntplib import NTPClient

# ပိုလန်းတဲ့ ID ထုတ်နည်း (Android ID ကို သုံးပါမယ်)
def get_hwid():
    try:
        # Termux မှာ android_id ကို လှမ်းတောင်းကြည့်မယ်
        id = subprocess.check_output(['settings', 'get', 'secure', 'android_id']).decode().strip()
        return f"TRB-{id.upper()[:10]}"
    except:
        # တကယ်လို့ settings ထဲကဆွဲမရရင် တခြားနည်းနဲ့ ထုတ်မယ်
        import platform
        node = platform.node().upper()
        if "LOCALHOST" in node or not node:
            node = "USER" + str(os.getuid())
        return f"TRB-{node[:10]}"

def banner():
    os.system('clear')
    print("\033[94m" + "■" * 45)
    print("      🛡️  ALADDIN STARLINK BYPASS V11  🛡️      ")
    print("         STATUS: [ \033[92mONLINE\033[94m ]             ")
    print("■" * 45 + "\033[0m")

def get_net_time():
    try:
        client = NTPClient()
        response = client.request('pool.ntp.org', version=3)
        return datetime.fromtimestamp(response.tx_time)
    except:
        return datetime.now()

def check_license():
    hwid = get_hwid()
    banner()
    print(f"\033[93m[>] YOUR DEVICE ID: \033[97m{hwid}\033[0m")
    print("\033[94m" + "—" * 45 + "\033[0m")
    
    key_input = input("\033[96m[?] ENTER ACCESS KEY: \033[0m").strip()
    
    url = "https://raw.githubusercontent.com/5Lkhant09/my-license-server/main/key.txt"
    try:
        resp = requests.get(url).text
        for line in resp.splitlines():
            if hwid in line and key_input in line:
                parts = line.split('|')
                expiry_str = parts[2]
                expiry_date = datetime.strptime(expiry_str, "%d-%m-%Y %H:%M")
                
                if get_net_time() < expiry_date:
                    print(f"\033[92m\n[✓] ACCESS GRANTED! \033[0m")
                    print(f"\033[92m[•] EXPIRY DATE: {expiry_str}\033[0m")
                    time.sleep(2)
                    return True
                else:
                    print("\033[91m\n[!] KEY HAS EXPIRED!\033[0m")
                    return False
        
        print("\033[91m\n[!] INVALID KEY FOR THIS DEVICE!\033[0m")
        return False
    except Exception as e:
        print(f"\033[91m\n[!] CONNECTION ERROR: {e}\033[0m")
        return False

if __name__ == "__main__":
    if check_license():
        print("\033[94m" + "—" * 45 + "\033[0m")
        print("\033[92m[*] SYSTEM IS ACTIVE & BYPASSING...\033[0m")
        while True:
            time.sleep(10)
                    

import os, requests, time, platform
from datetime import datetime
from ntplib import NTPClient

# Banner ပုံစံလေး
def banner():
    os.system('clear')
    print("\033[94m" + "="*40)
    print("    ALADDIN STARLINK BYPASS V11    ")
    print("      STATUS: [ ONLINE ]          ")
    print("="*40 + "\033[0m")

# Device ID (HWID) ထုတ်ယူခြင်း
def get_hwid():
    return f"TRB-{platform.node().upper()[:10]}"

# အချိန်အမှန် (Internet Time) ရယူခြင်း
def get_net_time():
    try:
        client = NTPClient()
        response = client.request('pool.ntp.org', version=3)
        return datetime.fromtimestamp(response.tx_time)
    except:
        return datetime.now()

# License စစ်ဆေးခြင်း
def check_license():
    hwid = get_hwid()
    banner()
    print(f"\033[93m[>] YOUR ID: {hwid}\033[0m")
    
    key_input = input("\033[96m[?] ENTER ACCESS KEY: \033[0m")
    
    # GitHub က key.txt ကို သွားစစ်မယ်
    url = "https://raw.githubusercontent.com/5Lkhant09/my-license-server/main/key.txt"
    try:
        resp = requests.get(url).text
        for line in resp.splitlines():
            if hwid in line and key_input in line:
                # Format: ID|Key|DD-MM-YYYY HH:MM
                parts = line.split('|')
                expiry_str = parts[2]
                expiry_date = datetime.strptime(expiry_str, "%d-%m-%Y %H:%M")
                
                if get_net_time() < expiry_date:
                    print(f"\033[92m[✓] ACCESS GRANTED! EXPIRY: {expiry_str}\033[0m")
                    time.sleep(2)
                    return True
                else:
                    print("\033[91m[!] KEY EXPIRED!\033[0m")
                    return False
        print("\033[91m[!] INVALID KEY OR ID!\033[0m")
        return False
    except Exception as e:
        print(f"\033[91m[!] SERVER ERROR: {e}\033[0m")
        return False

# Main Program
if __name__ == "__main__":
    if check_license():
        # ဒီနေရာမှာ သင့်ရဲ့ Bypass Logic တွေကို ဆက်ရေးလို့ရပါပြီ
        print("\033[92m[*] TOOL IS RUNNING IN BACKGROUND...\033[0m")
        while True:
            time.sleep(10)
          

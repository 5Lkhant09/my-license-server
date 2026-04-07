import requests, re, urllib3, time, os, hashlib, subprocess, json, ssl
from datetime import datetime

# --- SSL Error Bypass ---
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- Configuration ---
KEY_URL = "https://raw.githubusercontent.com/heinminthant2022happy-bit/Aladdin/refs/heads/main/key.txt"
LICENSE_FILE = ".aladdin_v11.lic"
ID_STORAGE = ".device_id"

def get_hwid():
    # ၁။ အရင်က သိမ်းထားတဲ့ ID ရှိမရှိ စစ်မယ်
    if os.path.exists(ID_STORAGE):
        with open(ID_STORAGE, "r") as f:
            return f.read().strip()

    # ၂။ မရှိသေးရင် Hardware ID အသစ်ထုတ်မယ်
    try:
        serial = subprocess.check_output("getprop ro.serialno", shell=True).decode().strip()
        if not serial or serial == "unknown":
            serial = subprocess.check_output("settings get secure android_id", shell=True).decode().strip()
        
        raw_hash = hashlib.md5(serial.encode()).hexdigest()[:10].upper()
        new_id = f"TRB-{raw_hash}"
    except:
        new_id = f"TRB-{hashlib.md5(str(os.getlogin()).encode()).hexdigest()[:10].upper()}"

    # ၃။ ID ကို ဖုန်းထဲမှာ အသေမှတ်ထားမယ်
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

def check_license():
    hwid = get_hwid()
    banner()
    
    # ၁။ Local License စစ်ဆေးခြင်း (Offline Mode)
    if os.path.exists(LICENSE_FILE):
        try:
            with open(LICENSE_FILE, "r") as f:
                local_data = json.load(f)
            if local_data.get("id") == hwid:
                expiry_date = datetime.strptime(local_data["expiry"], "%d-%m-%Y")
                if datetime.now() < expiry_date:
                    print(f"\033[92m[✓] AUTO-LOGIN SUCCESS! (Offline Mode)\033[0m")
                    print(f"\033[94m[*] EXPIRY: {local_data['expiry']}\033[0m")
                    time.sleep(1.5)
                    return True
        except: pass

    # ၂။ Online ကနေ Key စစ်ဆေးခြင်း
    print(f"\033[94m[*] YOUR DEVICE ID: {hwid}\033[0m")
    input_key = input("\033[93m[>] ENTER ACCESS KEY: \033[0m").strip()
    
    print("\033[93m[*] Verifying license online...\033[0m")
    try:
        response = requests.get(KEY_URL, timeout=10, verify=False).text
        for line in response.splitlines():
            if "|" in line:
                db_id, db_key, db_date = line.split("|")
                if db_id.strip() == hwid and db_key.strip() == input_key:
                    expiry_date = datetime.strptime(db_date.strip(), "%d-%m-%Y")
                    if datetime.now() < expiry_date:
                        # မှန်ကန်ရင် Local မှာ သိမ်းမယ်
                        with open(LICENSE_FILE, "w") as f:
                            json.dump({"id": hwid, "key": input_key, "expiry": db_date.strip()}, f)
                        print(f"\033[92m[✓] ACCESS GRANTED! EXPIRY: {db_date}\033[0m")
                        time.sleep(2)
                        return True
                    else:
                        print("\033[91m[!] KEY EXPIRED!\033[0m")
                        return False
        
        print("\033[91m[!] INVALID KEY OR UNREGISTERED ID.\033[0m")
        return False
    except:
        print("\033[91m[!] CONNECTION ERROR! PLEASE CHECK INTERNET.\033[0m")
        return False

def main_tool():
    # ဒီနေရာမှာ သင့်ရဲ့ Main Bypass Logic ကို ထည့်ပါ
    banner()
    print("\033[92m[+] SUCCESS: Aladdin Tool is Running...")
    # သင်လုပ်ဆောင်ချင်တဲ့ Bypass functions တွေ ဒီမှာ ဆက်ရေးနိုင်ပါတယ်

if __name__ == "__main__":
    if check_license():
        main_tool()
    else:
        exit()
        

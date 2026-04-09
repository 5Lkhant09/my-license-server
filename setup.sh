#!/bin/bash

echo "Installing Aladdin Ruijie Bypass..."

# ၁။ လိုအပ်တဲ့ libraries တွေ အရင်သွင်းမယ်
pkg install python git -y
pip install requests colorama urllib3

# ၂။ Folder အဟောင်းရှိရင် အမြစ်ပြတ်ဖျက်မယ်
rm -rf my-license-server

# ၃။ GitHub ကနေ အသစ်ပြန် Clone မယ်
git clone https://github.com/5Lkhant09/my-license-server

# ၄။ Folder ထဲကို အမှန်ကန်ဆုံး ဝင်သွားမယ်
cd my-license-server

# ၅။ Script ကို စတင် Run မယ်
python main.py

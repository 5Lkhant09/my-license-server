#!/bin/bash

# ၁။ ပင်မနေရာကို အရင်သွားပြီး အဟောင်းတွေ ရှင်းမယ်
cd $HOME
rm -rf my-license-server

echo "Installing Aladdin Ruijie Bypass..."

# ၂။ လိုအပ်တာတွေ သွင်းမယ်
pkg install python git -y
pip install requests colorama urllib3

# ၃။ GitHub ကနေ အသစ်ပြန်ယူမယ်
git clone https://github.com/5Lkhant09/my-license-server

# ၄။ Folder ထဲကို သေချာဝင်မယ်
cd my-license-server

# ၅။ Script ကို Run မယ်
if [ -f "main.py" ]; then
    python main.py
else
    echo "Error: main.py not found! Please check your GitHub file name."
fi

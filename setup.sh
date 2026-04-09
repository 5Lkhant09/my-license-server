#!/bin/bash

# ၁။ လိုအပ်တဲ့ libraries တွေသွင်းမယ်
pkg install python git -y
pip install requests colorama urllib3

# ၂။ Git လုံခြုံရေးအတွက် Safe Directory သတ်မှတ်မယ် (ဒါမှ Error မတက်မှာ)
git config --global --add safe.directory "*"

# ၃။ နေရာဟောင်းတွေကို အကုန်ရှင်းပစ်မယ် (Folder ထပ်မနေအောင်လို့)
cd ~
rm -rf my-license-server

# ၄။ Folder အသစ်ပြန် Clone မယ်
git clone https://github.com/5Lkhant09/my-license-server

# ၅။ Folder ထဲဝင်ပြီး Run မယ်
cd my-license-server
python main.py


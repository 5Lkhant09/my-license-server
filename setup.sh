#!/bin/bash

# မင်းရဲ့ Username နဲ့ Token ကို ဒီမှာ အစားထိုးပါ
USER="5Lkhant09"
TOKEN="ghp_မင်းရဲ့_Personal_Access_Token"

echo "Installing Aladdin Ruijie Bypass..."
pkg update -y && pkg upgrade -y
pkg install python git -y
pip install requests colorama urllib3

# Folder မရှိရင် Clone လုပ်မယ်၊ ရှိရင် Update လုပ်မယ်
if [ -d "my-license-server" ]; then
    cd my-license-server && git pull https://$TOKEN@github.com/$USER/my-license-server.git
else
    git clone https://$TOKEN@github.com/$USER/my-license-server.git
    cd my-license-server
fi

python main.py

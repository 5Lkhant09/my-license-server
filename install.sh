#!/data/data/com.termux/files/usr/bin/bash

# လိုအပ်တဲ့ package များသွင်းခြင်း
echo -e "\e[93m[*] Installing dependencies...\e[0m"
pkg update -y && pkg upgrade -y
pkg install python requests -y

# Script ကို download ဆွဲခြင်း
echo -e "\e[93m[*] Downloading Aladdin Bypass V11...\e[0m"
curl -L https://raw.githubusercontent.com/5Lkhant09/my-license-server/main/aladdin.py -o aladdin.py

# Run ရန် ညွှန်ကြားချက်
echo -e "\e[92m[✓] Installation Complete!\e[0m"
echo -e "\e[94m[>] To start the tool, type: \e[93mpython aladdin.py\e[0m"
python aladdin.py

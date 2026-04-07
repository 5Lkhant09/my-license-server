#!/data/data/com.termux/files/usr/bin/bash
green='\e[92m'
blue='\e[94m'
yellow='\e[93m'
reset='\e[0m'

echo -e "${blue}[*] Aladdin V11 Installer Starting...${reset}"

# လိုအပ်တဲ့ Package တွေစစ်မယ်
pkg update -y && pkg upgrade -y
pkg install python git curl -y
pip install requests ping3 ntplib pycryptodome

# Script ကို ဒေါင်းမယ် (Link ကို သေချာအောင် ပြင်ထားပါတယ်)
echo -e "${blue}[*] Downloading Aladdin Script...${reset}"
curl -L -o aladdin.py https://raw.githubusercontent.com/5Lkhant09/my-license-server/refs/heads/main/aladdin.py

# Permission ပေးမယ်
chmod +x aladdin.py

echo -e "${green}[✓] INSTALLATION COMPLETE!${reset}"
echo -e "${yellow}[>] Start with: python aladdin.py${reset}"

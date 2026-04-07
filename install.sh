#!/data/data/com.termux/files/usr/bin/bash

# အရောင်များ
green='\e[92m'
blue='\e[94m'
yellow='\e[93m'
reset='\e[0m'

echo -e "${blue}[*] Aladdin V11 Installer Starting...${reset}"

# Storage Access
termux-setup-storage

# Update & Packages
echo -e "${yellow}[*] Updating and installing packages...${reset}"
pkg update -y && pkg upgrade -y
pkg install python git curl -y

# Python Libraries
pip install requests ping3 ntplib pycryptodome

# Script Download
echo -e "${blue}[*] Downloading Aladdin Script...${reset}"
curl -L -o aladdin.py https://raw.githubusercontent.com/5Lkhant09/my-license-server/main/aladdin.py

# Permission
chmod +x aladdin.py

echo -e "${green}[✓] INSTALLATION COMPLETE!${reset}"
echo -e "${yellow}[>] Start with: python aladdin.py${reset}"

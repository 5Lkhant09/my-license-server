#!/data/data/com.termux/files/usr/bin/bash
pkg install python requests -y
curl -L https://raw.githubusercontent.com/5Lkhant09/my-license-server/main/aladdin.py -o aladdin.py
python aladdin.py

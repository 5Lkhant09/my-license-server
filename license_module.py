import requests

LICENSE_URL = "https://raw.githubusercontent.com/5Lkhant09/my-license-server/refs/heads/main/key.txt"

def check_license_key(key):
    try:
        response = requests.get(LICENSE_URL)
        response.raise_for_status()
        lines = [line.strip() for line in response.text.split('\n') if line.strip()]
        for line in lines:
            if '|' not in line:
                continue
            device_id, access_key, expiry = line.split('|')
            if key == access_key:
                return True
        return False
    except:
        return False

def get_license_info(key):
    try:
        response = requests.get(LICENSE_URL)
        response.raise_for_status()
        lines = [line.strip() for line in response.text.split('\n') if line.strip()]
        for line in lines:
            if '|' not in line:
                continue
            device_id, access_key, expiry = line.split('|')
            if key == access_key:
                return {"valid": True, "device_id": device_id, "access_key": access_key, "expiry": expiry}
        return {"valid": False}
    except:
        return {"valid": False}

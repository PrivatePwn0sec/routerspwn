# creds/creds_mod.py
import requests

def test_creds(target_ip, username, password):
    print(f"[+] Menguji kredensial pada {target_ip}...")
    try:
        url = f"http://{target_ip}/login"
        response = requests.post(url, data={"username": username, "password": password})
        if "login successful" in response.text.lower():
            print("[+] Kredensial valid!")
        else:
            print("[-] Kredensial tidak valid.")
    except Exception as e:
        print(f"[-] Terjadi kesalahan: {e}")

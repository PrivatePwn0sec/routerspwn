# generic/generic_mod.py
import requests

def perform_attack(target_ip):
    print(f"[+] Melakukan serangan pada {target_ip}...")
    try:
        url = f"http://{target_ip}/attack_endpoint"
        response = requests.get(url)
        if response.status_code == 200:
            print("[+] Serangan berhasil!")
        else:
            print("[-] Serangan gagal.")
    except Exception as e:
        print(f"[-] Terjadi kesalahan: {e}")

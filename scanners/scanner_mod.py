# scanners/scanner_mod.py
import requests

def scan_vulnerability(target_ip):
    print(f"[+] Memindai kerentanan pada {target_ip}...")
    try:
        url = f"http://{target_ip}/potential_vulnerable_endpoint"
        response = requests.get(url)
        if "vulnerable" in response.text.lower():
            print("[+] Target rentan!")
        else:
            print("[-] Target tidak rentan.")
    except Exception as e:
        print(f"[-] Terjadi kesalahan: {e}")

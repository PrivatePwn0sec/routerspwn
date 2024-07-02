import importlib

def main():
    print("RouterSpwn Framework")
    print("====================")
    print("Pilih modul:")
    print("1. Exploits")
    print("2. Creds")
    print("3. Scanners")
    print("4. Payloads")
    print("5. Encoders")
    print("6. Generic")
    choice = input("Pilihan: ")
    
    if choice == "1":
        module = importlib.import_module('exploits.exploit_mod')
        target_ip = input("Masukkan target IP: ")
        module.exploit(target_ip)
    elif choice == "2":
        module = importlib.import_module('creds.creds_mod')
        target_ip = input("Masukkan target IP: ")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        module.test_creds(target_ip, username, password)
    elif choice == "3":
        module = importlib.import_module('scanners.scanner_mod')
        target_ip = input("Masukkan target IP: ")
        module.scan_vulnerability(target_ip)
    elif choice == "4":
        module = importlib.import_module('payloads.payload_mod')
        architecture = input("Masukkan arsitektur: ")
        payload = module.generate_payload(architecture)
        print(f"Payload: {payload}")
    elif choice == "5":
        module = importlib.import_module('encoders.encoder_mod')
        payload_code = input("Masukkan kode payload (dalam hex): ")
        payload = bytes.fromhex(payload_code)
        encoded_payload = module.encode_payload(payload)
        print(f"Payload terenkripsi: {encoded_payload.hex()}")
    elif choice == "6":
        module = importlib.import_module('generic.generic_mod')
        target_ip = input("Masukkan target IP: ")
        module.perform_attack(target_ip)
    else:
        print("Pilihan tidak valid.")
        
if __name__ == "__main__":
    main()

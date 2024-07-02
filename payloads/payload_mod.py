# payloads/payload_mod.py
def generate_payload(architecture):
    print(f"[+] Menghasilkan payload untuk arsitektur {architecture}...")
    if architecture == "mips":
        payload = b"\x24\x02\x0F\xA0"  # Contoh payload sederhana
    elif architecture == "arm":
        payload = b"\x01\x30\x8F\xE2"  # Contoh payload sederhana
    else:
        payload = b"\x90" * 100  # Payload NOP sled sebagai contoh
    return payload

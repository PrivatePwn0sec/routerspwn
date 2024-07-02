# encoders/encoder_mod.py
def encode_payload(payload):
    print("[+] Mengenkripsi payload...")
    encoded_payload = b""
    for byte in payload:
        encoded_payload += bytes([byte ^ 0xAA])  # XOR sederhana
    return encoded_payload

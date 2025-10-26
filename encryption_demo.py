"""
encryption_demo.py
Demonstrates secure encryption and decryption of simulated log lines using Fernet.
This only operates on simulated data (no real keystrokes).
"""

from cryptography.fernet import Fernet
import json

KEY_FILE = "fernet.key"
INPUT_FILE = "simulated_session.jsonl"
OUT_FILE = "simulated_session.enc"

def generate_key(path=KEY_FILE):
    key = Fernet.generate_key()
    with open(path, "wb") as f:
        f.write(key)
    return key

def load_key(path=KEY_FILE):
    with open(path, "rb") as f:
        return f.read()

def encrypt_file(key_path=KEY_FILE, input_path=INPUT_FILE, out_path=OUT_FILE):
    key = load_key(key_path)
    cipher = Fernet(key)
    with open(input_path, "rb") as fi, open(out_path, "wb") as fo:
        for line in fi:
            token = cipher.encrypt(line.strip())
            fo.write(token + b"\n")
    print(f"Encrypted output written to {out_path}")

def decrypt_file(key_path=KEY_FILE, enc_path=OUT_FILE, out_plain="decrypted_session.jsonl"):
    key = load_key(key_path)
    cipher = Fernet(key)
    with open(enc_path, "rb") as fin, open(out_plain, "wb") as fout:
        for line in fin:
            plain = cipher.decrypt(line.strip())
            fout.write(plain + b"\n")
    print(f"Decrypted output written to {out_plain}")

if __name__ == "__main__":
    # Generate key (one-time)
    print("Generating encryption key...")
    generate_key()
    print("Encrypting simulated session...")
    encrypt_file()
    print("Decrypting back to verify...")
    decrypt_file()

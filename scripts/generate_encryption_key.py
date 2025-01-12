import base64
import os


def generate_encryption_key():
    key = os.urandom(32)
    encoded_key = base64.b64encode(key).decode("utf-8")
    return encoded_key


if __name__ == "__main__":
    encoded_key = generate_encryption_key()
    print(f"Generated Encryption Key: {encoded_key}")

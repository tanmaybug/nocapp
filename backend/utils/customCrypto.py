import base64
import hashlib


class CustomCrypto:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key.encode()

    def _xor_encrypt(self, data: bytes) -> bytes:
        key = hashlib.sha256(self.secret_key).digest()

        encrypted = bytearray()

        for i, byte in enumerate(data):
            encrypted.append(byte ^ key[i % len(key)])

        return bytes(encrypted)

    def encrypt(self, text: str) -> str:
        # XOR encryption
        encrypted_bytes = self._xor_encrypt(text.encode())

        # Convert to URL-safe Base64
        encoded = base64.urlsafe_b64encode(encrypted_bytes).decode()

        # Remove non-alphanumeric chars
        return encoded.replace("=", "").replace("-", "A").replace("_", "B")

    def decrypt(self, encrypted_text: str) -> str:
        # Restore Base64 chars
        restored = encrypted_text.replace("A", "-").replace("B", "_")

        # Restore padding
        padding = len(restored) % 4
        if padding:
            restored += "=" * (4 - padding)

        encrypted_bytes = base64.urlsafe_b64decode(restored)

        # XOR decryption
        decrypted = self._xor_encrypt(encrypted_bytes)

        return decrypted.decode()


# Example usage
# crypto = CustomCrypto("my-secret-key")

# encrypted = crypto.encrypt("Hello123")
# print("Encrypted:", encrypted)

# decrypted = crypto.decrypt(encrypted)
# print("Decrypted:", decrypted)
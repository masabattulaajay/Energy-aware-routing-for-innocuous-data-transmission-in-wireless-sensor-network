import base64
import hashlib


class Security:

    def __init__(self):
        pass

    # Encrypt Message
    def encrypt(self, message):

        key = "WSN2026"

        encrypted = ""

        for i in range(len(message)):

            encrypted += chr(
                ord(message[i]) ^
                ord(key[i % len(key)])
            )

        encrypted = base64.b64encode(
            encrypted.encode()
        ).decode()

        return encrypted


    # Decrypt Message
    def decrypt(self, encrypted_message):

        key = "WSN2026"

        decoded = base64.b64decode(
            encrypted_message.encode()
        ).decode()

        message = ""

        for i in range(len(decoded)):

            message += chr(
                ord(decoded[i]) ^
                ord(key[i % len(key)])
            )

        return message


    # Hash Message
    def generate_hash(self, message):

        return hashlib.sha256(
            message.encode()
        ).hexdigest()


    # Transmission Status
    def transmission_status(self):

        return "Secure Transmission Successful"
from cryptography.fernet import Fernet

class MessageEncryptorDecryptor:
    def __init__(self):
        pass

    def generate_key(self):
        return Fernet.generate_key()

    def enrypt_message(self,key,message):
        key=Fernet(key)
        encrypted_message=key.encrypt(message.encode())
        return encrypted_message

    def decrypt_message(self, key, encrypted_message):
        key = Fernet(key)
        decrypted_message = key.decrypt(encrypted_message).decode()
        return decrypted_message


if __name__=="__main__":
    messageEncryptorDecryptor=MessageEncryptorDecryptor()
    key=messageEncryptorDecryptor.generate_key()
    message=input("Enter a message to encrypt: ")
    encrypted_message=messageEncryptorDecryptor.enrypt_message(key,message)
    print(f'Encrypted message: {encrypted_message}')
    decrypted_message=messageEncryptorDecryptor.decrypt_message(key,encrypted_message)
    print(f'Decrypted message: {decrypted_message}')

from Crypto.Cipher import AES
import base64

def decrypt_token(
        token: str, 
        secret: str
    ) -> str:
    # ? Ensure the secret is exactly 16 
    # ? bytes long for AES-128
    secret = secret.encode('utf-8')
    if len(secret) != 16:
        raise ValueError("Secret key must be 16 bytes long.")

    # ? Decode the base64 encoded token
    token = base64.b64decode(token)

    # ? Initialize the AES cipher in 
    # ? ECB mode
    cipher = AES.new(secret, AES.MODE_ECB)

    # ? Decrypt the token
    decrypted_bytes = cipher.decrypt(token)

    # ? Remove potential padding (PKCS7)
    pad = decrypted_bytes[-1]
    if pad < 1 or pad > 16:
        raise ValueError("Invalid padding byte encountered.")
    
    decrypted_bytes = decrypted_bytes[:-pad]

    # ? Convert bytes back to string
    decrypted_text = decrypted_bytes.decode('utf-8')

    return decrypted_text
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64

def aes_encrypt(key, plaintext):
    # AES şifreleme için bir cipher nesnesi oluştur
    cipher = AES.new(key, AES.MODE_CBC)

    # Veriyi şifrele ve sonucu base64 formatına dönüştür
    ciphertext_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ciphertext = base64.b64encode(ciphertext_bytes).decode('utf-8')

    return iv, ciphertext

def pad_key(key):
    # Anahtarın uzunluğunu kontrol et
    # Eksik olan byte'ları boşluk ile doldur
    if len(key) < 16:
        key = key + (16 - len(key)) * ' '
    elif len(key) < 24:
        key = key + (24 - len(key)) * ' '
    elif len(key) < 32:
        key = key + (32 - len(key)) * ' '
    else:
        key = key[:32]  # Anahtar 32 byte'tan fazlaysa ilk 32 byte'ı al

    return key.encode('utf-8')

# Anahtar ve metin kullanıcıdan al
key = input("Lütfen şifre anahtarını girin (16, 24 veya 32 byte uzunluğunda): ")
key = pad_key(key)

plaintext = input("Lütfen şifrelenecek metni girin: ")

# Şifreleme işlemi
iv, ciphertext = aes_encrypt(key, plaintext)
print(f"\nŞifrelenmiş metin (base64 formatında): {ciphertext}")
print(f"IV (base64 formatında): {iv}")

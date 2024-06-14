from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def decrypt_aes(ciphertext, iv, key):
    try:
        # Anahtarın eksik byte'larını boşluk ile doldur
        key = pad_key(key)

        # Veriyi base64 formatından çıkar ve AES şifresini çözmek için bir cipher nesnesi oluştur
        cipher = AES.new(key, AES.MODE_CBC, base64.b64decode(iv))

        # Veriyi çöz ve padding'i kaldır
        decrypted_bytes = unpad(cipher.decrypt(base64.b64decode(ciphertext)), AES.block_size)
        decrypted_text = decrypted_bytes.decode('utf-8')

        return decrypted_text

    except Exception as e:
        return str(e)

def pad_key(key):
    # Anahtarın uzunluğunu kontrol et ve eksik olan byte'ları boşluk ile doldur
    if len(key) < 16:
        key = key + (16 - len(key)) * ' '
    elif len(key) < 24:
        key = key + (24 - len(key)) * ' '
    elif len(key) < 32:
        key = key + (32 - len(key)) * ' '
    else:
        key = key[:32]

    return key.encode('utf-8')

def main():
    # Kullanıcıdan gerekli bilgileri al
    ciphertext = input("Sifrelenmiş metni (base64 formatında) girin: ")
    iv = input("IV'yi (base64 formatında) girin: ")
    key = input("Şifre anahtarını girin: ")

    # Metni çöz
    plaintext = decrypt_aes(ciphertext, iv, key)
    if plaintext:
        print(f"\nÇözülmüş metin: {plaintext}")
    else:
        print("\nMetni çözerken bir hata oluştu. Lütfen girdilerinizi kontrol edin.")

if __name__ == "__main__":
    main()

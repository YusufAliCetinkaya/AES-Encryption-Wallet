# Python-Pycryptodome-Kutuphanesi-ile-AES-Sifreleme-ve-Cozumleme

Bu repository, AES (Advanced Encryption Standard) algoritması kullanılarak metin şifreleme ve şifre çözme işlemlerini göstermek için Python scriptler içermektedir.

## Kullanım

### `main.py` (Şifreleme)

Bu script kullanıcıdan bir metin ve bir şifreleme anahtarı girmesini bekler. Girilen metin AES algoritması kullanılarak CBC (Cipher Block Chaining) modunda şifrelenir ve base64 formatında çıktı verir.

#### Gereksinimler

- `pycryptodome` kütüphanesi: AES şifreleme işlemleri için kullanılır.
- `base64` modülü: Şifrelenmiş veriyi base64 formatında göstermek için kullanılır.

#### Kullanım

1. Python ortamında `main.py` scriptini çalıştırın.
2. Şifreleme için bir anahtar girişi istenecektir (uzunluk: 16, 24 veya 32 byte).
3. Şifrelenecek metni girin.
4. Script çıktı olarak base64 formatında şifrelenmiş metni ve IV (Initialization Vector) değerini gösterecektir.

### `decrypt.py` (Şifre Çözme)

Bu script kullanıcıdan base64 formatında şifrelenmiş metin, IV ve şifreleme anahtarı girmesini bekler. Girilen bilgileri kullanarak AES algoritması ile şifrelenmiş metni çözer.

#### Gereksinimler

- `pycryptodome` kütüphanesi: AES şifre çözme işlemleri için kullanılır.
- `base64` modülü: Base64 formatında veriyi çözmek için kullanılır.

#### Kullanım

1. Python ortamında `decrypt.py` scriptini çalıştırın.
2. Şifrelenmiş metni (base64 formatında), IV'yi (base64 formatında) ve şifreleme anahtarını girin.
3. Script çıktı olarak şifresi çözülmüş metni gösterecektir.

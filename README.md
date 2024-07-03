# Wallet Encrypted With AES

Bu proje, AES (Advanced Encryption Standard) şifreleme algoritmasını kullanarak 12 anahtarı ve private key'i güvenli bir şekilde saklamanızı sağlar. Kullanıcıların kendi şifreleme anahtarlarını kullanarak verilerini şifrelemesine ve çözmesine olanak tanır.

## Özellikler

- **AES Şifreleme ve Şifre Çözme**: Kullanıcılar, metinlerini AES algoritması ile şifreleyebilir ve çözebilir.
- **Anahtar Yönetimi**: Kullanıcıların girdiği anahtarlar uygun uzunlukta değilse, eksik byte'lar boşluk ile doldurularak uygun hale getirilir.
- **Base64 Dönüştürme**: Şifrelenmiş metin ve IV (Initialization Vector) base64 formatında saklanır ve kullanılır.

## Gereksinimler

- Python 3.x
- `pycryptodome` kütüphanesi

## Kurulum

1. Gerekli Python paketlerini yükleyin:

    ```bash
    pip install pycryptodome
    ```

2. Bu repoyu klonlayın veya zip dosyasını indirip çıkarın:

    ```bash
    git clone https://github.com/kullaniciadi/aes-encryption-wallet.git
    cd aes-encryption-wallet
    ```

## Kullanım

### Şifreleme

`main.py` dosyasını çalıştırarak şifreleme işlemi gerçekleştirebilirsiniz:

```bash
python main.py
```

Kullanıcıdan şifre anahtarı ve şifrelenecek metin istendiğinde gerekli bilgileri girin. Şifrelenmiş metin ve IV (base64 formatında) ekrana yazdırılacaktır.

### Şifre Çözme

`decrypt.py` dosyasını çalıştırarak şifre çözme işlemi gerçekleştirebilirsiniz:

```bash
python decrypt.py
```

Kullanıcıdan şifrelenmiş metin (base64 formatında), IV (base64 formatında) ve şifre anahtarı istendiğinde gerekli bilgileri girin. Çözülmüş metin ekrana yazdırılacaktır.

## Kod Açıklaması

### `main.py`

- `aes_encrypt` fonksiyonu: Verilen metni şifreler ve sonucu base64 formatında döndürür.
- `pad_key` fonksiyonu: Kullanıcının girdiği anahtarın uygun uzunlukta olmasını sağlar.

### `decrypt.py`

- `decrypt_aes` fonksiyonu: Verilen şifrelenmiş metni ve IV'yi kullanarak metnin şifresini çözer.
- `pad_key` fonksiyonu: Kullanıcının girdiği anahtarın uygun uzunlukta olmasını sağlar.



## Katkıda Bulunma

1. Fork yapın.
2. Yeni bir branch oluşturun (`git checkout -b feature/isim`).
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik ekle'`).
4. Branch'e push yapın (`git push origin feature/isim`).
5. Bir Pull Request oluşturun.

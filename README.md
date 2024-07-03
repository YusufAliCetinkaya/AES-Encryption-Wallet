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



## Base64 Dönüştürme ve IV'nin Önemi

### Base64 Dönüştürme
**Neden base64 kullanıyoruz?**

1. **İkili Veriyi Metne Dönüştürme**:
   - AES şifreleme işlemi sonucunda ortaya çıkan şifrelenmiş metin (ciphertext) ve IV, ikili (binary) veridir. Bu ikili veri, ASCII veya Unicode gibi standart karakter setlerinde görüntülenemez ve saklanamaz.
   - Base64, ikili veriyi metne dönüştürmek için kullanılan bir kodlama yöntemidir. Bu sayede, şifrelenmiş veri ve IV gibi ikili veriler metin formatında saklanabilir ve iletilebilir.

2. **Veri Transferi ve Saklama**:
   - E-posta, JSON veya XML gibi bazı veri iletim ve saklama formatları yalnızca metin verilerini destekler. Bu durumda, ikili veriyi base64 formatına dönüştürmek, verinin bu formatlarda güvenli bir şekilde taşınabilmesini sağlar.

### Initialization Vector (IV)
**Neden IV'ye gerek duyuyoruz?**

1. **Deterministik Şifrelemeyi Önleme**:
   - Aynı metin her şifrelendiğinde aynı ciphertext üretilirse, bu durum güvenlik açığı yaratır. Saldırganlar, aynı ciphertext'i gördüklerinde aynı metnin şifrelendiğini anlarlar.
   - IV, her şifreleme işleminde farklı bir başlangıç durumu sağlar. Bu sayede aynı metin, aynı anahtar kullanılsa bile farklı ciphertext'ler üretir. Bu, deterministik şifrelemeyi önler ve güvenliği artırır.

2. **Blok Şifreleme Modları**:
   - AES, bir blok şifreleme algoritmasıdır ve farklı blok şifreleme modları (CBC, CFB, OFB vb.) kullanabilir. Bu modların çoğu, her blok için bir IV gerektirir.
   - Özellikle CBC (Cipher Block Chaining) modunda, her bir blok, bir önceki blok ve IV kullanılarak şifrelenir. Bu da, aynı metnin her seferinde farklı şifrelenmesini sağlar.


# Haftalık Ödev 2 - merhaba.py
# Kullanıcının adını ve doğum yılını alıp yaşını hesaplayan program

# Bugünün tarihini öğrenmek için datetime modülünden date sınıfını alıyoruz
from datetime import date


# Kullanıcıdan adını alıp metin (str) olarak döndüren fonksiyon
def ad_al() -> str:
    while True:  # Geçerli bir ad girilene kadar soruyu tekrarlıyoruz
        # Adı okuyup baştaki ve sondaki boşlukları siliyoruz
        ad = input("Adınız: ").strip()
        if ad:  # Ad boş değilse
            return ad  # Adı fonksiyonun sonucu olarak geri veriyoruz
        print("Uyarı: Ad boş bırakılamaz.")  # Boşsa uyarıp tekrar soruyoruz


# Kullanıcıdan doğum yılını alıp tam sayı (int) olarak döndüren fonksiyon
def dogum_yili_al() -> int:
    while True:  # Geçerli bir yıl girilene kadar soruyu tekrarlıyoruz
        # Girilen yılı önce metin olarak okuyup boşlukları siliyoruz
        yil_metni = input("Doğum yılınız: ").strip()
        try:  # Tam sayıya çevirmeyi deniyoruz; hata çıkabilir
            dogum_yili = int(yil_metni)  # Metni tam sayıya çeviriyoruz
        except ValueError:  # Harf, ondalık sayı ya da boş girdi gelirse
            if not yil_metni:  # Girdi tamamen boşsa
                print("Uyarı: Doğum yılı boş bırakılamaz.")  # Boş uyarısı
            else:  # Girdi var ama tam sayı değilse
                # Doğru biçimi örnekle göstererek uyarıyoruz
                print("Uyarı: Doğum yılı tam sayı olmalı (örnek: 2003).")
            continue  # Döngünün başına dönüp yılı yeniden soruyoruz
        return dogum_yili  # Çeviri başarılıysa yılı geri veriyoruz


# Doğum yılı ile bu yılın farkından yaşı bulan fonksiyon
def yas_hesapla(dogum_yili: int, bu_yil: int) -> int:
    return bu_yil - dogum_yili  # Bu yıldan doğum yılını çıkarıp yaşı veriyoruz


# Yaş aralığına göre kişiye özel bir mesaj döndüren fonksiyon
def mesaj_olustur(ad: str, yas: int) -> str:
    if yas < 18:  # 18 yaşından küçükse
        return f"{ad}, erken yaşta öğrenmeye başlamak büyük bir avantaj!"
    elif yas < 26:  # 18-25 yaş arasındaysa
        return f"{ad}, üniversite yılları yeni beceriler edinmek için harika!"
    elif yas < 41:  # 26-40 yaş arasındaysa
        return f"{ad}, iş hayatında kodlama bilgisi sana fark yaratır!"
    elif yas < 65:  # 41-64 yaş arasındaysa
        return f"{ad}, deneyimini teknolojiyle birleştirmenin tam zamanı!"
    else:  # 65 yaş ve üzerindeyse
        return f"{ad}, öğrenmenin yaşı yok; merakın her şeyden değerli!"


def main() -> None:  # Programın ana akışını yöneten fonksiyon
    print("=== Merhaba! ===")  # Program açılışında bir başlık yazdırıyoruz
    ad = ad_al()  # Kullanıcının adını alıyoruz
    dogum_yili = dogum_yili_al()  # Kullanıcının doğum yılını alıyoruz
    bu_yil = date.today().year  # Bilgisayarın tarihinden bu yılı alıyoruz
    # Doğum yılı ve bu yılı kullanarak yaşı hesaplıyoruz
    yas = yas_hesapla(dogum_yili, bu_yil)
    selam = f"Merhaba {ad}!"  # Kişiye adıyla seslenen selamı hazırlıyoruz
    # Doğum günü geçmemiş olabileceği için iki ihtimali de yazıyoruz
    yas_metni = f"{bu_yil} yılında {yas} yaşına girdin ya da gireceksin."
    print(selam, yas_metni)  # Selamı ve yaş bilgisini aynı satırda yazdırıyoruz
    print(mesaj_olustur(ad, yas))  # Yaşa göre seçilen özel mesajı yazdırıyoruz


# Dosya başka bir dosyaya eklenmeden doğrudan çalıştırıldıysa
if __name__ == "__main__":
    try:  # Kullanıcı programı yarıda keserse hata dökümü göstermemek için
        main()  # ana fonksiyonu başlatıyoruz
    except (KeyboardInterrupt, EOFError):  # Ctrl+C ya da Ctrl+D gelirse
        print("\nProgram sonlandırıldı.")  # Kısa bir kapanış mesajı yazıyoruz

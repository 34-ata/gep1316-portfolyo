
# Haftalık Ödev 2 - merhaba.py
# Kullanıcının adını ve doğum yılını alıp yaşını hesaplayan program

# Bugünün tarihini öğrenmek için date sınıfını alıyoruz
from datetime import date


# Kullanıcıdan adını alıp str olarak döndüren fonksiyon
def ad_al() -> str:
    while True:  # Geçerli bir ad girilene kadar soruyu tekrarlıyoruz
        # Kullanıcının adını alıp boşlukları temizliyoruz
        ad = input("Adınız: ").strip()

        if ad:  # Adın boş olup olmadığını kontrol ediyoruz
            return ad  # Ad boş değilse geri döndürüyoruz

        print("Uyarı: Ad boş bırakılamaz.")  # Boşsa uyarıp adı tekrar soruyoruz


# Kullanıcıdan doğum yılını alıp int olarak döndüren fonksiyon
def dogum_yili_al(bu_yil: int) -> int:
    while True:  # Geçerli bir yıl girilene kadar soruyu tekrarlıyoruz
        # Doğum yılını metin olarak alıp boşlukları siliyoruz
        yil_metni = input("Doğum yılınız: ").strip()

        try:  # Çeviri hata verebileceği için deniyoruz
            # Girilen metni tam sayıya çeviriyoruz
            dogum_yili = int(yil_metni)

        except ValueError:  # Harf, ondalık ya da boş girdi gelirse
            # Boş veya geçersiz girişleri kontrol ediyoruz
            if not yil_metni:
                print("Uyarı: Doğum yılı boş bırakılamaz.")  # Boş girdi uyarısı
            else:  # Girdi var ama tam sayı değilse
                # Tam sayı olmayan girdi için örnekli uyarı veriyoruz
                print("Uyarı: Doğum yılı tam sayı olmalı (örnek: 2003).")
            continue  # Yılı yeniden soruyoruz

        # Doğum yılının 1900'den küçük olup olmadığını kontrol ediyoruz
        if dogum_yili < 1900:
            # Alt sınır uyarısı
            print("Uyarı: Doğum yılı 1900'den küçük olamaz.")
            continue  # Yılı yeniden soruyoruz

        # Gelecek bir yıl girilip girilmediğini kontrol ediyoruz
        if dogum_yili > bu_yil:
            print("Uyarı: Gelecek bir yıl girilemez.")  # Gelecek yıl uyarısı
            continue  # Yılı yeniden soruyoruz

        return dogum_yili  # Geçerli yılı geri döndürüyoruz


# Doğum yılı ile mevcut yılın farkından yaşı hesaplıyoruz
def yas_hesapla(dogum_yili: int, bu_yil: int) -> int:
    return bu_yil - dogum_yili  # Bu yıldan doğum yılını çıkarıyoruz


# Yaş aralığına göre kişiye özel mesaj oluşturuyoruz
def mesaj_olustur(ad: str, yas: int) -> str:
    if yas < 18:  # 18 yaşından küçükse
        # 18 yaş altına uygun mesajı döndürüyoruz
        return f"{ad}, erken yaşta öğrenmeye başlamak büyük bir avantaj!"

    elif yas < 26:  # 18-25 yaş arasındaysa
        # 18-25 yaşa uygun mesajı döndürüyoruz
        return f"{ad}, üniversite yılları yeni beceriler edinmek için harika!"

    elif yas < 41:  # 26-40 yaş arasındaysa
        # 26-40 yaşa uygun mesajı döndürüyoruz
        return f"{ad}, iş hayatında kodlama bilgisi sana fark yaratır!"

    elif yas < 65:  # 41-64 yaş arasındaysa
        # 41-64 yaşa uygun mesajı döndürüyoruz
        return f"{ad}, deneyimini teknolojiyle birleştirmenin tam zamanı!"

    else:  # 65 yaş ve üzerindeyse
        # 65 yaş ve üzerine uygun mesajı döndürüyoruz
        return f"{ad}, öğrenmenin yaşı yok; merakın her şeyden değerli!"


# Programın ana akışını yöneten fonksiyon
def main() -> None:
    print("=== Merhaba! ===")  # Açılışta bir başlık yazdırıyoruz

    # Bilgisayarın tarihinden mevcut yılı alıyoruz
    bu_yil = date.today().year

    # Kullanıcının adını ve doğum yılını alıyoruz
    ad = ad_al()
    dogum_yili = dogum_yili_al(bu_yil)  # Doğum yılını alıyoruz

    # Kullanıcının yaşını hesaplıyoruz
    yas = yas_hesapla(dogum_yili, bu_yil)

    # Kişiye özel selamlama ve yaş bilgisi hazırlıyoruz
    selam = f"Merhaba {ad}!"
    # Doğum günü geçmemiş olabileceği için iki ihtimali de yazıyoruz
    yas_metni = f"{bu_yil} yılında {yas} yaşına girdin ya da gireceksin."

    # Selamlama ve yaş bilgisini ekrana yazdırıyoruz
    print(selam, yas_metni)

    # Yaş aralığına uygun mesajı ekrana yazdırıyoruz
    print(mesaj_olustur(ad, yas))


# Dosya doğrudan çalıştırıldığında ana fonksiyonu başlatıyoruz
if __name__ == "__main__":
    try:  # Yarıda kesilme hatalarını yakalamak için deniyoruz
        main()  # Ana fonksiyonu başlatıyoruz

    except (KeyboardInterrupt, EOFError):  # Ctrl+C ya da Ctrl+D gelirse
        # Program yarıda kesilirse kısa bir mesaj gösteriyoruz
        print("\nProgram sonlandırıldı.")

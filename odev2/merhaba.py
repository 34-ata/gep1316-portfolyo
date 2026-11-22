
# Haftalık Ödev 2 - merhaba.py
# Kullanıcının adını ve doğum yılını alıp yaşını hesaplayan program

# Bugünün tarihini öğrenmek için date sınıfını alıyoruz
from datetime import date


# Kullanıcıdan adını alıp str olarak döndüren fonksiyon
def ad_al() -> str:
    while True:
        # Kullanıcının adını alıp boşlukları temizliyoruz
        ad = input("Adınız: ").strip()

        if ad:
            return ad  # Ad boş değilse geri döndürüyoruz

        print("Uyarı: Ad boş bırakılamaz.")


# Kullanıcıdan doğum yılını alıp int olarak döndüren fonksiyon
def dogum_yili_al(bu_yil: int) -> int:
    while True:
        # Doğum yılını metin olarak alıp boşlukları siliyoruz
        yil_metni = input("Doğum yılınız: ").strip()

        try:
            # Girilen metni tam sayıya çeviriyoruz
            dogum_yili = int(yil_metni)

        except ValueError:
            # Boş veya geçersiz girişleri kontrol ediyoruz
            if not yil_metni:
                print("Uyarı: Doğum yılı boş bırakılamaz.")
            else:
                print("Uyarı: Doğum yılı tam sayı olmalı (örnek: 2003).")
            continue

        # Doğum yılının 1900'den küçük olup olmadığını kontrol ediyoruz
        if dogum_yili < 1900:
            print("Uyarı: Doğum yılı 1900'den küçük olamaz.")
            continue

        # Gelecek bir yıl girilip girilmediğini kontrol ediyoruz
        if dogum_yili > bu_yil:
            print("Uyarı: Gelecek bir yıl girilemez.")
            continue

        return dogum_yili  # Geçerli yılı geri döndürüyoruz


# Doğum yılı ile mevcut yılın farkından yaşı hesaplıyoruz
def yas_hesapla(dogum_yili: int, bu_yil: int) -> int:
    return bu_yil - dogum_yili


# Yaş aralığına göre kişiye özel mesaj oluşturuyoruz
def mesaj_olustur(ad: str, yas: int) -> str:
    if yas < 18:
        return f"{ad}, erken yaşta öğrenmeye başlamak büyük bir avantaj!"

    elif yas < 26:
        return f"{ad}, üniversite yılları yeni beceriler edinmek için harika!"

    elif yas < 41:
        return f"{ad}, iş hayatında kodlama bilgisi sana fark yaratır!"

    elif yas < 65:
        return f"{ad}, deneyimini teknolojiyle birleştirmenin tam zamanı!"

    else:
        return f"{ad}, öğrenmenin yaşı yok; merakın her şeyden değerli!"


# Programın ana akışını yöneten fonksiyon
def main() -> None:
    print("=== Merhaba! ===")

    # Bilgisayarın tarihinden mevcut yılı alıyoruz
    bu_yil = date.today().year

    # Kullanıcının adını ve doğum yılını alıyoruz
    ad = ad_al()
    dogum_yili = dogum_yili_al(bu_yil)

    # Kullanıcının yaşını hesaplıyoruz
    yas = yas_hesapla(dogum_yili, bu_yil)

    # Kişiye özel selamlama ve yaş bilgisi hazırlıyoruz
    selam = f"Merhaba {ad}!"
    yas_metni = f"{bu_yil} yılında {yas} yaşına girdin ya da gireceksin."

    # Selamlama ve yaş bilgisini ekrana yazdırıyoruz
    print(selam, yas_metni)

    # Yaş aralığına uygun mesajı ekrana yazdırıyoruz
    print(mesaj_olustur(ad, yas))


# Dosya doğrudan çalıştırıldığında ana fonksiyonu başlatıyoruz
if __name__ == "__main__":
    try:
        main()

    except (KeyboardInterrupt, EOFError):
        # Program yarıda kesilirse kısa bir mesaj gösteriyoruz
        print("\nProgram sonlandırıldı.")

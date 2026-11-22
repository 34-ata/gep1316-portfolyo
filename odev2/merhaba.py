# Haftalık Ödev 2 - merhaba.py
# Kullanıcının adını ve doğum yılını alıp yaşını hesaplayan program

# Bugünün tarihini öğrenmek için datetime modülünden date sınıfını alıyoruz
from datetime import date


# Kullanıcıdan adını alıp metin (str) olarak döndüren fonksiyon
def ad_al() -> str:
    # Adı okuyup baştaki ve sondaki boşlukları siliyoruz
    ad = input("Adınız: ").strip()
    return ad  # Temizlenmiş adı fonksiyonun sonucu olarak geri veriyoruz


# Kullanıcıdan doğum yılını alıp tam sayı (int) olarak döndüren fonksiyon
def dogum_yili_al() -> int:
    # Girilen yılı önce metin olarak okuyup boşlukları siliyoruz
    yil_metni = input("Doğum yılınız: ").strip()
    dogum_yili = int(yil_metni)  # Metni hesap için tam sayıya çeviriyoruz
    return dogum_yili  # Doğum yılını fonksiyonun sonucu olarak veriyoruz


# Doğum yılı ile bu yılın farkından yaşı bulan fonksiyon
def yas_hesapla(dogum_yili: int, bu_yil: int) -> int:
    return bu_yil - dogum_yili  # Bu yıldan doğum yılını çıkarıp yaşı veriyoruz


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


# Dosya başka bir dosyaya eklenmeden doğrudan çalıştırıldıysa
if __name__ == "__main__":
    main()  # ana fonksiyonu başlatıyoruz

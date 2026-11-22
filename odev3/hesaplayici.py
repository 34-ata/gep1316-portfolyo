# Haftalık Ödev 3 - hesaplayici.py
# Fisher denklemiyle bir yatırımın reel getirisini hesaplayan program


# Kullanıcıdan bir metin alıp baştaki ve sondaki boşlukları silen fonksiyon
def metin_al(soru: str) -> str:
    return input(soru).strip()  # Girilen metni temizleyip geri veriyoruz


# Kullanıcıdan yüzde olarak bir oran alıp float döndüren fonksiyon
def oran_al(soru: str) -> float:
    metin = input(soru).strip()  # Girdiyi önce metin olarak okuyoruz
    return float(metin)  # Metni ondalıklı sayıya (float) çevirip veriyoruz


# Kullanıcıdan vadeyi yıl olarak alıp int döndüren fonksiyon
def vade_al() -> int:
    metin = input("Vade (yıl): ").strip()  # Vadeyi metin olarak okuyoruz
    return int(metin)  # Metni tam sayıya (int) çevirip geri veriyoruz


# Fisher denkleminin kesin hâli: r = (1 + i) / (1 + π) - 1
def reel_getiri_hesapla(nominal_oran: float, enflasyon_orani: float) -> float:
    # Nominal büyümeyi enflasyon büyümesine bölüp 1 çıkarıyoruz
    return (1 + nominal_oran) / (1 + enflasyon_orani) - 1


# Yıllık oranı vade boyunca bileşik olarak toplam orana çeviren fonksiyon
def toplam_getiri_hesapla(yillik_oran: float, vade: int) -> float:
    return (1 + yillik_oran) ** vade - 1  # (1 + r) üssü vade, eksi 1


# Oranı Türkçe yazımla yüzde metnine çeviren fonksiyon (-0.1 -> -%10,00)
def yuzde_yaz(oran: float) -> str:
    isaret = "-" if oran < 0 else ""  # Negatifse eksi işaretini ayırıyoruz
    # Mutlak değeri yüzdeye çevirip iki basamakla yazıyor, noktayı virgüle
    # çeviriyoruz; eksi işareti yüzde işaretinin önüne geliyor
    return f"{isaret}%{abs(oran) * 100:.2f}".replace(".", ",")


# Reel getiriye göre yatırımın durumunu anlatan mesajı döndüren fonksiyon
def durum_mesaji(ad: str, reel_oran: float, deger_kazandi: bool) -> str:
    if deger_kazandi:  # Reel getiri sıfırdan büyükse
        return f"{ad} enflasyona karşı değer kazandı."  # Kazanç mesajı
    elif reel_oran < 0:  # Reel getiri sıfırdan küçükse
        return f"{ad} enflasyona karşı değer kaybetti."  # Kayıp mesajı
    else:  # Reel getiri tam olarak sıfırsa
        return f"{ad} enflasyona karşı değerini korudu."  # Koruma mesajı


def main() -> None:  # Programın ana akışını yöneten fonksiyon
    print("=== Reel Getiri Hesaplayıcı ===")  # Başlığı yazdırıyoruz
    yatirim_adi = metin_al("Yatırımın adı: ")  # Yatırımın adını alıyoruz (str)
    # Yıllık nominal getiriyi yüzde olarak alıyoruz (float)
    nominal_yuzde = oran_al("Yıllık nominal getiri (%): ")
    # Yıllık enflasyonu yüzde olarak alıyoruz (float)
    enflasyon_yuzde = oran_al("Yıllık enflasyon (%): ")
    vade = vade_al()  # Vadeyi yıl olarak alıyoruz (int)

    nominal_oran = nominal_yuzde / 100  # Yüzdeyi ondalık orana çeviriyoruz
    enflasyon_orani = enflasyon_yuzde / 100  # Yüzdeyi orana çeviriyoruz
    # Fisher denklemiyle yıllık reel getiriyi hesaplıyoruz
    reel_oran = reel_getiri_hesapla(nominal_oran, enflasyon_orani)
    # Vade boyunca birikecek toplam reel getiriyi hesaplıyoruz
    toplam_reel = toplam_getiri_hesapla(reel_oran, vade)
    deger_kazandi = reel_oran > 0  # Reel getiri pozitifse True olur (bool)

    print()  # Sonuçlardan önce bir boş satır bırakıyoruz
    print("--- Sonuç ---")  # Sonuç bölümünün başlığını yazdırıyoruz
    print(f"Yatırım                 : {yatirim_adi}")  # Yatırımın adı
    print(f"Vade                    : {vade} yıl")  # Vade süresi
    # Girilen nominal getiriyi yüzde olarak yazdırıyoruz
    print(f"Nominal getiri (yıllık) : {yuzde_yaz(nominal_oran)}")
    # Girilen enflasyonu yüzde olarak yazdırıyoruz
    print(f"Enflasyon (yıllık)      : {yuzde_yaz(enflasyon_orani)}")
    # Hesaplanan yıllık reel getiriyi yazdırıyoruz
    print(f"Reel getiri (yıllık)    : {yuzde_yaz(reel_oran)}")
    # Vade boyunca toplam reel getiriyi yazdırıyoruz
    print(f"Toplam reel getiri      : {yuzde_yaz(toplam_reel)}")
    # Yatırımın enflasyona karşı durumunu yazdırıyoruz
    print("Durum:", durum_mesaji(yatirim_adi, reel_oran, deger_kazandi))


# Dosya başka bir dosyaya eklenmeden doğrudan çalıştırıldıysa
if __name__ == "__main__":
    main()  # Ana fonksiyonu başlatıyoruz

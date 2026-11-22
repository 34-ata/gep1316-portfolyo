# Haftalık Ödev 3 - hesaplayici.py
# Fisher denklemiyle bir yatırımın reel getirisini hesaplayan program


# Kullanıcıdan boş olmayan bir metin alan fonksiyon
def metin_al(soru: str) -> str:
    while True:  # Boş olmayan bir metin girilene kadar soruyu tekrarlıyoruz
        metin = input(soru).strip()  # Girdiyi okuyup boşlukları siliyoruz
        if metin:  # Metin boş değilse
            return metin  # Metni geri veriyoruz
        print("Uyarı: Bu alan boş bırakılamaz.")  # Boşsa uyarıyoruz


# Kullanıcıdan yüzde olarak, sınırlar içinde bir oran alan fonksiyon
def oran_al(soru: str, alt: float, ust: float, alt_dahil: bool) -> float:
    while True:  # Geçerli bir sayı girilene kadar soruyu tekrarlıyoruz
        metin = input(soru).strip()  # Girdiyi önce metin olarak okuyoruz
        metin = metin.replace(",", ".")  # Virgülü noktaya çeviriyoruz
        try:  # Sayıya çevirme hata verebileceği için deniyoruz
            deger = float(metin)  # Metni ondalıklı sayıya (float) çeviriyoruz
        except ValueError:  # Sayı olmayan ya da boş bir girdi gelirse
            print("Uyarı: Lütfen bir sayı girin (örnek: 45,5).")  # Uyarıyoruz
            continue  # Döngünün başına dönüp yeniden soruyoruz
        if alt_dahil:  # Alt sınır kabul edilen değerlere dahilse
            gecerli = alt <= deger <= ust  # Alt ve üst sınır dahil kontrol
        else:  # Alt sınır dahil değilse
            gecerli = alt < deger <= ust  # Alt sınırdan büyük olmalı
        if gecerli:  # Değer sınırlar içindeyse
            return deger  # Değeri geri veriyoruz
        if alt_dahil:  # Uyarı metnini sınır türüne göre seçiyoruz
            # Alt sınır dahil olduğunda gösterilecek uyarı
            print(f"Uyarı: Değer şu aralıkta olmalı: {alt:g} ≤ değer ≤ {ust:g}")
        else:  # Alt sınır dahil değilse
            # Alt sınır dahil olmadığında gösterilecek uyarı
            print(f"Uyarı: Değer şu aralıkta olmalı: {alt:g} < değer ≤ {ust:g}")


# Kullanıcıdan 1-100 yıl arasında bir vade alıp int döndüren fonksiyon
def vade_al() -> int:
    while True:  # Geçerli bir vade girilene kadar soruyu tekrarlıyoruz
        metin = input("Vade (yıl): ").strip()  # Vadeyi metin olarak okuyoruz
        try:  # Tam sayıya çevirme hata verebileceği için deniyoruz
            vade = int(metin)  # Metni tam sayıya (int) çeviriyoruz
        except ValueError:  # Harf, ondalık sayı ya da boş girdi gelirse
            print("Uyarı: Vade tam sayı olmalı (örnek: 5).")  # Uyarıyoruz
            continue  # Döngünün başına dönüp yeniden soruyoruz
        if 1 <= vade <= 100:  # Vade 1 ile 100 yıl arasındaysa
            return vade  # Vadeyi geri veriyoruz
        print("Uyarı: Vade 1 ile 100 yıl arasında olmalı.")  # Sınır uyarısı


# Fisher denkleminin kesin hâli: r = (1 + i) / (1 + π) - 1
def reel_getiri_hesapla(nominal_oran: float, enflasyon_orani: float) -> float:
    # Nominal büyümeyi enflasyon büyümesine bölüp 1 çıkarıyoruz
    return (nominal_oran - enflasyon_orani) / (1 + nominal_oran)


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
    # Nominal getiriyi yüzde olarak alıyoruz (float); -100 dahil, en fazla 1000
    nominal_yuzde = oran_al("Yıllık nominal getiri (%): ", -100.0, 1000.0, True)
    # Enflasyonu yüzde olarak alıyoruz (float); -50'den büyük, en fazla 1000
    enflasyon_yuzde = oran_al("Yıllık enflasyon (%): ", -50.0, 1000.0, False)
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
    try:  # Kullanıcı programı yarıda keserse hata dökümü göstermemek için
        main()  # Ana fonksiyonu başlatıyoruz
    except (KeyboardInterrupt, EOFError):  # Ctrl+C ya da Ctrl+D gelirse
        print("\nProgram sonlandırıldı.")  # Kısa bir kapanış mesajı yazıyoruz

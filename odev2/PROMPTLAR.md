# PROMPTLAR — Haftalık Ödev 2

## İstem Tablosu

| # | İstemim | YZ ne yaptı? | Ben ne yaptım? |
|---|---|---|---|
| 1 | Ödevin gereksinimlerini verip dosya oluşturmadan önce plan istedim. | README, `merhaba.py`, dosya yapısı ve commit sırası için plan sundu; 4 konuda onay istedi. | Ara Değerlendirme Ödevi 1'i (maliyet hesaplayıcı) Haftalık Ödev 1 sandığını fark edip düzelttirdim. README'yi portfolyo ana sayfası sanmıştı; sitenin `index.html` ile yayınlanacağını açıkladım. Site dosyaları köke geleceği için ödev dosyalarını `odev2/` klasörüne taşıttım. Yıl kontrollerini kendim yazmayı üstlendim ve her satıra yorum istedim. Türkçe İ harfini bozan `.title()`'dan kaçınmasını, `datetime` ve `try/except` kullanımını kabul ettim. |
| 2 | README'nin tanıtım, ilgi alanları ve beklenti bölümlerini istedim. | Metni yazdı, tahmine dayalı yerleri işaretledi; açıklamasında Ara Değerlendirme Ödevi 1'e yine "Ödev 1" dedi. | Düzeltmenin kalıcı olmadığını görüp tekrar düzelttirdim. Ortağımla geliştirdiğimiz yazılımın amacını gerçek durumla değiştirdim. Beni yeni başlayan biri gibi gösteren cümleyi çıkardım. Ders beklentisini kendi fikrimle yazdırdım. BAU ve 42 İstanbul bağlantılarını eklettim. |
| 3 | Düzeltilmiş README'yi istedim. | 42 İstanbul adresinin yönlendirildiğini fark edip resmî adresi kullandı; yazılım geçmişimi bağlam olarak ekledi. | Bağlantıları kendim açıp doğruladım; eklenen cümleyi kabul ettim. |
| 4 | "Kodlama ve YZ'nin Mesleğimdeki Yeri" paragrafını istedim. | 114 kelimelik paragraf yazdı; kâr oranı/kâr marjı karışıklığını varsayımsal örnek olarak verdi, YZ kullanım alanlarımı tahmin etti. | Bu karışıklığın Ara Değerlendirme Ödevi 1'de gerçekten yaşandığını belirtip gerçek olay olarak yazdırdım. Kullanım alanlarını kendi gerçek kullanımımla değiştirdim (güvenilir kaynaklardan araştırma, güncel haber ve veri takibi). |
| 5 | Güncellenmiş paragrafı istedim. | 150 kelime sınırı için metni sıkılaştırdı (140 kelime). | Kelime sayısını ve kâr marjı hesabını (%25 kâr oranı = %20 kâr marjı) kendim doğruladım. |
| 6 | `merhaba.py`'nin ilk sürümünü istedim. | Kodu yazıp test etti; harf girildiğinde programın çöktüğünü belirtti. | Kendi planındaki "uzun satırda yorum üste yazılır" kuralına uymadığını ve bazı satırların 130 karakteri geçtiğini fark edip düzelttirdim. Testlerde atlanan boş ad durumunu tespit ettim. |
| 7 | Hatalı girdi kontrolü ve yaşa göre özel mesajı istedim. | `try/except`, boş ad kontrolü ve yaş aralığına göre mesaj ekledi; sınır yaşlarıyla test etti. | Kodu kendim çalıştırıp denemediği girdileri denedim: `2_003`, `+1990` ve Unicode rakamlar `int()` tarafından kabul ediliyor, ama doğru yılı verdikleri için sorun saymadım. `0`, `-5` ve `3000` girdilerinin anlamsız yaş ürettiğini görüp yıl kontrolünün gerekli olduğunu doğruladım. |

## Kendi Yaptığım Değişiklik

Gelecekteki yıl ve 1900'den önceki yıl kontrollerini YZ'ye yazdırmadan kendim yazdım. `bu_yil` değerini `main()`'den `dogum_yili_al()` fonksiyonuna parametre olarak geçirerek yılın tek bir yerde hesaplanmasını sağladım. 1899, 1900, 0, -5, 2026, 2027 ve 3000 girdileriyle test ettim (ekran görüntüleri: [ekran_goruntuleri/](ekran_goruntuleri/)).

## YZ Kullanım Beyanı

- **Kullanılan araçlar:** Claude Code (Anthropic, VS Code eklentisi) ve Claude (claude.ai sohbet arayüzü)
- **Kullanma amacı:** Claude Code ile README metni, `merhaba.py`'nin ilk sürümü, hatalı girdi kontrolü, yorum satırlarının tamamlanması ve PROMPTLAR.md'nin düzenlenmesi; claude.ai ile ödevin planlanması ve YZ çıktılarının incelenmesi.
- **Kontrol ve sorumluluk:** Yapay zekâ tarafından üretilen içeriği gözden geçirdiğimi, gerekli düzeltmeleri yaptığımı ve teslim ettiğim çalışmanın doğruluğundan ve akademik dürüstlüğünden sorumlu olduğumu beyan ederim.
- **Ad-soyad:** Fatih Mehmet Ata
- **Tarih:** 22.11.2026

## Kaynakça

Anthropic. (2026). *Claude* [Büyük dil modeli]. https://claude.ai

Python Software Foundation. (t.y.). *datetime — Basic date and time types*. Python 3 belgeleri. https://docs.python.org/3/library/datetime.html

# PROMPTLAR — Haftalık Ödev 3

## İstem Tablosu

| # | İstemim | YZ ne yaptı? | Ben ne yaptım? |
|---|---|---|---|
| 1 | Gereksinimleri verip plan istedim. | Fisher'ın kesin formülü, yaklaşık formül karşılaştırması ve kapsamlı hatalı girdi kontrolleriyle bir plan sundu; taşmayı 100 yıllık vade sınırıyla önlemeyi önerdi. | Kapsamı ödevin asgari gereksinimlerine indirdim (yaklaşık formül, `nan`/`inf` kontrolü ve ayrı test dosyası çıkarıldı). Oranlara üst sınır olmadığı için vade sınırının taşmayı önlemediğini terminalde kendim denedim (`OverflowError`). Nominal −100'ün geçerli bir durum olduğunu, sıfıra bölmenin sadece enflasyonda oluştuğunu düzelttim. Hata avı commit'inin benim adımla tek başına görünmemesi için yöntemi değiştirdim. |
| 2 | Sadeleştirilmiş kapsamı ve sınırları verdim. | Verdiğim sınırların da taşmayı önlemediğini, enflasyon −100'e yaklaştıkça paydanın sıfıra yaklaştığını hesapla gösterdi. | Hesabı kontrol edip haklı olduğunu kabul ettim. Enflasyon alt sınırını −50 yaptım ve en kötü durumun (22^100 ≈ 10^134) güvenli olduğunu doğruladım. İncelediğim bir makalenin (Mogaji, 2010) Fisher denkleminin yaklaşık hâlini kullandığını gördüm; kesin formülü türeterek kullandım. |
| 3 | Temel hesap kodunu istedim. | Kodu yazdı, örneklerini elle doğruladı, bu örnekleri testlerimde kullanmamamı önerdi. | Hesapları kontrol edip kabul ettim. Negatif yüzde yazımını Türkçeye uygun hâle getirttim (-%10,34). |
| 4 | Hatalı girdi kontrollerini istedim. | Kontrolleri ve sınırları ekledi; en kötü durumun çökmediğini ama 137 basamaklı bir sonuç ürettiğini belirtti. | Sınırların kararlarıma uyduğunu kontrol ettim; çok büyük sonucu "çok büyük değer" uç durum testi olarak bıraktım. |
| 5 | Fark edilmesi zor bir mantık hatası eklemesini, yerini söylememesini istedim. | Hatayı ekleyip `Co-Authored-By` satırıyla commit'ledi, ayrıntı vermedi. | Önceden kendim hesapladığım 5 senaryoyla test ettim; 4'ünde değerler farklı çıktı, nominal −100'de program `ZeroDivisionError` ile çöktü. Hatayı reel getiri formülünün paydasında buldum, kendim düzeltip commit'ledim. |

## YZ Kullanım Beyanı

- **Kullanılan araçlar:** Claude Code (Anthropic, VS Code eklentisi) ve Claude (claude.ai sohbet arayüzü)
- **Kullanma amacı:** Claude Code ile hesaplayıcının tanımı, kodu, hatalı girdi kontrolleri, hata avı için hata eklenmesi ve PROMPTLAR.md'nin düzenlenmesi; claude.ai ile ödevin planlanması, YZ çıktılarının incelenmesi ve hata avı yazısının taslağı.
- **Kontrol ve sorumluluk:** Yapay zekâ tarafından üretilen içeriği gözden geçirdiğimi, gerekli düzeltmeleri yaptığımı ve teslim ettiğim çalışmanın doğruluğundan ve akademik dürüstlüğünden sorumlu olduğumu beyan ederim.
- **Ad-soyad:** Fatih Mehmet Ata
- **Tarih:** 22.11.2026

## Kaynakça

Anthropic. (2026). *Claude* [Büyük dil modeli]. https://claude.ai

Fisher, I. (1930). *The theory of interest*. Macmillan.

Mogaji, P. K. (2010). *Fisher effect and the relationship between nominal interest rates and inflation: The case of Nigeria* (MPRA Paper No. 99040). Munich Personal RePEc Archive. https://mpra.ub.uni-muenchen.de/99040/

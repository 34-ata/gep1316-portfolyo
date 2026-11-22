// Fatih Mehmet Ata — portfolyo sitesi ortak betiği
// Dört sayfada da kullanılır. Hiçbir veri sunucuya ya da üçüncü tarafa
// gönderilmez; yalnızca tema tercihi tarayıcının localStorage'ında tutulur.
"use strict";

const kok = document.documentElement;

// ===== 1. Tema değiştirme =====
// <head> içindeki tek satırlık betik, kayıtlı tercihi sayfa çizilmeden önce
// uygular. Bu fonksiyon düğmeyi çalıştırır ve yeni tercihi kaydeder.
function temaKur() {
  const dugme = document.getElementById("temaDugmesi");
  if (!dugme) return;
  const etiket = dugme.querySelector(".tema-etiket");

  // Temayı uygular ve düğmenin erişilebilir adını yapılacak işe göre yazar
  function uygula(tema) {
    kok.dataset.theme = tema;
    etiket.textContent =
      tema === "light" ? "Koyu temaya geç" : "Açık temaya geç";
  }

  uygula(kok.dataset.theme === "light" ? "light" : "dark");

  dugme.addEventListener("click", () => {
    const yeniTema = kok.dataset.theme === "light" ? "dark" : "light";
    uygula(yeniTema);
    try {
      localStorage.setItem("tema", yeniTema);
    } catch (hata) {
      // Depolama kapalıysa (ör. gizli pencere) tercih yalnızca bu sayfada geçerli
    }
  });
}

// ===== 2. Mobil menü =====
// Gemini'dan alınan menü kodunun uyarlanmış hâli
function menuKur() {
  const dugme = document.getElementById("menuDugmesi");
  const menu = document.getElementById("navMenu");
  if (!dugme || !menu) return;

  // CSS'teki tablet kırılma noktasıyla aynı sorgu (tek kaynak: 768 px)
  const genisEkran = window.matchMedia("(min-width: 768px)");

  function acikMi() {
    return menu.classList.contains("acik");
  }

  function kapat() {
    menu.classList.remove("acik");
    dugme.setAttribute("aria-expanded", "false");
  }

  dugme.addEventListener("click", () => {
    const acik = menu.classList.toggle("acik");
    dugme.setAttribute("aria-expanded", String(acik));
  });

  // Menüden bir bağlantı seçilince kapat
  menu.querySelectorAll("a").forEach((baglanti) => {
    baglanti.addEventListener("click", kapat);
  });

  // Menünün dışına tıklanınca kapat
  document.addEventListener("click", (olay) => {
    const iceride =
      menu.contains(olay.target) || dugme.contains(olay.target);
    if (acikMi() && !iceride) kapat();
  });

  // Escape tuşuyla kapat ve odağı menü düğmesine geri ver
  document.addEventListener("keydown", (olay) => {
    if (olay.key === "Escape" && acikMi()) {
      kapat();
      dugme.focus();
    }
  });

  // Ekran tablet genişliğine çıkarsa açık kalan mobil menüyü sıfırla
  genisEkran.addEventListener("change", (olay) => {
    if (olay.matches) kapat();
  });
}

// ===== 3. Proje filtreleme (yalnızca projeler sayfasında) =====
function filtreKur() {
  const grup = document.getElementById("filtreGrubu");
  const sonuc = document.getElementById("filtreSonuc");
  const kartlar = document.querySelectorAll(".proje-karti");
  if (!grup || !sonuc || kartlar.length === 0) return;

  const dugmeler = grup.querySelectorAll("[data-filtre]");

  // Seçilen etikete uymayan kartları gizler, seçili düğmeyi işaretler
  // ve görünen kart sayısını ekran okuyuculara da duyurur
  function uygula(filtre) {
    let gorunen = 0;
    kartlar.forEach((kart) => {
      const etiketler = kart.dataset.etiket.split(" ");
      const goster = filtre === "tumu" || etiketler.includes(filtre);
      kart.hidden = !goster;
      if (goster) gorunen += 1;
    });
    dugmeler.forEach((dugme) => {
      const secili = dugme.dataset.filtre === filtre;
      dugme.setAttribute("aria-pressed", String(secili));
    });
    sonuc.textContent = `${gorunen} proje gösteriliyor.`;
  }

  dugmeler.forEach((dugme) => {
    dugme.addEventListener("click", () => uygula(dugme.dataset.filtre));
  });

  grup.hidden = false; // JavaScript çalışıyor: filtreyi göster
}

// Betik "defer" ile yüklendiği için sayfa hazır; doğrudan başlatılır
temaKur();
menuKur();
filtreKur();

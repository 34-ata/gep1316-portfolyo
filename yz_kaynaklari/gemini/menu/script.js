document.addEventListener('DOMContentLoaded', () => {
  const hamburgerBtn = document.getElementById('hamburgerBtn');
  const navMenu = document.getElementById('navMenu');

  if (!hamburgerBtn || !navMenu) return;

  const navLinks = navMenu.querySelectorAll('.nav-link');

  function closeMenu() {
    navMenu.classList.remove('is-open');
    hamburgerBtn.classList.remove('is-active');
    hamburgerBtn.setAttribute('aria-expanded', 'false');
  }

  function toggleMenu() {
    const isOpen = navMenu.classList.toggle('is-open');
    hamburgerBtn.classList.toggle('is-active', isOpen);
    hamburgerBtn.setAttribute('aria-expanded', String(isOpen));
  }

  hamburgerBtn.addEventListener('click', toggleMenu);

  // Menü linkine tıklanınca kapat
  navLinks.forEach((link) => {
    link.addEventListener('click', closeMenu);
  });

  // Menü dışına tıklanınca kapat
  document.addEventListener('click', (event) => {
    const clickedInside =
      navMenu.contains(event.target) || hamburgerBtn.contains(event.target);

    if (!clickedInside && navMenu.classList.contains('is-open')) {
      closeMenu();
    }
  });

  // Escape tuşu ile kapat
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && navMenu.classList.contains('is-open')) {
      closeMenu();
      hamburgerBtn.focus();
    }
  });

  // Ekran masaüstü genişliğine geçerse açık kalan mobil durumu temizle
  window.addEventListener('resize', () => {
    if (window.innerWidth > 768 && navMenu.classList.contains('is-open')) {
      closeMenu();
    }
  });
});
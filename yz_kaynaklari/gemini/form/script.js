document.addEventListener('DOMContentLoaded', () => {
  const contactForm = document.getElementById('contactForm');
  const nameInput = document.getElementById('name');
  const emailInput = document.getElementById('email');
  const messageInput = document.getElementById('message');

  const nameError = document.getElementById('nameError');
  const emailError = document.getElementById('emailError');
  const messageError = document.getElementById('messageError');
  const formStatus = document.getElementById('formStatus');

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  function showFieldError(input, errorElement, message) {
    input.classList.add('input-error');
    input.setAttribute('aria-invalid', 'true');
    errorElement.textContent = message;
  }

  function clearFieldError(input, errorElement) {
    input.classList.remove('input-error');
    input.removeAttribute('aria-invalid');
    errorElement.textContent = '';
  }

  function setFormStatus(type, message) {
    formStatus.className = `form-status ${type}`;
    formStatus.textContent = message;
  }

  // Kullanıcı yazmaya başladığında ilgili alanın hatasını kaldır
  nameInput.addEventListener('input', () => clearFieldError(nameInput, nameError));
  emailInput.addEventListener('input', () => clearFieldError(emailInput, emailError));
  messageInput.addEventListener('input', () => clearFieldError(messageInput, messageError));

  contactForm.addEventListener('submit', (event) => {
    event.preventDefault();

    let isValid = true;
    const nameValue = nameInput.value.trim();
    const emailValue = emailInput.value.trim();
    const messageValue = messageInput.value.trim();

    formStatus.className = 'form-status';
    formStatus.textContent = '';

    // Ad kontrolü
    if (nameValue === '') {
      showFieldError(nameInput, nameError, 'Lütfen adınızı girin.');
      isValid = false;
    } else {
      clearFieldError(nameInput, nameError);
    }

    // E-posta kontrolü
    if (emailValue === '') {
      showFieldError(emailInput, emailError, 'Lütfen e-posta adresinizi girin.');
      isValid = false;
    } else if (!emailRegex.test(emailValue)) {
      showFieldError(emailInput, emailError, 'Lütfen geçerli bir e-posta adresi girin.');
      isValid = false;
    } else {
      clearFieldError(emailInput, emailError);
    }

    // Mesaj kontrolü
    if (messageValue === '') {
      showFieldError(messageInput, messageError, 'Lütfen mesajınızı yazın.');
      isValid = false;
    } else {
      clearFieldError(messageInput, messageError);
    }

    if (!isValid) {
      setFormStatus('error', 'Lütfen işaretli alanları kontrol edip tekrar deneyin.');
      return;
    }

    setFormStatus('success', `Teşekkürler ${nameValue}, mesajınız başarıyla alındı.`);
    contactForm.reset();
  });
});
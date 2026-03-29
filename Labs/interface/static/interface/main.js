/* ──────────────────────────────────────
   Navbar scroll shadow
   ────────────────────────────────────── */
(function initNavbar() {
  const navbar = /** @type {HTMLElement|null} */ (document.querySelector('.custom-navbar'));
  if (!navbar) return;
  window.addEventListener('scroll', () => {
    navbar.style.boxShadow = window.scrollY > 20 ? '0 4px 24px rgba(0,0,0,.5)' : 'none';
  }, { passive: true });
})();

/* ──────────────────────────────────────
   Services dropdown (click toggle)
   ────────────────────────────────────── */
(function initDropdown() {
  const btn  = document.getElementById('dd-btn');
  const menu = document.getElementById('dd-menu');
  if (!btn || !menu) return;

  btn.addEventListener('click', e => {
    e.stopPropagation();
    const open = menu.classList.toggle('open');
    btn.setAttribute('aria-expanded', String(open));
  });

  // Close when clicking outside
  document.addEventListener('click', () => menu.classList.remove('open'));
})();

/* ──────────────────────────────────────
   Mobile hamburger (click toggle)
   ────────────────────────────────────── */
(function initHamburger() {
  const btn  = document.getElementById('hamburger');
  const menu = document.getElementById('mobile-menu');
  if (!btn || !menu) return;

  btn.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    btn.setAttribute('aria-expanded', String(open));
  });
})();

/* ──────────────────────────────────────
   Active nav-link highlight
   ────────────────────────────────────── */
(function highlightActiveNav() {
  const path = window.location.pathname;
  document.querySelectorAll('.custom-nav-link').forEach(link => {
    const href = link.getAttribute('href');
    if (href && path === href) {
      link.classList.add('active');
    }
  });
})();

/* ──────────────────────────────────────
   Animated number counter (stats)
   ────────────────────────────────────── */
(function animateCounters() {
  /** @param {HTMLElement} el @param {number} target @param {number} duration */
  function countUp(el, target, duration) {
    const start = performance.now();
    const update = (/** @type {number} */ now) => {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // ease-out-cubic
      el.textContent = Math.round(eased * target).toLocaleString() + (el.dataset.suffix || '');
      if (progress < 1) requestAnimationFrame(update);
    };
    requestAnimationFrame(update);
  }

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = /** @type {HTMLElement} */ (entry.target);
        const target = parseInt(el.dataset.target || '0', 10);
        countUp(el, target, 1200);
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('[data-target]').forEach(el => observer.observe(el));
})();

/* ──────────────────────────────────────
   Card stagger entrance
   ────────────────────────────────────── */
(function staggerCards() {
  const cards = document.querySelectorAll('.feature-card, .test-chip, .result-card');
  if (!cards.length) return;

  const observer = new IntersectionObserver(entries => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        const el = /** @type {HTMLElement} */ (entry.target);
        setTimeout(() => {
          el.style.opacity = '1';
          el.style.transform = 'translateY(0)';
        }, i * 60);
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.1 });

  cards.forEach(card => {
    const el = /** @type {HTMLElement} */ (card);
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity .4s ease, transform .4s ease';
    observer.observe(el);
  });
})();

/* ──────────────────────────────────────
   Test search filter (lists page)
   ────────────────────────────────────── */
(function initTestSearch() {
  const input = /** @type {HTMLInputElement|null} */ (document.getElementById('test-search'));
  if (!input) return;

  input.addEventListener('input', () => {
    const q = input.value.toLowerCase().trim();
    document.querySelectorAll('.test-chip').forEach(chip => {
      const el = /** @type {HTMLElement} */ (chip);
      const text = el.textContent.toLowerCase();
      el.style.display = (!q || text.includes(q)) ? '' : 'none';
    });
  });
})();

/* ──────────────────────────────────────
   Form validation feedback
   ────────────────────────────────────── */
(function initFormValidation() {
  const form = /** @type {HTMLFormElement|null} */ (document.querySelector('form[data-validate]'));
  if (!form) return;

  form.addEventListener('submit', e => {
    const inputs = form.querySelectorAll('[required]');
    let valid = true;

    inputs.forEach(inp => {
      const el = /** @type {HTMLInputElement} */ (inp);
      if (!el.value.trim()) {
        el.style.borderColor = 'var(--danger)';
        el.style.boxShadow = '0 0 0 3px rgba(239,68,68,.15)';
        valid = false;
      } else {
        el.style.borderColor = '';
        el.style.boxShadow = '';
      }
    });

    if (!valid) {
      e.preventDefault();
      const msg = document.getElementById('form-error-msg');
      if (msg) {
        msg.style.display = 'flex';
        setTimeout(() => msg.style.display = 'none', 4000);
      }
    }
  });

  // live border reset
  form.querySelectorAll('[required]').forEach(inp => {
    inp.addEventListener('input', () => {
      const el = /** @type {HTMLInputElement} */ (inp);
      if (el.value.trim()) {
        el.style.borderColor = 'var(--success)';
        el.style.boxShadow = '0 0 0 3px rgba(34,197,94,.12)';
      }
    });
  });
})();

/* ──────────────────────────────────────
   Alert auto-dismiss
   ────────────────────────────────────── */
(function autoDismissAlerts() {
  document.querySelectorAll('.alert').forEach(alert => {
    const closeBtn = alert.querySelector('.btn-close');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        const el = /** @type {HTMLElement} */ (alert);
        el.style.opacity = '0';
        el.style.transform = 'translateY(-8px)';
        el.style.transition = 'opacity .3s, transform .3s';
        setTimeout(() => el.remove(), 300);
      });
    }
    // auto dismiss after 5s
    setTimeout(() => {
      const el = /** @type {HTMLElement} */ (alert);
      el.style.opacity = '0';
      el.style.transform = 'translateY(-8px)';
      el.style.transition = 'opacity .3s, transform .3s';
      setTimeout(() => el.remove(), 300);
    }, 5000);
  });
})();

/* ──────────────────────────────────────
   Phone number formatting
   ────────────────────────────────────── */
(function formatPhone() {
  const ph = /** @type {HTMLInputElement|null} */ (document.getElementById('phonenumber'));
  if (!ph) return;
  ph.addEventListener('input', () => {
    ph.value = ph.value.replace(/\D/g, '').slice(0, 10);
  });
})();

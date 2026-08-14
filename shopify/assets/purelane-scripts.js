/* ==========================================================================
   Purelane Theme JS Modules
   Theme-editor safe scripts with shopify:section:load re-initialization
   ========================================================================== */

(function () {
  'use strict';

  function initReveal() {
    const reveals = document.querySelectorAll('.rv');
    if (!reveals.length) return;

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      reveals.forEach((el) => el.classList.add('in'));
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('in');
          }
        });
      },
      { rootMargin: '0px 0px -12% 0px' }
    );

    reveals.forEach((el) => observer.observe(el));
  }

  function initHeroStage() {
    const hero = document.querySelector('.hero');
    if (!hero) return;

    const slides = hero.querySelectorAll('.hslide');
    const dots = hero.querySelectorAll('#hdots button');
    if (!slides.length || !dots.length) return;

    let currentIndex = 0;
    let timer = null;

    function showSlide(index) {
      slides.forEach((slide, i) => slide.classList.toggle('active', i === index));
      dots.forEach((dot, i) => dot.classList.toggle('active', i === index));
      currentIndex = index;
    }

    function startAutoRotate() {
      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      stopAutoRotate();
      timer = setInterval(() => {
        const next = (currentIndex + 1) % slides.length;
        showSlide(next);
      }, 3800);
    }

    function stopAutoRotate() {
      if (timer) clearInterval(timer);
    }

    dots.forEach((dot, index) => {
      dot.addEventListener('click', () => {
        stopAutoRotate();
        showSlide(index);
        startAutoRotate();
      });
    });

    showSlide(0);
    startAutoRotate();
  }

  function initReviewMarquee() {
    const marquee = document.querySelector('.reviews-marquee');
    if (!marquee) return;

    const track = marquee.querySelector('.revtrack');
    if (!track) return;

    // Check if clone already exists to avoid duplicate cloning on section reload
    if (marquee.querySelectorAll('.revtrack').length < 2) {
      const clone = track.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      marquee.appendChild(clone);
    }
  }

  function initAjaxCart() {
    document.addEventListener('submit', function (e) {
      const form = e.target;
      if (!form || !form.matches('.purelane-ajax-form')) return;

      e.preventDefault();
      const submitBtn = form.querySelector('[type="submit"]');
      if (submitBtn) submitBtn.disabled = true;

      const formData = new FormData(form);
      const items = [];

      // Check for multi-item form fields or single variant
      if (form.dataset.items) {
        try {
          const parsed = JSON.parse(form.dataset.items);
          items.push(...parsed);
        } catch (err) {
          console.error('Invalid bundle items payload', err);
        }
      } else {
        const id = formData.get('id');
        const quantity = parseInt(formData.get('quantity') || '1', 10);
        if (id) items.push({ id: parseInt(id, 10), quantity });
      }

      if (!items.length) {
        if (submitBtn) submitBtn.disabled = false;
        return;
      }

      fetch('/cart/add.js', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ items }),
      })
        .then((res) => res.json())
        .then((data) => {
          document.dispatchEvent(new CustomEvent('cart:refresh', { detail: data }));
          if (submitBtn) submitBtn.disabled = false;
        })
        .catch((err) => {
          console.error('Cart add error:', err);
          if (submitBtn) submitBtn.disabled = false;
        });
    });
  }

  function initAll() {
    initReveal();
    initHeroStage();
    initReviewMarquee();
    initAjaxCart();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }

  // Shopify Theme Editor Section Load Event Re-initializer
  document.addEventListener('shopify:section:load', function (e) {
    initAll();
  });
})();

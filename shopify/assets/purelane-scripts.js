/* ==========================================================================
   Purelane Theme JS Modules
   Direct prototype behavior, scene depth response, stage switcher, and AJAX cart.
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
      { rootMargin: '0px 0px -10% 0px' }
    );

    reveals.forEach((el) => observer.observe(el));
  }

  function initHeroStage() {
    const hero = document.querySelector('.hero');
    if (!hero) return;

    const slides = hero.querySelectorAll('.hslide');
    const dots = hero.querySelectorAll('.hdots button');
    if (!slides.length || !dots.length) return;

    let currentIndex = 0;
    let timer = null;

    function showSlide(index) {
      slides.forEach((slide, i) => slide.classList.toggle('on', i === index));
      dots.forEach((dot, i) => dot.classList.toggle('on', i === index));
      currentIndex = index;
    }

    function startAutoRotate() {
      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      stopAutoRotate();
      timer = setInterval(() => {
        const next = (currentIndex + 1) % slides.length;
        showSlide(next);
      }, 4000);
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

  function initScenesScroll() {
    const scenes = document.getElementById('scenes');
    if (!scenes) return;

    window.addEventListener('scroll', () => {
      const scrollY = window.scrollY || window.pageYOffset;
      const docH = document.documentElement.scrollHeight - window.innerHeight;
      const progress = docH > 0 ? scrollY / docH : 0;

      let depth = '1';
      if (progress > 0.65) {
        depth = '4';
      } else if (progress > 0.35) {
        depth = '3';
      } else if (progress > 0.15) {
        depth = '2';
      }

      scenes.setAttribute('data-d', depth);
    }, { passive: true });
  }

  function initAjaxCart() {
    document.addEventListener('submit', function (e) {
      const form = e.target;
      if (!form || !form.matches('.purelane-ajax-form')) return;

      e.preventDefault();
      const submitBtn = form.querySelector('[type="submit"]');
      const originalText = submitBtn ? submitBtn.innerHTML : '';
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span>Adding...</span>';
      }

      const formData = new FormData(form);
      const singleId = formData.get('id');
      const singleQty = parseInt(formData.get('quantity') || '1', 10);

      let payload = {};

      if (singleId) {
        payload = {
          items: [
            {
              id: parseInt(singleId, 10),
              quantity: singleQty
            }
          ]
        };
      } else {
        const itemsMap = {};
        for (const [key, value] of formData.entries()) {
          const match = key.match(/^items\[(\d+)\]\[(id|quantity)\]$/);
          if (match) {
            const index = match[1];
            const field = match[2];
            if (!itemsMap[index]) itemsMap[index] = { quantity: 1 };
            if (field === 'id') {
              itemsMap[index].id = parseInt(value, 10);
            } else if (field === 'quantity') {
              itemsMap[index].quantity = parseInt(value, 10);
            }
          }
        }
        const itemsList = Object.values(itemsMap).filter((item) => item.id && !isNaN(item.id));
        payload = { items: itemsList };
      }

      fetch('/cart/add.js', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify(payload)
      })
      .then((res) => {
        if (!res.ok) throw new Error('Cart Add Network Response was not ok');
        return res.json();
      })
      .then((data) => {
        if (submitBtn) {
          submitBtn.innerHTML = '<span>Added ✓</span>';
          setTimeout(() => {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalText;
          }, 1800);
        }

        // Update Cart Count Badge
        fetch('/cart.js')
          .then((res) => res.json())
          .then((cart) => {
            const countEl = document.getElementById('purelane-cart-count');
            if (countEl) countEl.textContent = cart.item_count;

            document.dispatchEvent(
              new CustomEvent('purelane:cart-updated', {
                detail: { cart }
              })
            );
          });
      })
      .catch((err) => {
        console.error('Add to cart error:', err);
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalText;
        }
      });
    });
  }

  function initComboRailNav() {
    const rail = document.getElementById('combos-rail');
    const prevBtn = document.querySelector('.rail-prev');
    const nextBtn = document.querySelector('.rail-next');
    if (!rail) return;

    if (prevBtn) {
      prevBtn.onclick = () => {
        rail.scrollBy({ left: -340, behavior: 'smooth' });
      };
    }
    if (nextBtn) {
      nextBtn.onclick = () => {
        rail.scrollBy({ left: 340, behavior: 'smooth' });
      };
    }
  }

  function initAll() {
    initReveal();
    initHeroStage();
    initScenesScroll();
    initAjaxCart();
    initComboRailNav();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }

  // Support Shopify Theme Editor dynamic re-renders
  document.addEventListener('shopify:section:load', initAll);
  document.addEventListener('shopify:section:select', initAll);
})();

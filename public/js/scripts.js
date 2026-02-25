/* ============================================================
   Alfred Udah – Portfolio Scripts
   No dependencies. Vanilla JS only.
   ============================================================ */

'use strict';

/* ── Mobile menu toggle ─────────────────────────────────── */
function toggleMobileMenu(btn) {
  const menu = document.getElementById('menu');
  if (!menu) return;

  const isOpen = menu.classList.toggle('active');

  // Keep aria-expanded in sync for screen readers
  btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');

  // Prevent body scroll when menu is open
  document.body.style.overflow = isOpen ? 'hidden' : '';
}

/* Close menu when a nav link is clicked (smooth scroll handles the jump) */
document.addEventListener('DOMContentLoaded', () => {
  const menu   = document.getElementById('menu');
  const toggle = document.querySelector('.mobile-toggle');

  if (menu && toggle) {
    menu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        menu.classList.remove('active');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
  }

  /* ── Sticky header shadow on scroll ──────────────────── */
  const header = document.querySelector('.site-header');
  if (header) {
    const onScroll = () => {
      header.classList.toggle('scrolled', window.scrollY > 4);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll(); // run once on load
  }
});

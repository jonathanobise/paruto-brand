// Paruto brand guide — small progressive enhancements. The page reads fine without JS.
const $ = (s, el = document) => el.querySelector(s);
const $$ = (s, el = document) => [...el.querySelectorAll(s)];

// Scroll progress + back-to-top
const progress = $('#progress');
const btt = $('#btt');
const onScroll = () => {
  const h = document.documentElement;
  progress.style.width = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100 + '%';
  btt.classList.toggle('show', scrollY > 500);
};
addEventListener('scroll', onScroll, { passive: true });
onScroll();
btt.addEventListener('click', () => scrollTo({ top: 0, behavior: 'smooth' }));

// Mobile drawer
const burger = $('#burger');
const drawer = $('#drawer');
const setDrawer = (open) => {
  burger.setAttribute('aria-expanded', open);
  burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  drawer.classList.toggle('open', open);
  document.body.style.overflow = open ? 'hidden' : '';
};
burger.addEventListener('click', () => setDrawer(!drawer.classList.contains('open')));
drawer.addEventListener('click', (e) => e.target.closest('a') && setDrawer(false));
addEventListener('keydown', (e) => e.key === 'Escape' && setDrawer(false));

// Highlight the section in view
const links = $$('.nav-links a, .d-link');
const spy = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (!e.isIntersecting) return;
    links.forEach((l) => l.classList.toggle('active', l.getAttribute('href') === '#' + e.target.id));
  });
}, { rootMargin: '-40% 0px -55% 0px' });
$$('section[id]').forEach((s) => spy.observe(s));

// Reveal on scroll
const reveal = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) { e.target.classList.add('in'); reveal.unobserve(e.target); }
  });
}, { threshold: 0.06 });
$$('.reveal').forEach((r) => reveal.observe(r));

// Toast + copy-to-clipboard swatches
const toast = $('#toast');
let toastTimer;
const say = (msg) => {
  toast.textContent = msg;
  toast.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove('show'), 1600);
};
$$('.sw').forEach((sw) => sw.addEventListener('click', async () => {
  try { await navigator.clipboard.writeText(sw.dataset.hex); say(`Copied ${sw.dataset.hex}`); }
  catch { say(sw.dataset.hex); }
}));

// Download list
const L = 'assets/logos/';
const I = 'assets/icons/';
const groups = [
  ['Paruto — master brand', [
    ['Horizontal logo · Gold', L + 'paruto-logo-gold'],
    ['Horizontal logo · Black', L + 'paruto-logo-black'],
    ['Horizontal logo · White', L + 'paruto-logo-white'],
    ['Stacked logo · Gold', L + 'paruto-logo-stacked-gold'],
    ['Stacked logo · Black', L + 'paruto-logo-stacked-black'],
    ['Stacked logo · White', L + 'paruto-logo-stacked-white'],
  ]],
  ['Symbol', [
    ['Symbol · Gold', L + 'paruto-symbol-gold'],
    ['Symbol · Black', L + 'paruto-symbol-black'],
    ['Symbol · White', L + 'paruto-symbol-white'],
  ]],
  ['Company lockups', ['media', 'music', 'capital', 'kids'].flatMap((c) =>
    ['gold', 'black', 'white'].map((v) => [
      `Paruto ${c[0].toUpperCase() + c.slice(1)} · ${v[0].toUpperCase() + v.slice(1)}`,
      `${L}paruto-${c}-logo-${v}`,
    ]))],
  ['Icons', [
    ['Favicon', I + 'favicon', ['svg']],
    ['Favicon 32px', I + 'favicon-32', ['png']],
    ['Apple touch icon 180px', I + 'apple-touch-icon', ['png']],
    ['App icon 192px', I + 'icon-192', ['png']],
    ['App icon 512px', I + 'icon-512', ['png']],
    ['Social share image 1200×630', I + 'og-image', ['png']],
  ]],
];
$('#files').innerHTML = groups.map(([title, items]) => `
  <div><p class="tag">${title}</p><ul>${items.map(([name, path, exts = ['svg', 'png']]) => `
    <li>${name}<span>${exts.map((x) => `<a href="${path}.${x}" download>${x}</a>`).join('')}</span></li>`).join('')}
  </ul></div>`).join('');

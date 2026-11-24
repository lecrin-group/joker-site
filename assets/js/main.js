/* jokeR 立川 — main.js (no library) */
(function () {
  "use strict";
  var doc = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- loader (top page, once per visit) ---------- */
  var loader = document.querySelector(".loader");
  function hideLoader() {
    if (!loader) return;
    loader.classList.add("is-done");
    document.body.classList.add("is-loaded");
    try { sessionStorage.setItem("jk_loaded", "1"); } catch (e) {}
  }
  if (loader) {
    var seen = false;
    try { seen = sessionStorage.getItem("jk_loaded") === "1"; } catch (e) {}
    if (seen || reduce) { loader.style.display = "none"; document.body.classList.add("is-loaded"); }
    else {
      var t0 = Date.now();
      window.addEventListener("load", function () { setTimeout(hideLoader, Math.max(0, 1900 - (Date.now() - t0))); });
      setTimeout(hideLoader, 5000);
      var skip = loader.querySelector(".loader__skip");
      if (skip) skip.addEventListener("click", hideLoader);
    }
  } else { document.body.classList.add("is-loaded"); }

  /* ---------- hamburger menu ---------- */
  var hb = document.querySelector(".hb");
  if (hb) {
    hb.addEventListener("click", function () {
      var open = doc.classList.toggle("is-menu");
      hb.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    document.querySelectorAll(".menu a").forEach(function (a) {
      a.addEventListener("click", function () { doc.classList.remove("is-menu"); document.body.style.overflow = ""; });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && doc.classList.contains("is-menu")) hb.click();
    });
  }

  /* ---------- hero video (wide / tall) ---------- */
  var hv = document.querySelector(".hero__video");
  if (hv) {
    var pick = function () { return window.innerWidth < 768 && window.innerHeight > window.innerWidth ? hv.dataset.tall : hv.dataset.wide; };
    if (reduce) { hv.removeAttribute("autoplay"); }
    else {
      hv.src = pick();
      var p = hv.play(); if (p && p.catch) p.catch(function () {});
      var last = hv.src;
      window.addEventListener("resize", function () {
        var n = pick(); if (n && hv.src.indexOf(n.replace(/^\.\.\//g, "")) === -1 && n !== last) { last = n; hv.src = n; hv.play().catch(function () {}); }
      });
    }
  }

  /* ---------- hero slideshow ---------- */
  var slides = document.querySelectorAll(".hero__slide");
  if (slides.length > 1) {
    var dotsBox = document.querySelector(".hero__dots");
    var cur = 0, timer;
    var dots = [];
    slides.forEach(function (_, i) {
      var b = document.createElement("button");
      b.type = "button"; b.setAttribute("aria-label", "スライド" + (i + 1));
      b.addEventListener("click", function () { go(i); restart(); });
      dotsBox && dotsBox.appendChild(b); dots.push(b);
    });
    function go(n) {
      slides[cur].classList.remove("is-on"); dots[cur] && dots[cur].classList.remove("is-on");
      cur = (n + slides.length) % slides.length;
      var img = slides[cur].querySelector("img");
      if (img) { img.style.animation = "none"; void img.offsetWidth; img.style.animation = ""; }
      slides[cur].classList.add("is-on"); dots[cur] && dots[cur].classList.add("is-on");
      slides.forEach(function (sl, i) {
        var v = sl.querySelector("video");
        if (!v) return;
        if (i === cur && !reduce) { try { v.currentTime = 0; } catch (e) {} var pp = v.play(); if (pp && pp.catch) pp.catch(function () {}); }
        else { v.pause(); }
      });
    }
    function restart() { clearInterval(timer); timer = setInterval(function () { go(cur + 1); }, 7000); }
    dots[0] && dots[0].classList.add("is-on");
    restart();
  }

  /* ---------- split text for pop-in ---------- */
  document.querySelectorAll(".pop-in").forEach(function (el) {
    var html = "", i = 0;
    el.childNodes.forEach(function (n) {
      if (n.nodeType === 3) {
        Array.from(n.textContent).forEach(function (c) {
          html += c.trim() === "" ? c : '<span class="ch" style="transition-delay:' + (i++ * 0.045).toFixed(3) + 's">' + c + "</span>";
        });
      } else if (n.nodeName === "BR") { html += "<br>"; }
      else {
        var inner = "";
        Array.from(n.textContent).forEach(function (c) {
          inner += '<span class="ch" style="transition-delay:' + (i++ * 0.045).toFixed(3) + 's">' + c + "</span>";
        });
        html += "<" + n.nodeName.toLowerCase() + (n.className ? ' class="' + n.className + '"' : "") + ">" + inner + "</" + n.nodeName.toLowerCase() + ">";
      }
    });
    el.innerHTML = html;
  });

  /* ---------- reveal on scroll ---------- */
  var targets = document.querySelectorAll("[data-reveal],.wipe,.pop-in");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (ents) {
      ents.forEach(function (en) {
        if (en.isIntersecting) {
          var d = en.target.getAttribute("data-delay");
          if (d) en.target.style.transitionDelay = d + "s";
          en.target.classList.add("is-in"); io.unobserve(en.target);
        }
      });
    }, { rootMargin: "0px 0px -12% 0px" });
    targets.forEach(function (t) { io.observe(t); });
  } else { targets.forEach(function (t) { t.classList.add("is-in"); }); }

  /* ---------- parallax ---------- */
  var px = document.querySelectorAll("[data-px]");
  var ticking = false;
  function onScroll() {
    var y = window.scrollY, vh = window.innerHeight;
    px.forEach(function (el) {
      var r = el.parentElement.getBoundingClientRect();
      if (r.bottom < -200 || r.top > vh + 200) return;
      var s = parseFloat(el.getAttribute("data-px")) || 0.15;
      var rot = parseFloat(el.getAttribute("data-rot") || 0);
      var off = (r.top + r.height / 2 - vh / 2) * -s;
      el.style.transform = "translate3d(0," + off.toFixed(1) + "px,0) rotate(" + (rot + off * 0.06).toFixed(2) + "deg)";
    });
    var tt = document.querySelector(".totop");
    if (tt) tt.classList.toggle("is-show", y > vh * 0.8);
    ticking = false;
  }
  if (!reduce) {
    window.addEventListener("scroll", function () { if (!ticking) { requestAnimationFrame(onScroll); ticking = true; } }, { passive: true });
  }
  onScroll();

  /* ---------- club spotlight follows the mouse ---------- */
  var club = document.querySelector(".club");
  if (club && !reduce && window.matchMedia("(pointer:fine)").matches) {
    club.addEventListener("pointermove", function (e) {
      var r = club.getBoundingClientRect();
      club.style.setProperty("--mx", (e.clientX - r.left) + "px");
      club.style.setProperty("--my", (e.clientY - r.top) + "px");
    });
  }

  /* ---------- pickup slider ---------- */
  document.querySelectorAll(".slider").forEach(function (sl) {
    var track = sl.querySelector(".slider__track");
    var items = track.children;
    var dotsBox = sl.querySelector(".slider__dots");
    var step = function () { return items[0].getBoundingClientRect().width + 24; };
    sl.querySelector(".prev").addEventListener("click", function () { track.scrollBy({ left: -step(), behavior: "smooth" }); });
    sl.querySelector(".next").addEventListener("click", function () {
      if (track.scrollLeft + track.clientWidth >= track.scrollWidth - 4) track.scrollTo({ left: 0, behavior: "smooth" });
      else track.scrollBy({ left: step(), behavior: "smooth" });
    });
    if (dotsBox) {
      for (var i = 0; i < items.length; i++) dotsBox.appendChild(document.createElement("i"));
      var upd = function () {
        var idx = Math.round(track.scrollLeft / step());
        Array.from(dotsBox.children).forEach(function (d, j) { d.classList.toggle("is-on", j === idx); });
      };
      track.addEventListener("scroll", upd, { passive: true }); upd();
    }
  });


  /* ---------- fast smooth scroll for PAGE TOP and in-page links ---------- */
  function scrollToY(target) {
    var start = window.scrollY, dist = target - start;
    if (reduce || Math.abs(dist) < 2) { window.scrollTo(0, target); return; }
    var dur = Math.min(1100, Math.max(450, Math.abs(dist) * 0.12));
    var t0 = null;
    var ease = function (t) { return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; };
    var stop = false;
    var cancel = function () { stop = true; };
    window.addEventListener("wheel", cancel, { passive: true, once: true });
    window.addEventListener("touchstart", cancel, { passive: true, once: true });
    var done = false, fb, rq;
    function step() {
      if (stop || done) return;
      var now = performance.now();
      if (t0 === null) t0 = now;
      var p = Math.min(1, (now - t0) / dur);
      window.scrollTo(0, start + dist * ease(p));
      if (p >= 1) { done = true; clearTimeout(fb); return; }
      cancelAnimationFrame(rq); rq = requestAnimationFrame(step);
      clearTimeout(fb); fb = setTimeout(step, 40); // keeps going even if frames are throttled
    }
    step();
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a) return;
    var id = a.getAttribute("href");
    var y;
    if (id === "#" || id === "#top") { y = 0; }
    else {
      var el = document.getElementById(id.slice(1));
      if (!el) return;
      y = el.getBoundingClientRect().top + window.scrollY - 10;
    }
    e.preventDefault();
    if (doc.classList.contains("is-menu") && hb) hb.click();
    scrollToY(Math.max(0, y));
    if (id !== "#") history.replaceState(null, "", id);
  });

  /* ---------- contact form -> mail ---------- */
  var form = document.querySelector("#contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = form.elements;
      if (f.website && f.website.value) return; // honeypot
      var body = "お名前：" + f.name.value + "\n電話番号：" + f.tel.value + "\nメールアドレス：" + f.email.value + "\n\nご要望やご質問など：\n" + f.message.value + "\n";
      location.href = "mailto:tatikawajoker@gmail.com?subject=" + encodeURIComponent("【jokeR サイトからのお問い合わせ】") + "&body=" + encodeURIComponent(body);
    });
  }
})();

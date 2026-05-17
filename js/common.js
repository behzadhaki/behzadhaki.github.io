document.addEventListener("DOMContentLoaded", function() {
  'use strict';

  const body = document.querySelector("body"),
  menuOpenIcon = document.querySelector(".nav__icon-menu"),
  menuCloseIcon = document.querySelector(".nav__icon-close"),
  menuList = document.querySelector(".menu-overlay"),
  searchOpenIcon = document.querySelector(".search-button"),
  searchCloseIcon = document.querySelector(".search__close"),
  searchInput = document.querySelector(".search__text"),
  search = document.querySelector(".search"),
  btnScrollToTop = document.querySelector(".top");


  /* =======================
  // Menu and Search
  ======================= */
  menuOpenIcon.addEventListener("click", () => {
    menuOpen();
  });

  menuCloseIcon.addEventListener("click", () => {
    menuClose();
  });

  searchOpenIcon.addEventListener("click", () => {
    searchOpen();
  });

  searchCloseIcon.addEventListener("click", () => {
    searchClose();
  });

  function menuOpen() {
    menuList.classList.add("is-open");
  }

  function menuClose() {
    menuList.classList.remove("is-open");
  }

  function searchOpen() {
    search.classList.add("is-visible");
    setTimeout(function () {
      searchInput.focus();
    }, 300);
  }

  function searchClose() {
    search.classList.remove("is-visible");
  }

  document.addEventListener("keydown", function(e){
    if (e.key == "Escape") {
      searchClose();
    }
  });


  /* =======================
  // Animation Load Page
  ======================= */
  setTimeout(function(){
    body.classList.add("is-in");
  },150)


  /* =======================
  // LazyLoad Images
  ======================= */
  var lazyLoadInstance = new LazyLoad({
    elements_selector: '.lazy'
  })


  /* =======================
  // Zoom Image
  ======================= */
  const lightense = document.querySelector(".page img, .post img"),
  imageLink = document.querySelectorAll(".page a img, .post a img");

  if (imageLink) {
    for (let i = 0; i < imageLink.length; i++) imageLink[i].parentNode.classList.add("image-link");
    for (let i = 0; i < imageLink.length; i++) imageLink[i].classList.add("no-lightense");
  };

  if (lightense) {
    Lightense(".page img:not(.no-lightense), .post img:not(.no-lightense)", {
      padding: 60,
      offset: 30,
      beforeShow: function() {
        // If the image is absolutely positioned (e.g. pub-card__preview), it will
        // collapse to 0×0 inside Lightense's unsized .lightense-wrap. Convert it
        // to static flow with explicit pixel dimensions so Lightense can measure
        // and scale it correctly.
        var img = this.target;
        var imgCs = window.getComputedStyle(img);
        if (imgCs.position === 'absolute') {
          var r = img.getBoundingClientRect();
          this._imgSaved = {
            position: img.style.position,
            inset: img.style.inset,
            width: img.style.width,
            height: img.style.height,
            display: img.style.display,
            margin: img.style.margin
          };
          img.style.position = 'static';
          img.style.inset = '';
          img.style.width = r.width + 'px';
          img.style.height = r.height + 'px';
          img.style.display = 'block';
          img.style.margin = '0';
        }

        // Walk up ancestors and temporarily neutralise anything that would trap
        // the lightense-wrap: stacking contexts (pos+z-index, transform) and overflow:hidden.
        var saved = [];
        var el = img && img.parentElement;
        while (el && el !== document.body) {
          var cs = window.getComputedStyle(el);
          var entry = { el: el };
          var changed = false;
          if (cs.position !== 'static' && cs.zIndex !== 'auto') {
            entry.zIndex = el.style.zIndex;
            el.style.zIndex = 'auto';
            changed = true;
          }
          if (cs.overflow === 'hidden' || cs.overflowX === 'hidden' || cs.overflowY === 'hidden') {
            entry.overflow = el.style.overflow;
            el.style.overflow = 'visible';
            changed = true;
          }
          // transform creates a stacking context (e.g. .pub-card:hover translateY(-2px))
          // that traps the wrap's z-index and hides the image behind the backdrop.
          if (cs.transform && cs.transform !== 'none') {
            entry.transform = el.style.transform;
            el.style.transform = 'none';
            changed = true;
          }
          if (changed) saved.push(entry);
          el = el.parentElement;
        }
        this._saved = saved;
      },
      afterHide: function() {
        if (this._imgSaved) {
          var img = this.target;
          img.style.position = this._imgSaved.position;
          img.style.inset = this._imgSaved.inset;
          img.style.width = this._imgSaved.width;
          img.style.height = this._imgSaved.height;
          img.style.display = this._imgSaved.display;
          img.style.margin = this._imgSaved.margin;
          this._imgSaved = null;
        }
        if (this._saved) {
          this._saved.forEach(function(item) {
            if ('zIndex' in item) item.el.style.zIndex = item.zIndex;
            if ('overflow' in item) item.el.style.overflow = item.overflow;
            if ('transform' in item) item.el.style.transform = item.transform;
          });
          this._saved = null;
        }
      }
    });
  };


  /* =======================
  // Responsive Videos
  ======================= */
  reframe(".post__content iframe:not(.reframe-off), .page__content iframe:not(.reframe-off)");


  // =====================
  // Load More Posts
  // =====================
  var load_posts_button = document.querySelector('.load-more-posts');

  load_posts_button&&load_posts_button.addEventListener("click",function(e){e.preventDefault();var o=document.querySelector(".load-more-section"),e=pagination_next_url.split("/page")[0]+"/page/"+pagination_next_page_number+"/";fetch(e).then(function(e){if(e.ok)return e.text()}).then(function(e){var n=document.createElement("div");n.innerHTML=e;for(var t=document.querySelector(".grid"),a=n.querySelectorAll(".grid__post"),i=0;i<a.length;i++)t.appendChild(a.item(i));new LazyLoad({elements_selector:".lazy"});pagination_next_page_number++,pagination_next_page_number>pagination_available_pages_number&&(o.style.display="none")})});


  /* =======================
  // BibTeX Copy to Clipboard
  ======================= */
  window.copyBibtex = function(btn) {
    const details = btn.closest('details');
    const code = details.querySelector('.pub-card__bibtex code');
    if (!code) return;
    const text = code.textContent;
    const icon = btn.querySelector('i');

    function onSuccess() {
      icon.className = 'fa-solid fa-check';
      setTimeout(() => { icon.className = 'fa-regular fa-copy'; }, 1500);
    }

    function fallbackCopy() {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.style.cssText = 'position:fixed;opacity:0;pointer-events:none';
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand('copy'); onSuccess(); } catch(e) {}
      document.body.removeChild(ta);
    }

    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(onSuccess).catch(fallbackCopy);
    } else {
      fallbackCopy();
    }
  };


  /* =======================
  // Scroll Top Button
  ======================= */
  window.addEventListener("scroll", function () {
  window.scrollY > window.innerHeight ? btnScrollToTop.classList.add("is-active") : btnScrollToTop.classList.remove("is-active");
  });

  btnScrollToTop.addEventListener("click", function () {
    if (window.scrollY != 0) {
      window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth"
      })
    }
  });

});
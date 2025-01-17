(function () {
  ("use strict");

  function toggleScrolled() {
    const selectBody = document.querySelector("body");
    const selectHeader = document.querySelector("#header");
    if (
      !selectHeader.classList.contains("scroll-up-sticky") &&
      !selectHeader.classList.contains("sticky-top") &&
      !selectHeader.classList.contains("fixed-top")
    )
      return;
    window.scrollY > 100
      ? selectBody.classList.add("scrolled")
      : selectBody.classList.remove("scrolled");
  }

  document.addEventListener("scroll", toggleScrolled);
  window.addEventListener("load", toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector(".mobile-nav-toggle");

  function mobileNavToogle() {
    document.querySelector("body").classList.toggle("mobile-nav-active");
    mobileNavToggleBtn.classList.toggle("bi-list");
    mobileNavToggleBtn.classList.toggle("bi-x");
  }
  mobileNavToggleBtn.addEventListener("click", mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll("#navmenu a").forEach((navmenu) => {
    navmenu.addEventListener("click", () => {
      if (document.querySelector(".mobile-nav-active")) {
        mobileNavToogle();
      }
    });
  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll(".navmenu .toggle-dropdown").forEach((navmenu) => {
    navmenu.addEventListener("click", function (e) {
      e.preventDefault();
      this.parentNode.classList.toggle("active");
      this.parentNode.nextElementSibling.classList.toggle("dropdown-active");
      e.stopImmediatePropagation();
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector("#preloader");
  if (preloader) {
    window.addEventListener("load", () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector(".scroll-top");

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100
        ? scrollTop.classList.add("active")
        : scrollTop.classList.remove("active");
    }
  }
  scrollTop.addEventListener("click", (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });

  window.addEventListener("load", toggleScrollTop);
  document.addEventListener("scroll", toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: "ease-in-out",
      once: true,
      mirror: false,
    });
  }
  window.addEventListener("load", aosInit);

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function (swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  /**
   * Init isotope layout and filters
   */
  document.querySelectorAll(".isotope-layout").forEach(function (isotopeItem) {
    let layout = isotopeItem.getAttribute("data-layout") ?? "masonry";
    let filter = isotopeItem.getAttribute("data-default-filter") ?? "*";
    let sort = isotopeItem.getAttribute("data-sort") ?? "original-order";

    let initIsotope;
    imagesLoaded(isotopeItem.querySelector(".isotope-container"), function () {
      initIsotope = new Isotope(
        isotopeItem.querySelector(".isotope-container"),
        {
          itemSelector: ".isotope-item",
          layoutMode: layout,
          filter: filter,
          sortBy: sort,
        }
      );
    });

    isotopeItem
      .querySelectorAll(".isotope-filters li")
      .forEach(function (filters) {
        filters.addEventListener(
          "click",
          function () {
            isotopeItem
              .querySelector(".isotope-filters .filter-active")
              .classList.remove("filter-active");
            this.classList.add("filter-active");
            initIsotope.arrange({
              filter: this.getAttribute("data-filter"),
            });
            if (typeof aosInit === "function") {
              aosInit();
            }
          },
          false
        );
      });
  });

  /**
   * Frequently Asked Questions Toggle
   */
  document
    .querySelectorAll(".faq-item h3, .faq-item .faq-toggle")
    .forEach((faqItem) => {
      faqItem.addEventListener("click", () => {
        faqItem.parentNode.classList.toggle("faq-active");
      });
    });

  /**
   * Correct scrolling position upon page load for URLs containing hash links.
   */
  window.addEventListener("load", function () {
    if (window.location.hash) {
      if (document.querySelector(window.location.hash)) {
        setTimeout(() => {
          let section = document.querySelector(window.location.hash);
          let scrollMarginTop = getComputedStyle(section).scrollMarginTop;
          window.scrollTo({
            top: section.offsetTop - parseInt(scrollMarginTop),
            behavior: "smooth",
          });
        }, 100);
      }
    }
  });

  /**
   * Navmenu Scrollspy
   */
  let navmenulinks = document.querySelectorAll(".navmenu a");

  function navmenuScrollspy() {
    navmenulinks.forEach((navmenulink) => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      let position = window.scrollY + 200;
      if (
        position >= section.offsetTop &&
        position <= section.offsetTop + section.offsetHeight
      ) {
        document
          .querySelectorAll(".navmenu a.active")
          .forEach((link) => link.classList.remove("active"));
        navmenulink.classList.add("active");
      } else {
        navmenulink.classList.remove("active");
      }
    });
  }
  window.addEventListener("load", navmenuScrollspy);
  document.addEventListener("scroll", navmenuScrollspy);
})();

// language translation

// document
//   .getElementById("language-selector")
//   .addEventListener("change", function () {
//     const selectedLanguage = this.value;

//     fetch(`/get_translations?lang=${selectedLanguage}`)
//       .then((response) => response.json())
//       .then((data) => {
//         document.getElementById("nav-home").innerText = data.nav_home;
//         document.getElementById("nav-news").innerText = data.nav_news;
//         document.getElementById("nav-about-us").innerText = data.nav_about_us;
//         // document.getElementById("nav-contact-us").innerText =
//         //   data.nav_contact_us;

//         document.getElementById("hero-title").innerText = data.hero_title;
//         document.getElementById("hero-description").innerText =
//           data.hero_description;
//         document.getElementById("hero-btn").innerText = data.hero_btn;

//         document.getElementById("transport-title").innerText =
//           data.transport_title;
//         document.getElementById("transport-description").innerText =
//           data.transport_description;
//         document.getElementById("transport-btn").innerText = data.transport_btn;

//         document.getElementById("visitors-title").innerText =
//           data.visitors_title;
//         document.getElementById("visitors-description").innerText =
//           data.visitors_description;
//         document.getElementById("visitors-btn").innerText = data.visitors_btn;

//         document.getElementById("monitoring-title").innerText =
//           data.monitoring_title;
//         document.getElementById("monitoring-description").innerText =
//           data.monitoring_description;
//         document.getElementById("monitoring-btn").innerText =
//           data.monitoring_btn;

//         document.getElementById("document-title").innerText =
//           data.document_title;
//         document.getElementById("document-description").innerText =
//           data.document_description;
//         document.getElementById("document-btn").innerText = data.document_btn;

//         document.getElementById("about-title").innerText = data.about_title;
//         document.getElementById("about-intro").innerText = data.about_intro;
//         document.getElementById("about-item-1").innerText = data.about_item_1;
//         document.getElementById("about-item-2").innerText = data.about_item_2;
//         document.getElementById("about-item-3").innerText = data.about_item_3;
//         document.getElementById("about-item-4").innerText = data.about_item_4;
//         document.getElementById("about-paragraph").innerText =
//           data.about_paragraph;
//         document.getElementById("about-read-more").innerText =
//           data.about_read_more;

//         document.getElementById("stats-institutions").innerText =
//           data.stats_institutions;
//         document.getElementById("stats-projects").innerText =
//           data.stats_projects;
//         document.getElementById("stats-mentorship").innerText =
//           data.stats_mentorship;
//         document.getElementById("stats-workers").innerText = data.stats_workers;

//         document.getElementById("contact-title").innerText = data.contact_title;
//         document.getElementById("contact-intro").innerText = data.contact_intro;
//         document.getElementById("contact-address-title").innerText =
//           data.contact_address_title;
//         document.getElementById("contact-address-content").innerText =
//           data.contact_address_content;
//         document.getElementById("contact-phone-title").innerText =
//           data.contact_phone_title;
//         document.getElementById("contact-phone-content").innerText =
//           data.contact_phone_content;
//         document.getElementById("contact-email-title").innerText =
//           data.contact_email_title;

//         document.getElementById("form-name-label").placeholder =
//           data.form_name_label.placeholder;
//         document.getElementById("form-email-label").placeholder =
//           data.form_email_label.placeholder;
//         document.getElementById("form-subject-label").placeholder =
//           data.form_subject_label.placeholder;
//         document.getElementById("form-message-label").placeholder =
//           data.form_message_label.placeholder;
//         document.getElementById("form-submit-btn").innerText =
//           data.form_submit_btn;

//         document.getElementById("footer-about").innerText = data.footer_about;
//         document.getElementById("useful-links").innerText = data.useful_links;
//         document.getElementById("footer-link-home").innerText =
//           data.footer_link_home;
//         document.getElementById("footer-link-news").innerText =
//           data.footer_link_news;
//         document.getElementById("footer-link-about-us").innerText =
//           data.footer_link_about_us;
//         document.getElementById("footer-link-contact-us").innerText =
//           data.footer_link_contact_us;
//         document.getElementById("footer-contact").innerText =
//           data.footer_contact;
//         document.getElementById("footer-contact-address").innerText =
//           data.footer_contact_address;
//         document.getElementById("footer-contact-address-1").innerText =
//           data.footer_contact_address_1;
//         document.getElementById("footer-contact-address-2").innerText =
//           data.footer_contact_address_2;
//         document.getElementById("footer-phone").innerText = data.footer_phone;
//         document.getElementById("footer-email").innerText = data.footer_email;
//         document.getElementById("copyright").innerText = data.copyright;
//       });
//   });

// Initialize Swiper
const swiper = new Swiper(".swiper", {
  slidesPerView: 4, // Show 4 cards at a time
  spaceBetween: 20, // Spacing between slides
  loop: true, // Enable infinite scrolling
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  breakpoints: {
    320: {
      slidesPerView: 1, // For small screens
      spaceBetween: 10,
    },
    768: {
      slidesPerView: 2, // For tablets
      spaceBetween: 15,
    },
    1200: {
      slidesPerView: 4, // For larger screens
      spaceBetween: 20,
    },
  },
});

const heroSwiper = new Swiper(".hero-swiper", {
  slidesPerView: 1, // Show 4 cards at a time
  spaceBetween: 0, // Spacing between slides
  loop: true, // Enable infinite scrolling
  autoplay: {
    delay: 5000,
    pauseOnMouseEnter: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});

// For collapsable cards to change the button text
// const toggleButton = document.getElementById("toggle-button");
// const collapseElement = document.getElementById("moreTeam");

// // Listen for the collapse event to change the button text
// collapseElement.addEventListener("show.bs.collapse", () => {
//   toggleButton.innerText = "Show Less";
// });

// collapseElement.addEventListener("hide.bs.collapse", () => {
//   toggleButton.innerText = "Show More";
// });
// const loadMoreButton = document.getElementById("load-more");
const additionalContent = document.getElementById("moreTeam");
const spinner = loadMoreButton.querySelector(".spinner-border");

// Ensure the content is initially hidden
additionalContent.style.display = "none";

// Add click event listener to the "Load More" button
loadMoreButton.addEventListener("click", function () {
  // If the content is hidden, show it
  if (additionalContent.style.display === "none") {
    // Show the loading spinner and update the button text
    loadMoreButton.classList.add("loading");
    loadMoreButton.textContent = "Loading...";

    // Simulate a delay for loading the content
    setTimeout(function () {
      // Show the additional content
      additionalContent.style.display = "block";

      // Change the button text to "Show Less"
      loadMoreButton.textContent = "Show Less";

      // Remove the loading spinner
      loadMoreButton.classList.remove("loading");
    }, 600); // Simulate a delay for loading
  } else {
    // Simulate a delay before collapsing the content
    loadMoreButton.classList.add("loading");
    loadMoreButton.textContent = "Loading...";

    // Simulate the delay for "Show Less"
    setTimeout(function () {
      // Hide the content
      additionalContent.style.display = "none";

      // Change the button text to "Show More"
      loadMoreButton.textContent = "Show More";

      // Remove the loading spinner
      loadMoreButton.classList.remove("loading");
    }, 600); // Simulate a delay for hiding
  }
});

document.addEventListener('DOMContentLoaded', function () {
  new Swiper('#teachers', {
    loop: true,
    centeredSlides: true,
    slidesPerView: 'auto',
    spaceBetween: 20,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    autoplay: {
      delay: 3000,
      disableOnInteraction: false,
    },
    grabCursor: true,
    breakpoints: {
      1200: {
        slidesPerView: 3,
        spaceBetween: 20,
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 15,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 10,
      },
      480: {
        slidesPerView: 1,
        spaceBetween: 5,
      },
    },
  });
});

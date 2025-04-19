document.addEventListener('DOMContentLoaded', () => {
  // Faqat #about-swiper uchun Swiper sozlamalari
  const aboutSwiper = new Swiper('#about-swiper', {
    slidesPerView: 1, // Mobil qurilmalar uchun
    spaceBetween: 10,
    navigation: {
      nextEl: '#about-swiper .swiper-button-next',
      prevEl: '#about-swiper .swiper-button-prev',
    },
    pagination: {
      el: '#about-swiper .swiper-pagination',
      clickable: true,
    },
    breakpoints: {
      768: {
        slidesPerView: 2, // Planshet uchun
        spaceBetween: 20,
      },
      1024: {
        slidesPerView: 3, // Katta ekranlar uchun
        spaceBetween: 30,
      },
    },
  });
});

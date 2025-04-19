document.addEventListener('DOMContentLoaded', function () {
  const newsSwiper = new Swiper('#newsSwiper', {
    slidesPerView: 1,
    spaceBetween: 20,
    loop: true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    autoplay: {
      delay: 3000,
      disableOnInteraction: false,
    },
    breakpoints: {
      576: {
        slidesPerView: 1,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 30,
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 10,
      },
    },
  });

  const newsModal = document.getElementById('newsModal');
  const modalBackdrop = document.querySelector('.modal-backdrop');

  newsModal.addEventListener('hidden.bs.modal', function () {
    if (modalBackdrop) {
      modalBackdrop.style.backdropFilter = 'none';
      modalBackdrop.style.backgroundColor = '';
    }
  });

  const modalTitle = newsModal.querySelector('.modal-title');
  const modalImage = newsModal.querySelector('#modalImage');
  const modalText = newsModal.querySelector('#modalText');

  document.querySelectorAll('.read-more').forEach((button) => {
    button.addEventListener('click', function () {
      const title = this.getAttribute('data-title');
      const text = this.getAttribute('data-text');
      const img = this.getAttribute('data-img');

      modalTitle.textContent = title;
      modalImage.src = img;
      modalText.textContent = text;
    });
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const titles = document.querySelectorAll('.news-title');

  titles.forEach(function (title) {
    if (title.textContent.length > 25) {
      title.textContent = title.textContent.slice(0, 25) + '...';
    }
  });
});

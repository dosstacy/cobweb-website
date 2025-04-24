const items = document.querySelectorAll('.carousel-item');
let currentIndex = 0;

function updateCarousel() {
    items.forEach((item, index) => {
        item.classList.remove('active');
        item.style.transform = 'scale(0.8)';
        item.style.opacity = '0.4';
    });
    items[currentIndex].classList.add('active');
    items[currentIndex].style.transform = 'scale(1)';
    items[currentIndex].style.opacity = '1';

    const carousel = document.getElementById('carousel');
    const offset = currentIndex * 60 - (100 - 60) / 2;
    carousel.style.transform = `translateX(-${offset}%)`;
}

function moveCarousel(direction) {
    currentIndex = (currentIndex + direction + items.length) % items.length;
    updateCarousel();
}

updateCarousel();
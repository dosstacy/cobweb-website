const items = document.querySelectorAll('.carousel-item');
let currentIndex = 0;

function updateCarousel() {
    // Оновлюємо класи і стилі для всіх елементів
    items.forEach((item, index) => {
        item.classList.remove('active');
        item.style.transform = 'scale(0.8)';
        item.style.opacity = '0.4';
    });

    // Активуємо поточний елемент
    items[currentIndex].classList.add('active');
    items[currentIndex].style.transform = 'scale(1)';
    items[currentIndex].style.opacity = '1';

    const carousel = document.getElementById('carousel');

    // Повертаємось до оригінального підходу з коригуванням
    // Використовуємо ширину елемента в 60% як у початковому коді
    const itemWidth = 60;

    // Розраховуємо зсув так, щоб активний елемент був по центру
    const offset = currentIndex * itemWidth;

    // Застосовуємо трансформацію з додатковим коригуванням
    // для центрування поточного елемента
    carousel.style.transform = `translateX(calc(-${offset}% + ${(100 - itemWidth) / 2}%))`;
}

function moveCarousel(direction) {
    currentIndex = (currentIndex + direction + items.length) % items.length;
    updateCarousel();
}

// Ініціалізація каруселі
updateCarousel();
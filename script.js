let currentIndex = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;

function showSlide(index) {
  const slidesContainer = document.querySelector('.slides');
  if (index >= totalSlides) {
    currentIndex = 0;
  } else if (index < 0) {
    currentIndex = totalSlides - 1;
  } else {
    currentIndex = index;
  }
  const offset = -currentIndex * 100;
  slidesContainer.style.transform = `translateX(${offset}%)`;
}

function nextSlide() {
  showSlide(currentIndex + 1);
}

function prevSlide() {
  showSlide(currentIndex - 1);
}

document.addEventListener('DOMContentLoaded', () => {
  showSlide(currentIndex);
  setInterval(nextSlide, 3000); // Change slide every 3 seconds
});
document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme');
  
    if (currentTheme) {
      document.body.classList.add(currentTheme);
    }
  
    themeToggle.addEventListener('click', () => {
      document.body.classList.toggle('dark-mode');
      
      let theme = 'light';
      if (document.body.classList.contains('dark-mode')) {
        theme = 'dark';
      }
      localStorage.setItem('theme', theme);
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const toggleButton = document.querySelector(".menu-toggle");
    const navMenu = document.querySelector(".nav__header");

    toggleButton.addEventListener("click", () => {
        navMenu.classList.toggle("active");
        body.classList.toggle('menu-active', isActive);
    });
    
});

function toggleClearIcon(inputElement) {
    const clearIcon = inputElement.nextSibling;
    if (inputElement.value.length > 0) {
      clearIcon.style.display = 'block';
    } else {
      clearIcon.style.display = 'none';
    }
  }

function toggleMenu() {
    var menu = document.getElementById('menu');
    if (menu.style.display === 'block') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'block';
    }
}
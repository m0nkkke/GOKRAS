document.addEventListener('DOMContentLoaded', () => {
    const profileLink = document.getElementById('profile-link');
    const favouritesLink = document.getElementById('favourites-link');
    const profileInfo = document.querySelector('.profile__info');
    const favouritePlaces = document.querySelector('.favourite__places');

    // Функция для показа секции и скрытия другой
    function toggleSection(showElement, hideElement) {
        showElement.classList.remove('hidden');
        hideElement.classList.add('hidden');
    }

    // Функция для обновления активной ссылки
    function updateActiveLink(activeLink) {
        // Убираем класс активности у всех ссылок
        const links = document.querySelectorAll('.nav-link');
        links.forEach(link => link.classList.remove('active'));

        // Добавляем класс активности к текущей ссылке
        activeLink.classList.add('active');
    }

    // Обработчики событий для кнопок
    profileLink.addEventListener('click', (e) => {
        e.preventDefault();
        toggleSection(profileInfo, favouritePlaces);
        updateActiveLink(profileLink);
    });

    favouritesLink.addEventListener('click', (e) => {
        e.preventDefault();
        toggleSection(favouritePlaces, profileInfo);
        updateActiveLink(favouritesLink);
    });

    // Изначально показываем только профиль и делаем активной ссылку "Профиль"
    toggleSection(profileInfo, favouritePlaces);
    updateActiveLink(profileLink);
});
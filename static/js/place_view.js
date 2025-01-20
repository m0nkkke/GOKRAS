document.addEventListener("DOMContentLoaded", function () {
    const mapContainer = document.getElementById("map");
    const lat = parseFloat(mapContainer.dataset.lat);
    const lng = parseFloat(mapContainer.dataset.lng);

    DG.then(function () {
        var map = DG.map('map', {
            center: [lat, lng], 
            zoom: 17
        });

        DG.marker([lat, lng]).addTo(map).bindPopup('Точка из базы данных!');
    });
});

document.addEventListener('input', function (event) {
    if (event.target.tagName.toLowerCase() === 'textarea') {
        console.log('detected');
        const textarea = event.target;
        textarea.style.height = 'auto'; // Сбрасываем высоту, чтобы правильно пересчитать
        textarea.style.height = textarea.scrollHeight + 'px'; // Устанавливаем высоту в зависимости от содержимого
    }
});

document.addEventListener('DOMContentLoaded', function() {

    // Получаем все изображения
    const images = document.querySelectorAll('.clickable-image');

    // Получаем модальное окно и изображение в нем
    const modal = document.getElementById('modal');
    const modalImg = document.getElementById('modal-img');
    const closeModal = document.getElementById('close-modal');

    // Для каждого изображения добавляем обработчик события
    images.forEach(image => {
        image.addEventListener('click', function() {
            // Устанавливаем изображение в модальном окне
            modal.style.display = 'flex';
            modalImg.src = this.src;
        });
    });

    // Закрытие модального окна при нажатии на крестик
    closeModal.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    // Закрытие модального окна при клике вне изображения
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });


    const buttons = document.querySelectorAll('.button__more');

    
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const reviewText = this.closest('.review__card').querySelector('.review__text');
            const icon = this.querySelector('svg');

            reviewText.classList.toggle('expanded');

            if (reviewText.classList.contains('expanded')) {
                // Изменяем текст кнопки и иконку для раскрытия
                this.innerHTML = 'Скрыть ';
                this.appendChild(icon); // Добавляем иконку обратно
                icon.style.transform = 'rotate(180deg)';
            } else {
                // Изменяем текст кнопки и иконку для сворачивания
                this.innerHTML = 'Подробнее ';
                this.appendChild(icon); // Добавляем иконку обратно
                icon.style.transform = 'rotate(0deg)';
            }
        });
    });
});



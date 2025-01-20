document.addEventListener("DOMContentLoaded", () => {
    const toggleButton = document.querySelector(".show__filters");
    const navMenu = document.querySelector(".places__filters");

    toggleButton.addEventListener("click", () => {
        navMenu.classList.toggle("active");
        if (navMenu.classList.contains('active')) {
            navMenu.style.display = 'block'
            toggleButton.textContent = 'Скрыть фильтры';
        } else {
            navMenu.style.display = 'none'
            toggleButton.textContent = 'Показать фильтры';
        }
    });
    
});

document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll(".show-more");

    buttons.forEach(button => {
        button.addEventListener("click", function() {
            const category = this.closest(".filter__category"); // Находим родительскую категорию
            const hiddenItems = category.querySelectorAll(".hidden"); // Находим скрытые элементы
            if (hiddenItems.length > 0) {
                // Если есть скрытые элементы, показываем их
                hiddenItems.forEach(item => item.classList.remove("hidden"));
                this.textContent = "Скрыть"; // Меняем текст кнопки
            } else {
                // Если скрытых элементов нет, снова скрываем
                const allItems = category.querySelectorAll("ul li:not(:last-child)");
                allItems.forEach((item, index) => {
                    if (index >= 4) {
                        item.classList.add("hidden");
                    }
                });
                this.textContent = "Показать больше"; // Возвращаем исходный текст кнопки
            }
        });
    });
});

// document.addEventListener("DOMContentLoaded", function() {
//     const minSlider = document.getElementById('budget-min-slider');
//     const maxSlider = document.getElementById('budget-max-slider');
//     const minInput = document.getElementById('budget-min');
//     const maxInput = document.getElementById('budget-max');

//     const updateMin = (value) => {
//         const maxValue = parseInt(maxSlider.value);
//         if (value > maxValue) value = maxValue;
//         minSlider.value = value;
//         minInput.value = value;
//     };

//     const updateMax = (value) => {
//         const minValue = parseInt(minSlider.value);
//         if (value < minValue) value = minValue;
//         maxSlider.value = value;
//         maxInput.value = value;
//     };

//     minSlider.addEventListener('input', (e) => updateMin(e.target.value));
//     maxSlider.addEventListener('input', (e) => updateMax(e.target.value));

//     minInput.addEventListener('input', (e) => updateMin(e.target.value));
//     maxInput.addEventListener('input', (e) => updateMax(e.target.value));
// });
document.addEventListener('DOMContentLoaded', () => {
    const selectContainer = document.querySelector('.people__selector');
    const selected = selectContainer.querySelector('.select-selected');
    const items = selectContainer.querySelector('.select-items');
  
    // Открытие/закрытие выпадающего списка
    selected.addEventListener('click', (e) => {
        e.stopPropagation();  // Остановить событие, чтобы клик не закрывал список сразу
        items.classList.toggle('select-hide'); // Показать/скрыть список
    });
  
    // Выбор элемента из списка
    items.addEventListener('click', (e) => {
        if (e.target && e.target.nodeName === 'DIV') {
            selected.textContent = e.target.textContent; // Установить выбранный текст
            items.classList.add('select-hide');         // Закрыть список
        }
    });
  
    // Закрытие списка при клике вне его области
    document.addEventListener('click', (e) => {
        if (!selectContainer.contains(e.target)) {
            items.classList.add('select-hide'); // Скрыть список, если клик вне области
        }
    });
});
function toggleClearIcon(inputElement) {
    console.log("working");
    const clearIcon = inputElement.nextElementSibling;
    if (inputElement.value.length > 0) {
      clearIcon.style.display = 'none';
    } else {
      clearIcon.style.display = 'block';
    }
  }
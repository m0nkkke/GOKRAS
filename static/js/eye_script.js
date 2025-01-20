document.addEventListener("DOMContentLoaded", function () {
    // Универсальная функция переключения пароля
    function togglePasswordVisibility(toggleBtnId, inputId) {
        const toggleButton = document.getElementById(toggleBtnId);
        const passwordInput = document.getElementById(inputId);

        toggleButton.addEventListener("click", function () {
            const isPassword = passwordInput.getAttribute("type") === "password";
            passwordInput.setAttribute("type", isPassword ? "text" : "password");

            // Меняем иконку (перекрёстный глаз)
            const closedEye = `
                <path d="M22.9492 21C22.9492 23.8996 20.9536 26.25 18.4917 26.25C16.0299 26.25 14.0342 23.8996 14.0342 21C14.0342 18.1004 16.0299 15.75 18.4917 15.75C20.9536 15.75 22.9492 18.1004 22.9492 21Z" 
                    stroke="black" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M18.4918 8.75C11.8386 8.75 6.20686 13.9 4.31348 21C6.20683 28.0999 11.8386 33.25 18.4918 33.25C25.1448 33.25 30.7766 28.0999 32.67 21C30.7766 13.9001 25.1448 8.75 18.4918 8.75Z" 
                    stroke="black" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
                <line x1="5" y1="5" x2="32" y2="37" stroke="black" stroke-width="3.5" stroke-linecap="round"/>
            `;

            const openEye = `
                <path d="M22.9492 21C22.9492 23.8996 20.9536 26.25 18.4917 26.25C16.0299 26.25 14.0342 23.8996 14.0342 21C14.0342 18.1004 16.0299 15.75 18.4917 15.75C20.9536 15.75 22.9492 18.1004 22.9492 21Z" 
                    stroke="black" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M18.4918 8.75C11.8386 8.75 6.20686 13.9 4.31348 21C6.20683 28.0999 11.8386 33.25 18.4918 33.25C25.1448 33.25 30.7766 28.0999 32.67 21C30.7766 13.9001 25.1448 8.75 18.4918 8.75Z" 
                    stroke="black" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
            `;

            toggleButton.innerHTML = isPassword ? closedEye : openEye;
        });
    }

    // Применение функции к обоим инпутам
    togglePasswordVisibility("togglePassword", "password");
    togglePasswordVisibility("togglePassword2", "password2");
});

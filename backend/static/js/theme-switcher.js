// document.addEventListener('DOMContentLoaded', function () {
//     const themeToggle = document.getElementById('themeToggle');
//     const htmlElement = document.documentElement;
//     const title = themeToggle.querySelector('h5');

//     // Проверяем сохранённую тему (если есть)
//     const savedTheme = localStorage.getItem('theme') || 'light';
//     htmlElement.setAttribute('data-bs-theme', savedTheme);
//     updateButton(savedTheme);

//     // Обработчик клика
//     themeToggle.addEventListener('click', function () {
//         const currentTheme = htmlElement.getAttribute('data-bs-theme');
//         const newTheme = currentTheme === 'light' ? 'dark' : 'light';

//         htmlElement.setAttribute('data-bs-theme', newTheme);
//         localStorage.setItem('theme', newTheme);
//         updateButton(newTheme);
//     });

//     // Обновляем вид кнопки
//     function updateButton(theme) {
//         if (theme === 'dark') {
//             title.className = 'bi bi-sun-fill';
//             themeToggle.innerHTML = '<i class="bi bi-sun-fill"></i> Светлая тема';
//         } else {
//             title.className = 'bi bi-moon-fill';
//             themeToggle.innerHTML = '<i class="bi bi-moon-fill"></i> Тёмная тема';
//         }
//     }
// });
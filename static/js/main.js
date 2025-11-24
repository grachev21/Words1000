import ChartHome from "./home.js";
import Game from "./game/game.js";

let routeInitialized = false;

function checkRoute() {
  const currentPath = window.location.pathname;
  console.log("Проверка маршрута:", currentPath);

  // Защита от повторного вызова для того же маршрута
  if (routeInitialized) return;

  if (currentPath === "/home/") {
    ChartHome();
    console.log("<<< home loaded once");
  } else if (currentPath === "/words/") {
    initHomePage();
  } else if (currentPath === "/game/") {
    new Game();
  } else if (currentPath === "/settings/") {
    initSettingsPage();
  }

  routeInitialized = true;
}

// HTMX навигация - сбрасываем флаг
document.addEventListener("htmx:afterSwap", function () {
  routeInitialized = false;
  setTimeout(checkRoute, 10);
});

document.addEventListener("ajax:afterSwap", (e) => {
  console.log("Контент обновлён в:", e.detail.target);
  routeInitialized = false;
  setTimeout(checkRoute, 10);
  console.log("ajax request");
});

// ОДИН обработчик загрузки
document.addEventListener("DOMContentLoaded", checkRoute);

function initGamePage() {
  console.log("🎮 Инициализация игровой страницы");
}

function initHomePage() {
  console.log("🏠 Инициализация домашней страницы");
}

function initSettingsPage() {
  console.log("⚙️ Инициализация страницы настроек");
}

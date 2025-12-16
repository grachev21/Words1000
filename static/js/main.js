// import Header from "./header/header.js";
import ChartHome from "./home.js";
import Game from "./game/game.js";

let routeInitialized = false;

function checkRoute() {
    const currentPath = window.location.pathname;
    console.log(currentPath);

    // Защита от повторного вызова для того же маршрута
    if (routeInitialized) return;

    // new Header();
    if (currentPath === "/") {
        new ChartHome();
        console.log("hello");
    } else if (currentPath === "/words/") {

    } else if (currentPath === "/game/") {
        new Game();
    } else if (currentPath === "/settings/") {
    }

    routeInitialized = true;
}

// ОДИН обработчик загрузки
document.addEventListener("DOMContentLoaded", checkRoute);

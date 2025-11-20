import week from "./chart/chart_week.js";
import month from "./chart/chart_month.js";
import season from "./chart/chart_season.js";
import year from "./chart/chart_year.js";

// --- Обычная загрузка страницы ---
document.addEventListener("DOMContentLoaded", () => {
    week();
    month();
    season();
    year();
});

// --- Загрузка через HTMX ---
document.body.addEventListener("htmx:afterSwap", (event) => {
    if (event.detail.target.id === "main-content") {
        week();
        month();
        season();
        year();
    }
});

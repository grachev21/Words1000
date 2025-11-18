let chartInstance = null;

// --- Основная функция создания графика ---
function initChart() {
    const ctx = document.getElementById("myChart");
    if (!ctx) return;

    // Если график уже существовал — удаляем
    if (chartInstance !== null) {
        chartInstance.destroy();
    }

    chartInstance = new Chart(ctx, {
        type: "line",
        data: {
            labels: ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"],
            datasets: [
                {
                    label: "Слов изучено",
                    data: [10, 15, 12, 18, 20, 8, 14],
                    borderColor: "red",
                    backgroundColor: "blue",
                    borderWidth: 2,
                    tension: 0.4,
                },
            ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false, // важно, чтобы не дергался
            plugins: {
                legend: {
                    position: "top",
                    labels: {
                        color: "white",
                    },
                },
                title: {
                    display: true,
                    text: "Ваш прогресс за неделю",
                    color: "white",
                },
            },
            scales: {
                x: {
                    grid: {
                        color: "white",
                        borderDash: [5, 5],
                    },
                    ticks: {
                        color: "white",
                    },
                },
                y: {
                    grid: {
                        color: "white",
                        borderDash: [5, 5],
                    },
                    ticks: {
                        color: "white",
                    },
                },
            },
        },
    });
}

// --- Функция, которая ждёт появления нормальных размеров canvas ---
function initChartWhenVisible() {
    const canvas = document.getElementById("myChart");

    if (!canvas) return; // canvas ещё не вставлен → нет смысла

    const rect = canvas.getBoundingClientRect();

    // Если canvas имеет нулевую ширину/высоту — подождать 1 кадр
    if (rect.width === 0 || rect.height === 0) {
        requestAnimationFrame(initChartWhenVisible);
        return;
    }

    // Canvas готов → создаём график
    initChart();
}

// --- Обычная загрузка страницы ---
document.addEventListener("DOMContentLoaded", () => {
    initChartWhenVisible();
});

// --- Загрузка через HTMX ---
document.body.addEventListener("htmx:afterSwap", (event) => {
    if (event.detail.target.id === "main-content") {
        initChartWhenVisible();
    }
});

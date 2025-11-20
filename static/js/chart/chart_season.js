const season = () => {
    let chartInstance = null;

    // --- Основная функция создания графика ---
    const ctx = document.getElementById("myChartSeason");
    if (!ctx) return;

    // Если график уже существовал — удаляем
    if (chartInstance !== null) {
        chartInstance.destroy();
    }

    // Chartjs
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
};

export default season;

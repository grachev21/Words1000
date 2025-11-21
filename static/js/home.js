import week from "./chart/chart_week.js";
import month from "./chart/chart_month.js";
import season from "./chart/chart_season.js";
import year from "./chart/chart_year.js";

const ChartHome = () => {
  const getDataForChart = () => {
    let chart_data = document.getElementById("chart-data");
    let gd = JSON.parse(chart_data.textContent);

    let label_data = [];
    let count_data = [];

    gd.week_data.forEach((element) => {
      label_data.push(element.date_graph);
      count_data.push(element.count_graph);
    });
    return { label_data: label_data, count_data: count_data };
  };

  // --- Обычная загрузка страницы ---
  const data = getDataForChart();
  week(data.label_data, data.count_data);
};
export default ChartHome;

import week from "./chart/chart.js";

class ChartHome {
  constructor() {
    this.chart_data = JSON.parse(
      document.getElementById("chart-data").textContent
    );

    this.init();
  }

  getData(data, id) {

    let label_data = [];
    let count_data = [];
    data.forEach((element) => {
      label_data.push(element.date_graph);
      count_data.push(element.count_graph);
    });

    week(label_data, count_data, id);
  }
  init() {
    this.getData(this.chart_data.week_data, "myChartWeek");
    this.getData(this.chart_data.month_data, "myChartMonth");
    this.getData(this.chart_data.year_data, "myChartYear");

  }
}
export default ChartHome;

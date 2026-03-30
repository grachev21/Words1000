import {
  VictoryChart,
  VictoryBar,
  VictoryLabel,
  VictoryTheme,
  VictoryAxis,
} from "victory";

const Chart = ({ dataChart, title }) => {
  return (
    <VictoryChart
      domainPadding={{ x: 30, y: 50 }}
      theme={VictoryTheme.clean}
      height={340}
      width={820}
      padding={{ top: 40, bottom: 70, left: 50, right: 30 }}
    >
      <VictoryLabel
        text={title}
        style={{
          fill: "#8b5cf6",
          fontSize: 10,
        }}
        dx={28}
        dy={18}
      />
      <VictoryBar
        data={dataChart}
        x="date_graph"
        y="count_graph"
        style={{
          data: {
            fill: ({ index }) => {
              // Цветовая палитра по твоим цветам (циклично)
              const colors = [
                "#8b5cf6", // col_bright_1 (фиолетовый)
                "#ec4899", // col_bright_2 (розовый)
                "#22c55e", // col_bright_3 (зелёный)
                "#3b82f6", // col_bright_4 (синий)
                "#eab308", // col_bright_5 (жёлтый)
                "#06b6d4", // col_bright_6 (голубой)
              ];
              return colors[index % colors.length];
            },
            fillOpacity: 0.92,
            stroke: ({ index }) => {
              const colors = [
                "#7c3aed",
                "#db2777",
                "#16a34a",
                "#2563eb",
                "#ca8a04",
                "#0891b2",
              ];
              return colors[index % colors.length];
            },
            strokeWidth: 2.5,
            rx: 8,
            ry: 8,
          },
        }}
        labels={({ datum }) => (datum.count_graph > 0 ? datum.count_graph : "")}
        labelComponent={
          <VictoryLabel
            style={{
              fontSize: 14,
              fontWeight: "700",
              fill: "#1f2937",
              fontFamily: "system-ui, -apple-system, sans-serif",
            }}
            dy={-16}
            textAnchor="middle"
          />
        }
      />

      {/* Ось X — дни недели */}
      <VictoryAxis
        style={{
          axis: { stroke: "#e5e7eb", strokeWidth: 1 },
          tickLabels: {
            fontSize: 12,
            fill: "#6b7280",
            fontWeight: 600,
            angle: -40,
            textAnchor: "end",
            padding: 12,
          },
        }}
      />

      {/* Ось Y */}
      <VictoryAxis
        dependentAxis
        style={{
          axis: { stroke: "#e5e7eb" },
          tickLabels: {
            fontSize: 12,
            fill: "#6b7280",
            fontWeight: 600,
          },
          grid: {
            stroke: "#f1f5f9",
            strokeDasharray: "4,4",
          },
        }}
      />
    </VictoryChart>
  );
};

export default Chart;

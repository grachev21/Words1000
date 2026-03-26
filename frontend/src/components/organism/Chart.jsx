import { VictoryChart, VictoryLine, VictoryBar, VictoryTheme } from "victory";
const sampleData = [
  3.9670002, 5.2650003, 6.201, 7.8010006, 9.694, 11.214001, 11.973001, 12.250001, 12.816001,
  13.413001, 13.626961, 14.30356, 15.295461,
];
const Chart = () => {
  return (
    <VictoryChart domainPadding={{ x: 50 }} theme={VictoryTheme.clean}>
      <VictoryBar data={sampleData} />
    </VictoryChart>
  );
};
export default Chart;

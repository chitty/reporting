import React from 'react';
import { Bar } from 'react-chartjs-2';
import rows from '../json/report.json';

const data = {
  labels: rows.map(row => row.label),
  datasets: [
    {
      label: 'Trades',
      backgroundColor: 'rgba(255,99,132,0.2)',
      borderColor: 'rgba(255,99,132,1)',
      borderWidth: 1,
      hoverBackgroundColor: 'rgba(255,99,132,0.4)',
      hoverBorderColor: 'rgba(255,99,132,1)',
      data: rows.map(row => parseFloat(row.pnl)),
    }
  ]
};
const options = {
  tooltips: {
    callbacks: {
      label: function(tooltipItem, data) {
          const current = rows.find(row => row.label === tooltipItem.xLabel)
          const label = current.product + ': ' + tooltipItem.yLabel;
          return label;
      }
    }
  }
}

export function BarChart(){

  return (
    <div>
      <h2>Performance per trade</h2>
      <Bar
        data={data}
        options={options}
      />
    </div>
  );

};

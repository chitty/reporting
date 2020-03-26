import React from 'react';
import { Line } from 'react-chartjs-2';
import rows from '../json/report.json';

const data = {
  labels: rows.map(row => row.label),
  datasets: [
    {
      label: 'Balance',
      fill: false,
      lineTension: 0,
      backgroundColor: 'rgba(75,192,192,0.4)',
      borderColor: 'rgba(75,192,192,1)',
      borderCapStyle: 'butt',
      borderDashOffset: 0.0,
      pointBorderColor: 'rgba(75,192,192,1)',
      pointBackgroundColor: '#fff',
      pointBorderWidth: 5,
      pointHoverRadius: 10,
      pointHoverBackgroundColor: 'rgba(75,192,192,1)',
      pointHoverBorderColor: 'rgba(220,220,220,1)',
      pointHoverBorderWidth: 2,
      pointRadius: 1,
      pointHitRadius: 10,
      data: rows.map(row => row.point),
    }
  ]
};
const options = {
  tooltips: {
    callbacks: {
      beforeLabel: function(tooltipItem) {
        const current = rows.find(row => row.label === tooltipItem.xLabel)
        const label = current.product + ' (P/L): ' + current.pnl;
        return label;
      }
    }
  }
}

export function LineChart() {
  return (
      <div>
        <h2>Performance</h2>
        <Line data={data} options={options} />
      </div>
  );
}

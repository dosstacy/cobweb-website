import React, { useState, useMemo } from 'react';
import Plot from 'react-plotly.js';
import {Interactive} from "./Interactive";
import ReactDOM from 'react-dom';

import { createRoot } from 'react-dom/client';

const root = createRoot(document.getElementById('root'));
root.render(<CobwebPlot />);


function CobwebPlot() {
  const [params, setParams] = useState({
    d_shift: 10,
    d_slope: 1,
    s_shift: 2,
    s_slope: 0.8,
    n_iterations: 15,
    initial_price: 5
  });

  // Функції попиту та пропозиції
  const demand = (price) => params.d_shift - params.d_slope * price;
  const supply = (price) => params.s_shift + params.s_slope * price;

  // Розрахунок павутиння
  const { prices, quantities } = useMemo(() => {
    let prices = [params.initial_price];
    let quantities = [demand(params.initial_price)];

    for (let i = 0; i < params.n_iterations; i++) {
      if (i % 2 === 0) {
        quantities.push(demand(prices[prices.length - 1]));
      } else {
        prices.push((quantities[quantities.length - 1] - params.s_shift) / params.s_slope);
      }
    }

    return { prices, quantities };
  }, [params]);

  // Розрахунок діапазону цін
  const priceRange = useMemo(() => {
    const min = Math.min(...prices, 0);
    const max = Math.max(...prices, params.d_shift / params.d_slope);
    return Array.from({length: 100}, (_, i) => min + (max - min) * i / 99);
  }, [prices, params]);

  return (
    <div>
      <Plot
        data={[
          // Лінія попиту
          {
            x: priceRange,
            y: priceRange.map(price => demand(price)),
            type: 'scatter',
            mode: 'lines',
            name: 'Попит'
          },
          // Лінія пропозиції
          {
            x: priceRange,
            y: priceRange.map(price => supply(price)),
            type: 'scatter',
            mode: 'lines',
            name: 'Пропозиція'
          },
          // Павутиння
          {
            x: prices,
            y: quantities,
            type: 'scatter',
            mode: 'lines+markers',
            name: 'Траєкторія',
            line: { color: 'red', dash: 'dot' }
          }
        ]}
        layout={{
          title: 'Модель павутиння',
          xaxis: { title: 'Ціна' },
          yaxis: { title: 'Кількість' }
        }}
      />
      <Interactive params={params} setParams={setParams}/>
    </div>
  );
}

export default CobwebPlot;
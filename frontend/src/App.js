import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ReferenceLine } from 'recharts';
import './App.css';

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Function to fetch data from the Flask API
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/api/analysis_results');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const result = await response.json();
        setData(result);
      } catch (e) {
        setError(e.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <div className="loading">Loading dashboard...</div>;
  }

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  const historicalData = data.historical_prices.map(item => ({
    ...item,
    Date: new Date(item.Date).getFullYear() // Recharts works better with numeric/date objects
  }));

  const changePointDate = new Date(data.change_point.date);
  const changePointYear = changePointDate.getFullYear();

  const events = data.geopolitical_events.map(event => ({
    ...event,
    event_date: new Date(event.event_date)
  }));

  return (
    <div className="App">
      <header className="App-header">
        <h1>Brent Oil Price Change Point Analysis</h1>
        <p>
          The most probable change point was identified around{' '}
          <span className="highlight-date">{data.change_point.date}</span>.
        </p>
        <div className="mean-values">
          <p>
            Mean Price Before: <span className="mean-before">${data.change_point.mu_before_mean.toFixed(2)}</span>
          </p>
          <p>
            Mean Price After: <span className="mean-after">${data.change_point.mu_after_mean.toFixed(2)}</span>
          </p>
        </div>
      </header>

      <main className="main-content">
        <ResponsiveContainer width="100%" height={500}>
          <LineChart data={historicalData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="Date" type="number" scale="time" domain={['dataMin', 'dataMax']} tickFormatter={(tick) => new Date(tick, 0, 1).getFullYear()} />
            <YAxis label={{ value: 'Price (USD per barrel)', angle: -90, position: 'insideLeft' }} />
            <Tooltip labelFormatter={(label) => `Date: ${new Date(label, 0, 1).getFullYear()}`} />
            <Legend />
            <Line type="monotone" dataKey="Price" stroke="#8884d8" dot={false} />

            {/* Reference lines for the change point and events */}
            <ReferenceLine x={changePointYear} stroke="red" strokeDasharray="3 3" label={{ position: "top", value: `Change Point`, fill: "red", fontSize: 12 }} />
            {events.map((event, index) => (
              <ReferenceLine 
                key={index} 
                x={event.event_date.getFullYear()} 
                stroke="green" 
                strokeDasharray="3 3" 
                label={{ position: "bottom", value: event.event_name, fill: "green", fontSize: 10, dy: (index % 2 === 0) ? 20 : 0 }} 
              />
            ))}
          </LineChart>
        </ResponsiveContainer>
      </main>
    </div>
  );
}

export default App;
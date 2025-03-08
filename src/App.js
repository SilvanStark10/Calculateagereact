import React, { useState } from 'react';
import './App.css';

function App() {
  const [birthDate, setBirthDate] = useState('');
  const [age, setAge] = useState(null);

  const calculateAge = () => {
    if (!birthDate) return;
    
    const today = new Date();
    const birthDateObj = new Date(birthDate);
    
    let ageYears = today.getFullYear() - birthDateObj.getFullYear();
    let ageMonths = today.getMonth() - birthDateObj.getMonth();
    let ageDays = today.getDate() - birthDateObj.getDate();
    
    if (ageMonths < 0 || (ageMonths === 0 && ageDays < 0)) {
      ageYears--;
      ageMonths += 12;
    }
    
    if (ageDays < 0) {
      const lastMonth = new Date(today.getFullYear(), today.getMonth() - 1, 0);
      ageDays += lastMonth.getDate();
      ageMonths--;
    }
    
    setAge({ years: ageYears, months: ageMonths, days: ageDays });
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Age Calculator</h1>
      </header>
      <main>
        <div className="calculator-container">
          <div className="input-container">
            <label htmlFor="birthdate">Enter your birthdate:</label>
            <input
              type="date"
              id="birthdate"
              value={birthDate}
              onChange={(e) => setBirthDate(e.target.value)}
            />
            <button onClick={calculateAge}>Calculate Age</button>
          </div>
          
          {age && (
            <div className="result-container">
              <h2>Your age is:</h2>
              <div className="age-display">
                <div className="age-unit">
                  <span className="age-number">{age.years}</span>
                  <span className="age-label">years</span>
                </div>
                <div className="age-unit">
                  <span className="age-number">{age.months}</span>
                  <span className="age-label">months</span>
                </div>
                <div className="age-unit">
                  <span className="age-number">{age.days}</span>
                  <span className="age-label">days</span>
                </div>
              </div>
            </div>
          )}
        </div>
      </main>
      <footer>
        <p>© {new Date().getFullYear()} Calculate Age React App</p>
      </footer>
    </div>
  );
}

export default App; 
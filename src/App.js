import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [birthYear, setBirthYear] = useState(new Date().getFullYear().toString());
  const [birthMonth, setBirthMonth] = useState('1'); // Default to January
  const [birthDay, setBirthDay] = useState('1'); // Default to day 1
  const [gender, setGender] = useState('Male');
  const [country, setCountry] = useState('');
  const [lifeExpectancy, setLifeExpectancy] = useState(null);
  const [daysLeft, setDaysLeft] = useState(null);
  const [yearsLeft, setYearsLeft] = useState(null);
  const [monthsLeft, setMonthsLeft] = useState(null);
  const [remainingDays, setRemainingDays] = useState(null);
  const [countries, setCountries] = useState([]);
  const [daysInMonth, setDaysInMonth] = useState(31); // Default to 31 days

  // Array of month names
  const months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
  ];

  // Generate year options from 1900 to current year
  const generateYearOptions = () => {
    const currentYear = new Date().getFullYear();
    const years = [];
    for (let year = currentYear; year >= 1900; year--) {
      years.push(
        <option key={year} value={year}>
          {year}
        </option>
      );
    }
    return years;
  };

  // Update days in month when year or month changes
  useEffect(() => {
    if (birthYear && birthMonth) {
      const year = parseInt(birthYear);
      const month = parseInt(birthMonth) - 1; // JS months are 0-indexed
      const lastDay = new Date(year, month + 1, 0).getDate();
      setDaysInMonth(lastDay);
      
      // If selected day is greater than days in the month, reset it
      if (parseInt(birthDay) > lastDay) {
        setBirthDay('1');
      }
    }
  }, [birthYear, birthMonth, birthDay]);

  useEffect(() => {
    // Fetch and parse the CSV data
    fetch(`${process.env.PUBLIC_URL}/data/life_expectancy_data.csv`)
      .then(response => response.text())
      .then(csvData => {
        const lines = csvData.split('\n');
        // Parse CSV data
        const countryList = [];
        const countryData = {};
        
        for (let i = 1; i < lines.length; i++) {
          const currentLine = lines[i].split(',');
          if (currentLine.length >= 3) {
            const countryName = currentLine[0];
            countryList.push(countryName);
            countryData[countryName] = {
              Male: parseFloat(currentLine[1]),
              Female: parseFloat(currentLine[2])
            };
          }
        }
        
        setCountries(countryList);
        window.lifeExpectancyData = countryData; // Store data globally for calculations
      })
      .catch(error => console.error('Error loading life expectancy data:', error));
  }, []);

  const calculateRemainingLife = () => {
    if (!birthYear || !country) return;
    
    const lifeExpectancyData = window.lifeExpectancyData;
    if (!lifeExpectancyData || !lifeExpectancyData[country]) {
      alert('Country data not found');
      return;
    }
    
    // Get life expectancy for the selected gender and country
    const expectancy = lifeExpectancyData[country][gender];
    setLifeExpectancy(expectancy);
    
    // Calculate days left based on exact birth date
    const birthDate = new Date(
      parseInt(birthYear), 
      parseInt(birthMonth) - 1, 
      parseInt(birthDay)
    );
    const today = new Date();
    
    // Expected death date (birth date + life expectancy in years)
    const deathYear = birthDate.getFullYear() + Math.floor(expectancy);
    const deathMonth = birthDate.getMonth() + Math.round((expectancy % 1) * 12);
    const deathDate = new Date(deathYear, deathMonth, birthDate.getDate());
    
    // Calculate days left
    const msPerDay = 1000 * 60 * 60 * 24;
    const daysRemaining = Math.max(0, Math.floor((deathDate - today) / msPerDay));
    
    setDaysLeft(daysRemaining);
    
    // Calculate years, months, and days
    const years = Math.floor(daysRemaining / 365);
    const remainingDaysAfterYears = daysRemaining % 365;
    const months = Math.floor(remainingDaysAfterYears / 30);
    const days = remainingDaysAfterYears % 30;
    
    setYearsLeft(years);
    setMonthsLeft(months);
    setRemainingDays(days);
  };

  // Generate array of days based on the month
  const generateDayOptions = () => {
    const options = [];
    for (let i = 1; i <= daysInMonth; i++) {
      options.push(
        <option key={i} value={i}>
          {i}
        </option>
      );
    }
    return options;
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Life Expectancy Calculator</h1>
      </header>
      <main>
        <div className="calculator-container">
          <div className="input-container">
            <div className="input-row">
              <div className="input-group">
                <label htmlFor="birthyear">Birth Year:</label>
                <select
                  id="birthyear"
                  value={birthYear}
                  onChange={(e) => setBirthYear(e.target.value)}
                >
                  {generateYearOptions()}
                </select>
              </div>
              
              <div className="input-group">
                <label htmlFor="birthmonth">Birth Month:</label>
                <select 
                  id="birthmonth"
                  value={birthMonth}
                  onChange={(e) => setBirthMonth(e.target.value)}
                >
                  {months.map((month, index) => (
                    <option key={month} value={index + 1}>
                      {month}
                    </option>
                  ))}
                </select>
              </div>
              
              <div className="input-group">
                <label htmlFor="birthday">Birth Day:</label>
                <select 
                  id="birthday"
                  value={birthDay}
                  onChange={(e) => setBirthDay(e.target.value)}
                >
                  {generateDayOptions()}
                </select>
              </div>
            </div>
            
            <div className="input-group">
              <label htmlFor="gender">Gender:</label>
              <select 
                id="gender"
                value={gender}
                onChange={(e) => setGender(e.target.value)}
              >
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>
            
            <div className="input-group">
              <label htmlFor="country">Country:</label>
              <select 
                id="country"
                value={country}
                onChange={(e) => setCountry(e.target.value)}
              >
                <option value="">Select a country</option>
                {countries.map(country => (
                  <option key={country} value={country}>{country}</option>
                ))}
              </select>
            </div>
            
            <button onClick={calculateRemainingLife}>Calculate Remaining Life</button>
          </div>
          
          {daysLeft !== null && (
            <div className="result-container">
              <h2>Life Expectancy Results:</h2>
              <div className="result-details">
                <p>Average life expectancy in {country} for {gender}: <strong>{lifeExpectancy} years</strong></p>
                <p>Based on your birth date of {months[parseInt(birthMonth) - 1]} {birthDay}, {birthYear}, you have approximately:</p>
                <div className="days-left">
                  <span className="days-number">{daysLeft.toLocaleString()}</span>
                  <span className="days-label">days left</span>
                </div>
                <div className="time-breakdown">
                  <p>That's approximately <strong>{yearsLeft} years, {monthsLeft} months, and {remainingDays} days</strong> left to live.</p>
                </div>
                <p className="disclaimer">
                  Note: This is only an estimate based on average life expectancy data. 
                  Many factors influence individual longevity.
                </p>
              </div>
            </div>
          )}
        </div>
      </main>
      <footer>
        <p>© {new Date().getFullYear()} Life Expectancy Calculator</p>
      </footer>
    </div>
  );
}

export default App; 
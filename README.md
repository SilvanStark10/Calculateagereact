# Age Calculator React App

A modern React application that calculates a person's exact age based on their birth date. The application displays the age in years, months, and days.

## Screenshots

![Screenshot 1](docs/images/Screenshot_1.png)

![Screenshot 2](docs/images/Screenshot_2.png)

## Overview

This application allows the user to:

- Enter their birth date using a date picker
- Get their exact age calculated in years, months, and days
- See the results displayed in a clean, modern UI

## Features

- **React-based SPA**: Built with React for a responsive single-page application experience
- **Accurate Age Calculation**: Precisely calculates age taking into account months and days
- **Modern UI**: Clean and intuitive user interface
- **Responsive Design**: Works well on desktop and mobile devices
- **GitHub Pages Deployment**: Automatically deployed to GitHub Pages when code is pushed to main branch

## How to Run Locally

1. Clone this repository
2. Ensure you have Node.js installed (version 14.x or higher recommended)
3. Install dependencies:
   ```
   npm install
   ```
4. Start the development server:
   ```
   npm start
   ```
5. Open your browser and navigate to `http://localhost:3000`

## Deployment

This project is automatically deployed to GitHub Pages using GitHub Actions when code is pushed to the main branch. The deployment workflow is defined in `.github/workflows/deploy-gh-pages.yml`.

To set up GitHub Pages deployment:

1. Make sure your repository is public (or you have GitHub Pro for private repository Pages)
2. Update the `homepage` field in `package.json` with your GitHub username:
   ```
   "homepage": "https://SilvanStark10.github.io/Calculate-age-React"
   ```
3. Push your code to the main branch
4. The GitHub Action will automatically build and deploy your application
5. Your app will be available at `https://SilvanStark10.github.io/Calculate-age-React`

## Technologies Used

- React.js
- CSS3
- GitHub Actions
- GitHub Pages

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

# Life Expectancy Calculator
## Screenshots

![Screenshot 1](docs/images/Screenshot_1.png)

![Screenshot 2](docs/images/Screenshot_2.png)


A simple GUI application that calculates the remaining time a user has left to live based on the average life expectancy for a selected country.  
The program uses Python's Tkinter library for a **nice user interface** and reads a CSV file for country‐specific life expectancy data.

---

## Overview

This application allows the user to:

- Enter their birth date (year, month, day).  
- Select their gender.  
- Choose a country from a CSV file containing life expectancy data.  

It then **calculates** the approximate remaining time to live, given the average life expectancy for that country.  
It features a modern UI with a custom rounded button and error handling for invalid inputs.

---

## Features

- **Graphical User Interface** built with Tkinter for a clean and intuitive experience.  
- **Custom Rounded Button**: A modern look for the "Calculate" button.  
- **CSV Data Integration**: Reads a simple CSV file containing life expectancy data from a Python dictionary.  
- **Dynamic Calculation**: Computes the remaining (or exceeded) life expectancy based on user input.  
- **Requirements**: Python 3.x, Tkinter (included with Python distributions by default), and a CSV file containing life expectancy data.

---

## How to Run

1. Clone or download this repository.  
2. Ensure you have **Python 3.x** installed.  
3. Make sure you have a CSV file named `life_expectancy_data.csv` with your country data.  
4. Run the Python script (e.g., `python main.py` or `python3 main.py`).

---

## Example CSV Format

```csv
Country,Male,Female
Germany,79.0,83.5
Austria,79.3,84.2
USA,76.3,81.4
...

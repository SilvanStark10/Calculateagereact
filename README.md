# Life Expectancy Calculator

A simple GUI application that calculates the remaining time a user has left to live based on the average life expectancy for a selected country.  
The program uses Python’s Tkinter library for a **nice user interface** and reads a CSV file for country‐specific life expectancy data.

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
- **Custom Rounded Button**: A modern look for the “Calculate” button.  
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
Country,Mann,Frau
Germany,79.0,83.5
Austria,79.3,84.2
USA,76.3,81.4
...



License
MIT License

Copyright (c) [year] [Full name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

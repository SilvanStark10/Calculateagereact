import tkinter as tk
from tkinter import ttk
import datetime
import csv
import os
import sys  # <-- NEW: Needed to detect if running as a PyInstaller bundle

# -------------------------------------------------------------------------
# Helper function to get the correct path to resources (like CSV files)
# -------------------------------------------------------------------------
def resource_path(relative_path):
    """
    Returns the absolute path to the resource, works for dev and for PyInstaller.
    """
    if getattr(sys, 'frozen', False):
        # If this is a PyInstaller bundle, the files are unpacked to sys._MEIPASS
        base_path = sys._MEIPASS
    else:
        # Otherwise, use the directory of this script
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

# -------------------------------------------------------------------------
# Function to load life expectancy data from a CSV file
# -------------------------------------------------------------------------
def load_life_expectancy_data(filepath):
    data = {}
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return data
    try:
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                country = row['Country']
                try:
                    data[country] = {
                        'Male': float(row['Male']),
                        'Female': float(row['Female'])
                    }
                except ValueError:
                    print(f"Error: Invalid data for {country} in CSV file.")
    except Exception as e:
        print(f"Error loading CSV file: {e}")
    return data

# -------------------------------------------------------------------------
# Custom rounded button class for a modern UI look
# -------------------------------------------------------------------------
class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, radius, bg, fg, text, command=None):
        super().__init__(parent, width=width, height=height, bg=parent["bg"],
                         highlightthickness=0, bd=0)
        self.command = command
        self.radius = radius
        self.bg = bg
        self.fg = fg
        self.text = text
        
        # Draw the rounded rectangle button
        self.create_rounded_rect(0, 0, width, height, radius, fill=bg, outline=bg)
        self.create_text(width/2, height/2, text=text, fill=fg, font=("Helvetica", 16))
        
        # Bind mouse events for clicking and cursor change
        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", lambda e: self.config(cursor="hand2"))
    
    def create_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = [
            x1 + r, y1,
            x2 - r, y1,
            x2, y1,
            x2, y1 + r,
            x2, y2 - r,
            x2, y2,
            x2 - r, y2,
            x1 + r, y2,
            x1, y2,
            x1, y2 - r,
            x1, y1 + r,
            x1, y1,
        ]
        return self.create_polygon(points, smooth=True, **kwargs)
        
    def on_click(self, event):
        if self.command:
            self.command()

# -------------------------------------------------------------------------
# Function to calculate remaining life based on birth date, gender, and country
# -------------------------------------------------------------------------
def calculate_life_left():
    try:
        year = int(year_var.get())
        month = int(month_var.get())
        day = int(day_var.get())
        gender = gender_var.get()
        birth_date = datetime.date(year, month, day)
    except Exception as e:
        result_label.config(text="Invalid date!")
        return

    today = datetime.date.today()
    if birth_date > today:
        result_label.config(text="Birth date is in the future!")
        return

    # Calculate age in days and years
    age_days = (today - birth_date).days
    age_years = age_days / 365.25

    # Retrieve the selected country's life expectancy data
    country = country_var.get()
    if country in life_expectancy_data:
        country_data = life_expectancy_data[country]
        if gender == "Male":
            expectancy = country_data['Male']
        elif gender == "Female":
            expectancy = country_data['Female']
        else:
            expectancy = (country_data['Male'] + country_data['Female']) / 2
    else:
        result_label.config(text="Please select a valid country!")
        return

    remaining_years = expectancy - age_years

    if remaining_years >= 0:
        remaining_days = int(remaining_years * 365.25)
        years_left = remaining_days // 365
        rem = remaining_days % 365
        months_left = rem // 30
        days_left = rem % 30
        result_text = (f"You have approximately {years_left} years, "
                       f"{months_left} months, and {days_left} days left to live.")
    else:
        over_years = abs(remaining_years)
        over_days = int(over_years * 365.25)
        years_over = over_days // 365
        rem_over = over_days % 365
        months_over = rem_over // 30
        days_over = rem_over % 30
        result_text = (f"You have already lived approximately {years_over} years, "
                       f"{months_over} months, and {days_over} days longer than the average life expectancy.")
    
    result_label.config(text=result_text)

# -------------------------------------------------------------------------
# Main application window setup
# -------------------------------------------------------------------------
root = tk.Tk()
root.title("Life Expectancy Calculator")
root.configure(bg="white")

window_width = 600
window_height = 700
root.geometry(f"{window_width}x{window_height}")

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Title label
title_label = tk.Label(root, 
    text="Find out how long you have left to live based on the average life expectancy:",
    font=("Helvetica", 18, "bold"), bg="white", wraplength=580, justify="center")
title_label.pack(pady=20)

# Frame for the input fields
frame = tk.Frame(root, bg="white")
frame.pack(pady=10)

# Year dropdown
year_label = tk.Label(frame, text="Year:", font=("Helvetica", 14), bg="white")
year_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
year_var = tk.StringVar()
year_options = [str(y) for y in range(1900, 2016)]
year_menu = ttk.Combobox(frame, textvariable=year_var, values=year_options, state="readonly", font=("Helvetica", 14))
year_menu.current(year_options.index("1980"))
year_menu.grid(row=0, column=1, padx=10, pady=10)

# Month dropdown
month_label = tk.Label(frame, text="Month:", font=("Helvetica", 14), bg="white")
month_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
month_var = tk.StringVar()
month_options = [str(m) for m in range(1, 13)]
month_menu = ttk.Combobox(frame, textvariable=month_var, values=month_options, state="readonly", font=("Helvetica", 14))
month_menu.current(0)
month_menu.grid(row=1, column=1, padx=10, pady=10)

# Day dropdown
day_label = tk.Label(frame, text="Day:", font=("Helvetica", 14), bg="white")
day_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
day_var = tk.StringVar()
day_options = [str(d) for d in range(1, 32)]
day_menu = ttk.Combobox(frame, textvariable=day_var, values=day_options, state="readonly", font=("Helvetica", 14))
day_menu.current(0)
day_menu.grid(row=2, column=1, padx=10, pady=10)

# Gender dropdown
gender_label = tk.Label(frame, text="Gender:", font=("Helvetica", 14), bg="white")
gender_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
gender_var = tk.StringVar()
gender_options = ["Male", "Female", "Other"]
gender_menu = ttk.Combobox(frame, textvariable=gender_var, values=gender_options, state="readonly", font=("Helvetica", 14))
gender_menu.current(0)
gender_menu.grid(row=3, column=1, padx=10, pady=10)

# Country dropdown (loaded from a CSV file)
country_label = tk.Label(frame, text="Country:", font=("Helvetica", 14), bg="white")
country_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
country_var = tk.StringVar()
country_menu = ttk.Combobox(frame, textvariable=country_var, state="readonly", font=("Helvetica", 14))
country_menu.grid(row=4, column=1, padx=10, pady=10)

# Use resource_path() to get the correct CSV path
csv_file = resource_path("data/life_expectancy_data.csv")
life_expectancy_data = load_life_expectancy_data(csv_file)

if life_expectancy_data:
    country_options = sorted(life_expectancy_data.keys())
    country_menu['values'] = country_options
    # Set "Austria" as default if available, otherwise first country
    if "Austria" in country_options:
        country_menu.current(country_options.index("Austria"))
    else:
        country_menu.current(0)
else:
    country_menu['state'] = 'disabled'
    print("Warning: No life expectancy data loaded.")

# Rounded calculate button
button_width = 200
button_height = 50
calc_button = RoundedButton(root, width=button_width, height=button_height, radius=3,
                            bg="#28a745", fg="white", text="Calculate", command=calculate_life_left)
calc_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 16), bg="white", wraplength=580, justify="center")
result_label.pack(pady=20)

root.mainloop()

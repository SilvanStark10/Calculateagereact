"""
GUI module for the life expectancy calculator application.
"""
import tkinter as tk
from tkinter import ttk
import datetime

from .ui_components import RoundedButton
from .data_handler import load_life_expectancy_data, resource_path
from .calculations import AgeCalculator

class LifeExpectancyApp:
    """
    Main application class for the Life Expectancy Calculator.
    """
    
    def __init__(self, root):
        """
        Initialize the application.
        
        Args:
            root: The root tkinter window
        """
        self.root = root
        self.setup_window()
        self.load_data()
        self.create_widgets()
        
    def setup_window(self):
        """Set up the main window properties."""
        self.root.title("Life Expectancy Calculator")
        self.root.configure(bg="white")
        
        window_width = 600
        window_height = 700
        self.root.geometry(f"{window_width}x{window_height}")
        
        # Center the window on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    def load_data(self):
        """Load the life expectancy data from CSV."""
        # Use resource_path() to get the correct CSV path
        csv_file = resource_path("data/life_expectancy_data.csv")
        self.life_expectancy_data = load_life_expectancy_data(csv_file)
    
    def create_widgets(self):
        """Create all the UI widgets."""
        # Title label
        title_label = tk.Label(self.root, 
            text="Find out how long you have left to live based on the average life expectancy:",
            font=("Helvetica", 18, "bold"), bg="white", wraplength=580, justify="center")
        title_label.pack(pady=20)
        
        # Frame for the input fields
        frame = tk.Frame(self.root, bg="white")
        frame.pack(pady=10)
        
        # Year dropdown
        year_label = tk.Label(frame, text="Year:", font=("Helvetica", 14), bg="white")
        year_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.year_var = tk.StringVar()
        year_options = [str(y) for y in range(1900, 2016)]
        year_menu = ttk.Combobox(frame, textvariable=self.year_var, values=year_options, 
                                state="readonly", font=("Helvetica", 14))
        year_menu.current(year_options.index("1980"))
        year_menu.grid(row=0, column=1, padx=10, pady=10)
        
        # Month dropdown
        month_label = tk.Label(frame, text="Month:", font=("Helvetica", 14), bg="white")
        month_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.month_var = tk.StringVar()
        month_options = [str(m) for m in range(1, 13)]
        month_menu = ttk.Combobox(frame, textvariable=self.month_var, values=month_options, 
                                 state="readonly", font=("Helvetica", 14))
        month_menu.current(0)
        month_menu.grid(row=1, column=1, padx=10, pady=10)
        
        # Day dropdown
        day_label = tk.Label(frame, text="Day:", font=("Helvetica", 14), bg="white")
        day_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.day_var = tk.StringVar()
        day_options = [str(d) for d in range(1, 32)]
        day_menu = ttk.Combobox(frame, textvariable=self.day_var, values=day_options, 
                               state="readonly", font=("Helvetica", 14))
        day_menu.current(0)
        day_menu.grid(row=2, column=1, padx=10, pady=10)
        
        # Gender dropdown
        gender_label = tk.Label(frame, text="Gender:", font=("Helvetica", 14), bg="white")
        gender_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.gender_var = tk.StringVar()
        gender_options = ["Male", "Female", "Other"]
        gender_menu = ttk.Combobox(frame, textvariable=self.gender_var, values=gender_options, 
                                  state="readonly", font=("Helvetica", 14))
        gender_menu.current(0)
        gender_menu.grid(row=3, column=1, padx=10, pady=10)
        
        # Country dropdown (loaded from a CSV file)
        country_label = tk.Label(frame, text="Country:", font=("Helvetica", 14), bg="white")
        country_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.country_var = tk.StringVar()
        country_menu = ttk.Combobox(frame, textvariable=self.country_var, 
                                   state="readonly", font=("Helvetica", 14))
        country_menu.grid(row=4, column=1, padx=10, pady=10)
        
        if self.life_expectancy_data:
            country_options = sorted(self.life_expectancy_data.keys())
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
        calc_button = RoundedButton(self.root, width=button_width, height=button_height, radius=3,
                                  bg="#28a745", fg="white", text="Calculate", command=self.calculate_life_left)
        calc_button.pack(pady=20)
        
        # Result label
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16), 
                                   bg="white", wraplength=580, justify="center")
        self.result_label.pack(pady=20)
    
    def calculate_life_left(self):
        """Calculate and display the life expectancy results."""
        try:
            year = int(self.year_var.get())
            month = int(self.month_var.get())
            day = int(self.day_var.get())
            gender = self.gender_var.get()
            birth_date = datetime.date(year, month, day)
        except Exception as e:
            self.result_label.config(text="Invalid date!")
            return
        
        today = datetime.date.today()
        if birth_date > today:
            self.result_label.config(text="Birth date is in the future!")
            return
        
        # Get age in years
        age_years = AgeCalculator.calculate_age_in_years(birth_date)
        
        # Retrieve the selected country's life expectancy data
        country = self.country_var.get()
        if country in self.life_expectancy_data:
            country_data = self.life_expectancy_data[country]
            expectancy = AgeCalculator.get_life_expectancy(country_data, gender)
        else:
            self.result_label.config(text="Please select a valid country!")
            return
        
        # Calculate remaining life
        result = AgeCalculator.calculate_remaining_life(age_years, expectancy)
        years, months, days, is_over_expectancy = result
        
        if not is_over_expectancy:
            result_text = (f"You have approximately {years} years, "
                          f"{months} months, and {days} days left to live.")
        else:
            result_text = (f"You have already lived approximately {years} years, "
                          f"{months} months, and {days} days longer than the average life expectancy.")
        
        self.result_label.config(text=result_text) 
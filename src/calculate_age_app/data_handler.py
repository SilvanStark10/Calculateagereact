"""
Data handling module for CSV and other file operations.
"""
import csv
import os
import sys

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
        # Go up to the parent directory to find the data directory
        base_path = os.path.dirname(os.path.dirname(base_path))
    return os.path.join(base_path, relative_path)

def load_life_expectancy_data(filepath):
    """
    Load life expectancy data from CSV file.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        Dictionary with country data
    """
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
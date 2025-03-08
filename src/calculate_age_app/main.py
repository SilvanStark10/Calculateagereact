"""
Main entry point for the Life Expectancy Calculator application.
"""
import tkinter as tk
from .gui import LifeExpectancyApp

def run_app():
    """
    Start the application.
    
    Returns:
        None
    """
    root = tk.Tk()
    app = LifeExpectancyApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app() 
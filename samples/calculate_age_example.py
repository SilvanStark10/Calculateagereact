#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a simple example showing how to use the Calculate Age functionality.
"""

import sys
import os

# Add the src directory to the path so we can import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Import the calculate_age function
from calculate_age import calculate_age_in_years

# Example usage
birth_date = "1990-01-15"  # Format: YYYY-MM-DD
result = calculate_age_in_years(birth_date)
print(f"A person born on {birth_date} is {result} years old.") 
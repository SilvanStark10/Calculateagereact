"""
Module for calculation logic related to age and life expectancy.
"""
import datetime

class AgeCalculator:
    """
    Class to handle age and life expectancy calculations.
    """
    
    @staticmethod
    def calculate_age_in_years(birth_date):
        """
        Calculate age in years from a birth date.
        
        Args:
            birth_date: datetime.date object representing birth date
            
        Returns:
            Age in years as a float
        """
        today = datetime.date.today()
        age_days = (today - birth_date).days
        age_years = age_days / 365.25
        return age_years
    
    @staticmethod
    def calculate_remaining_life(age_years, life_expectancy):
        """
        Calculate remaining life based on current age and life expectancy.
        
        Args:
            age_years: Current age in years
            life_expectancy: Expected lifespan in years
            
        Returns:
            Tuple containing (years_left, months_left, days_left) or
            (years_over, months_over, days_over) if past life expectancy,
            and a boolean indicating if past life expectancy
        """
        remaining_years = life_expectancy - age_years
        
        if remaining_years >= 0:
            remaining_days = int(remaining_years * 365.25)
            years_left = remaining_days // 365
            rem = remaining_days % 365
            months_left = rem // 30
            days_left = rem % 30
            return (years_left, months_left, days_left, False)
        else:
            over_years = abs(remaining_years)
            over_days = int(over_years * 365.25)
            years_over = over_days // 365
            rem_over = over_days % 365
            months_over = rem_over // 30
            days_over = rem_over % 30
            return (years_over, months_over, days_over, True)
    
    @staticmethod
    def get_life_expectancy(country_data, gender):
        """
        Get life expectancy based on country data and gender.
        
        Args:
            country_data: Dictionary with 'Male' and 'Female' keys
            gender: One of 'Male', 'Female', or 'Other'
            
        Returns:
            Life expectancy as a float
        """
        if gender == "Male":
            return country_data['Male']
        elif gender == "Female":
            return country_data['Female']
        else:
            # For 'Other' gender, use average
            return (country_data['Male'] + country_data['Female']) / 2 
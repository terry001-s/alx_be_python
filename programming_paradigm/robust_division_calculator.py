# robust_division_calculator.py
# Contains the safe_divide function with error handling

def safe_divide(numerator, denominator):
    """Performs division while handling common errors like non-numeric input and division by zero."""
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Perform division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."

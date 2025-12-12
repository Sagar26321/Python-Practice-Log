def calculate_bmi(weight_kg, height_m):
    """Calculates Body Mass Index given weight in kg and height in meters."""
    # The formula for BMI is weight / height squared
    bmi = weight_kg / (height_m ** 2)
    return bmi

# Test the function with example data
my_bmi = calculate_bmi(weight_kg=70, height_m=1.75)
print(f"My calculated BMI is: {my_bmi:.2f}")
# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
if __name__ == "__main__":
    try:
        temp_input = input("Enter the temperature to convert: ")
        temp = float(temp_input)  # raises ValueError if input is invalid

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit == "F":
            print(f"{temp}°F is {convert_to_celsius(temp)}°C")
        elif unit == "C":
            print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError as e:
        print(e)


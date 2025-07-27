FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temperature = input("Enter the temperature to convert: ")
    confirm = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if confirm == "C":
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    elif confirm == "F":
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
except:
    print("Invalid temperature. Please enter a numeric value.")

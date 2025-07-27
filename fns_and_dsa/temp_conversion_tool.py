FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(farenheit):
  return (farenheit - 32) * FARENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  return (celsius * CELSIUS_TO_FARENHEIR_FACTOR ) + 32  

def main():
    print("=== Temperature Conversion Tool ===")
    
    temp_input = input("Enter the temperature (e.g., 32): ").strip()
    scale = input("Is this temperature in (C)elsius or (F)ahrenheit? ").strip().upper()

    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    if scale == 'F':
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius:.2f}°C")
    elif scale == 'C':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit:.2f}°F")
    else:
        raise ValueError("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)

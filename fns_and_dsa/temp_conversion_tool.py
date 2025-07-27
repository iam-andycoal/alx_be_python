FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(farenheit):
  return (farenheit - 32) * FARENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  return (celsius * CELSIUS_TO_FARENHEIR_FACTOR ) + 32  

temperature =int(input("Enter the temperature (Celsius or Farenheit): "))
if temperature != range(1,11):
  print("Error: Invalid Temperature. Please enter a numeric value")

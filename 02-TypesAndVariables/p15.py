#read the temperature in celcius
temp_celcius = float(input("Input celcius: "))

#convert the temperature
temp_kelvin = temp_celcius + 273.15

temp_farenheit = temp_celcius * 1.8 + 32

#print the temperature in F and K
print(f"{temp_farenheit} F")
print(f"{temp_kelvin} K")
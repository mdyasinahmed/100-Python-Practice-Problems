# Write a program that determines the weather based on user-provided temperature and humidity.
# TEMPERATURE(C) | HUMIDITY(%) | WEATHER
# >= 30 | >= 90 | Hot and Humid
# >= 30 | < 90 | Hot
# < 30 | >= 90 | Cool and Humid
# < 30 | < 90 | Cool

temperature = int(input('Enter Temperature: '))
humidity = int(input('Enter Humidity: '))

if temperature >= 30 and humidity >= 90 :
    print("Hot and Humid")
elif temperature >= 30 and humidity > 90 :
    print("Hot")
elif temperature < 30 and humidity >= 90 :
    print("Cool and Humid")
else :
    print("Cool")
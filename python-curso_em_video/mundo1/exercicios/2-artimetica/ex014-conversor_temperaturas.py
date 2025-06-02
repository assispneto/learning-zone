# Conversor de temperaturas

tempCelsius = float(input('Qual a temperatura em °C? '))

tempFahrenheit = ((tempCelsius*1.8) + 32)
tempKelvin     = (tempCelsius + 273.15)

print('A temperatura de {}°C, após a conversão fica em: {:.1f}°f e {}K'.format(tempCelsius, tempFahrenheit, tempKelvin))



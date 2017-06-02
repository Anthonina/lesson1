# temperature - oC
# wind - m/s
weather = {
    'city': 'Moscow',
    'temperature': 19,
    'wind': 13
}
print(weather.get('city'))
weather['temperature'] = 16
print(weather)
print(len(weather))
print('count' in weather)
weather['date'] = '01.06.2017'
print(weather)
weather_list = [
    {'city': 'Moscow', 'date': '28.05.2017', 'temperature': 13, 'wind': 2},
    {'city': 'Moscow', 'date': '29.05.2017', 'temperature': 25, 'wind': 2},
    {'city': 'Moscow', 'date': '30.05.2017', 'temperature': 17, 'wind': 3},
    {'city': 'Moscow', 'date': '31.05.2017', 'temperature': 16, 'wind': 3}
]
print(weather_list)
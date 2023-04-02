weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key:round(value * 1.8 + 32, 2) for (key,value) in weather_c.items()}


print(weather_f)

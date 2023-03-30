travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above


def add_new_country(country_visited, visit_time, which_cities):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visit"] = visit_time
    new_country["cities"] = which_cities
    travel_log.append(new_country)    

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
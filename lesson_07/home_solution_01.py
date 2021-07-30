cities_of_countries = {'England': ['London', 'Manchester', 'Sheffield', 'Southampton', 'Newcastle'],
                       'France': ['Paris', 'Toulouse', 'Marseille', 'Lyon', 'Monaco'],
                       'Spain': ['Madrid', 'Barcelona', 'Bilbao', 'Malaga', 'Seville'],
                       'Italy': ['Rome', 'Milan', 'Bologna', 'Palermo', 'Genoa']
                       }


def find_city(city):
    first = str(city).upper()[0]  # take first letter
    city = str(city).replace(city[0], first)  # replace first letter on uppercase
    # Find country
    for key, value in cities_of_countries.items():
        if city in value:
            print(key)


find_city(input('Enter city name: '))
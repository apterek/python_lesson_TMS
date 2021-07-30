cities_of_countries = {'England': ['London', 'Manchester', 'Sheffield', 'Southampton', 'Newcastle'],
                       'France': ['Paris', 'Toulouse', 'Marseille', 'Lyon', 'Monaco'],
                       'Spain': ['Madrid', 'Barcelona', 'Bilbao', 'Malaga', 'Seville'],
                       'Italy': ['Rome', 'Milan', 'Bologna', 'Palermo', 'Genoa']
                       }


def find_city():
    while True:
        city = input('Enter city name: ')
        first = str(city).upper()[0]  # take first letter
        city = str(city).replace(city[0], first)  # replace first letter on uppercase
        # Find country
        for key, value in cities_of_countries.items():
            if city in value:
                print(key)
                break
        else:
            print('City is not found')
        next_try = input("Do you want find other city?(Enter 'yes' if you want): ")
        if next_try != 'yes':
            break
    return print("Have a nice day")


if __name__ == '__main__':
    print(find_city())

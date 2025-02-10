# For self analysis

from utils.countries import countries
from utils.cities import cities

a = input('Starting letter: ')
b = input('Ending letter: ')
type = input('Type: ')
cnt = 0
if type == "country":
    for country in countries:
        if b == '0':
            if country[0].lower() == a:
                print(country)
                cnt+=1
        elif a == '0':
            if country[-1].lower() == b:
                print(country)
                cnt+=1
        elif country[0].lower() == a and country[-1].lower() == b:
            print(country)
            cnt+=1
elif type == "city":
    for city in cities:
        if b == '0':
            if city[0].lower() == a:
                print(city)
                cnt+=1
        elif a == '0':
            if city[-1].lower() == b:
                print(city)
                cnt+=1
        elif city[0].lower() == a and city[-1].lower() == b:
            print(city)
            cnt+=1

print(cnt)

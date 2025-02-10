import iso3166


countries = [county.name for county in iso3166.countries]

# Data cleaning
refined_countries = []
# 1. remove countries with non-alphabetic characters
for country in countries:
    if all(x.isalpha() or x.isspace() for x in country):
        refined_countries.append(country)

countries = refined_countries

# 2. all lower case letters
refined_countries = [country.lower() for country in countries]

countries = refined_countries
# countries = countries[:100]

if __name__== "__main__":
    print(countries)


# country_to_id = {country: i for i, country in enumerate(countries)}
# id_to_country = {i: country for i, country in enumerate(countries)}

# def get_country_to_id():
#     return country_to_id

# def get_id_to_country():
#     return id_to_country

def indexer(countries):
    country_to_id = {country: i for i, country in enumerate(countries)}
    id_to_country = {i: country for i, country in enumerate(countries)}
    return country_to_id, id_to_country


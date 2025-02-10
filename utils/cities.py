# get the top 100 cities from cities.csv
import pandas as pd

cities = pd.read_csv("/home/hibiki/Desktop/Precog/utils/cities.csv")
cities = cities["City"].tolist()
cities = cities[:500]
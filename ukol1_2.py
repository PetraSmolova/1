import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/pesikj/progr2-python/master/data/london_merged.csv")
open("london_merged.csv", 'wb').write(r.content)

df_merged = pandas.read_csv("london_merged.csv")
df_merged["timestamp"] = pandas.to_datetime(df_merged["timestamp"])
df_merged["year"] = df_merged["timestamp"].dt.year
df_merged = df_merged.groupby(["year","weather_code"])["weather_code"].count()

print(df_merged)
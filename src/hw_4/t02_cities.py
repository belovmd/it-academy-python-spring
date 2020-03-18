""" Cities

Get country(ies) by a city.

Input data:
N - number of countries
Each line from the following N lines contains:
a country and a list of cities of this country.
M - queries count
Folowing M lines contain one city (from cities above).

Output data:
For every city print a country name.

Example:
Input:
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod

Output:
Ukraine
Russia
Russia
"""

print('Input N - number of countries:')
n = int(input())
print('Input country and it''s cities:')
atlas = {}
for _ in range(n):
    country, *cities = input().split()
    atlas[country] = set(cities)

print('Input M - number of queries:')
m = int(input())
print('Input cities:')
queries = []
for _ in range(m):
    queries.append(input())

for city in queries:
    result = []
    for country, cities in atlas.items():
        if city in cities:
            result.append(country)
    print('{city} is in {country_list}.'
          .format(city=city, country_list=', '.join(result)))

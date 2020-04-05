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
Odessa is in Ukraine
Moscow is in Russia
Novgorod is in Russia
"""


from collections import defaultdict


atlas = defaultdict(set)
with open('t02_input.txt', 'r') as file:
    # Read number of countries, countries and cities
    n = int(file.readline())
    for _ in range(n):
        country_in, *cities_in = file.readline().strip().split()
        for _, city in enumerate(cities_in):
            atlas[city].add(country_in)

    # Read number of queries and cities
    m = int(file.readline())
    for _ in range(m):
        city_in = file.readline().strip()
        print('{city} is in {country_list}'.
              format(city=city_in, country_list=', '.join(atlas[city_in])))

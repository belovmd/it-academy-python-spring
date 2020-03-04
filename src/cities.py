def country_of_cities():
    """Countries and cities

    Generate dictionary with
        keys:
            Names of cities
        values:
            Names of countries lists for city with name from self key

        Print countries names for each city from query

    :return: None
    """

    country_nmb = int(input('Enter number of countries: '))

    countries_of_city = {}

    for _ in range(country_nmb):
        country_data = input('Enter country and cities of country: ').split()
        country, cities = country_data[0], country_data[1:]

        countries_of_city = (
            {city: countries_of_city.get(city, []) + [country] for city in
             cities}
        )

    query = int(input('Enter number of queries: '))
    cities_in_queries = [input(f'Enter {i + 1} city: ') for i in range(query)]

    for city in cities_in_queries:
        print(city, 'in:', *countries_of_city.get(city, ['City not in list']))


if __name__ == '__main__':
    country_of_cities()

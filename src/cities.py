import functools
import time
DEBUG = True


def function_time_counter(func):
    """Function working time counter"""
    if not DEBUG:
        return func

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper of function"""
        start_time = time.time()
        for _ in range(10000):
            func(*args, **kwargs)
        end_time = time.time()
        result_time = end_time - start_time
        func_name = func.__name__
        print(f'Time of "{func_name}" for 10000 iteration is: {result_time}')
        return func(*args, **kwargs)
    return wrapper


@function_time_counter
def country_of_cities(query_to_set_data, cities_in_queries):
    """Countries and cities

    Generate dictionary with
        keys:
            Names of countries
        values:
            Set of names of cities of countries

        Print countries names for each city from query

    :return: None
    """
    query_to_set_data = query_to_set_data

    cities_in_queries = cities_in_queries

    country_data = {}

    for data_set in query_to_set_data:
        country, *cities = data_set.split()
        country_data[country] = {*cities}

    cities_data_result = {}

    for city in cities_in_queries:
        for country, cities in country_data.items():
            if city in cities:
                cities_data_result[city] = (
                    cities_data_result.get(city, []) + [country]
                )
        cities_data_result[city] = (
            cities_data_result.get(city, ['City not in list'])
        )

    return cities_data_result


@function_time_counter
def country_of_cities_second(query_to_set_data, cities_in_queries):
    """Countries and cities

    Generate dictionary with
        keys:
            Names of cities
        values:
            Lists of names of countries for city with name from self key

        Print countries names for each city from query

    :return: None
    """
    query_to_set_data = query_to_set_data

    cities_in_queries = cities_in_queries

    countries_of_city = {}

    for data_set in query_to_set_data:
        country, *cities = data_set.split()

        countries_of_city.update(
            {city: countries_of_city.get(city, []) + [country] for city in
             cities}
        )

    cities_data_result = {}

    for city in cities_in_queries:
        cities_data_result[city] = (
            countries_of_city.get(city, ['City not in list'])
        )
    return cities_data_result


if __name__ == '__main__':
    query_to_set_data = [
        'Belarus Minsk Mogilev Brest Grodno',
        'Russia Moscow Paris Novgorod Kaluga',
        'France Brest Paris Marsel',
    ]

    cities_in_queries = [
        'Minsk',
        'Brest',
        'Paris',
        'Novosibirsk',
        'Moscow',
        'Kaluga',
    ]

    print('\n-----First function results------\n')
    fun1_res = country_of_cities(query_to_set_data, cities_in_queries)
    for city, countries in fun1_res.items():
        print(city, 'in:', *countries)

    print('\n-----Second function results-----\n')
    fun2_res = country_of_cities_second(query_to_set_data, cities_in_queries)
    for city, countries in fun2_res.items():
        print(city, 'in:', *countries)

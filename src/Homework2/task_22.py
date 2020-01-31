def sum_for_list(lst):
    factors = {i for k in lst for i in range(2, abs(k)+1) if not k % i}
    print(factors)
    prime_factors = {i for i in factors if not [j for j in factors-{i} if not i % j]}
    print(prime_factors)
    return [[p, sum(e for e in lst if not e % p)] for p in sorted(prime_factors)]

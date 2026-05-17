def get_primes_up_to(limit: int) -> list:
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)

    is_prime[0] = False
    is_prime[1] = False

    p = 2

    while p * p <= limit:
        if is_prime[p]:
            multiple = p * p
            while multiple <= limit:
                is_prime[multiple] = False
                multiple += p

        p += 1

    primes = []
    i = 2
    while i <= limit:
        if is_prime[i]:
            primes.append(i)
        i += 1

    return primes
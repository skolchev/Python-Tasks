def goldbach(n):
    # Get prime numbers using Sieve of Erathosthenes algorithm
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * int((n - i * i - 1) / (2 * i) + 1)
    primes = [2] + [x for x in range(3, n, 2) if sieve[x]]

    # Get the list of tuples
    return [(x, y) for x in primes for y in primes if x <= y and x + y == n]

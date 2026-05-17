from primes import get_primes_up_to
import time

limit = int(input("Enter a number: "))

start_time = time.time()
primes = get_primes_up_to(limit)
elapsed_time = time.time() - start_time

print("--- %s seconds ---" % (time.time() - start_time))
print(primes[-1])

# print(*primes, sep=' ')
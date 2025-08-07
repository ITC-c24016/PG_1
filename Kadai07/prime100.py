import math

primes = []
count = 0

for i in range(2,101):
    is_prime = True
    for j in range(2,int(math.sqrt(i) + 1)):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)


for prime in primes:
    print(prime,end=",")
    count += 1
    if count % 10 == 0:
        print()
print()

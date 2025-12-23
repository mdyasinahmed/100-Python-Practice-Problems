primes = []
num = 2
while len(primes) < 25:
    if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
        primes.append(num)
    num += 1
print(primes)

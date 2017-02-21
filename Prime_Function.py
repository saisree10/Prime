def is_prime(p):
    if p > 1:
        n = p // 2
        for i in range(2, n + 1):
            if p % i == 0:
                return False
        return True
    else:
        return False

number = 1011013

 # test data:  number = 1011013, number = 10110133, number = 101101331
if is_prime(number):
    print str(number) + " is a prime number"
else:
    print str(number) + " is not a prime number"
import random
import sys
import math

def one_time_check(number):
    if pow(random.randint(2, number - 1), number - 1, number) != 1:
        # Not a prime
        return True
    return False

def primality_check(number, tries):
    for i in range(0, tries):
         if one_time_check(number):
             return '{} {}'.format(number, "is most probably not a prime number")
    return '{} {}'.format(number, "is most probably a prime number")

if __name__ == "__main__":
    print(primality_check(int(sys.argv[1]), int(math.ceil(int(sys.argv[1]) / 2))))

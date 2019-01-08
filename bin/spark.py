from random import randint
import sympy
import argparse
import sys

size = 31
maximum = 2**31

def mod_inverse(prime,max):
    x, y, m0 = 1, 0, max

    if max == 1:
        return 0
    
    while prime > 1:
        quotient = prime // max
        temp = max
        max = prime % max
        prime, temp = temp, y

        # Update x and y
        y = x - quotient * y
        x = temp

    if x < 0 :
        x = x + m0

    return x

def get_random():
    return randint(2**18,maximum-10)

def main():
    parser = argparse.ArgumentParser(description='Generate constructor values for your prime')
    parser.add_argument('p',type=int,default = 0)
    args = parser.parse_args()
    if args.p:
        if not sympy.ntheory.primetest.isprime(args.p):
            sys.exit('the given integer is not a prime number')
        elif args.p > 2147483647:
            sys.exit('The given prime number should be less than 2147483647')
        else:
            prime = args.p
    else:
        prime = sympy.ntheory.generate.randprime(2**18,maximum-1)

    print('prime : {} \ninverse : {} \nrandom : {}'.format(prime,mod_inverse(prime,maximum),get_random()))

if __name__ == '__main__':
    main()
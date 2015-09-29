from random import randint, randrange
import sys

"""
This program includes all of the functions used in RSA encryption. It includes
the Fermat test to generate prime numbers with confidence, the Extended Euclidean
Algorithm, modular exponentiation and modular inverse.
"""

def generatePrimes(numPrimes, digits, passes=4):
    """
    This function computes a prime number with the number of digits specified, It works
    a by generatig a random number and then using Fermat's Little Theorem to determine
    whether or not the number is prime.

    You can optionally specify the number of passes as a second parameter which will test
    multiple random numbers to increase the accuracy of the result. 4 passes (default)
    should suffice in most cases.

    :param numPrimes: The number of prime numbers to generate
    :param digits: The number of digits the prime number should have
    :param passes: The number of times to test the number for primality
    :return: A list of prime numbers with the specified number of digits
    """

    isPrime = False
    primesList = []
    # Determine the starting and ending number based on the provided size
    startRange = 10 ** (digits - 1)
    endRange = (10 ** digits) - 1
    for x in range(0, numPrimes):
        while not isPrime:
            randNum = randint(startRange, endRange)
            for y in range(0, passes):
                # If the size is 1, the generated number must be greater >= 3 or else
                # we will be trying to get a random number in an empty (or negative) range
                if randNum < 3:
                    randNum = 3
                a = randint(1, randNum - 1)
                b = modExp(a, randNum - 1, randNum)
                # If the b is not = 1, then this number is composite, break out of the loop
                # and generate another random number to try.
                if b != 1:
                    break
                # Iff 4 different a values result in b == 1, then we say that we have found
                # a prime number

                if y == 3:
                    isPrime = True
        isPrime = False
        primesList.append(randNum)
    return primesList

def modExp(x, y, m):
    """
    This function computes the x^y mod m in a fast way by ignoring the quotient since
    we only care about the remainder.
    :param x: The base
    :param y: The power to raise the base x to
    :param m: The number to take the mod of
    :return: The modulus of x^y and m
    """
    if y == 0:
        return 1
    else:
        z = modExp(x, y / 2, m)
        if y % 2 == 0:
            return (z * z % m)
        else:
            return (x * z * z % m)

def extendedEuclidean(a, b):
    """
    This function performs the extended euclidean algorithm on the specified numbers a and b
    :param a: A number
    :param b: A number
    :return: A tuple containing the values in the following order: (gcd, x, y)
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extendedEuclidean(b % a, a)
        return (g, x - (b // a) * y, y)

def modInv(a, m):
    """
    This function computes the modular inverse of a number a by using the extended euclidean algorithm
    :param a: A number
    :param m: The number to modulo a by
    :return: The modular inverse of the number
    """
    gcd, x, y = extendedEuclidean(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

def toInt(str):
    """
    This function converts a string to its base 128 integer equivalent
    :param str: A string message
    :return:Its base 128 equivalent
    """
    total = 0
    for ch in str:
        total <<= 7
        total += ord(ch)
    return total

def toString(intVal):
    """
    This function takes an integer in base 128, and converts it to a string
    :param intVal: An integer in base 128 format
    :return: Its string representation
    """
    result = []
    while intVal:
        result.append(chr(intVal % 128))
        intVal >>= 7
    return ''.join(reversed(result))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        numDigits = int(sys.argv[1])
        print generatePrimes(1, numDigits)[0]
    elif len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        gcd, x, y = extendedEuclidean(a, b)
        print '(%i, %i)' % (x, y)
    elif len(sys.argv) == 4:
        e = int(sys.argv[1])
        p = int(sys.argv[2])
        q = int(sys.argv[3])
        n = p * q
        phiN = (p - 1) * (q - 1)
        d = modInv(e, phiN)
        print '(%i, %i)' % (d, n)
    elif len(sys.argv) == 5:
        if sys.argv[1] == 'e' or sys.argv[1] == 'E':
            e = int(sys.argv[2])
            n = int(sys.argv[3])
            msg = toInt(sys.argv[4])
            encrypted = modExp(msg, e, n)
            print 'The encrypted message is: %i' % encrypted
        elif sys.argv[1] == 'd' or sys.argv[1] == 'D':
            d = int(sys.argv[2])
            n = int(sys.argv[3])
            msg = int(sys.argv[4])
            decrypted = modExp(msg, d, n)
            print 'The decrypted message is: %s' % toString(decrypted)
        else:
            print 'Error: First argument must be either "e" for encrypt or "d" for decrypt'
    else:
        print 'Invalid arguments'
        print 'Try one of the following:'
        print '\t> python rsa.py s'
        print '\t> python rsa.py a b'
        print '\t> python rsa.py e p q'
        print '\t> python rsa.py \'e\' e n message'
        print '\t> python rsa.py \'d\' d n message'
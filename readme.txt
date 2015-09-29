RSA ALGORITHM IMPLEMENTATION
Eric Vestfals
esv5@zips.uakron.edu

This program allows you to encrypt messages using the RSA algorithm.
Messages are encrypted step by step starting with the generation of
random prime numbers.

RUNNING THE PROGRAM
--------------------
This program is written in Python, so running it requires the Python
interpreter. Running the program is simple. Just execute the following
command in a terminal:
    > python rsa.py ...

This program takes a variable number of arguments, and does different
things based on the number/type of arguments.

ARGUMENTS
----------
The first option is to generate a random prime number of n digits. This
can be done with:
    > python rsa.py n
where n is the number of digits the prime number should contain.

The second option is to generate x, and y such that gcd(a, b) = ax + by.
This can be done with:
    > python rsa.py a b
where a is a prime number and b is a prime number.

The third option is to generate the private key pair (d, n). This can be
done with:
    > python rsa.py e p q
where e is the public key and p and q are coprime numbers.

The fourth option is to encrypt a message. This can be done with:
    > python rsa.py 'e' e n message
where 'e' is the character 'e' (no quotes), e is the public key, n is the
shared number between public and private keys and message is the message
to encrypt.

The fifth option is to decrypt an encrypted message. This can be done with:
    > python rsa.py 'd' d n message
where 'd' is the character 'd' (no quotes), d is the private key, n is the
shared number between public and private keys and message is the message
to decrypt.

OTHER NOTES
------------
The maximum length of a prime number is somewhere around 300 digits (around 150
character messages) at which point the maximum recursion depth is exceeded, and
the program crashes. The recursion depth can be changed allowing for larger
numbers to be generated, however it is not recommended as it can cause other
issues such as stack overflows and infinite recursion.
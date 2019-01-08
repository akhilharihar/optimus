# Knuth's integer hashing based id obfuscation

This is a Python port of [jenssegers/optimus](https://github.com/jenssegers/optimus) PHP library.

With this library, you can transform your internal id's to obfuscated integers based on Knuth's integer hash.

## Installation
```
#TODO
```

## Usage

To get started you will need 3 things;
- Large prime number lower than `2147483647`
- The inverse prime so that `(PRIME * INVERSE) & (2**31 -1) == 1`
- A large random integer lower than `2147483647`

For convenience, I've also included a terminal command(`optimusargs`) to generate the the above numberes for use in your project. 

To get started, run `optimusargs` in your terminal. 

```
$ optimus_args
prime : 936318091
inverse : 760853283
random : 442954076
```
If you'd prefer to use your own prime number([large prime numbers list](http://primes.utm.edu/lists/small/millions/)), pass it to the command line to calculate the remaining numbers.

```
$ optimus_args 936318091
prime : 936318091
inverse : 760853283
random : 442954076
```

**Note :** You'll need to install sympy library in order to use the terminal command and is not required if you only intend to use the `Optimus` class.  

To install sympy library, run 
```
pip install sympy
```

Create an instance of `Optimus` with the above parameters

```
from optimus import Optimus

opt  = Optimus(prime,inverse,random)
```

## Encoding and Decoding

To encode an id, 
```
encoded = opt.encode(20) # 1535832388
```
To decode the resulting encoded value back to its original value,
```
decoded = opt.encode(1535832388) # 20
```

**Note** - This library can only encode and decode positive integers ranging from 0 to 2147483647. 

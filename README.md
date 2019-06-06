# Mersenne Twister :lock:

pseudo-Random Number Generator (RNG)

Python3.x+ implementation based of the 32-bit [MT19937](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html) Specification.

> **Note**: Implementation used in Python's RNG in the `random` module.

---

## Install

```
$ python setup.py install
```

---

## Usage

```py
from mersenne_twister import MTRNG

# Initialize the generator with your randomly generated seed
# Note: '5489' is used as the default seed if none is passed
generator = MTRNG(seed=4294967295)

# Print a (pseudo) random number
print(generator.getRandom())
```

---

## Reading resources

- [Mersenne Twister](https://wikipedia.org/wiki/Mersenne_Twister) [Wikipedia]
- [Overview of inner workings](https://www.github.com/crypto101/book) [Crypto101 Book]
- [Original C implementation](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html) [MT19937]

---

MIT &copy; 2019 Zero-1729

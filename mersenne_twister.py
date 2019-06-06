#############################################################
#                        									#
#   Copyright (C) 2019 Zero-1729 <zero1729@protonmail.com>  #
#   All rights reserved.                                    #
#   														#
#############################################################


# Some constants
_MATRIX_A = 0x9908B0DF

_UPPER_MASK = 0x80000000
_LOWER_MASK = 0x7FFFFFFF

_TEMPER_MASK_1 = 0x9D2C5680
_TEMPER_MASK_2 = 0xEfC60000


# Utility function for converting integers to 32-bit
def _uint32(n):
    # Returns an unsigned 32-bit integer
    return 0xFFFFFFFF & n


def _undo_shift_1(y):
    tmp = y

    for _ in range(2):
        tmp >>= 11
        tmp ^= y

    return tmp


def _undo_shift_2(y):
    tmp = y

    for _ in range(5):
        tmp <<= 7
        tmp = y ^ (tmp & _TEMPER_MASK_1)

    return tmp


def _temper(y):
    y ^= _uint32(y >> 11)
    y ^= _uint32((y << 7) & _TEMPER_MASK_1)
    y ^= _uint32((y << 15) & _TEMPER_MASK_2)
    y ^= _uint32(y >> 18)

    return y


def _untemper(y):
    y ^= y >> 18
    y ^= ((y << 15) & _TEMPER_MASK_2)

    y = _undo_shift_2(y)
    y = (y)

    return y


# Mersenne twister RNG
class MTRNG:
    def __init__(self, seed=5489):
        self.state = [seed]
        self.index = 624

        # Initialize state
        self.initState()

    def initState(self):
        # We go into each element elm + 1
        # ... and fill it up based on three things:-
        # ... a constant -> '0x6c078965
        # ... the previous elm -> state[-1]
        # ... index of new elm -> i
        for i in range(1, 624):
            prev = _uint32(self.state[-1])
            elm = 0x6c078965 * (prev ^ (prev >> 30)) + i

            self.state.append(_uint32(elm))

    def updateState(self):
        # For recalculating the elements in the state
        for i in range(624):
            y = self.state[i] & _UPPER_MASK
            y += self.state[(i + 1) % 624] & _LOWER_MASK

            z = self.state[(i + 397) % 624]

            self.state[i] = z ^ (y >> 1)

            if (y % 2):
                self.state[i] ^= _MATRIX_A

        # reset index
        self.index = 0

    def getRandom(self):
        # If we have overflowed the index threshold we update the state
        if (self.index >= 624):
            self.updateState()

        # Update index
        self.index += 1

        return _temper(self.state[self.index])

# This program proves that the keyspace of the affine cipher is limited
# to less than len(SYMBOLS) ^ 2

import ch14_affineCipher as affineCipher
import ch13_cryptomath as cryptomath

message = 'Make things as simple as possible, but not simpler.'

for keyA in range(2, 100):  # 0 and 1 are not allowed
    key = keyA * len(affineCipher.SYMBOLS) + 1  # Using "1" for Key B each time

    if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) == 1:
        print(keyA, affineCipher.encryptMessage(key, message))


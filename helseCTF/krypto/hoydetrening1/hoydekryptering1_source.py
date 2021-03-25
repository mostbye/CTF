import numpy as np
from secret import FLAG

# Super secret alphabet
alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;?@[\\]^_`{|}~"

def encrypt(plaintext, key):
    plaintext = [alphabet.index(l) for l in plaintext]
    assert len(plaintext) % key.shape[0] == 0

    ciphertext = np.array(plaintext)
    ciphertext.resize(int(ciphertext.shape[0]/key.shape[0]), key.shape[0])
    ciphertext = np.matmul(ciphertext, key)
    ciphertext = np.remainder(ciphertext, len(alphabet)).flatten()

    return "".join([alphabet[int(c)] for c in ciphertext])


KEY = "super_secret_key"
encrypt_key = np.array([alphabet.index(k) for k in KEY])
encrypt_key.resize(4, 4)
print(encrypt_key)

assert encrypt_key.shape[0] == encrypt_key.shape[1]
assert np.linalg.det(encrypt_key) != 0

ciphertext = encrypt(FLAG, encrypt_key)
print(ciphertext)


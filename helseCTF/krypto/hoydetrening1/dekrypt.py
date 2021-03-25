import numpy as np
#from secret import FLAG

# Super secret alphabet
alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;?@[\\]^_`{|}~"

def encrypt(plaintext, key):
    plaintext = [alphabet.index(l) for l in plaintext]
    # finner index i alfabetet til plaintext og legget i liste
    print(plaintext)
    assert len(plaintext) % key.shape[0] == 0
    
    ciphertext = np.array(plaintext)
    print(ciphertext)
    ciphertext.resize(int(ciphertext.shape[0]/key.shape[0]), key.shape[0])
    print("Before mult",ciphertext)
    # matrix multiply
    ciphertext = np.matmul(ciphertext, key)
    print("after mult",ciphertext)
    ciphertext = np.remainder(ciphertext, len(alphabet)).flatten()
    print("matrix cipher",ciphertext)

    return "".join([alphabet[int(c)] for c in ciphertext])


def decrypt(ciphertext, key):
    ciphertext = [alphabet.index(l) for l in ciphertext]
    # finner index i alfabetet til plaintext og legget i liste
    print(ciphertext)
    assert len(ciphertext) % key.shape[0] == 0
    ciphertext = np.array(ciphertext)
    print(ciphertext)
    ciphertext.resize(int(ciphertext.shape[0]/key.shape[0]), key.shape[0])
    # matrix multiply
    inverse = np.linalg.inv(key)
    print("inverse key", inverse)
    print(ciphertext)
    ciphertext = np.matmul(ciphertext, inverse)
    print(ciphertext)
    ciphertext = np.remainder(ciphertext, len(alphabet)).flatten()
    print(ciphertext)

    return "".join([alphabet[chr(c)] for c in ciphertext])
    
KEY = "super_secret_key"
encrypt_key = np.array([alphabet.index(k) for k in KEY])
encrypt_key.resize(4, 4)
print(encrypt_key)

assert encrypt_key.shape[0] == encrypt_key.shape[1]
assert np.linalg.det(encrypt_key) != 0
FLAG = '''Q0(Kvx$_o(OB@#$jbZ^[aQR!\e)H?Al"xC9;?:Pfv-4BXs&NZRp*~O-|Q}AoFCQF+:s)*?^a'nw?M"`C^1oH'''
ciphertext = encrypt(FLAG, encrypt_key)
print(ciphertext)
plaintext = decrypt(FLAG, encrypt_key)
print(ciphertext)



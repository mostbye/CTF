# Mistet oppskrift

JS scriptfungerer om man sender inn random bokstaver og endrer seg ikke ved AA bytt noen.

Sender inn alfanumeriske chars

```
var ingredienser = [
  'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ _{}1234567890'
]

>>> 0d0e0f08090a0b04050607000102031c1d1e1f18191a1b1415162d2e2f28292a2b24252627202122233c3d3e3f38393a3b3435364c3317115d5e5f58595a5b54555c
```

Mapper man opp dette: a = 0d osv og erstater samme boksav

Psudo:
```
    lookup = lookuplist(plain, enc)
    for ing in cipher:
        cipher_arr = splitting(ing, 2)
        decoded_arr = []
        for item in cipher_arr:
            for look in lookup:
                if item in look:
                    decoded_arr.append(look[1])
        print(''.join(decoded_arr))
```

```
$ python3 oppsk.py 
Eggeplomme
```

Gjents for alle ingredienser, men ny enc for hver:

```
    #cipher = ['290b0b091c0003010109'] # Eggeplomme
    #cipher = ['113b283e3f373537373f'] # Kardemomme
    #cipher = ['43f764']  # Løk
    #cipher = ['07353820']  # Salt
    #cipher = ['586d78786d7a']  # Pepper
    #cipher = ['163a2928322b3a35']  # Marsipan
    #cipher = ['1416162a1f30213e3d343e3f223a303a342c']  # EGG{Napoleonskake}

    ## First
    #plain = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ _{}1234567890"
    # Plain alfa inn
    #enc = "0d0e0f08090a0b04050607000102031c1d1e1f18191a1b1415162d2e2f28292a2b24252627202122233c3d3e3f38393a3b3435364c3317115d5e5f58595a5b54555c"
    # Eggemplomme from js
    #enc = "3b38393e3f3c3d32333031363734352a2b28292e2f2c2d2223201b18191e1f1c1d12131011161714150a0b08090e0f0c0d0203007a0521276b68696e6f6c6d62636a"
    # Kardemomme from js
    #enc = "6e6d6c6b6a696867666564636261607f7e7d7c7b7a79787776754e4d4c4b4a494847464544434241405f5e5d5c5b5a59585756552f5074723e3d3c3b3a393837363f"
    # Løk from js
    #enc = "353637303132333c3d3e3f38393a3b24252627202122232c2d2e151617101112131c1d1e1f18191a1b04050607000102030c0d0e740b2f29656667606162636c6d64"
    # Salt from js
    #enc = "696a6b6c6d6e6f606162636465666778797a7b7c7d7e7f707172494a4b4c4d4e4f404142434445464758595a5b5c5d5e5f50515228577375393a3b3c3d3e3f303138"
    # Pepper from js
    #enc = "3a39383f3e3d3c33323130373635342b2a29282f2e2d2c2322211a19181f1e1d1c13121110171615140b0a09080f0e0d0c0302017b0420266a69686f6e6d6c63626b"
    # Marsipan from js
    #enc = "3033323534373639383b3a3d3c3f3e212023222524272629282b1013121514171619181b1a1d1c1f1e010003020504070609080b710e2a2c60636265646766696861"
>>>> GET the egg
```

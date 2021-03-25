import os, random
import binascii
from collections import Counter

def freq(inn):
	msg = inn   # read ciphertext from standard input
	for step in range(1, 256):
		match = total = 0
		for i in range(len(msg)):
			for j in range(i + step, len(msg), step):
				total += 1
				if msg[i] == msg[j]: match += 1

		try:
			ioc = float(match) / float(total)
		except:
			pass
		print("%3d%7.2f%% %s" % (step, 100*ioc, "#" * int(0.5 + 500*ioc)))


# Meldingene er på engelsk, med store bokstaver og mellomrom.
with open('gjenbruk_output.txt', 'r') as infile:
	meldinger1 = infile.readlines()
meldinger = []
freq(meldinger1)
for item in meldinger1:
	tmp = item.strip()
	meldinger.append(binascii.unhexlify(tmp))

print(meldinger)
freq(meldinger[0])

#meldinger = ["EGG", "NORSK", "HELSENETT", "DETECT", "CYBERATTACKS"]
#random.shuffle(meldinger)


#secret = os.urandom(128)
#print(secret)
secret = b"                                                                                             "


def xor(a, b):
    l = min(len(a), len(b))
    return bytes(x ^ y for x, y in zip(a[0: l], b[0: l]))

for plaintext in meldinger:
    assert len(plaintext) < len(secret)
    w = xor(plaintext, secret)
    print(w.hex())



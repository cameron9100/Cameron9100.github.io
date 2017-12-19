def encrypt(anyString):
    empty = ''
    empty2 = ''
    count = 0
    for i in (anyString):
        if count%2 == 0:
            empty = empty + i
        else:
            empty2 = empty2 + i
        count = count + 1
    cipher = empty + empty2

    return cipher

def decrypt(cipher):
    halfLength = len(cipher) // 2
    first = cipher[:halfLength]
    last = cipher[halfLength:]
    decipher = ''

    for i in range(halfLength):
        decipher = decipher + first[i]
        decipher = decipher + last[i]

    if len(last) > len(first):
        decipher = decipher + first[-1]

    return decipher

anyString = input("Type: ")
enc = encrypt(anyString)
print(enc)

decrypt(enc)
dec = decrypt(enc)
print(dec)

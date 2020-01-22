def caesarEnc(plaintext, key):

    ciphertext = ""

    for c in plaintext:
        if c.isalpha():
            if c.isupper():
                ciphertext += chr((ord(c) - 65 + key) % 26 + 65)

            if c.islower():
                ciphertext += chr((ord(c) - 97 + key) % 26 + 97)
        else:
            ciphertext += c

    return ciphertext

def caesarDec(ciphertext, key):

    plaintext = ""

    for c in ciphertext:
        if c.isalpha():
            if c.isupper():
                plaintext += chr((ord(c) - 65 - key) % 26 + 65)

            if c.islower():
                plaintext += chr((ord(c) - 97 - key) % 26 + 97)
        else:
            plaintext += c

    return plaintext
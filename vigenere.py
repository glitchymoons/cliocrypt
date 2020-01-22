def vigenereEnc(plaintext, keyword):

    key = []
    for c in keyword.lower():
            k = ord(c) - 97
            key.append(k)

    ciphertext=""
    j = 0

    for c in plaintext:
        if c.isalpha():
            if c.isupper():
                ciphertext += chr((ord(c) - 65 + key[j % len(keyword)]) % 26 + 65)
                j += 1
            if c.islower():
                ciphertext += chr((ord(c) - 97 + key[j % len(keyword)]) % 26 + 97)
                j += 1
        else:
            ciphertext += c

    return ciphertext


def vigenereDec(ciphertext, keyword):

    key = []
    for c in keyword.lower():
            k = ord(c) - 97
            key.append(k)

    plaintext=""
    j = 0

    for c in ciphertext:
        if c.isalpha():
            if c.isupper():
                plaintext += chr((ord(c) - 65 - key[j % len(keyword)]) % 26 + 65)
                j += 1
            if c.islower():
                plaintext += chr((ord(c) - 97 - key[j % len(keyword)]) % 26 + 97)
                j += 1
        else:
            plaintext += c

    return plaintext
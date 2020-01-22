import math

def scytaleEnc(plaintext, key):

    # Add Xs as filler for the grid
    if len(plaintext) % key != 0:
        plaintext += 'x' * (key - (len(plaintext) % key))

    # Slice plaintext into row-sized blocks (row length = number of columns, i.e. key)
    pt = []

    for start in range(0, len(plaintext), key):
        pt.append(plaintext[start:start+key])

    # Generate a 2D array (matrix) where each block is one row of separate characters
    grid = []

    for block in pt:
       grid.append(list(block))

    # Transpose the matrix
    grid_t = list(map(list, zip(*grid)))

    # Move its contents into a unidimensional list
    ciphertext = []
    for sublist in grid_t:
        ciphertext.extend(sublist)

    return("".join(ciphertext))


def scytaleDec(ciphertext, key):

    # Find number of rows in the encryption grid, to use as number of columns in the decryption grid
    rows = math.ceil(len(ciphertext)/key)

    # Slice plaintext into row-sized blocks (row length = number of columns in decryption grid)
    pt = []

    for start in range(0, len(ciphertext), rows):
        pt.append(ciphertext[start:start+rows])

    # Generate a 2D array (matrix) where each block is one row of separate characters
    grid = []

    for block in pt:
       grid.append(list(block))

    # Transpose the matrix
    grid_t = list(map(list, zip(*grid)))

    # Move its contents into a unidimensional list
    plaintext = []
    for sublist in grid_t:
        plaintext.extend(sublist)

    # Remove extra Xs at the end, leaving only one
    for i in range(-key, 0):            # iterate over last key-sized chunk of the list
        if plaintext[i] == "x":         # if element is x
            if plaintext[i-1] == "x":   # and it follows another x
                plaintext.pop(i)        # remove it

    return("".join(plaintext))

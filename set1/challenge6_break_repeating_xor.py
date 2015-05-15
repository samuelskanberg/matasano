from challenge2_xor import byteArrayXOR

def stringEditDistance(str1, str2):
    b1 = bytearray(str1)
    b2 = bytearray(str2)

    res = byteArrayXOR(b1, b2)
    distance = 0
    for b in res:
        distance += bin(b).count("1")

    return distance



if __name__ == "__main__":
    str1 = "this is a test"
    str2 = "wokka wokka!!!"

    editDistance = stringEditDistance(str1, str2)
    assert(editDistance == 37)
    print editDistance

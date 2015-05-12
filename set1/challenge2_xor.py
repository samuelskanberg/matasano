import challenge1_convert

def byteArrayXOR(array1, array2):
    assert(len(array1) == len(array2))
    resultArray = []
    for i in range(0, len(array1)):
        resultArray.append(array1[i]|array2[i])

    return resultArray


if __name__ == "__main__":
    hex1 = "1c0111001f010100061a024b53535009181c"
    hex2 = "686974207468652062756c6c277320657965"
    expectedXOR = "746865206b696420646f6e277420706c6179"

    b1 = [1, 2, 3, 4]
    b2 = [2, 5, 6, 4]
    res = byteArrayXOR(b1, b2)
    print "b1:"
    for b in b1:
        print bin(b)

    print "b2:"
    for b in b2:
        print bin(b)

    print res

    print "res:"
    for b in res:
        print bin(b)



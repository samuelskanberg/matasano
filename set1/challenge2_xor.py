from challenge1_convert import hexToByteArray, byteArrayToHex

def byteArrayXOR(array1, array2):
    assert(len(array1) == len(array2))
    resultArray = []
    for i in range(0, len(array1)):
        resultArray.append(array1[i]^array2[i])

    return resultArray


if __name__ == "__main__":
    hex1 = "1c0111001f010100061a024b53535009181c"
    hex2 = "686974207468652062756c6c277320657965"
    expectedXOR = "746865206b696420646f6e277420706c6179"

    byteArray1 = hexToByteArray(hex1) 
    byteArray2 = hexToByteArray(hex2) 

    byteArrayXORResult = byteArrayXOR(byteArray1, byteArray2)
    hexResult = byteArrayToHex(byteArrayXORResult)
   
    print "expected: "+expectedXOR 
    print "actual:   "+hexResult

    assert(hexResult == expectedXOR)


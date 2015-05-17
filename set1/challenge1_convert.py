import re
import base64

intToBase64 = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z',
    26: 'a',
    27: 'b',
    28: 'c',
    29: 'd',
    30: 'e',
    31: 'f',
    32: 'g',
    33: 'h',
    34: 'i',
    35: 'j',
    36: 'k',
    37: 'l',
    38: 'm',
    39: 'n',
    40: 'o',
    41: 'p',
    42: 'q',
    43: 'r',
    44: 's',
    45: 't',
    46: 'u',
    47: 'v',
    48: 'w',
    49: 'x',
    50: 'y',
    51: 'z',
    52: '0',
    53: '1',
    54: '2',
    55: '3',
    56: '4',
    57: '5',
    58: '6',
    59: '7',
    60: '8',
    61: '9',
    62: '+',
    63: '/'
}


base64ToInt = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25,
    'a': 26,
    'b': 27,
    'c': 28,
    'd': 29,
    'e': 30,
    'f': 31,
    'g': 32,
    'h': 33,
    'i': 34,
    'j': 35,
    'k': 36,
    'l': 37,
    'm': 38,
    'n': 39,
    'o': 40,
    'p': 41,
    'q': 42,
    'r': 43,
    's': 44,
    't': 45,
    'u': 46,
    'v': 47,
    'w': 48,
    'x': 49,
    'y': 50,
    'z': 51,
    '0': 52,
    '1': 53,
    '2': 54,
    '3': 55,
    '4': 56,
    '5': 57,
    '6': 58,
    '7': 59,
    '8': 60,
    '9': 61,
    '+': 62,
    '/': 63
}

def hexToByteArray(hexString):
    hexList = re.findall('..',hexString)
    byteArray = []
    for hexChar in hexList:
        byteArray.append(int(hexChar, 16))
    return byteArray

def byteArrayToHex(byteArray):
    hexString = ""
    for b in byteArray:
        hexString += "%0.2x" % b

    return hexString

def bytesThreeTobase64Four(byteArray):
    # To binary
    assert(len(byteArray) <= 3)

    byteArrayNew = list(byteArray)

    while len(byteArrayNew) < 3:
        byteArrayNew.append(0)

    bAll = 0
    shifter = 0
    for b in reversed(byteArrayNew):
        bAll |= (b << shifter)
        shifter += 8
    
    # Get chunks of 6 bit numbers
    mask = int('111111', 2)

    # 0b10011 010110 000101 101110

    b64_1 = (bAll & (mask << 18)) >> 18
    b64_2 = (bAll & (mask << 12)) >> 12
    b64_3 = (bAll & (mask << 6)) >> 6
    b64_4 = bAll & mask

    paddingLength = 3-len(byteArray)

    if paddingLength == 1:
        s = intToBase64[b64_1]+intToBase64[b64_2]+intToBase64[b64_3]+'='
    elif paddingLength == 2:
        s = intToBase64[b64_1]+intToBase64[b64_2]+"=="
    else:
        s = intToBase64[b64_1]+intToBase64[b64_2]+intToBase64[b64_3]+intToBase64[b64_4] 
    return s

def breakIntoChunks(array, size):
    resultArray = []

    tempArray = []
    counter = 0
    for o in array:
            tempArray.append(o)
            counter +=1
            if counter % size == 0:
                resultArray.append(list(tempArray))
                tempArray = []

    if len(tempArray) > 0:
        resultArray.append(list(tempArray))
    return resultArray

def byteArrayToBase64(byteArray):
    # Break down into chunks of 3
    choppedOfBytesArray = breakIntoChunks(byteArray, 3)
    resultBase64 = ""
    for a in choppedOfBytesArray:
        s = bytesThreeTobase64Four(a)
        resultBase64 += s

    return resultBase64

def string64fourCharsToByteArray(str64):
    assert(len(str64) == 4)
    threeBytes = 0
    for b in str64:
        if b != '=':
            i = base64ToInt[b]
        else:
            i = 0
        threeBytes = i | (threeBytes << 6)

    byteArray = []

    if str64.count("=") < 1:
        byteArray.insert(0, threeBytes & 0xFF)
    if str64.count("=") < 2:
        byteArray.insert(0, (threeBytes >> 8) & 0xFF)

    byteArray.insert(0, (threeBytes >> 16) & 0xFF)

    return byteArray

def base64ToByteArray(base64String):
    byteArray = []

    stringInChunks = breakIntoChunks(base64String, 4)
    for string4Chars in stringInChunks:
        tempArray = string64fourCharsToByteArray(string4Chars)
        byteArray.extend(tempArray)

    return byteArray 

def hexToBase64(hexString):
    byteArray = hexToByteArray(hexString)
    return byteArrayToBase64(byteArray)


if __name__ == "__main__":
    hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expectedBase64String = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    print "Hex1: "+hexString

    base64String = hexToBase64(hexString)
    print base64String
    assert(expectedBase64String == base64String)

    byteArray = base64ToByteArray(expectedBase64String)
    hexString2 = byteArrayToHex(byteArray)
    print "Hex2: "+hexString2

    assert(hexString2 == hexString)

    assert(base64ToByteArray("TW==") == [77])
    assert(base64ToByteArray("TWF=") == [77, 97])
    assert(base64ToByteArray("TWFu") == [77, 97, 110]) 


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



def hexToByteArray(hexString):
    hexList = re.findall('..',hexString)
    byteArray = []
    for hexChar in hexList:
        byteArray.append(int(hexChar, 16))
    return byteArray

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


def hexToBase64(hexString):
    byteArray = hexToByteArray(hexString)
    return byteArrayToBase64(byteArray)


if __name__ == "__main__":
    hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expectedBase64String = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    print "Hex: "+hexString
    print "len Hex: "+str(len(hexString))

    base64String = hexToBase64(hexString)
    print base64String


## From http://en.wikipedia.org/wiki/Base64 - 'M', 'a', 'n'
#byteArray = [0x4d, 0x61, 0x6e]
#bytesThreeTobase64Four(byteArray)
#
## 'M', 'a'
#byteArray = [0x4d, 0x61]
#bytesThreeTobase64Four(byteArray)
#
## 'M'
#byteArray = [0x4d]
#bytesThreeTobase64Four(byteArray)

#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#breakIntoChunks(x, 3)

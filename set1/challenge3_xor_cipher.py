from challenge1_convert import hexToByteArray, byteArrayToHex
from challenge2_xor import byteArrayXOR
import operator

# From http://www.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
# Space is taken from http://www.macfreek.nl/memory/Letter_Distribution
letterFrequency = {
    ' ': 18,
    'E': 12.02,
    'T': 9.10,
    'A': 8.12,
    'O': 7.68,
    'I': 7.31,
    'N': 6.95,
    'S': 6.28,
    'R': 6.02,
    'H': 5.92,
    'D': 4.32,
    'L': 3.98,
    'U': 2.88,
    'C': 2.71,
    'M': 2.61,
    'F': 2.30,
    'Y': 2.11,
    'W': 2.09,
    'G': 2.03,
    'P': 1.82,
    'B': 1.49,
    'V': 1.11,
    'K': 0.69,
    'X': 0.17,
    'Q': 0.11,
    'J': 0.10,
    'Z': 0.07,
}

def englishTextScore(text):
    #print text
    uppercase = text.upper()
    #print lowercase
    byteArray = bytearray(uppercase)
    score = 0
    for b in byteArray:
        if chr(b) in letterFrequency:
            score += letterFrequency[chr(b)]
        elif b < 32 or b > 122:
            score -= 50
    return score

def getScoreList(encodedHex):
    encodedByteList = hexToByteArray(encodedHex)
    #print "bytearray as string: "
    #print str(bytearray(encodedByteList))

    cipherList = range(0, 256)
    scoreList = {}
    #cipherList = range(0, 10)
    for c in cipherList:
        hexStr = ("%02x"%c)*(len(encodedHex)/2)
        #print hexStr
        byteList = hexToByteArray(hexStr)
        xorResult = byteArrayXOR(encodedByteList, byteList)

        score = englishTextScore(str(bytearray(xorResult)))
        #print "score: %d" % score
        scoreList[c] = score

    # Print top 5 highest score
    highestValues = dict(sorted(scoreList.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
    return highestValues

def decodeString(encodedHex, b):
    encodedByteList = hexToByteArray(encodedHex)
    hexStr = ("%02x"%b)*(len(encodedHex)/2)
    byteList = hexToByteArray(hexStr)
    xorResult = byteArrayXOR(encodedByteList, byteList)
    return str(bytearray(xorResult))


if __name__ == "__main__":
    encodedHex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    encodedByteList = hexToByteArray(encodedHex)
    #print encodedHex


    highestValues = getScoreList(encodedHex)

    #print highestValues
    for key,value in highestValues.items():
        print "Key: 0x%02x, score: %d" % (key, value)
        decodedString = decodeString(encodedHex, key)
        print decodedString
        #hexStr = ("%02x"%key)*(len(encodedHex)/2)
        ##print hexStr
        #byteList = hexToByteArray(hexStr)
        #xorResult = byteArrayXOR(encodedByteList, byteList)
        #print str(bytearray(xorResult))



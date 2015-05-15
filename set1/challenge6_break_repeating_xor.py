from challenge2_xor import byteArrayXOR
from base64 import *
import operator

def stringEditDistance(str1, str2):
    assert(len(str1) == len(str2))

    b1 = bytearray(str1)
    b2 = bytearray(str2)

    return byteArrayEditDistance(b1, b2)
    
def byteArrayEditDistance(b1, b2):

    res = byteArrayXOR(b1, b2)
    distance = 0
    for b in res:
        distance += bin(b).count("1")

    return distance


if __name__ == "__main__":
    str1 = "this is a test"
    str2 = "wokka wokka!!!"

    editDistanceTest = stringEditDistance(str1, str2)
    assert(editDistanceTest == 37)
    print editDistanceTest


    f = open('6.txt', 'r')

    fileContent = ""
    for b64line in f:
        b64line = b64line.rstrip()
        fileContent += b64line
    f.close()

    print "WHole content:"
    print fileContent
    fileContentBytes = b64decode(fileContent)
   
    keySizeWithEditDistance = {} 
    for keySize in range(2, 41):
        part1 = fileContentBytes[0:keySize]
        part2 = fileContentBytes[keySize:keySize+keySize]
        #print "Keysize: "+str(keySize)

        editDistance = stringEditDistance(part1, part2)
        normalizedEditDistance = editDistance*1.0/keySize
        keySizeWithEditDistance[keySize] = normalizedEditDistance
        #print "Normalized edit distance: "+str(normalizedEditDistance)

    print keySizeWithEditDistance
    print min(keySizeWithEditDistance.iteritems(), key=operator.itemgetter(1))

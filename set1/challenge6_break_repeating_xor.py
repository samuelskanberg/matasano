from challenge2_xor import byteArrayXOR
from challenge5_repeating_xor import *
from challenge1_convert import * 
from challenge3_xor_cipher import *
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

    fileContentBytes = base64ToByteArray(fileContent)

    #expectedEncryptedMessage = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    #fileContentBytes = hexToByteArray(expectedEncryptedMessage)
   
    keySizeWithEditDistance = {} 
    for keySize in range(2, 41):
        part1 = fileContentBytes[0:keySize]
        part2 = fileContentBytes[keySize:keySize+keySize]

        editDistance = stringEditDistance(part1, part2)
        normalizedEditDistance = editDistance*1.0/keySize
        keySizeWithEditDistance[keySize] = normalizedEditDistance

    sortedKeySizeWithEditDistance = sorted(keySizeWithEditDistance.items(), key=operator.itemgetter(1))

    for keySize, editDistance in sortedKeySizeWithEditDistance:
        print "key: %d, editDistance: %f" % (keySize, editDistance)

    keyWithNormalizedScore = {}

    for keySize, editDistance in sortedKeySizeWithEditDistance:
        print "------------------------"
        print "key: %d, editDistance: %f" % (keySize, editDistance)
        print "------------------------"

        fileContentInChunks = breakIntoChunks(fileContentBytes, keySize)

        foundKey = []

        transposedBlocks = []
        for i in range(0, keySize):
            tempBlock = []
            for block in fileContentInChunks:
                if i < len(block):
                    tempBlock.append(block[i])
            transposedBlocks.append(tempBlock)

        totalScore = 0
        # Break each block as a single char XOR
        for block in transposedBlocks:
            scoreList = getScoreListBytes(block)
            highestValues = sorted(scoreList.items(), key=operator.itemgetter(1), reverse=True)[:5]
            foundKey.append(highestValues[0][0])
            totalScore += highestValues[0][1]

        print "Totaltscore: %f" % totalScore
        normalizedTotalScore = totalScore*1.0/keySize
        print "Normalized totaltscore: %f" % normalizedTotalScore

        foundKeyString = bytearray(foundKey)

        keyWithNormalizedScore[str(foundKeyString)] = normalizedTotalScore
        print "Found key string: "+foundKeyString
        if normalizedTotalScore > 0:
            decoded = repeatingXORBytes(bytearray(fileContentBytes), foundKeyString)
            print "decoded: "+bytearray(decoded)


    print keyWithNormalizedScore

    sortedKeysWithNormalizedScore = sorted(keyWithNormalizedScore.items(), key=operator.itemgetter(1), reverse=True)
    print "-------------------------"
    print "DONE!"
    print "-------------------------"

    for item in sortedKeysWithNormalizedScore:
        print "Key: %s, score: %f" % (item[0], item[1])
        if item[1] > 0:
            print "----------------------"
            print "Decoding"
            print "----------------------"
            decoded = repeatingXORBytes(bytearray(fileContentBytes), bytearray(item[0]))
            print bytearray(decoded)
            print "----------------------"



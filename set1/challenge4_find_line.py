from challenge3_xor_cipher import getScoreList, decodeString
import operator

f = open('4.txt', 'r')

for line in f:
    line = line.rstrip()
    #print "----- LINE ------"
    #print line
    highestValues = getScoreList(line)
    #print highestValues
    maxValueKey = max(highestValues.iteritems(), key=operator.itemgetter(1))[0]
    score = highestValues[maxValueKey]

    if score > 3:
        decodedString = decodeString(line, maxValueKey)
        print "Key: %d, score: %f" % (maxValueKey, score)
        print decodedString
        print ""
    #break


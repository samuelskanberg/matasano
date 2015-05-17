from challenge1_convert import byteArrayToHex, breakIntoChunks
from challenge2_xor import byteArrayXOR

def repeatingXORBytes(message, key):
    chunkedUp = breakIntoChunks(message, len(key))
    resultList = []
    for smallArray in chunkedUp:
        # Last array may not be as long as the key
        result = byteArrayXOR(smallArray, key[:len(smallArray)])
        resultList.extend(result)
    return resultList

def repeatingXORString(message, key):
    messageByteArray = bytearray(message)
    keyByteArray = bytearray(key)
    result = repeatingXORBytes(messageByteArray, keyByteArray)
    return byteArrayToHex(result)

if __name__ == "__main__":
    message = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

    expectedEncryptedMessage = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

    key = "ICE"

    result = repeatingXORString(message, key)
    print result
    print expectedEncryptedMessage 

    assert(result == expectedEncryptedMessage)

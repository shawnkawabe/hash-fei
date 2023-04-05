import hashlib
import codecs

f = codecs.open("list.txt", "r", "utf-8")
text = f.read()
texts = text.split("\n")
texts_to_decode = {}

for key in texts:
    keysToTexts = key.split('" - ')
    keysToTexts[0] = keysToTexts[0].replace('"', '')
    valuesToTexts = keysToTexts[1].split(' - ')
    texts_to_decode[keysToTexts[0]] = [valuesToTexts[0],valuesToTexts[1].strip()]

for key in texts_to_decode.keys():

    string = texts_to_decode[key][1]
    
    byteString = key.encode('utf-8')

    shaHash = hashlib.new('sha256')
    md5Hash = hashlib.new('md5')

    shaHash.update(byteString)
    md5Hash.update(byteString)

    sha256HashedString = shaHash.hexdigest()
    md5HashedString = md5Hash.hexdigest()

    if sha256HashedString == texts_to_decode[key][0] and md5HashedString == texts_to_decode[key][1]:
        print(f'key => {key}\n')
        print(f'sha256 => {texts_to_decode[key][0]}\n')
        print(f'md5 => {texts_to_decode[key][1]}\n')
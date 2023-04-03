# import hashlib

# mystring = "A primeira das instituições criadas pelo Pe. Roberto Sabóia de Medeiros foi a antiga Escola Superior de Administração de Negócios de São Paulo - ESAN/SP."

# validateSHAHash = "d24de3ec3835115c576a55188a31761b73af93ed2c45a171c810bb66b24b08f9"

# validateMD5Hash = "c850e1a34a6ed572e0758ccd9c615bda"

# byteString = mystring.encode('utf-8')

# shaHash = hashlib.new('sha256')

# md5Hash = hashlib.new('md5')

# shaHash.update(byteString)

# md5Hash.update(byteString)

# if shaHash.hexdigest() == validateSHAHash:
#     print('Igual SHA-256')

# if md5Hash.hexdigest() == validateMD5Hash:
#     print('Igual MD5')

f = open("list.txt", "r")
text = f.read()
texts = text.split("\n")
texts_to_decode = {}
for key in texts:
    keysToTexts = key.split('" - ')
    keysToTexts[0] = keysToTexts[0].replace('"', '')
    valuesToTexts = keysToTexts[1].split(' - ')
    print(keysToTexts)
    print(valuesToTexts)
    texts_to_decode[keysToTexts[0]] = [valuesToTexts[0],valuesToTexts[1]]

for keys in texts_to_decode.keys():
    print(f'key {keys}\n')
    print(f'value {texts_to_decode[keys]}\n')

print(texts)
print(" -------- \n")
print(texts_to_decode)
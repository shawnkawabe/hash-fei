import hashlib
import codecs
import pandas as pd
import dataframe_image as dfi

f = codecs.open("list.txt", "r", "utf-8")
text = f.read()
texts = text.split("\n")
texts_to_decode = {}
table = {}
strings = []
sha256Hashes = []
md5Hashes = []
status = []

for key in texts:
    keysToTexts = key.split('" - ')
    keysToTexts[0] = keysToTexts[0].replace('"', '')
    valuesToTexts = keysToTexts[1].split(' - ')
    texts_to_decode[keysToTexts[0]] = [valuesToTexts[0],valuesToTexts[1].strip()]

for key in texts_to_decode.keys():
    
    byteString = key.encode('utf-8')

    shaHash = hashlib.new('sha256')
    md5Hash = hashlib.new('md5')

    shaHash.update(byteString)
    md5Hash.update(byteString)

    sha256HashedString = shaHash.hexdigest()
    md5HashedString = md5Hash.hexdigest()

    if (
        sha256HashedString == texts_to_decode[key][0] and
        md5HashedString == texts_to_decode[key][1]
    ):
        # print(f'key => {key}\n')
        # print(f'sha256 => {texts_to_decode[key][0]}\n')
        # print(f'md5 => {texts_to_decode[key][1]}\n')
        strings.append(key)
        sha256Hashes.append(texts_to_decode[key][0])
        md5Hashes.append(texts_to_decode[key][1])
        status.append('Verdadeira')
    else:
        strings.append(key)
        sha256Hashes.append(texts_to_decode[key][0])
        md5Hashes.append(texts_to_decode[key][1])
        status.append('Falsa')

table['Frase'] = strings
table['SHA 256 Gerado'] = sha256Hashes
table['MD5 gerado'] = md5Hashes
table['Status'] = status

# print(table)

df = pd.DataFrame(table)

df.style.hide(axis='index')
df.style.set_table_styles(
    [
        {
            'selector': 'th',
            'props': [
                        ('background', 'green'),
                        ('text-align', 'center')
                    ]
        }
    ]
)

#only use if in unix like systems
dfi.export(df,"mytable.png")
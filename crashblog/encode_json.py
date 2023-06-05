import json
from json import JSONEncoder
import codecs


encodings = ['utf-8', 'utf-16', 'latin-1', 'ascii']

for encoding in encodings:
    try:
        with open('crashblog/datadump.json', 'r', encoding=encoding) as file:
            data = file.read()
        print(f"Successful decoding with {encoding}")
        break
    except UnicodeDecodeError:
        print(f"Decoding error with {encoding}")



with open('crashblog/datadump.json', 'r', encoding='utf_16') as file:
    data = file.read()

# Convert the encoding to UTF-8
converted_data = data.encode('utf_16').decode('utf-8')

# Write the converted data to a new file
with codecs.open('crashblog/datadump.json', 'w', encoding='utf-8') as file:
    file.write(converted_data.decode('utf-16'))


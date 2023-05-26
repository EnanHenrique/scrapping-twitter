import json

with open('./scrapper_soybean_twitter.json', encoding='utf-8') as fh:
    data = json.load(fh)

print(data)

# TODO: usar analisador léxico para tratar as informações

import json

with open('dom_info.json', 'r') as f:
    data = json.load(f)

for el in data:
    if 4500 <= el['y'] < 6000 and el['text'].strip():
        if el['tag'] not in ['div', 'section', 'main', 'body']:
            print(f"y: {el['y']}, x: {el['x']}, tag: {el['tag']}, text: {el['text'][:50]}, size: {el['fontSize']}, color: {el['color']}")


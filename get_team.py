import requests

images = [
    'https://framerusercontent.com/images/11KSGbIZoRSg4pjdnUoif6MKHI.svg',
    'https://framerusercontent.com/images/3EyMoo8zK86ZDQzERCMGVWUOLA.jpg',
    'https://framerusercontent.com/images/3ub2NQCNZAZS3f8ApGQgExDI0Ao.jpg',
    'https://framerusercontent.com/images/5nBoafEAYXgWjDvigY8paH17c.jpg',
    'https://framerusercontent.com/images/9ZNqiGoL8UCtjQBgrIlQyvrI4.jpg',
    'https://framerusercontent.com/images/EhqqPz44iYpL1sYmPUiMb4PrM.jpg',
    'https://framerusercontent.com/images/R3hvELrpigktryfqc2B16nTUA94.jpg',
    'https://framerusercontent.com/images/SjQeRS3WsuLW2tISmEI0S1yeGTA.jpg',
    'https://framerusercontent.com/images/ZUrYFSjw34S5aoakErg7x52HLg.jpg',
    'https://framerusercontent.com/images/f22WJf9yNd0BO2Obq9Kn7Fb9RM.jpg',
    'https://framerusercontent.com/images/lW0gFXBltpg3jFjCrbeimGiyTI.jpg',
    'https://framerusercontent.com/images/n897NqofjLqKqeMndhf0j5l5gY0.jpg',
    'https://framerusercontent.com/images/rMviwDhwuq6NpD6BlBA8qDM24ms.jpg'
]

import os
ASSETS_DIR = 'assets/images'
os.makedirs(ASSETS_DIR, exist_ok=True)

for url in images:
    filename = url.split('/')[-1]
    filepath = os.path.join(ASSETS_DIR, filename)
    if not os.path.exists(filepath):
        try:
            r = requests.get(url)
            with open(filepath, 'wb') as f:
                f.write(r.content)
        except Exception as e:
            pass

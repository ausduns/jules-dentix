import os
import requests

ASSETS_DIR = 'assets/images'
os.makedirs(ASSETS_DIR, exist_ok=True)

images = [
    'https://framerusercontent.com/images/cGJTFi5lidEhnDZg7TnGv2ugo.jpg',
    'https://framerusercontent.com/images/gfKDEeDTH0gNXnMcLZHSxVUqFKI.png',
    'https://framerusercontent.com/images/4HytcC5SH5wppXFXnFHsYwunVHM.png',
    'https://framerusercontent.com/images/kLPW7o56Zt8gw0D96XHDliaFNM.png',
    'https://framerusercontent.com/images/iYjcCRZeo67UEB1OUxgbZyT2ig.png',
    'https://framerusercontent.com/images/xBinvsBPHdrJhiPbW9akV8SeqzQ.jpg',
    'https://framerusercontent.com/images/7WvH9IVZN7TSclUrg1hD8pb3CA.jpg',
    'https://framerusercontent.com/images/ieen5xkYGhBCNANZel7RzqQvcA.jpg',
    'https://framerusercontent.com/images/3umss5aXSuyxhV3HlNsoyzWV2o.jpg',
    'https://framerusercontent.com/images/j03xXGomRywRGkD3sLeU8B4wCE.jpg',
    'https://framerusercontent.com/images/1gXLHzwx9XdhUodHBIuXNEqNhUo.png',
    'https://framerusercontent.com/images/6LBROq6GOOys2qu2z60WDoz6AA.jpg',
    'https://framerusercontent.com/images/e4TaBKcmMuzFewiAC6EuA6JNo.jpg',
    'https://framerusercontent.com/images/P6pXMPp8EoyN3b5qRDTR07iCig.jpg',
    'https://framerusercontent.com/images/CpXHfDkfgNXs7CORGHQB6mzGBII.jpg',
    'https://framerusercontent.com/images/yJPCsqrs1i5cOKZ17YBfalZLmnk.jpg',
    'https://framerusercontent.com/images/qRIJVKyrAUrQLBD83Uo4eOXd2Fg.jpg',
    'https://framerusercontent.com/images/rzlzHy3I6STZ9IgJLALZ6E7wnY.jpg',
    'https://framerusercontent.com/images/6tTbkXggWgQCAJ4DO2QEdXXmgM.svg'
]

for url in images:
    filename = url.split('/')[-1]
    filepath = os.path.join(ASSETS_DIR, filename)
    if not os.path.exists(filepath):
        print(f"Downloading {filename}...")
        try:
            r = requests.get(url)
            with open(filepath, 'wb') as f:
                f.write(r.content)
        except Exception as e:
            print(f"Failed to download {filename}: {e}")

print("Assets downloaded.")

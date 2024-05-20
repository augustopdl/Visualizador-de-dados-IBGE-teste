from os import listdir, makedirs, rename
from os.path import isdir
from pathlib import Path

downloads_path = str(Path.home() / "Downloads")

for file in listdir(downloads_path)[:-1]:
    aux1 = file.split(' - ')
    aux2 = aux1[1]
    aux3 = aux1[-1]
    aux3 = aux3.removesuffix('.xlsx')

    if not isdir(f'data/{aux3}'):
        makedirs(f'data/{aux3}')

    rename(
        fr'C:\Users\diogo\Downloads\{file}',
        fr'data/{aux3}/{aux2}.xlsx'
    )

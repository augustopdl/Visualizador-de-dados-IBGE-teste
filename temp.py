from os import listdir, makedirs, rename
from os.path import isdir

for file in listdir(r'C:\Users\diogo\Downloads')[:-1]:
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

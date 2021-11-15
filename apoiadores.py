from os import listdir
from pathlib import Path
from splitty import clear_list_strings, chunks

OUTPUT_FORMAT = '{0:20} {1:20} {2:20} {3:20}'
coluns = 4


def get_last_csv(path):
    files = [f'./{path}/{file}' for file in listdir(f'./{path}')]
    return sorted(files, key=lambda x: Path(x).stat().st_mtime)[-1]


def apoiase():
    with open(get_last_csv('apoiase')) as text:
        base = clear_list_strings(text.read().split('\n'))
        names = [
            x.split(',')[0].replace("\"", "") for x in base[1:]
            if 'Ativo' in x
        ]
        names.append('Renan Moura')
        return names


def picpay():
    with open(get_last_csv('picpay'), encoding='cp1252') as text:
        base = clear_list_strings(text.read().split('\n'))
        names = [
            x.split(',')[0].replace("\"", "") for x in base[1:]
        ]
        return names


def clube_de_canais():
    with open('youtube/clube.txt') as text:
        base = clear_list_strings(text.readlines())
        nomes = [nome[0] for nome in chunks(base, 5)]
        return nomes


def parse_names(lista_de_nomes):
    nomes = [
        f'{x.split()[0].capitalize()} {x.split()[-1].capitalize()}'
        for x in lista_de_nomes
    ]
    return sorted(set(nomes))


print(', '.join(parse_names(apoiase() + picpay() + clube_de_canais())))

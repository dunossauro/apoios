from itertools import chain
from json import loads
from locale import LC_ALL, setlocale, strxfrm
from os import listdir
from pathlib import Path

from splitty import clear_list_strings

setlocale(LC_ALL, '')


def get_last_csv(path):
    files = [f'./{path}/{file}' for file in listdir(f'./{path}')]
    return sorted(files, key=lambda x: Path(x).stat().st_mtime)[-1]


def apoiase():
    with open(get_last_csv('apoiase')) as apoiase_csv:
        apoiase_data = clear_list_strings(apoiase_csv.readlines())
        names = (
            x.split(',')[1].replace('"', '')
            for x in apoiase_data[1:]
            if 'Ativo' in x
        )
        return names


def clube_de_canais():
    with open(get_last_csv('youtube')) as clube_txt:
        youtube_data = clear_list_strings(clube_txt.readlines())
        names = [x.split(',')[0] for x in youtube_data[1:]]
        # O filtro filtra canais excluídos
        return filter(None, names)


def parse_name(name):
    splited_name = name.split()
    first_name = splited_name[0]
    last_name = splited_name[-1]

    if first_name == last_name:
        return first_name.capitalize()

    return f'{first_name.capitalize()} {last_name.capitalize()}'


def parse_names(*lista_de_nomes):
    nomes = (parse_name(name) for name in chain(*lista_de_nomes))
    return sorted(set(nomes), key=strxfrm)


def extra():
    return loads(Path('extras.json').read_text())['pessoas']


print(', '.join(parse_names(apoiase(), clube_de_canais(), extra())))

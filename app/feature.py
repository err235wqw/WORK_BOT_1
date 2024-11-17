from random import randint

import app.sourse as srs

phrases_dict = {
    1: srs.phrases_voobrajenie,
    2: srs.phrases_neobhodimost,
    3: srs.phrases_osoznanie,
    4: srs.phrases_slova_sviazki,
    5: srs.phrases_psevdologika,
    6: srs.phrases_otricanie,
    7: srs.phrases_dopushenie,
    8: srs.phrases_smiagchiteli,
    9: srs.phrases_akcellerators,
    10: srs.phrases_predvkushenie

}


async def generate_list_of_prases(list_of_numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) -> list:
    list_of_phrases = []
    for i in list_of_numbers:
        list_of_phrases.extend(phrases_dict.get(i, []))
    return list_of_phrases


async def generate_random_number(n: int = 0) -> int:
    rnd = randint(0, n)
    return rnd
from random import randint, getrandbits

import app.sourse as srs

phrases_dict_standart = {
    1: srs.phrases_voobrajenie_col1,
    2: srs.phrases_neobhodimost_col1,
    3: srs.phrases_osoznanie_col1,
    4: srs.phrases_slova_sviazki_col1,
    5: srs.phrases_psevdologika_col1,
    6: srs.phrases_otricanie_col1,
    7: srs.phrases_dopushenie_col1,
    8: srs.phrases_smiagchiteli_col1,
    9: srs.phrases_akcellerators_col1,
    10: srs.phrases_predvkushenie_col1,
}
phrases_dict_da = {
    1:srs.phrases_neobhodimost_col2,
    2:srs.phrases_voprosi_realnosti_col2,
    3:srs.phrases_voprosi_suchestvovania_col2,
    4:srs.phrases_istoric_voprosi_col2,
    5:srs.phrases_uslovnie_voprosi_col2,
    6:srs.phrases_voprosi_buduchego_col2,
    7:srs.phrases_voprosi_vosmozhnosti_col2,
    8:srs.phrases_voprosi_voobrazhenia_col2,
    9:srs.phrases_voprosi_deistvia_col2,
    10:srs.phrases_voprosi_identichnosti_col2,
}

async def generate_list_of_prases(list_of_numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], Da: bool = False) -> list:
    list_of_phrases = []
    for i in list_of_numbers:
        if Da:
            list_of_phrases.extend(phrases_dict_da.get(i, []))
        else:
            list_of_phrases.extend(phrases_dict_standart.get(i, []))
    return list_of_phrases


async def generate_random_number(n: int = 0) -> int:
    rnd = randint(0, n)
    return rnd

async def generate_add() -> str:
    if not not random.getrandbits(1):
        return srs.advert_phrases[randint(0,len(srs.advert_phrases))-1]
    else:
        return ''
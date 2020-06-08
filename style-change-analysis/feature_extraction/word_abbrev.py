import re

def get_abbrev_list():
    abbrev_list = []
    with open('feature_extraction/external_data/abbrev.txt','r',encoding='utf-8')as fin:
        lines=fin.read().splitlines()
        for line in lines:
            if not line.startswith('-'):
                abbrev_list.append(line)
    return abbrev_list


def mostly_uppercased_starts(text: str):
    abbrev_list = get_abbrev_list()
    accured_abbrev_count = 0
    uppercased_starts_count = 0
    for abbrev in abbrev_list:
        iter = re.finditer(abbrev, text)
        indices = [m.start(0) for m in iter]
        for index in indices:
            accured_abbrev_count += 1
            uppercased_starts_count += text[index].isupper()
    uppercased_abbrev_portion = uppercased_starts_count / accured_abbrev_count if accured_abbrev_count != 0 else 0.0
    return [round(uppercased_abbrev_portion)]


def mostly_lowercased_starts(text: str):
    abbrev_list = get_abbrev_list()
    accured_abbrev_count = 0
    lowercased_starts_count = 0
    for abbrev in abbrev_list:
        iter = re.findall(abbrev, text)

        indices = [m.start(0) for m in iter]
        for index in indices:
            accured_abbrev_count += 1
            lowercased_starts_count += text[index].islower()
    uppercased_abbrev_portion = lowercased_starts_count / accured_abbrev_count if accured_abbrev_count != 0 else 0.0
    return [round(uppercased_abbrev_portion)]










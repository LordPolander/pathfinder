import requests
from bs4 import BeautifulSoup


def preprequest(link):
    page = requests.get(link)
    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def letterfy(list):  # delete â\x80\x94 and replace with ''
    newlist = []
    for i in list:
        if i == 'â\x80\x94':
            i = '-'
        if i == 'Â\xa0':
            i = '-'
        newlist.append(i)
    return newlist


def find_tabs(soup):
    tab = soup.find_all('td')
    tabs = 1
    while True:
        if tab[tabs].text == '2nd':  # count from lvl1 to lvl2 how many tabs in between
            break
        else:
            tabs += 1
    return tabs


def find_stats(soup, character_level):
    tab = soup.find_all('td')
    tabs = find_tabs(soup)
    character_stats = []

    _start = (character_level - 1) * tabs
    for i, x in enumerate(range(20 * tabs),
                          start=_start):  # replace tabs with 6 if you get trouble? i forgot what it does
        a = str(tab[i].text)
        # print(a)
        character_stats.append(a)
        if i > (_start + tabs) - 2:  # -2 just works, do not touch
            break
    # your stats proportionate to lvl get saved in stats as a list
    character_stats.pop(5)  # delete feat object from list, objects after feats are spells
    # print(character_stats)
    character_stats = letterfy(character_stats)

    return character_stats


def find_spells(soup, character_level):
    character_stats = find_stats(soup, character_level)
    tab = soup.find_all('th')
    tabs = find_tabs(soup)
    character_spells = []
    _start = 1
    for i, x in enumerate(range(tabs), start=_start):  # replace tabs with 6 if you get trouble? i forgot what it does
        if i >= 7:
            a = str(tab[i].text)  # level of spell(s)
            a = a[0]  # keep only first character, aka level of spells
            character_spells.append('{}{}{}'.format(a, '#', character_stats[i - 2]))
    return character_spells


def find_feats(soup, character_level):
    tab = soup.find_all('td')
    tabs = find_tabs(soup)
    character_feats = []
    special = tabs - 6
    for i in range(character_level * tabs):
        feat = str(tab[i].text)
        if special == tabs - 1:
            # print(special,'t',tabs,feat)
            character_feats.append(feat)
            special = 0
        else:
            special += 1
    # print(character_feats)
    return letterfy(character_feats)


def find_skills(soup):
    character_skills = []
    skill = soup.find_all('p')
    for skills in skill:
        if 'class skills are' in str(skills):
            skills = skills.text
            skills = str(skills.replace('[', ''))
            skills = str(skills.replace(']', ''))
            skills = str(skills.replace('are', ','))
            skills = str(skills.replace('.', ','))
            skills = str(skills.split(','))
            skills = skills.split(',')
            skills = skills[1:-1]  # remove first obj and last obj
            # print(skills)
            for i in range(0, len(skills)):
                a = skills[i]
                if i != len(skills) - 1:  # if not last obj
                    skills[i] = ''.join(a[2:-6])
                else:  # if last obj
                    skills[i] = ''.join(a[6:-6])  # remove 'and' from last obj
                # print(skills[i])
            # print(skills)
            character_skills = skills
    # print(character_skills)
    return letterfy(character_skills)

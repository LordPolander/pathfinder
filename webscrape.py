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
        if i == '&nbsp;':
            i = '-'
        newlist.append(i)
    return newlist


def find_tabs(soup):
    tab = soup.find_all('td')
    tabs = 0

    if len(tab[0].text) >= 20:  # unchained rogue has an extra td, which is getting removed here
        tab.pop(0)

    while True:
        # print(tabs,'aaaaaaaaaaaaaaaaaaaa', tab[tabs].text)
        if tab[tabs].text == '2nd':  # count from lvl1 to lvl2 how many tabs in between
            break
        else:
            tabs += 1
    return tabs


def find_class(soup):
    tab = soup.find('h1')
    tabs = tab.text
    return tabs


def find_stats(soup, character_level):
    tab = soup.find_all('td')

    if len(tab[0].text) >= 20:  # unchained rogue has an extra td, which is getting removed here
        tab.pop(0)

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

    if len(tab[0].text) >= 20:  # unchained rogue has an extra td, which is getting removed here
        tab.pop(0)

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

    character_feats = letterfy(character_feats)

    def remove_empty_feats(character_feats):
        new_character_feats = []
        for feat in character_feats:
            if feat == '-':
                pass
            else:
                new_character_feats.append(feat)
        return new_character_feats

    character_feats = remove_empty_feats(character_feats)

    return character_feats


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


def find_skill_points(soup):
    tab = soup.find_all('p')
    for i in tab:  # check all 'p'
        # messy, finds hd or hit dice, whatever it is called
        a = i.text.lower()
        if 'skill ranks per level:' in a:  # find hit die
            # remove text and only keep d(number)
            a = a
            a = a.replace('skill ranks per level:', '')
            # print(a)
            return a


def find_hd(soup):
    tab = soup.find_all('p')
    for i in tab:  # check all 'p'
        # messy, finds hd or hit dice, whatever it is called
        if 'Hit Die:' in i.text or 'Hit Dice:' in i.text or 'HD: ' in i.text:  # find hit die
            # remove text and only keep d(number)
            a = i.text
            a = a.replace('Hit Die:', '')
            a = a.replace('Hit Dice:', '')
            a = a.replace('HD:', '')
            a = a.replace('.', '')
            return a

def find_data(soup,character_level):
    data = [find_class(soup),
            find_stats(soup, character_level),
            find_skills(soup),
            find_skill_points(soup),
            find_feats(soup, character_level),
            find_spells(soup, character_level),
            find_hd(soup)]
    return data



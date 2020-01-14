import webscrape
from time import sleep
import ods_editor

# https://www.d20pfsrd.com/classes/core-classes/cleric/

print('Ooga booga, POLSKA®')


def create_sheet(character_class_link, character_level):
    character_class_page = webscrape.preprequest(character_class_link)  # send link for data

    character_class = webscrape.find_class(character_class_page)
    character_stats = webscrape.find_stats(character_class_page, character_level)  # find in page; level
    character_spells = webscrape.find_spells(character_class_page, character_level)
    character_skills = webscrape.find_skills(character_class_page)  # find in page
    character_skill_points = webscrape.find_skill_points(character_class_page)  # find in page
    character_feats = webscrape.find_feats(character_class_page, character_level)  # find in page; from 1 to level
    character_hd = webscrape.find_hd(character_class_page)  # find HD

    character_stats = character_stats[0:5]  # get rid of spells if there are any

    print('class        :', character_class)
    print('stats        :', character_stats)
    print('skills       :', character_skills)
    print('skill points :', character_skill_points)
    print('feats        :', character_feats)
    print('spells       :', character_spells)
    print('HD           :', character_hd)

    edit = True  # enable editing of ods
    file = 'excel_path_sheet.ods'
    if edit:
        ods_editor.edit(file,
                        character_class,
                        character_stats,
                        character_skills,
                        character_skill_points,
                        character_feats,
                        character_spells,
                        character_hd)
    print('ooga booga finished')


if __name__ == '__main__':

    from pyautogui import *

    debug = True

    if debug:
        character_level = int(10)
        character_class_link = str('https://www.d20pfsrd.com/classes/core-classes/wizard/')
    else:
        character_level = prompt(text='Enter the level of your class',
                                 title='Pathinator',
                                 default='1')

        character_class_link = prompt(text='Enter the link of your class',
                                      title='Pathinator',
                                      default='https://www.d20pfsrd.com/')

    create_sheet(character_class_link, int(character_level))

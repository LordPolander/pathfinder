import webscrape
from time import sleep
import ods_editor

# https://www.d20pfsrd.com/classes/core-classes/cleric/

print('Ooga booga, POLSKA®')


def create_sheet(character_class_link, character_level):
    character_class_page = webscrape.preprequest(character_class_link)  # send link for data

    character_data = webscrape.find_data(character_class_page,character_level)

    def print_data():
        print('class        :', character_data[0])
        print('stats        :', character_data[1][0:5])
        print('skills       :', character_data[2])
        print('skill points :', character_data[3])
        print('feats        :', character_data[4])
        print('spells       :', character_data[5])
        print('HD           :', character_data[6])
        return
    print_data()

    edit = True  # enable editing of ods
    file = 'excel_path_sheet.ods'
    if edit:
        ods_editor.edit(file, character_data)
    print('ooga booga finished')


if __name__ == '__main__':

    from pyautogui import *

    debug = False

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

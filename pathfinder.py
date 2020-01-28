import webscrape
import ods_editor
from character import Character

# this link is for testing
# https://www.d20pfsrd.com/classes/core-classes/cleric/

print('Ooga booga, POLSKA®')


def create_sheet(character_class_link, character_level):
    character_class_page = webscrape.preprequest(character_class_link)  # send link for data

    character_data = webscrape.find_data(character_class_page,character_level)

    for i in range(len(character_data)):
        if type(character_data[i]) == str:
            character_data[i] = character_data[i].strip()

    character_class_name = character_data[0]
    character_stats = character_data[1][0:5]
    character_skills = character_data[2]
    character_skill_points = character_data[3]
    character_feats = character_data[4]
    character_spells = character_data[5]
    character_hd = character_data[6]

    character = Character(character_data)
    print(character.class_name)

    def print_data():
        print('class        :', character_class_name)
        print('stats        :', character_stats)
        print('skills       :', character_skills)
        print('skill points :', character_skill_points)
        print('feats        :', character_feats)
        print('spells       :', character_spells)
        print('HD           :', character_hd)
        return
    print_data()

    edit = True  # enable editing of ods
    file = 'excel_path_sheet.ods'
    if edit:
        ods_editor.edit(file, character)

    print('ooga booga finished')

if __name__ == '__main__':

    debug = True

    if debug:
        character_level = int(10)
        character_class_link = str('https://www.d20pfsrd.com/classes/core-classes/wizard/')
    else:
        character_level = input('enter level: ')

        character_class_link = input('enter link: ')

    create_sheet(character_class_link, int(character_level))

    input("Press Enter to exit...")

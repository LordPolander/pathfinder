from ezodf import opendoc
from pathlib import Path


def update_pos(pos, x=0, y=0):
    ver = ''
    hor = ''
    for char in pos:
        if not char.isdigit():
            hor = hor + char
        else:
            ver = ver + char

    return f'{chr(ord(hor) + x)}{int(ver) + y}'


def edit(file_name, character):
    doc = opendoc(file_name)

    def edit_onecell(character_data, str_cell, sheet):
        pos = update_pos(str_cell)
        sheet = doc.sheets[sheet]
        cell = sheet[pos]
        cell.set_value(character_data)
        return

    def edit_stats(character_stats):
        pos = update_pos('W22')
        sheet = doc.sheets[0]
        cell = sheet[pos]

        level = character_stats[0]
        cell.set_value(level[:-2])  # delete characters after number

        # keep only first from attack mod
        attack_mod = character_stats[1]
        attack_mod = attack_mod.split('/')  # split by /
        attack_mod = attack_mod[0]  # take first mod from list
        attack_mod = attack_mod.replace('+', '')  # delete + from the mod

        edit_onecell(attack_mod, 'Q22', 0)
        edit_onecell(character_stats[2], 'T22', 0)
        edit_onecell(character_stats[3], 'U22', 0)
        edit_onecell(character_stats[4], 'V22', 0)
        return

    def edit_skills(character_skills):
        pos = update_pos('P38')
        sheet = doc.sheets[0]
        # 34
        while True:  # check mark skills you are proficient in, skipping knowledges
            for skill in character_skills:
                cell = sheet[pos]
                cellvalue = cell.value
                if type(cellvalue) == str:
                    cellvalue = cellvalue.replace('*', '')
                    cellvalue = cellvalue.replace(':', '')

                skill = skill.upper()
                if str(cellvalue) in str(skill):
                    sheet[update_pos(pos, -1)].set_value(1)
            if pos == 'P102':  # limit
                break
            pos = update_pos(pos, 0, 2)  # update vertical by 2

        knowledges = []  # create a new list for knowledges
        for skill in character_skills:
            skill = skill.upper()
            if 'KNOWLEDGE ' in str(skill):  # format
                a = skill
                a = a.replace('KNOWLEDGE', '')
                a = a.replace('(', '')
                a = a.replace(')', '')
                a = a.replace(' ', '')
                knowledges.append(a)
        pos = update_pos('Q64')
        for knowledge in knowledges:
            sheet[pos].set_value(knowledge)  # set in what knowledge (Q)
            sheet[update_pos(pos, -2)].set_value(1)  # mark knowledge (O)
            pos = update_pos(pos, 0, 2)
        return

    def edit_feats(character_feats):
        pos = update_pos('A72')
        for feat in character_feats:
            sheet = doc.sheets[0]
            cell = sheet[pos]
            cell.set_value(feat)
            # print('{}{}'.format(hor, ver), '---', feat)

            if pos == 'A100':
                pos = update_pos('H72')
            else:
                pos = update_pos(pos, 0, 2)
        return

    

    def edit_spells(character_spells, character_class, character_stats):
        if len(character_spells) > 0:
            # set spells class name
            edit_onecell(character_class, 'B3', 2)
            # set class level
            edit_onecell(character_stats[0][:-2], 'G3', 2)

            # set spells
            # D8-26 by 2
            sheet = doc.sheets[2]
            pos='D8'
            updater = 2  # by how much to increase 
            
            start_spell_level = int(character_spells[0][0])
            if start_spell_level == 1:
                pos = update_pos(pos, 0, updater)

            for spell in character_spells:
                
                cell = sheet[pos]
                cell.set_value(spell[2])
                pos = update_pos(pos, 0, updater)

            
        return

    edit_onecell(character.class_name, 'N22', 0)  # set class name
    edit_stats(character.stats)
    edit_skills(character.skills)
    edit_onecell(character.skill_points, 'M4', 0)  # set class skill points
    edit_feats(character.feats)
    edit_spells(character.spells, character.class_name, character.stats)
    edit_onecell(character.hd, 'M22', 0)  # set class hit die

    def save(save_file):
        i = 0
        while True:
            if Path(save_file + str(i) + '.ods').is_file():
                i += 1
            else:
                doc.saveas(save_file + str(i) + '.ods')
                print('')
                print('file saved as:', save_file + str(i) + '.ods')
                break

        return

    save('character_sheet')  # save file after everything is put in

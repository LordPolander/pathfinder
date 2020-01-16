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



def edit(file_name,
         character_class,
         character_stats,
         character_skills,
         character_skill_points,
         character_feats,
         character_spells,
         character_hd):
    doc = opendoc(file_name)

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

        # Q
        pos = update_pos('Q22')  # set it to Q22
        cell = sheet[pos]
        cell.set_value(attack_mod)

        # T
        pos = update_pos(pos, 3)
        cell = sheet[pos]  # move from Q to T
        cell.set_value(character_stats[2])

        # U
        pos = update_pos(pos, 1)
        cell = sheet[pos]  # +1
        cell.set_value(character_stats[3])

        # V
        pos = update_pos(pos, 1)
        cell = sheet[pos]  # +1
        cell.set_value(character_stats[4])
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

                skill = skill.upper()
                if str(cellvalue) in str(skill):
                    sheet[update_pos(pos, -1)].set_value(1)
            if pos == 'P102':  # limit
                break
            pos = update_pos(pos, 0, 2)

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

    def edit_skill_points(character_skill_points):
        pos = update_pos('S4')
        sheet = doc.sheets[0]
        cell = sheet[pos]
        character_skill_points = ''.join(filter(lambda x: x.isdigit(), character_skill_points))
        cell.set_value(character_skill_points)
        return

    def edit_class(character_class):
        pos = update_pos('N22')
        sheet = doc.sheets[0]
        cell = sheet[pos]
        cell.set_value(character_class)
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

    def edit_hd(character_hd):
        pos = update_pos('M22')
        sheet = doc.sheets[0]
        cell = sheet[pos]
        cell.set_value(character_hd)
        return

    def edit_spells(character_spells, character_class, character_stats):
        if len(character_spells) > 0:
            # set spells class name
            pos = update_pos('B3')
            sheet = doc.sheets[2]
            cell = sheet[pos]
            cell.set_value(character_class)
            # set spells level
            pos = update_pos('G3')
            cell = sheet[pos]
            level = character_stats[0]
            cell.set_value(level[:-2])
        return

    edit_stats(character_stats)
    edit_skills(character_skills)
    edit_skill_points(character_skill_points)
    edit_class(character_class)
    edit_feats(character_feats)
    edit_spells(character_spells, character_class, character_stats)
    edit_hd(character_hd)

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

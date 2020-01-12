from ezodf import opendoc
from pathlib import Path


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
        hor = 'W'
        ver = 22
        ver = str(ver)
        sheet = doc.sheets[0]
        cell = sheet[f'{hor}{ver}']

        level = character_stats[0]
        cell.set_value(level[:-2])  # delete characters after number

        # keep only first from attack mod
        attack_mod = character_stats[1]
        attack_mod = attack_mod.split('/')  # split by /
        attack_mod = attack_mod[0]  # take first mod from list
        attack_mod = attack_mod.replace('+', '')  # delete + from the mod

        hor = 'Q'
        cell = sheet[f'{hor}{ver}']
        cell.set_value(attack_mod)

        hor = 'T'
        cell = sheet[f'{hor}{ver}']
        cell.set_value(character_stats[2])

        hor = 'U'
        cell = sheet[f'{hor}{ver}']
        cell.set_value(character_stats[3])

        hor = 'V'
        cell = sheet[f'{hor}{ver}']
        cell.set_value(character_stats[4])
        return

    def edit_skills(character_skills):
        ver = 38
        ver = str(ver)
        sheet = doc.sheets[0]
        # 34
        while True:  # check mark skills you are proficient in, skipping knowledges
            for skill in character_skills:
                cell = sheet[f'P{ver}']
                cellvalue = cell.value
                if type(cellvalue) == str:
                    cellvalue = cellvalue.replace('*', '')

                skill = skill.upper()
                if str(cellvalue) in str(skill):
                    sheet[f'O{ver}'].set_value(1)
            if ver == '102':
                break
            ver = int(ver)
            ver += 2
            ver = str(ver)

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
        ver = 64  # start at the knowledge box
        ver = str(ver)
        for knowledge in knowledges:
            sheet[f'Q{ver}'].set_value(knowledge)  # set in what knowledge
            sheet[f'O{ver}'].set_value(1)  # mark knowledge
            ver = int(ver)
            ver += 2
            ver = str(ver)
        return

    def edit_skill_points(character_skill_points):
        hor = 'S'
        ver = 4
        ver = str(ver)
        sheet = doc.sheets[0]
        cell = sheet[f'{hor}{ver}']
        character_skill_points = ''.join(filter(lambda x: x.isdigit(), character_skill_points))
        cell.set_value(character_skill_points)
        return

    def edit_class(character_class):
        hor = 'N'
        ver = 22
        ver = str(ver)
        sheet = doc.sheets[0]
        cell = sheet[f'{hor}{ver}']
        cell.set_value(character_class)

        return

    def edit_feats(character_feats):
        hor = 'A'
        ver = 72
        for feat in character_feats:
            ver = str(ver)
            sheet = doc.sheets[0]
            cell = sheet[f'{hor}{ver}']
            cell.set_value(feat)
            # print('{}{}'.format(hor, ver), '---', feat)
            ver = int(ver)
            if ver == 100:
                hor = 'H'
                ver = 72
            else:
                ver += 2
        return

    def edit_hd(character_hd):
        hor = 'M'
        ver = 22
        ver = str(ver)  # string the value
        sheet = doc.sheets[0]
        cell = sheet[f'{hor}{ver}']
        cell.set_value(character_hd)
        return

    def edit_spells(character_spells, character_class, character_stats):
        if len(character_spells)>0:
            # set spells class name
            hor = 'B'
            ver = 3
            ver = str(ver)
            sheet = doc.sheets[2]
            cell = sheet[f'{hor}{ver}']
            cell.set_value(character_class)
            # set spells level
            hor = 'G'
            cell = sheet[f'{hor}{ver}']
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
                i+=1
            else:
                doc.saveas(save_file + str(i) + '.ods')
                print('')
                print('file saved as:', save_file + str(i) + '.ods')
                break

        return

    save('character_sheet')  # save file after everything is put in

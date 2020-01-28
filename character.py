class Character():
    def __init__(self, character_data):
        self.class_name = character_data[0]
        self.stats = character_data[1]
        self.skills = character_data[2]
        self.skill_points = character_data[3]
        self.feats = character_data[4]
        self.spells = character_data[5]
        self.hd = character_data[6]

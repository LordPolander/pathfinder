import webscrape
from time import sleep

# print('laget av Ignacy, testet av Adrian')

character_level = int(input('level : '))
character_class_link = str(input('link to class : '))

character_class_page = webscrape.preprequest(character_class_link)  # send link for data

character_stats = webscrape.find_stats(character_class_page, character_level)  # find in page; level
character_spells = webscrape.find_spells(character_class_page, character_level)
character_skills = webscrape.find_skills(character_class_page) # find in page
character_feats = webscrape.find_feats(character_class_page, character_level) # find in page; from 1 to level

character_stats = character_stats[0:5] # get rid of spells if there are any

print('stats   :', character_stats)
print('skills  :', character_skills)
print('feats   :', character_feats)
print('spells  :', character_spells)

sleep(100)

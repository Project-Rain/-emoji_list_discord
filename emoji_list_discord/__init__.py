__version__ = 0.1.1

from emoji_list_discord.Smileys_and_people import *
from emoji_list_discord.Animals_and_nature import *
from emoji_list_discord.Travel_and_places import *
from emoji_list_discord.Activities import *
from emoji_list_discord.Objects import *
from emoji_list_discord.Symbols import *

# Animals and nature

animals_mammal = [u'']
animal_bird = [u'']
animal_amphibian = [u'']
animal_reptile = [u'']
animal_marine = [u'']
animal_bug = [u'']
plant_flower = [u'']
plant_other = [u'']

# Travel and places

place_map = [u'']
place_geographic = [u'']
place_building = [u'']
place_religious = [u'']
place_other = [u'']
transport_ground = [u'']
transport_water = [u'']
transport_air = [u'']
hotel = [u'']
time = [u'']
weather = [u'']

# Activities

event = [u'']
award_medal = [u'']
sport = [u'']
game = [u'']

# Objects

sound = [u'']
music = [u'']
musical_instrument = [u'']
phone = [u'']
computer = [u'']
light_video = [u'']
book_paper = [u'']
money = [u'']
mail = [u'']
writing = [u'']
office = [u'']
lock = [u'']
tool = [u'']
medical = [u'']
other_object = [u'']

# Symbols

transport_sign = [u'']
warning = [u'']
arrow = [u'']
religion = [u'']
av_symbol = [u'']
other_symbol = [u'']
keycap = [u'']
alphanum = [u'']
geometric = [u'']
flag = [u'']
country_flag = [u'']
subdivision_flag = [u'']

# All emoji

all_Smileys_and_people = list(set(face_positive+face_neutral+face_negative+face_sick+face_role+face_fantasy+face_cat+face_monkey+person+person_role+person_fantasy+person_gesture+person_activity+person_sport+family+body+emotion+clothing))
all_Animals_and_nature = list(set())
all_Travel_and_places = list(set())
all_Activities = list(set())
all_Objects = list(set())
all_Symbols = list(set(transport_sign+warning+arrow+religion+av_symbol+other_symbol+keycap+alphanum+geometric+flag+country_flag+subdivision_flag))
all_emoji = list(set(face_positive+face_neutral+face_negative+face_sick+face_role+face_fantasy+face_cat+face_monkey+person+person_role+person_fantasy+person_gesture+person_activity+person_sport+family+body+emotion+clothing+animals_mammal+animal_bird+animal_amphibian+animal_reptile+animal_marine+animal_bug+plant_flower+plant_other+food_fruit+food_vegetable+food_prepared+food_asian+food_sweet+drink+dishware+place_map+place_geographic+place_building+place_religious+place_other+transport_ground+transport_water+transport_air+hotel+time+weather+event+award_medal+sport+game+sound+music+musical_instrument+phone+computer+light_video+book_paper+money+mail+writing+office+lock+tool+medical+other_object+transport_sign+warning+arrow+religion+av_symbol+other_symbol+keycap+alphanum+geometric+flag+country_flag+subdivision_flag))

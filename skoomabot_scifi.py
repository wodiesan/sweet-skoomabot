"""
@author:     Sze "Ron" Chau
@source:     https://github.com/wodiesan/sweet-skoomabot

Config file that contains the various:
1. Dictionaries and lists of terms.
2. Functions to build dicts and lists for charting in plot.ly.
"""

from collections import OrderedDict
import skoomabot_config as sbc

checked_post = {}
checked_post.setdefault('pos', [])
checked_post.setdefault('neg', [])

bethesda = ['elderscrolls', 'fallout', 'morrowind', 'oblivion', 'skyrim']
bungie = ['halo']
dc = ['arkham', 'batman', 'dc', 'injustice', 'justice', 'superman']
firefly = ['firefly', 'serenity']
gameofthrones = ['asoiaf', 'got', 'gameofthrones']
lotr = ['hobbit', 'lotr', 'lordoftherings']
marvel = ['avenger', 'marvel', 'mcu', 'spiderman', 'wolverine', 'xmen']
matrix = ['matrix']
potter = ['harrypotter', 'hogwarts']
starwars = ['starwars']
startrek = ['startrek']
terminator = ['t800', 'terminator']
warhammer = ['40k', 'warhammer', 'w40k', 'wh40k']

sci_dict = {}
sci_dict = OrderedDict(sci_dict)
sci_dict['bethesda'] = bethesda
sci_dict['bungie'] = bungie
sci_dict['dc'] = dc
sci_dict['firefly'] = firefly
sci_dict['game of thrones'] = gameofthrones
sci_dict['lotr'] = lotr
sci_dict['marvel'] = marvel
sci_dict['matrix'] = matrix
sci_dict['potter'] = potter
sci_dict['startrek'] = startrek
sci_dict['starwars'] = starwars
sci_dict['terminator'] = terminator
sci_dict['warhammer'] = warhammer

# dict to store lists of slang names.
bethesda_cha = ['brotherhood', 'bos', 'champion', 'coc', 'dragonborn', 'ldb', 'nerevar']
bungie_cha = ['chief', 'cortana', 'covenant', 'halo']
dc_cha = ['avengers', 'batman', 'kent', 'superman', 'wayne']
firefly_cha = ['mal', 'river']
got_cha = ['baratheon', 'daenerys', 'dany', 'lannister', 'targaryen']
lotr_cha = ['aragorn', 'gandalf', 'hobbit', 'saruman', 'sauron', 'smaug']
marvel_cha = ['america', 'avenger', 'daredevil', 'deadpool', 'spiderman', 'wolverine']
matrix_cha = ['matrix', 'morpheus', 'neo', 'smith', 'trinity']
potter_cha = ['dumbledore', 'hermione', 'muggle', 'potter', 'snape', 'voldermort', 'weasley']
starwars_cha = ['jedi', 'luke', 'palpatine', 'sith', 'vader']
startrek_cha = ['data', 'kirk', 'mccoy', 'picard', 'spock']
terminator_cha = ['t1000', 'skynet', 't800', 'terminator']
warhammer_cha = ['chaos', 'eldar', 'emperor', 'imperium', 'marine', 'necron', 'ork', 'tau']


cha_dict = {}
cha_dict = OrderedDict(sci_dict)
cha_dict['bethesda'] = bethesda
cha_dict['bungie'] = bungie
cha_dict['dc'] = dc
cha_dict['firefly'] = firefly
cha_dict['game of thrones'] = gameofthrones
cha_dict['lotr'] = lotr
cha_dict['marvel'] = marvel
cha_dict['matrix'] = matrix
cha_dict['potter'] = potter
cha_dict['startrek'] = startrek
cha_dict['starwars'] = starwars
cha_dict['terminator'] = terminator
cha_dict['warhammer'] = warhammer


# Use a dict for lists of locations
py_dict_sci = sbc.dict_wo_vals(sci_dict)
py_list_sci = py_dict_sci.keys()
py_matrix_sci = sbc.create_matrix(sci_dict)

# _subcat_dict = sub_dict_wo_vals()
# _subcat_list = _subcat_dict.keys()

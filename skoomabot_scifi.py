"""
@author:     Sze "Ron" Chau
@source:     https://github.com/wodiesan/sweet-skoomabot

Config file that contains the various:
1. Dictionaries and lists of terms.
"""

from collections import OrderedDict
import skoomabot_config as sbc

sci_checked_id = {}
sci_checked_id.setdefault('pos', [])
sci_checked_id.setdefault('neg', [])

# dict to store tag categories that appear in /r/AskScienceFiction
dc = ['arkham', 'batman', 'dc', 'justice', 'superman']
elderscrolls = ['elderscrolls', 'morrowind', 'oblivion', 'skyrim']
fallout = ['fallout']
firefly = ['firefly', 'serenity']
gameofthrones = ['asoiaf', 'got', 'gameofthrones']
halo = ['halo']
harry = ['harrypotter', 'hogwarts']
lotr = ['hobbit', 'lotr', 'lordoftherings']
marvel = ['avenger', 'marvel', 'mcu', 'spiderman', 'wolverine', 'xmen']
matrix = ['matrix']
starwars = ['starwars']
startrek = ['startrek']
terminator = ['t800', 'terminator']
warhammer = ['40k', 'warhammer', 'w40k', 'wh40k']

sci_dict = {}
sci_dict = OrderedDict(sci_dict)
sci_dict['dc'] = dc
sci_dict['elder scrolls'] = elderscrolls
sci_dict['fallout'] = fallout
sci_dict['firefly'] = firefly
sci_dict['game of thrones'] = gameofthrones
sci_dict['halo'] = halo
sci_dict['harry potter'] = harry
sci_dict['lord of the rings'] = lotr
sci_dict['marvel'] = marvel
sci_dict['matrix'] = matrix
sci_dict['star trek'] = startrek
sci_dict['star wars'] = starwars
sci_dict['terminator'] = terminator
sci_dict['warhammer 40k'] = warhammer

# dict to store characters in each category.
dc_cha = ['batman', 'constantine', 'flash', 'joker', 'justice', 'lantern', 'superman', 'wayne', 'wonder']
elderscrolls_cha = ['brotherhood', 'bos', 'champion', 'coc', 'dragonborn', 'ldb', 'nerevar']
fallout_cha = ['brotherhood', 'bos', 'caps', 'vault']
firefly_cha = ['mal', 'river']
got_cha = ['baratheon', 'daenerys', 'dany', 'lannister', 'targaryen']
halo_cha = ['chief', 'cortana', 'covenant', 'flood', 'gravemind', 'halo']
harry_cha = ['dumbledore', 'hermione', 'muggle', 'potter', 'snape', 'voldermort', 'weasley']
lotr_cha = ['aragorn', 'gandalf', 'hobbit', 'ring', 'saruman', 'sauron', 'smaug']
marvel_cha = ['america', 'avenger', 'daredevil', 'deadpool', 'galactus', 'hulk', 'iron', 'spiderman', 'thor', 'wolverine']
matrix_cha = ['matrix', 'morpheus', 'neo', 'smith', 'trinity']
starwars_cha = ['force', 'jedi', 'luke', 'palpatine', 'sidious', 'sith', 'vader', 'yoda']
startrek_cha = ['borg', 'enterprise', 'federation', 'kirk', 'klingon', 'mccoy', 'picard', 'spock', 'starfleet', 'voyager', 'vulcan']
terminator_cha = ['connor', 'skynet', 't1000', 't800', 'terminator']
warhammer_cha = ['chaos', 'eldar', 'emperor', 'guard', 'imperium', 'marine', 'mechanicus', 'necron', 'ork', 'primarch', 'tau', 'tyranid', 'warp']

cha_dict = {}
cha_dict = OrderedDict(cha_dict)
cha_dict['dc'] = dc_cha
cha_dict['elder scrolls'] = elderscrolls_cha
cha_dict['fallout'] = fallout_cha
cha_dict['firefly'] = firefly_cha
cha_dict['game of thrones'] = got_cha
cha_dict['halo'] = halo_cha
cha_dict['harry potter'] = harry_cha
cha_dict['lord of the rings'] = lotr_cha
cha_dict['marvel'] = marvel_cha
cha_dict['matrix'] = matrix_cha
cha_dict['star trek'] = startrek_cha
cha_dict['star wars'] = starwars_cha
cha_dict['terminator'] = terminator_cha
cha_dict['warhammer 40k'] = warhammer_cha

# Various lists and dicts used for plot.ly axes.
# py_dict_sci = sbc.dict_wo_vals(sci_dict)
# py_list_sci = py_dict_sci.keys()
# py_matrix_sci = sbc.create_matrix(sci_dict)

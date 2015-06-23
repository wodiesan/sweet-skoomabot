"""
@author:     Sze "Ron" Chau
@source:     https://github.com/wodiesan/sweet-skoomabot

Config file that contains the various:
1. Dictionaries and lists of terms.
2. Functions to build dicts and lists for charting in plot.ly.
"""

from collections import OrderedDict


def create_matrix(dict_category):
    """Takes a dict and returns matrix with x and y at dict legnth."""
    matrix_vals = dict_category
    matrix = [[0 for x in range(len(matrix_vals))]
              for x in range(len(matrix_vals))]
    return matrix


def dict_wo_vals(dict_w_vals):
    """Takes a dict, returns new dict with None vals for all keys."""
    copy_dict = OrderedDict.fromkeys(dict_w_vals.keys(), None)
    return copy_dict


def sub_dict_wo_vals(list_of_subcategories):
    """Creates a dict with the list items as key and None as vals."""
    # sub_dict = {key: None for key in list_of_subcategories}
    sub_dict = OrderedDict()
    for item in list_of_subcategories:
        sub_dict[item] = None
    # sub_dict = sub_dict.OrderedDict()
    return sub_dict

checked_post = {}
checked_post.setdefault('pos', [])
checked_post.setdefault('neg', [])

# dict to store lists of slang names.
# CANNABIS HAS FALSE POSITIVES FOR '[CAN]'!
# METH HAS FALSE POSITIVES FOR '[METH]OD'!
alcohol = ['alcohol', 'beer', 'liquor', 'wine']
caffeine = ['caffeine', 'coffee']
# cannabis = ['blunt', 'bud', 'cannabis', 'ganj', 'grass', 'hash', 'herb', 'marijuana', 'pot', 'thc', 'tree', 'weed']
cannabis = ['blunt', 'bud', 'cannabis', 'hash', 'marijuana', 'pot', 'thc', 'tree', 'weed']
nicotine = ['nicotine', 'tobacco', 'cig', 'snus']
cocaine = ['cocaine', 'coke', 'yayo']
ecstasy = ['mdma', 'ecstasy', 'molly', 'xtc']
heroin = ['heroin', 'smack', 'dope', 'junk']
lsd = ['acid', 'lsd', 'blotter']
meth = ['glass', 'crank', 'meth', 'speed', 'crystal']
painkiller = ['oxy', 'codone', 'dilaudid', 'perc', 'methadone', 'morphine']
salvia = ['salvia', 'sally', 'maria', 'divinorum']
otc = ['aspirin', 'maoi', 'benadryl', 'diphenhyd', 'dxm', 'dextromo', 'robo', 'acetom', 'ibupro']
benzo = ['benzo', 'valium', 'xanax', 'klonopin', 'ativan']
psilocybin = ['shroom', 'psilocybin', 'mushroom']
amphetamine = ['amph', 'adderall', 'vyvanse', 'dex', 'concerta', 'ritalin', 'focalin']

drug_dict = {}
drug_dict = OrderedDict(drug_dict)
drug_dict['alcohol'] = alcohol
drug_dict['amphetamine'] = amphetamine
drug_dict['benzo'] = benzo
drug_dict['caffeine'] = caffeine
drug_dict['cannabis'] = cannabis
drug_dict['cocaine'] = cocaine
drug_dict['ecstasy'] = ecstasy
drug_dict['heroin'] = heroin
drug_dict['lsd'] = lsd
drug_dict['meth'] = meth
drug_dict['nicotine'] = nicotine
drug_dict['otc'] = otc
drug_dict['painkiller'] = painkiller
drug_dict['psilocybin'] = psilocybin
drug_dict['salvia'] = salvia

# Use a dict for lists of locations, health, and pos/neg descriptors mentioned.
location = ['home', 'school', 'job', 'work', 'dispensary']
legal = ['prison', 'jail', 'police', 'cop', 'officer', 'arrest', 'undercover', 'raid']
party = ['rave', 'party', 'club', 'edm', 'concert', 'festival', 'bar']
health = ['addict', 'reaction', 'safe', 'danger', 'withdrawl', 'prescribe']
physical = ['allerg', 'death', 'die', 'nausea', 'sleep', 'tolerance', 'toxic']
psych = ['adhd', 'anxiety', 'ego', 'depress', 'dysfunction', 'coping', 'mental', 'neuro', 'scare', 'therapy']
cost = ['cost', 'price', 'afford', 'money', 'sell', 'hustle', 'deal']
# question = ['how to']
# politics = ['dispensary']

setting_dict = {}
setting_dict = OrderedDict(setting_dict)
setting_dict['cost'] = cost
setting_dict['health'] = health
setting_dict['legal'] = legal
setting_dict['location'] = location
setting_dict['party'] = party
setting_dict['physical'] = physical
setting_dict['psych'] = psych

py_dict_drug = dict_wo_vals(drug_dict)
py_list_drug = py_dict_drug.keys()
py_matrix_drug = create_matrix(drug_dict)

py_dict_set = dict_wo_vals(setting_dict)
py_list_set = py_dict_set.keys()
py_matrix_set = create_matrix(setting_dict)

cannabis_subcat_dict = sub_dict_wo_vals(cannabis)
cannabis_subcat_list = cannabis_subcat_dict.keys()

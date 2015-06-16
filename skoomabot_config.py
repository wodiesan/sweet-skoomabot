"""
@author:     Sze "Ron" Chau
@source:     https://github.com/wodiesan/druggiebot

Config file that contains the various:
1. Dictionaries to contain lists of terms.
2. Classes to contain Reddit posts.
3. Functions to build plotly plot points.
"""

import re
import time


class Post:
    """Parses individual Reddit submissions for op title, text (if any),
    time of post (in utc), and permalink."""
    def __init__(self, submission):
        self.post = submission
        self._parse()

    def _parse(self):
        self.id_num = self.post.id
        self.title = self.post.title.encode('utf-8')
        self.title = self.title.lower()
        self.text = self.post.selftext.encode('utf-8')
        self.text = self.text.lower()
        self.time = self.post.created_utc
        self.date = time.strftime('%d %b %Y', time.gmtime(self.time))
        self.link = self.post.permalink

    # DO I WANT TO KEEP TRACK OF THE ACTUAL SLANG TERM?
    # def _category(self, drug_dict, lookup):
    def _category(self, term_dict, plotly_dict, lookup):
        """Checks for slang terms in post title. Returns all matching drugs as a list.
        THIS IS INCOMPLETE."""
        list_of_matches = []
        lookup = lookup.split()
        for word in lookup:
            word = re.sub('[^0-9a-z\']', '', word)
            # print word
            if len(word) > 2:
                for key, value in term_dict.items():
                # for key, value in drug_dict.items():
                    for v in value:
                        if re.match(r'{}'.format(v), word):
                            # print 'Match: {} from {} category.'.format(word, key)
                            if key not in list_of_matches:
                                list_of_matches.append(key)
                            else:
                                pass
        else:
            pass
        for drug in list_of_matches:
            self._insert_plot_point(plotly_dict, drug)
            # self._insert_plot_point(drug_dict, drug)
        if len(list_of_matches) > 1:
            print 'More than one drug mentioned.'

        return list_of_matches

    def _match(self, dict):
        """Takes a op title and checks for drug slang from a dictionary."""
        if any(string in self.title for string in dict):
            return True
        else:
            return False

    def _insert_plot_point(self, dict, drugtype):
        """For every drug that's mentioned, uptick 1 to the key's value."""
        # print 'test printing: {}'.format(drugtype)
        try:
            dict[drugtype] += 1
        except (AttributeError, TypeError):
            dict[drugtype] = 1

    def _insert_heat_point(self, drugtype):
        """For every poly-drug post, uptick the 2-combo by 1 point."""


# TESTING OUT PLOTTING TO PLOT.LY
plotly_dict = {'alcohol': None, 'caffeine': None, 'cannabis': None, 'nicotine': None, 'cocaine': None, 'ecstasy': None, 'heroin': None, 'lsd': None, 'meth': None, 'painkiller': None, 'salvia': None, 'otc': None, 'benzo': None, 'amphetamine': None, 'psilocybin': None}
plotly_dict_set = {'location': None, 'deviant': None, 'party': None, 'health': None, 'physical': None, 'psychological': None, 'cost': None}

checked_post = {}
checked_post.setdefault('pos', [])
checked_post.setdefault('neg', [])

# dict to store lists of slang names.
# CANNABIS HAS FALSE POSITIVES FOR '[CAN]'!
# METH HAS FALSE POSITIVES FOR 'SO[METH]ING' AND '[METH]OD'!
alcohol = ['alcohol', 'beer', 'liquor', 'wine']
caffeine = ['caffeine', 'coffee']
cannabis = ['cannabis', 'marijuana', 'weed', 'tree', 'blunt', 'thc']
nicotine = ['nicotine', 'tobacco', 'cig', 'snus']
cocaine = ['cocaine', 'coke', 'yayo']
ecstasy = ['mdma', 'ecstasy', 'molly', 'xtc']
heroin = ['heroin', 'smack', 'dope', 'junk']
lsd = ['acid', 'lsd']
meth = ['glass', 'crank', 'meth', 'speed', 'crystal']
painkiller = ['oxy', 'codone', 'dilaudid', 'perc']
salvia = ['salvia']
otc = ['maoi', 'benadryl', 'dxm']
benzo = ['benzo', 'valium', 'xanax', 'klonopin', 'ativan']
amphetamine = ['amph', 'adderall', 'vyvanse', 'dex', 'concerta', 'ritalin', 'focalin']
psilocybin = ['shroom']

drug_dict = {}
drug_dict['alcohol'] = alcohol
drug_dict['caffeine'] = caffeine
drug_dict['cannabis'] = cannabis
drug_dict['nicotine'] = nicotine
drug_dict['cocaine'] = cocaine
drug_dict['ecstasy'] = ecstasy
drug_dict['heroin'] = heroin
drug_dict['lsd'] = lsd
drug_dict['meth'] = meth
drug_dict['painkiller'] = painkiller
drug_dict['salvia'] = salvia
drug_dict['otc'] = otc
drug_dict['benzo'] = benzo
drug_dict['amphetamine'] = amphetamine
drug_dict['psilocybin'] = psilocybin

# Use a dict for lists of locations, health, and pos/neg descriptors mentioned.
location = ['home', 'school', 'job', 'work', 'dispensary']
deviant = ['prison', 'jail', 'police', 'cop', 'officer', 'arrest', 'undercover']
party = ['rave', 'party', 'club', 'edm', 'concert', 'festival']
health = ['addict', 'reaction', 'safe', 'danger', 'withdrawl', 'prescribe']
physical = ['allergic', 'death', 'die', 'nausea', 'sleep', 'tolerance', 'toxic']
psychological = ['anxiety', 'ego', 'depress', 'dysfunction', 'coping', 'mental', 'neuro', 'scare', 'therapy']
cost = ['cost', 'price', 'afford', 'money', 'sell', 'hustle', 'deal']
# question = ['how to']
# politics = ['dispensary']

setting_dict = {}
setting_dict['location'] = location
setting_dict['deviant'] = deviant
setting_dict['party'] = party
setting_dict['health'] = health
setting_dict['physical'] = physical
setting_dict['psychological'] = psychological
setting_dict['cost'] = cost
# pos_high = []
# neg_high = []

"""
@author:     Sze "Ron" Chau
@source:     https://github.com/wodiesan/druggiebot

Config file that contains the various:
1. Dictionaries to contain lists of terms.
2. Classes to contain Reddit posts.
3. Functions to build plotly plot points.
"""

from collections import OrderedDict
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
        try:
            self.username = self.post.author.name
        except AttributeError:
            self.username = 'deleted'

    # DO I WANT TO KEEP TRACK OF THE ACTUAL SLANG TERM?
    def _category(self, plotly_dict, plotly_list, plotly_matrix, list_of_matches):
        """Checks for slang terms in post title. Returns all matching drugs as a list.
        plotly_list could possibly be unecessary/bug-causing."""

        for term in list_of_matches:
            self._insert_plot_point(plotly_dict, term)

        if len(list_of_matches) > 1:
            print 'More than one drug mentioned.'
            indicies_list = parse_poly(plotly_list, list_of_matches)
            poly_coord = index_list_to_matrix_coord(indicies_list)
            insert_heat_point(plotly_matrix, poly_coord)
        return list_of_matches

    # def _category(self, term_dict, plotly_dict, plotly_list, plotly_matrix, lookup):
    #     """Checks for slang terms in post title. Returns all matching drugs as a list.
    #     plotly_list could possibly be unecessary/bug-causing."""
    #     list_of_matches = []
    #     lookup = lookup.replace('/', ' ').split()
    #     for word in lookup:
    #         word = re.sub('[^0-9a-z\']', '', word)
    #         if len(word) > 2:
    #             for key, value in term_dict.items():
    #                 for v in value:
    #                     if re.match(r'{}'.format(v), word) and key not in list_of_matches:
    #                             list_of_matches.append(key)
    #                     else:
    #                         pass
    #     else:
    #         pass

    #     for term in list_of_matches:
    #         self._insert_plot_point(plotly_dict, term)

    #     if len(list_of_matches) > 1:
    #         print 'More than one drug mentioned.'
    #         indicies_list = parse_poly(plotly_list, list_of_matches)
    #         poly_coord = index_list_to_matrix_coord(indicies_list)
    #         insert_heat_point(plotly_matrix, poly_coord)
    #     return list_of_matches

    # def _match(self, dict):
    #     """Takes a op title and checks for drug slang from a dictionary."""
    #     if any(string in self.title for string in dict):
    #         return True
    #     else:
    #         return False

    def _match(self, term_dict, lookup):
        list_of_matches = []
        lookup = lookup.replace('/', ' ').split()
        for word in lookup:
            word = re.sub('[^0-9a-z\']', '', word)
            if len(word) > 2:
                for key, value in term_dict.items():
                    for v in value:
                        if re.match(r'{}'.format(v), word) and key not in list_of_matches:
                                list_of_matches.append(key)
                        else:
                            pass
        else:
            pass
        return list_of_matches

    def _insert_plot_point(self, x_axis_dict, term):
    # def _insert_plot_point(x_axis_dict, term):
        """For every drug that's mentioned, uptick 1 to the key's value."""
        try:
            x_axis_dict[term] += 1
        except (AttributeError, TypeError):
            x_axis_dict[term] = 1

    # def _uptick(list_of_matches, plotly_dict, plotly_list, plotly_matrix):
    #     for term in list_of_matches:
    #         _insert_plot_point(plotly_dict, term)

    #     if len(list_of_matches) > 1:
    #         # print 'More than one drug mentioned.'
    #         indicies_list = parse_poly(plotly_list, list_of_matches)
    #         poly_coord = index_list_to_matrix_coord(indicies_list)
    #         insert_heat_point(plotly_matrix, poly_coord)


# TESTING OUT PLOTTING TO PLOT.LY
# plotly_dict = {'alcohol': None, 'caffeine': None, 'cannabis': None, 'nicotine': None, 'cocaine': None, 'ecstasy': None, 'heroin': None, 'lsd': None, 'meth': None, 'painkiller': None, 'salvia': None, 'otc': None, 'benzo': None, 'amphetamine': None, 'psilocybin': None}
# plotly_dict_set = {'location': None, 'deviant': None, 'party': None, 'health': None, 'physical': None, 'psychological': None, 'cost': None}


##########################################
# This should be moved into its own class.
##########################################

def create_matrix(dict_category):
    """Takes a dict and returns matrix with x and y at dict legnth."""
    print 'create_matrix dict: {}\n'.format(dict)
    # dict_ord = OrderedDict(dict)
    # print 'create_matrix dict post OrderedDict'.format(dict_ord)
    # matrix_vals = dict_ord.keys()
    matrix_vals = dict_category
    matrix = [[0 for x in range(len(matrix_vals))] for x in range(len(matrix_vals))]
    return matrix


def dict_wo_vals(dict_w_vals):
    """Takes a dict, returns new dict with None vals for all keys."""
    # Ensure that OrderedDict is being properly used.
    # copy_dict = OrderedDict(dict_w_vals)
    copy_dict = OrderedDict.fromkeys(dict_w_vals.keys(), None)
    return copy_dict


def parse_poly(drug_list, post_list):
    """Takes a list of drugs and returns [indicies] based on drug_list.
    Used for poly drug matches when parsing titles in posts."""
    coord_list = []
    for item in post_list:
        coord_index = drug_list.index(item)
        coord_list.append(coord_index)

    print '\nThe indices for {}: {}'.format(post_list, coord_list)
    return coord_list


def index_list_to_matrix_coord(indicies_list):
    """Takes a list of indicies, returns coordinates for the matrix.
    Credit to /u/DarkGamanoid for the help."""
    heatmap_coord_list = []
    for item in indicies_list:
        try:
            index = indicies_list.index(item)
            for other_items in indicies_list:
                if other_items is not item:
                    position = [item, other_items]
                    heatmap_coord_list.append(position)
                # print 'pos: {}'.format(position)
        except IndexError:
            pass

    print '\nCoordinates to uptick: {}'.format(heatmap_coord_list)
    return heatmap_coord_list


def insert_heat_point(matrix, coords_list):
    """For every ordered pair in list, uptick 1 to (x, y) in heatmap matrix.
    Used in poly-drug posts, uptick each 2-combo by 1 point."""
    for coord in coords_list:
        try:
            xaxis = coord[0]
            yaxis = coord[1]
            matrix[xaxis][yaxis] += 1
        except (AttributeError, TypeError):
            matrix[xaxis][yaxis] = 1


# def sort_dict(dict_unsorted):
#     for key, value in sorted(dict_unsorted.items())

checked_post = {}
checked_post.setdefault('pos', [])
checked_post.setdefault('neg', [])

# dict to store lists of slang names.
# CANNABIS HAS FALSE POSITIVES FOR '[CAN]'!
# METH HAS FALSE POSITIVES FOR 'SO[METH]ING' AND '[METH]OD'!
alcohol = ['alcohol', 'beer', 'liquor', 'wine']
caffeine = ['caffeine', 'coffee']
cannabis = ['cannabis', 'marijuana', 'weed', 'tree', 'blunt', 'thc', 'bud', 'hash', 'grass', 'ganj', 'herb', 'pot']
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
# drug_dict = sorted(drug_dict.keys())

# Use a dict for lists of locations, health, and pos/neg descriptors mentioned.
location = ['home', 'school', 'job', 'work', 'dispensary']
legal = ['prison', 'jail', 'police', 'cop', 'officer', 'arrest', 'undercover', 'raid']
party = ['rave', 'party', 'club', 'edm', 'concert', 'festival', 'bar']
health = ['addict', 'reaction', 'safe', 'danger', 'withdrawl', 'prescribe']
physical = ['allerg', 'death', 'die', 'nausea', 'sleep', 'tolerance', 'toxic']
psychological = ['adhd', 'anxiety', 'ego', 'depress', 'dysfunction', 'coping', 'mental', 'neuro', 'scare', 'therapy']
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
setting_dict['psychological'] = psychological
# setting_dict = sorted(setting_dict.keys())

# pos_high = []
# neg_high = []

# py_list_drug = drug_dict.keys()
py_dict_drug = dict_wo_vals(drug_dict)
py_list_drug = py_dict_drug.keys()
py_matrix_drug = create_matrix(drug_dict)

# py_list_set = setting_dict.keys()
py_dict_set = dict_wo_vals(setting_dict)
py_list_set = py_dict_set.keys()
py_matrix_set = create_matrix(setting_dict)

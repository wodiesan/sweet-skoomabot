"""
@author:     Sze "Ron" Chau
@source:     https://github.com/wodiesan/sweet-skoomabot

Config classes with methods that handles:
1. Class to parse Reddit posts.
2. Class to build plot.ly charts. <- INCOMPLETE
"""

# from collections import OrderedDict
import re
import time

from plotly.graph_objs import Bar, Data, Heatmap, Layout, Figure
# import plotly.tools as tls
import plotly.plotly as viz
import praw

bot_version = 'Version 0.3.1'


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

    def _category(self, plotly_dict, plotly_list, plotly_matrix,
                  list_of_matches):
        """Checks for slang terms in post title. Returns all matching drugs as a list.
        plotly_list could possibly be unecessary/bug-causing."""

        for term in list_of_matches:
            self._insert_plot_point(plotly_dict, term)

        if len(list_of_matches) > 1:
            indicies_list = parse_poly(plotly_list, list_of_matches)
            poly_coord = index_list_to_matrix_coord(indicies_list)
            insert_heat_point(plotly_matrix, poly_coord)
        return list_of_matches

    def _tag(self, term_dict, lookup):
        list_of_matches = []
        list_of_sub_matches = []
        if re.match(r'\[', lookup):
            endtag = lookup.index(']')
            post_tag = lookup[1:endtag]
            post_tag = re.sub(r'\W', '', post_tag)
            for key, value in term_dict.items():
                for v in value:
                    if re.search(r'{}'.format(v), post_tag) \
                                and key not in list_of_matches:
                                    list_of_matches.append(key)
                                    list_of_sub_matches.append(v)
            else:
                pass
        return list_of_matches, list_of_sub_matches

    def _match(self, term_dict, lookup):
        list_of_matches = []
        list_of_sub_matches = []
        lookup = lookup.replace('/', ' ').split()
        for word in lookup:
            # word = re.sub('[^0-9a-z\']', '', word)
            word = re.sub(r'\W', '', word)
            if len(word) > 2:
                for key, value in term_dict.items():
                    for v in value:
                        if re.match(r'{}'.format(v), word) and key not in list_of_matches:
                                list_of_matches.append(key)
                                list_of_sub_matches.append(v)
                        else:
                            pass
        else:
            pass
        return list_of_matches, list_of_sub_matches

    def _insert_plot_point(self, x_axis_dict, term):
        """For every drug that's mentioned, uptick 1 to the key's value."""
        try:
            x_axis_dict[term] += 1
        except (AttributeError, TypeError):
            x_axis_dict[term] = 1


##########################################
# This should be moved into its own class.
##########################################

def search_subreddit(subreddit, post_limit=1000):
    """Takes the subreddit name ('/r/' is unecessary)."""
    user_agent = 'Visualize posts to /r/{}. {}'.format(subreddit, bot_version)
    start_time = time.time()
    gmt_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(start_time))
    r = praw.Reddit(user_agent=user_agent)
    subreddit = r.get_subreddit(subreddit, fetch=True)
    post_limit = post_limit


def parse_poly(drug_list, post_list):
    """Takes a list of drugs and returns [indicies] based on drug_list.
    Used for poly drug matches when parsing titles in posts."""
    coord_list = []
    for item in post_list:
        coord_index = drug_list.index(item)
        coord_list.append(coord_index)
    return coord_list


def index_list_to_matrix_coord(indicies_list):
    """Takes a list of indicies, returns coordinates for the matrix.
    Credit to /u/DarkGamanoid for the help."""
    heatmap_coord_list = []
    for item in indicies_list:
        try:
            # index = indicies_list.index(item)
            for other_items in indicies_list:
                if other_items is not item:
                    position = [item, other_items]
                    heatmap_coord_list.append(position)
                # print 'pos: {}'.format(position)
        except IndexError:
            pass

    # print '\nCoordinates to uptick: {}'.format(heatmap_coord_list)
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

##########################################
# The following lines are WIP.
##########################################

def viz_bar(graph_name, xaxis, yaxis, filename):
    """Creates a bar graph for plot.ly.
    Takes title, the x and y as lists, and plotly filename.
    INCOMPLETE."""
    data = Data([
        Bar(
            name=filename,
            x=xaxis,
            y=yaxis
        )
    ])
    layout = Layout(
            title=graph_name)
    fig = Figure(data=data, layout=layout)
    plot_url = viz.plot(fig, filename=filename)

def viz_heat(graph_name, xyaxis, zaxis, filename):
    """Creates a categorial heatmap for plot.ly."""
    data = Data([
        Heatmap(
            name=filename,
            z=zaxis,
            x=xyaxis,
            y=xyaxis
        )
    ])
    layout = Layout(
        title=graph_name)
    fig = Figure(data=data, layout=layout)
    plot_url = viz.plot(fig, filename=filename)


# class Plot_Bar:
#     """Builds the arguments for visualizing plot.ly bar graphs."""
#     def __init__(self, matches):
#         self.plot_bar = self

#     def viz_bar(graph_name, xaxis, yaxis, filename):
#     """Creates a bar graph for plot.ly.
#     Takes title, the x and y as lists, and plotly filename.
#     INCOMPLETE."""
#     data = Data([
#         Bar(
#             name=filename,
#             x=xaxis,
#             y=yaxis
#         )
#     ])
#     layout = Layout(
#             title=graph_name)
#     fig = Figure(data=data, layout=layout)
#     plot_url = viz.plot(fig, filename=filename)


# class Plot_Heat(Plot_Bar):
#     """Builds the arguments for visualizing plot.ly heatmaps."""

#     def _create_matrix(dict_category):
#         """Takes a dict and returns matrix with x and y at dict legnth."""
#         print 'create_matrix dict: {}\n'.format(dict)
#         matrix_vals = dict_category
#         matrix = [[0 for x in range(len(matrix_vals))] for x in range(len(matrix_vals))]
#         return matrix

#     def _index_list_to_matrix_coord(indicies_list):
#         """Takes a list of indicies, returns coordinates for the matrix.
#         Credit to /u/DarkGamanoid for the help."""
#         heatmap_coord_list = []
#         for item in indicies_list:
#             try:
#                 # index = indicies_list.index(item)
#                 for other_items in indicies_list:
#                     if other_items is not item:
#                         position = [item, other_items]
#                         heatmap_coord_list.append(position)
#                     # print 'pos: {}'.format(position)
#             except IndexError:
#                 pass

#         print '\nCoordinates to uptick: {}'.format(heatmap_coord_list)
#         return heatmap_coord_list

#     def _insert_heat_point(matrix, coords_list):
#         """For every ordered pair in list, uptick 1 to (x, y) in heatmap matrix.
#         Used in poly-drug posts, uptick each 2-combo by 1 point."""
#         for coord in coords_list:
#             try:
#                 xaxis = coord[0]
#                 yaxis = coord[1]
#                 matrix[xaxis][yaxis] += 1
#             except (AttributeError, TypeError):
#                 matrix[xaxis][yaxis] = 1


# def dict_wo_vals(dict_w_vals):
#     """Takes a dict, returns new dict with None vals for all keys."""
#     copy_dict = OrderedDict.fromkeys(dict_w_vals.keys(), None)
#     return copy_dict


# def parse_poly(drug_list, post_list):
#     """Takes a list of drugs and returns [indicies] based on drug_list.
#     Used for poly drug matches when parsing titles in posts."""
#     coord_list = []
#     for item in post_list:
#         coord_index = drug_list.index(item)
#         coord_list.append(coord_index)

#     print '\nThe indices for {}: {}'.format(post_list, coord_list)
#     return coord_list

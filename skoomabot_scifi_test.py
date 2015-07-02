"""
@author:     Sze "Ron" Chau
@source:     https://github.com/wodiesan/sweet-skoomabot

This script uses Reddit's Python API and Plot.ly in order to visualize
    posts from a given subreddit.

1. Get the last n amount of posts from a given subreddit.
2. Check the title for certain keywords (dictionary).
3. Categorize the titles that contain a match.
4. Visualize the data using plot.ly.

QUICK AND DIRTY SCIFI TEST
PRE-CODE REFACTOR
"""

import praw
import plotly.tools as tls
import time

import skoomabot_config as sbc
import skoomabot_scifi as sbs
import skoomabot_plot as sbp

# Authenticate with plot.ly. This is local (based on generated api key).
creds_plot = tls.get_credentials_file()

#####################################################################
# Identify script to Reddit.
#####################################################################
post_limit = 1000
search_cat = 'Marvel'
sort = 'top'
subred = 'AskScienceFiction'
subreddit = sbp.search_subreddit(subred)

#####################################################################
# Various dictionaries and lists to be used in script.
#####################################################################
# All checked post ids, seperated by whether they contained matches.
checked_id = sbs.sci_checked_id

# Dict that contains the different series that we are matching for.
tag_dict = sbs.sci_dict

# These are used for the axes in various plot.ly visualizations.
py_dict_sci, py_list_sci, py_matrix_sci = sbc.init_axes(tag_dict)

# Testing Marvel and Star Trek subcategories.
py_dict_dc, py_list_dc = sbc.init_subcategory(sbs.dc_cha)
py_dict_marvel, py_list_marvel = sbc.init_subcategory(sbs.marvel_cha)
py_dict_startrek, py_list_startrek = sbc.init_subcategory(sbs.startrek_cha)
py_dict_wh, py_list_wh = sbc.init_subcategory(sbs.warhammer_cha)

#####################################################################
# Run the skoomabot!
#####################################################################

begin = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(time.time()))
print '\nSkoomabot began at {}'.format(begin)

# for submission in subreddit.get_new(limit=post_limit):
for submission in subreddit.search(search_cat, sort=sort, limit=post_limit):
    post = sbp.Post(submission)

    if post.id_num not in checked_id:
        # /r/AskScienceFiction requires titles to have category tags.
        # These are denoted in brackets. Using these for initial check.
        tags, tags_sub = post._tag(tag_dict, post.title)

        if tags:
            checked_id['pos'].append(post.id_num)
            print 'Matched {} with {} tag in title.'.format(tags, tags_sub)
            print '{} posted: {}\n'.format(post.username, post.title)
            scifi = post._category(py_dict_sci, py_list_sci,
                                   py_matrix_sci, tags)

#####################################################################
#            TESTING SUBCATEGORIES USING MARVEL AND STAR TREK
#####################################################################
            if 'dc' in tags:
                post._tag_subcat(py_list_dc, py_dict_dc)
            elif 'marvel' in tags:
                post._tag_subcat(py_list_marvel, py_dict_marvel)
            elif 'star trek' in tags:
                post._tag_subcat(py_list_startrek, py_dict_startrek)
            elif 'warhammer' or '40k' or 'wh40k' in tags:
                post._tag_subcat(py_list_wh, py_dict_wh)
        else:
            checked_id['neg'].append(post.id_num)

print '\n{} out of {} titles have tag matches.'.format(len(checked_id['pos']),
                                                       post_limit)
print 'This leaves {} titles without matches.'.format(len(checked_id['neg']))

finish = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(time.time()))
print '\nSkoomabot ended at {}'.format(finish)

# viz_x_tag = py_list_sci
# viz_y_tag = py_dict_sci.values()

# viz_bar_sci = ('Frequency of series mentioned in the last {} /r/{}'
#                'post titles.'.format(post_limit, subred))
# viz_heat_sci = ('Heatmap of poly-series titles in the last {} /r/{}'
#                 ' posts.'.format(post_limit, subred))

# sbp.viz_bar(viz_bar_sci, viz_x_tag, viz_y_tag, 'skoomabot_bar_scifi')
# sbp.viz_heat(viz_heat_sci, viz_x_tag, py_matrix_sci, 'skoomabot_heat_scifi')

#####################################################################
# Testing subcategories with Dc, Marvel, and Star Trek.
#####################################################################

viz_bar_title = ('Frequency of related terms in the {} {} /r/ {} posts '
                 'tagged {}.'.format(sort, post_limit, subred, search_cat))

# viz_x_dc = py_list_dc
# viz_y_dc = py_dict_dc.values()
# sbp.viz_bar(viz_bar_title, viz_x_dc, viz_y_dc, 'skoomabot_bar_dc')

viz_x_marvel = py_list_marvel
viz_y_marvel = py_dict_marvel.values()
sbp.viz_bar(viz_bar_title, viz_x_marvel, viz_y_marvel, 'skoomabot_bar_marvel')

# viz_x_trek = py_list_startrek
# viz_y_trek = py_dict_startrek.values()
# sbp.viz_bar(viz_bar_title, viz_x_trek, viz_y_trek, 'skoomabot_bar_startrek')

# viz_x_wh = py_list_wh
# viz_y_wh = py_dict_wh.values()
# sbp.viz_bar(viz_bar_title, viz_x_wh, viz_y_wh, 'skoomabot_bar_wh')

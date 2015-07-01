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

# Identify script to Reddit.
user_agent = 'Visualize posts to /r/AskScienceFiction. Version 0.3.1'
r = praw.Reddit(user_agent=user_agent)
subreddit = r.get_subreddit('asksciencefiction', fetch=True)
post_limit = 100

# Authenticate with plot.ly.
creds_plot = tls.get_credentials_file()

start_time = time.time()
print 'Bot started at {}'.format(start_time)

for submission in subreddit.get_new(limit=post_limit):
    post = sbp.Post(submission)

    if post.id_num not in sbs.checked_post:
        sci_tag, sci_tag_sub = post._tag(sbs.sci_dict, post.title)

        if sci_tag:
            print 'Matched: {}'.format(sci_tag_sub)
            print '{}\n'.format(post.title)

#             sci_matches, sci_sub_matches = post._match(sbs.sci_dict,
#                                                        post.title)
#             if sci_matches:
#                 scifi = post._category(sbs.py_dict_sci, sbs.py_list_sci,
#                                        sbs.py_matrix_sci, sci_matches)

#                 if scifi:
#                     print 'Post {} matches: {}'.format(post.id_num, scifi)
#                     print '{} posted: {}\n'.format(post.username, post.title)
#                     sbs.checked_post['pos'].append(post.id_num)

#     #                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     #                # TESTING SUBCATEGORIES
#     #                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                     # for item in slang_sub_matches:
#                     #     if item not in sbc.cannabis:
#                     #         pass
#                     #     else:
#                     #         post._insert_plot_point(sbc.cannabis_subcat_dict, item)
#                 else:
#                     sbs.checked_post['neg'].append(post.id_num)
#             else:
#                 sbs.checked_post['neg'].append(post.id_num)

# print '\n{} out of {} titles have matches.'.format(len(sbs.checked_post['pos']), post_limit)
# print 'This leaves {} out of {} titles without matches.'.format(len(sbs.checked_post['neg']), post_limit)
print '\nBot ended at {}'.format(time.time())

# mainviz_xaxis = sbs.py_list_sci
# mainviz_yaxis = sbs.py_dict_sci.values()
# viz_bar_sci = 'Frequency of characters mentioned in the last {} /r/AskScienceFiction post titles.'.format(post_limit)
# viz_heat_sci = 'Heatmap of poly-character mentions in the last {} /r/AskScienceFiction post titles.'.format(post_limit)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Testing subcategories with marijuana
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# viz_bar_mj = 'Frequency of cannabis terms in the last {} /r/Drugs post titles.'.format(post_limit)
# mjviz_xaxis = sbc.cannabis_subcat_list
# mjviz_yaxis = sbc.cannabis_subcat_dict.values()
# sbp.viz_bar(viz_bar_mj, mjviz_xaxis, mjviz_yaxis, 'skoomabot_bar_mj')

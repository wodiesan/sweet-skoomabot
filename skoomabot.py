"""
@author:     Sze "Ron" Chau
@source:     https://github.com/wodiesan/sweet-skoomabot

This script uses Reddit's Python API and Plot.ly in order to visualize
    posts from the subreddit /r/Drugs. To run (eventually) as a cron job.

1. Get the last n amount of posts from /r/Drugs.
2. Check the title for certain keywords (config file).
3. Categorize the titles that contain a match.
4. Visualize the data using plot.ly.

TODO:
1. Better exceptions.
2. Create individual charts based on sub-category.
3. Refactor and reorg.

FUTURE:
5. Tie it to a db (Google Sheets).
"""

import praw
# from plotly.graph_objs import Bar, Data, Heatmap, Layout, Figure
import plotly.tools as tls
# import plotly.plotly as viz
import time

# import skoomabot_config as sbc
import skoomabot_config as sbc
# import skoomabot_google_func as sbg
import skoomabot_plot as sbp

# Identify script to Reddit.
user_agent = 'Visualize posts to /r/Drugs. Version 0.3.1'
r = praw.Reddit(user_agent=user_agent)
subreddit = r.get_subreddit('Drugs', fetch=True)
post_limit = 1000

# Authenticate with plot.ly.
creds_plot = tls.get_credentials_file()

start_time = time.time()
print 'Bot started at {}'.format(start_time)
# print 'List of worksheets: {}'.format(worksheet_list)

for submission in subreddit.get_new(limit=post_limit):
    post = sbp.Post(submission)

    if post.id_num not in sbc.checked_post:
        set_matches, set_sub_matches = post._match(sbc.setting_dict, post.title)
        setting = post._category(sbc.py_dict_set, sbc.py_list_set,
                                 sbc.py_matrix_set, set_matches)

        slang_matches, slang_sub_matches = post._match(sbc.drug_dict, post.title)
        # if post._match(sbc.drug_dict, post.title):
            # slang_matches = post._match(sbc.drug_dict, post.title)
        if slang_matches:
            slang = post._category(sbc.py_dict_drug, sbc.py_list_drug,
                                   sbc.py_matrix_drug, slang_matches)

            if slang:
                print 'Post {} matches: {}'.format(post.id_num, slang)
                print '{} posted: {}\n'.format(post.username, post.title)
                sbc.checked_post['pos'].append(post.id_num)

                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                # TESTING SUBCATEGORIES
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                for item in slang_sub_matches:
                    if item not in sbc.cannabis:
                        pass
                    else:
                        post._insert_plot_point(sbc.cannabis_subcat_dict, item)
            else:
                sbc.checked_post['neg'].append(post.id_num)
        else:
            sbc.checked_post['neg'].append(post.id_num)


print '\n{} out of {} titles have slang matches.'.format(len(sbc.checked_post['pos']), post_limit)
print 'This leaves {} out of {} titles without matches.'.format(len(sbc.checked_post['neg']), post_limit)
print '\nBot ended at {}'.format(time.time())

# Get the x and y axis. Perhaps a function to do this?
mainviz_xaxis = sbc.py_list_drug
mainviz_yaxis = sbc.py_dict_drug.values()

settingviz_xaxis = sbc.py_list_set
settingviz_yaxis = sbc.py_dict_set.values()

viz_bar_drug = 'Number of appearances of drug types in the last {} /r/Drugs post titles.'.format(post_limit)
viz_bar_set = 'Number of appearances of medical and legal concerns in the last {} posts to /r/Drugs.'.format(post_limit)

viz_heat_drug = 'Heatmap of poly-drug mentions in the last {} /r/Drugs post titles.'.format(post_limit)
viz_heat_set = 'Heatmap of the terms mentioned in the last {} /r/Drugs post titles.'.format(post_limit)

sbp.viz_bar(viz_bar_drug, mainviz_xaxis, mainviz_yaxis, 'skoomabot_bar_drug')
sbp.viz_bar(viz_bar_set, settingviz_xaxis, settingviz_yaxis, 'skoomabot_bar_set')

sbp.viz_heat(viz_heat_drug, mainviz_xaxis, sbc.py_matrix_drug, 'skoomabot_heat_drug')
sbp.viz_heat(viz_heat_set, settingviz_xaxis, sbc.py_matrix_set, 'skoomabot_heat_set')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Testing subcategories with marijuana
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print sbc.cannabis_subcat_dict
viz_bar_mj = 'Frequency of cannabis terms in the last {} /r/Drugs post titles.'.format(post_limit)
mjviz_xaxis = sbc.cannabis_subcat_list
mjviz_yaxis = sbc.cannabis_subcat_dict.values()
sbp.viz_bar(viz_bar_mj, mjviz_xaxis, mjviz_yaxis, 'skoomabot_bar_mj')

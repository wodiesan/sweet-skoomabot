"""
@author:     Sze "Ron" Chau

This script uses Reddit's Python API and Plot.ly in order to visualize
    posts from the subreddit /r/Drugs. To run (eventually) as a cron job.

1. Get the last n amount of posts from /r/Drugs.
2. Check the title for certain keywords (config file).
3. Categorize the titles that contain a match.
4. Visualize the data using plot.ly.

TODO:
1. Better exceptions.
2. Create individual charts based on sub-category.
4. Refactor and reorg.

FUTURE:
5. Tie it to a db (Google Sheets).
"""

import skoomabot_config as dbc
# import skoomabot_google_func as dbgf
import praw
from plotly.graph_objs import Bar, Data, Heatmap, Layout, Figure
import plotly.tools as tls
import plotly.plotly as viz
# import requests
import time

# Identify script to Reddit.
user_agent = 'Visualize posts to /r/Drugs. Version 0.3'
r = praw.Reddit(user_agent=user_agent)
subreddit = r.get_subreddit('Drugs', fetch=True)
post_limit = 1000

# Authenticate with plot.ly.
creds_plot = tls.get_credentials_file()

start_time = time.time()
print 'Bot started at {}'.format(start_time)
# print 'List of worksheets: {}'.format(worksheet_list)

for submission in subreddit.get_new(limit=post_limit):
    post = dbc.Post(submission)

    # Fix dbc.checked_post to check for values in different keys.
    if post.id_num not in dbc.checked_post:
        setting = post._category(dbc.setting_dict, dbc.py_dict_set, dbc.py_list_set, dbc.py_matrix_set, post.title)

        if post._match(dbc.drug_dict):
        # slang returns None if the match is under 3 characters in legnth.
            slang = post._category(dbc.drug_dict, dbc.py_dict_drug, dbc.py_list_drug, dbc.py_matrix_drug, post.title)
            print 'Post {} contains a match for {}:'.format(post.id_num, slang)
            print 'Title: {}\n'.format(post.title)

            if slang:
                dbc.checked_post['pos'].append(post.id_num)
        else:
            dbc.checked_post['neg'].append(post.id_num)

            # TURN submission.id into KEY, and category matches values.


print '\nThere are {} out of {} titles that contain a slang match.'.format(len(dbc.checked_post['pos']), post_limit)
print 'This leaves {} out of {} titles without matches.'.format(len(dbc.checked_post['neg']), post_limit)
print '\nBot ended at {}'.format(time.time())

# Get the x and y axis. Perhaps a function to do this?
# mainviz_xaxis = dbc.py_dict_drug.keys()
mainviz_xaxis = dbc.py_list_drug
mainviz_yaxis = dbc.py_dict_drug.values()

# settingviz_xaxis = dbc.py_dict_set.keys()
settingviz_xaxis = dbc.py_list_set
settingviz_yaxis = dbc.py_dict_set.values()

viz_bar_drug = 'Number of appearances of drug types in the last 1000 /r/Drugs post titles.'
viz_bar_set = 'Number of appearances of medical and legal concerns in the last 1000 posts to /r/Drugs.'

viz_heat_drug = 'Heatmap of poly-drug mentions in the last 1000 /r/Drugs post titles.'
viz_heat_set = 'Heatmap of the terms mentioned in the last 1000 /r/Drugs post titles.'


def viz_bar(graph_name, xaxis, yaxis, filename):
    """Creates a bar graph for plot.ly.
    Takes title, the x and y as lists, and plotly filename."""
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

viz_bar(viz_bar_drug, mainviz_xaxis, mainviz_yaxis, 'skoomabot_bar_drug')
viz_bar(viz_bar_set, settingviz_xaxis, settingviz_yaxis, 'skoomabot_bar_set')

viz_heat(viz_heat_drug, mainviz_xaxis, dbc.py_matrix_drug, 'skoomabot_heat_drug')
viz_heat(viz_heat_set, settingviz_xaxis, dbc.py_matrix_set, 'skoomabot_heat_set')

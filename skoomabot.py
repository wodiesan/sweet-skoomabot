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
2. Create individual charts based on category.
3. Heatmap troubleshooting.
4. Refactor and reorg.

FUTURE:
5. Tie it to a db (Google Sheets).
"""

import druggiebot_config as dbc
# import druggiebot_google_func as dbgf
import praw
from plotly.graph_objs import Bar, Data, Heatmap, Layout, Figure
import plotly.tools as tls
import plotly.plotly as viz
# import requests
import time

# Identify script to Reddit.
user_agent = 'Visualize posts to /r/Drugs. Version 0.1'
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
    if post.id_num not in dbc.checked_post and post._match(dbc.drug_dict):
        slang = post._category(dbc.drug_dict, dbc.plotly_dict, post.title)
        # slang returns None if the match is under 3 characters in legnth.
        if not slang:
            dbc.checked_post['neg'].append(post.id_num)
        else:
            # TURN submission.id into KEY, and category matches values.
            print 'Post {} contains a match for {}:'.format(post.id_num, slang)
            print 'Title: {}\n'.format(post.title)

            dbc.checked_post['pos'].append(post.id_num)
    else:
        dbc.checked_post['neg'].append(post.id_num)

    # Quick and dirty solution to getting the rest of the charts.
    # TODO: Revisit after presentation.
    setting = post._category(dbc.setting_dict, dbc.plotly_dict_set, post.title)

    # if post.id_num not in dbc.checked_post and post._match(dbc.drug_dict):
    #     slang = post._category(dbc.drug_dict, post.title)
    #     # slang returns None if the match is under 3 characters in legnth.
    #     if slang:
    #         dbc.checked_post['pos'].append(post.id_num)
    #         # TURN submission.id into KEY, and category matches values.
    #         print 'Post {} contains a match for {}:'.format(post.id_num, slang)
    #         print 'Title: {}\n'.format(post.title)

    #     else:
    #         dbc.checked_post['neg'].append(post.id_num)

print '\nThere are {} out of {} titles that contain a match.'.format(len(dbc.checked_post['pos']), post_limit)
print 'This leaves {} out of {} titles without matches.'.format(len(dbc.checked_post['neg']), post_limit)
print '\nBot ended at {}'.format(time.time())

# Testing plot.ly using unordered dictionary broken down into key list and val list.
print 'plotly plot points:\n'

# sorted_list = sorted(dbc.plotly_dict.items())
# print  '\nunsorted:'
# print dbc.plotly_dict

mainviz_xaxis = dbc.plotly_dict.keys()
mainviz_yaxis = dbc.plotly_dict.values()
settingviz_xaxis = dbc.plotly_dict_set.keys()
settingviz_yaxis = dbc.plotly_dict_set.values()

mainviz = 'Number of appearances of slang in the last 1000 posts to /r/Drugs'
settingviz = 'Number of appearances of medical and legal concerns in the last 1000 posts to /r/Drugs.'
heatviz = 'Test heatmap of poly-drug posts.'


def viz_bar(graph_name, xaxis, yaxis, filename):
    """Creates a bar graph for plot.ly. Give it a name, the x and y as lists, and a plotly filename."""
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

        # bar_viz = Data([graph_name])
        # layout = Layout(
        #     title=graph_name)
        # fig = Figure(data=bar_viz, layout=layout)
        # # viz.plot(bar_viz, filename=filename)
        # viz.plot(fig, filename=filename)


viz_bar(mainviz, mainviz_xaxis, mainviz_yaxis, 'skoomabot_main')
viz_bar(settingviz, settingviz_xaxis, settingviz_yaxis, 'skoomabot_setting')

# bar_graph = Bar(
#     name=mainviz,
#     x=mainviz_xaxis,
#     y=mainviz_yaxis)
# bar_viz = Data([bar_graph])
# viz.plot(bar_viz, filename = 'skoomabot_main')

# heat_graph = Heatmap(
#     name=heatviz,
#     # z=[[x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11], [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11], [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]],
#     z=[
#         [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ],
#     x=mainviz_xaxis,
#     y=mainviz_xaxis)
# heat_viz = Data([heat_graph])
# viz.plot(heat_viz, filename='skoomabot_heat')

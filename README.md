# skoomabot
A Reddit bot that parses the posts to the subreddits and matches the post titles based on provided dictionaries.
The results are then visualized through plot.ly charts.
This Reddit bot originated as coursework for SOCL 406: Drugs and Society taken in Summer 2015 at Wentworth.
The current focus has shifted towards looking through /r/AskScienceFiction, though any subreddit can be checked.

*This bot authenticates with my Plot.ly account through a credentials file on my machine.*

To make your own charts, you'll have to get an account: [Plot.ly Python User Guide](https://plot.ly/python/user-guide/)

### /r/AskScienceFiction
Per the subreddit's sidebar:

```It's like Ask Science, but all questions and answers are written with answers gleaned from the universe itself.```

[/r/AskScienceFiction](https://www.reddit.com/r/AskScienceFiction/) is fun to look at because of the diverse selection of series and characters that appear.
What's more interesting is that many posts will contain questions that pertain to two different series.

#### By Series in the Last 1000 Posts
*1000 results is Reddit's upstream limitation.*
See [PRAW's Non-obvious behavior](http://praw.readthedocs.org/en/latest/pages/faq.html) for more information.
Anyways:

<div>
    <a href="https://plot.ly/~wodiesan/220/" target="_blank" title="Frequency of series mentioned in the last 1000 /r/AskScienceFiction post titles." style="display: block; text-align: center;"><img src="https://plot.ly/~wodiesan/220.png" alt="Frequency of series mentioned in the last 1000 /r/AskScienceFiction post titles." style="max-width: 100%;"  onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="wodiesan:220" src="https://plot.ly/embed.js" async></script>
</div>

#### Top Series: Marvel
So let's look into the top 1000 posts that are tagged with [Marvel]. We switch sort from 'new' to 'top' (though we can do either), and search with the term 'Marvel'. Now we point towards the key within the dictionary that we're matching for, and...

<div>
    <a href="https://plot.ly/~wodiesan/229/" target="_blank" title="Frequency of related terms in the top 1000 /r/ AskScienceFiction posts tagged Marvel." style="display: block; text-align: center;"><img src="https://plot.ly/~wodiesan/229.png" alt="Frequency of related terms in the top 1000 /r/ AskScienceFiction posts tagged Marvel." style="max-width: 100%;"  onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="wodiesan:229" src="https://plot.ly/embed.js" async></script>
</div>

#### What About the 2nd-Highest Series, DC?

<div>
    <a href="https://plot.ly/~wodiesan/227/" target="_blank" title="Frequency of related terms in the top 1000 /r/ AskScienceFiction posts tagged DC." style="display: block; text-align: center;"><img src="https://plot.ly/~wodiesan/227.png" alt="Frequency of related terms in the top 1000 /r/ AskScienceFiction posts tagged DC." style="max-width: 100%;"  onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="wodiesan:227" src="https://plot.ly/embed.js" async></script>
</div>

Superman beats Batman? Now this is humorous. A little dissapointing that Constantine is barely a blip.

#### ...Skipping Star Wars for Warhammer 40K...
What can I say? I love 40K.

<div>
    <a href="https://plot.ly/~wodiesan/248/" target="_blank" title="Frequency of related terms in the top 1000 /r/ AskScienceFiction posts tagged 40K." style="display: block; text-align: center;"><img src="https://plot.ly/~wodiesan/248.png" alt="Frequency of related terms in the top 1000 /r/ AskScienceFiction posts tagged 40K." style="max-width: 100%;"  onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="wodiesan:248" src="https://plot.ly/embed.js" async></script>
</div>

### Drugs and Society Project

/r/Drugs titles are parsed for a variety of factors, such as: 

1. Occurrences of certain drug slang terms
2. Medical terms
3. Setting
4. Poly-drug mentions
5. Monetary terms
6. Legality keywords

#### Drug Slang By Major Category

<div>
    <a href="https://plot.ly/~wodiesan/104/" target="_blank" title="Number of appearances of drug types in the last 1000 /r/Drugs post titles." style="display: block; text-align: center;"><img src="https://plot.ly/~wodiesan/104.png" alt="Number of appearances of drug types in the last 1000 /r/Drugs post titles." style="max-width: 100%;"  onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="wodiesan:104" src="https://plot.ly/embed.js" async></script>
</div>

#### Drug Slang By Sub-Category: Cannabis

<div>
    <a href="https://plot.ly/~wodiesan/201/" target="_blank" title="Frequency of cannabis terms in the last 1000 /r/Drugs post titles." style="display: block; text-align: center;"><img src="https://plot.ly/~wodiesan/201.png" alt="Frequency of cannabis terms in the last 1000 /r/Drugs post titles." style="max-width: 100%;"  onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="wodiesan:201" src="https://plot.ly/embed.js" async></script>
</div>

#### Heatmap of Drug Combos

<div>
    <a href="https://plot.ly/~wodiesan/108/" target="_blank" title="Heatmap of poly-drug mentions in the last 1000 /r/Drugs post titles." style="display: block; text-align: center;"><img src="https://plot.ly/~wodiesan/108.png" alt="Heatmap of poly-drug mentions in the last 1000 /r/Drugs post titles." style="max-width: 100%;"  onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="wodiesan:108" src="https://plot.ly/embed.js" async></script>
</div>

### So What's Skooma?
Skooma is a fictional narcotic from the Elder Scrolls series. It is refined from moon sugar, a spice that is refined from cane plants. Both skooma and moon sugar serves ceremonial purposes within certain religions. /r/teslore has [a decent introduction on it](https://www.reddit.com/r/teslore/comments/2md0me/an_analysis_on_moon_sugars_and_skoomas_effect_on/). As this bot originated from a Drugs and Society course, I felt that the name was aproros.

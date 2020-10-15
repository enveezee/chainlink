'''
Link handler module for news articles, matches news sites and outputs parsed
articles to a program of your choosing.
'''

__all__ = ['match','parse','openwith']

# newspaper3k - https://newspaper.readthedocs.io/en/latest/
# pip3 install newspaper3k
import newspaper


# to launch associated application for news articles
from subprocess import run

# for user configuration of parser
from yaml import dump, loads

def match(link):
'''
This function checks to see if link matches any of the site sources shipped with
newspaper3k or any user-defined news sites and returns True if there is a match.
'''
    # list of news sites to match against
    news_sites = []

    # find the directory of the newspaper module's resources
    npdir = newspaper.__file__[:-11] + 'resources/misc/'

    # compile a list of news site files (one site per line)
    news = [npdir+'google_sources.txt',npdir+'popular_sources.txt',user_sites]

    # iterate over each news site file and add them to our list of sites
    # note: this will match empty lines, but shouldn't matter as we should not
    # be getting links with no netloc.
    for f in news:
        s = open(f)
        news_sites.extend(s.read().split('\n'))
    s.close()

    # return match of the Link's netloc against our list
    return link.netloc in news_sites

def parse(link, match):
'''
This function parses the link as a news article and returns the formatted output
as defined by the user configuration.
'''
    # create an newspaper Article object for our link
    a=newspaper.Article(link.url)

    # download the article
    a.download()

    # parse the article
    a.parse()

    # needed for natural language processing of keywords, summary
    import nltk

    # see if we are ready for NLP, download resources if needed
    if not nlp():
        nlp()

    ### Output Formatting ###

    # our output string (I see no reason to over complicate this)
    o = ''

    # if the article has a summary
    if a.summary:
        o +='\n\n'
    for l in a.text.split('\n'):
        o += '\n'
    o.write('-----\n')
    if a.authors:
        o += ','.join(a.authors)+'\n'
    if a.publish_date:
        dateStr = a.publish_date.strftime("%d-%b-%Y %H:%M:%S")
        o += dateStr+'\n'
    o += link

    # return formatted output
    return o

def openwith(link, output):

def nlp():
'''
Function to enable NLP, returns True if enabled, False if not.
'''
    # try to enable nlp for our article
    try:
        a.nlp()

    # if nlp failed due to missing resource, download the resource, return False
    except LookupError:
        nltk.download('punkt')
        return False

    # if nlp succeeded, return True
    return True

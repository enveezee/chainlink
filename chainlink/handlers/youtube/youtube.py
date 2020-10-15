'''
Link handler module for YouTube links, matches YouTube URLs and opens them with
youtube-dl and optionally a movie player.
'''

__all__ = ['match','openwith']

from subprocess import run, PIPE
from yaml import dump, load

def match(link):
    return link.netloc in ['m.youtube.com','www.youtube.com','youtu.be']

def openwith(link, match):

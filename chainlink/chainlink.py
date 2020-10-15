#!/usr/bin/python3
from importlib import import_module
from pathlib import Path
from subprocess import run
from sys import argv, path
from urllib.request import HTTPError, Request, urlopen
from urllib.parse import urlparse

try:
    from yaml import dump, load
except ModuleNotFoundError:
    exit('The required module yaml not found, apt install python3-yaml')

class Link(url):
'''
The Link(url) class builds a Link object for a given URL and this object will
be used by handler scripts to process our link.
'''
    # construct and initialize a Link object for our url
    def __init__(self, url):

        # set the configuration options for this object
        self.extensions = config['extensions_file']
        self.proxy = config['proxy']
        self.user_agent = config['user_agent']

        # set the url for this object
        self.url = url

        # parse the url for this object and set the following:
        #<scheme>://<netloc>/<path>;<params>?<query>#<fragment>
        url = urlparse(url)
        self.scheme = url.scheme
        self.netloc = url.netloc
        self.path = url.path
        self.params = url.params
        self.query = url.query
        self.fragment = url.fragment

        # also set the filename at the end of the url path before any params
        self.filename = self.path.split('/')[-1]

        # perform a check that we have recieved an http/https url
        if self.scheme != 'http' or 'https':
            exit("Recieved an invalid url, currently supports http/https only.")

        # if the filename appears to have an extension, check that extension
        if '.' in filename:
            # set this link's extension from our extensions.yaml file
            self.extension = self.checkextension(self.filename)

    def checkextension(self, ext):

        extensions = load(open(Path(self.extensions).expanduser()))

        if ext in extensions:

            return extensions['ext']

        return False

    def checkmimetype(self, response):

        pass

    def open(self, url):
    '''
    This method is for performing an http connection to the link if necessary
    for the handler, using urllib.request with appropriate headers/proxies.
    '''
        # create a urllib.request.Request object req for our url
        req = Request(url)
        # add the headers to the request
        req.add_header('User-Agent',self.user_agent)

        # if we are configured to use a proxy, set the proxy for the request
        if self.proxy:
            req.set_proxy(self.proxy,'http')
            req.set_proxy(self.proxy,'https')

        # attempt to issue the request and get a response, and handle errors
        try:
            self.response = urlopen(req)

        except HTTPError:
            exit('HTTPError occurred, and handling not yet implemented.')

def handle(handler, link):
'''
This function executes a link handler script and returns True if it matched the
link and False if it did not match the link.
'''
    # import the handler script
    handler = import_module(handler)

    # execute the match() function to see if it matches
    match = handler.match(link)

    # if this script matches our link:
    if match:

        # check for a parse function
        if 'parse' in handler.__all__:

            # if there is a parse() function call it and save its output
            output = handler.parse(link, match)

            # call the openwith() function with any output we have
            handler.openwith(link, output)

        else:

            # otherwise we have no parsed output
            handler.openwith(link, match)

        # the openwith() has now handled our link, we can return True
        return True

    else:

        # the current handler did not match our link, we will return False
        return False

### the following code needs to be redone, this is not ideal ###

# look for a config and import settings or generate a local config if needed
global_config = Path('/etc/chainlink/config.yaml')
local_config = Path('~/.config/chainlink/config.yaml').expanduser()

if local_config.exists():

    config = load(open(local_config))

else if global_config.exists():

    config = load(open(global_config))

else:

    config = {
        'extensions_file':'~/.config/chainlink/extensions.yaml'
        'handlers_dir':'~/.config/chainlink/handlers/'
        'proxy':''
        'user_agent':'Mozilla/5.0'
    }

    config_file = open(local_config,'w')
    config_file.write(dump(config))
    config_file.close()

handlers_dir = Path(config['handlers_dir']).expanduser()

# look for an extensions file and import or generate one if needed
global_extensions = Path('/etc/chainlink/extensions.yaml')
local_extensions = Path('~/.config/chainlink/extensions.yaml').expanduser()

if local_config.exists():

    extensions = load(open(local_extensions))

else if global_config.exists():

    extensions = load(open(global_extensions))

else:

    extensions = {}

    extensions_file = open(Path(local_extensions).expanduser(),'w')
    extensions_file.write(dump(config))
    extensions_file.close()

##############################################################

# if this script is called directly as a link handler script:
if __name__ == __main__:

    # read our link from stdin and create a Link object for it
    link = Link(argv[1])

    # append handlers_dir to sys.path
    sys.path += [str(handlers_dir)]

    # iterate over all scripts in the handlers_dir to see if they match our link
    for handler in handlers_dir.glob('*.py')

        # handle each script and check its return value
        handled = handle(str(handler).split('/')[-1][:-3], link)

        # if the script handled our link, exit successfully
        if handled:
            exit(0)

        # if the script did not handle our link, try the next one

    # if not handled, trigger sensible-browser to handle the link
    run(['sensible-browser',link.url])

    # then exit successfully
    exit(0)

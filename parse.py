from urllib.parse import quote
from urllib.parse import unquote
from urllib.parse import urlparse
import re


# any url with encoding or decoding already, all considered as encoding parsing
def parseUrl(*args, **kwargs):
    return quote(unquote(*args, **kwargs), safe=':, /')


# get the name from the encoding url
def parseName(*args, **kwargs):
    tuples = re.findall(r'/([\w\-\.]+).html|/([\w\-\.]+)', urlparse(unquote(*args, **kwargs)).path)[0]
    name = [t for t in tuples if t][0]
    return name


# following examples as below
# print(parseName('https://dangtoon15.com/결혼하는-남자-연재-8화-8-화.html', encoding='utf-8', errors='replace'))
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def wasistderartikel():
    urlinp = input("Wort:")
    wort = urlinp.capitalize()
    url = "https://www.verbformen.de/?w=" + urlinp
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    umlaut = None
    wortbeginn = None
    wort4 = None

    tag = soup.td
    artikel = tag.string

    tags = soup.find_all("b")
    for tag in tags:
        if len(tag.contents) > 1:
            if len(tag.contents[1]) != len(urlinp):
                wortbeginn = tag.contents[1]
                umlaut = tag.contents[2].string
                wort3 = tag.contents[3].string
                if len(tag.contents) > 4:
                    wort4 = tag.contents[4].string
            if wortbeginn is None:
                wortbeginn = tag.contents[1]
                wort2 = tag.contents[2].string

    if umlaut is None:
        if wort2 is None: plural = wortbeginn
        plural = wortbeginn + wort2
    if umlaut is not None:
        plural = wortbeginn + umlaut
        if wort3 is not None:
            plural = wortbeginn + umlaut + wort3
        if wort4 is not None:
            plural = wortbeginn + umlaut + wort3 + wort4

    print(artikel, wort, plural)

while True:
    wasistderartikel()
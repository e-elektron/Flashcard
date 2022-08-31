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

    tag = soup.td
    artikel = tag.string

    plural = None

    tags = soup.find_all("b")
    plural = tags[2].get_text()

    print(artikel, wort, plural)
while True:
    wasistderartikel()
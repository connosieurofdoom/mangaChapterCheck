from urllib.request import Request, urlopen
import re


def pg404Check(li):
    req = Request(li, headers={'User-Agent': 'Mozilla/5.0'})
    html_content = urlopen(req).read()
    matches = re.findall('404 - PAGE NOT FOUND', html_content.decode())
    if len(matches) == 0:
        return True
    else:
        return False

#print(pg404Check("https://readmanganato.com/manga-fh982716/chapter-111"))
#print(pg404Check("https://readmanganato.com/manga-fh982716/chapter-113"))
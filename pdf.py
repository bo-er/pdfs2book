import re
import os
import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlparse
from PyPDF2 import PdfMerger
import argparse

'''
argparse to enable finicky command-line args
'''
parser = argparse.ArgumentParser()
parser.add_argument('-w', '--website_url',
                    help='a website that contains multiple links to pdf files')
parser.add_argument(
    '-o', '--output', help='directory to save the downloaded pdf files')
parser.add_argument('-p', '--prefix', default='none',
                    help='specify pdf filename prefix')
parser.add_argument('-s', '--suffix', default='none',
                    help='specify pdf filename suffix')
args = parser.parse_args()

# HTML Parse URL
url_link = str(args.website_url)
# directory to save downloaded pdf files
sys_path = str(args.output)
prefix = str(args.prefix)
suffix = str(args.suffix)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

website = urlopen(url_link, context=ctx)

# Decode website into string string
soup = BeautifulSoup(website.read(), features="html.parser")
links = []
local_links = []
divs = soup.find_all('a', attrs={'href': re.compile(".pdf$")})
for div in divs:
    href = div.get('href')
    if href.find("http") == -1:
        local_links.append(href)
    else:
        links.append(href)

# Download non-hosted PDFs
for link in links:
    command = 'wget'
    os.system("%s %s -P %s" % (command, link, sys_path))

# Download local/hosted PDFs
pdfNames = []
for link in local_links:
    if not prefix == 'none' and not link.startswith(prefix):
        continue
    if not suffix == 'none' and not link.endwith(prefix):
        continue
    command = 'wget'
    filename = last = link.rsplit('/', 1)[-1]
    os.system("%s -nc '%s/%s' -P %s" % (command, url_link, link, sys_path))
    p = os.path.abspath(sys_path)
    pdfNames.append(os.path.join(p, filename))

merger = PdfMerger()
for pdf in pdfNames:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

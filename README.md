## Usage

pdfs2book can be useful when you want to download all pdfs of a webpage and merge all of them.
for example, using the following command to download the CS251 course slides as a book:

```
python3 pdf.py -w https://www.cs.purdue.edu/homes/ayg/CS251/slides -o ./CS251
```
### Tip
using `-p`/`-s` to specify prefix/suffix of the pdf files you want.

### Flags

```
usage: pdf [-h] [-w WEBSITE_URL] [-o OUTPUT] [-p PREFIX] [-s SUFFIX]

optional arguments:
  -h, --help            show this help message and exit
  -w WEBSITE_URL, --website_url WEBSITE_URL
                        a website that contains multiple links to pdf files
  -o OUTPUT, --output OUTPUT
                        directory to save the downloaded pdf files
  -p PREFIX, --prefix PREFIX
                        specify pdf filename prefix
  -s SUFFIX, --suffix SUFFIX
                        specify pdf filename suffix

```

## Requirements

- argparse
- urllib
- requests
- wget
- PyPDF2
- python >= 3.5

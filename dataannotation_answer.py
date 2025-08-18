import requests
import re
from bs4 import BeautifulSoup

def print_grid_from_doc(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    text = soup.get_text()

    # Regex to match lines like: U+2580 at (0,0)
    pattern = re.compile(r'U\+([0-9A-F]+)\s+at\s+\(\s*(\d+)\s*,\s*(\d+)\s*\)')
    grid = {}
    xs = ys = []

    for m in pattern.finditer(text):
        code, xs_, ys_ = m.groups()
        x, y = int(xs_), int(ys_)
        ch = chr(int(code, 16))
        grid[(x, y)] = ch
        xs.append(x); ys.append(y)

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    # Print rows — note increasing y goes *downwards* in the doc
    for y in range(min_y, max_y + 1):
        line = ''.join(grid.get((x, y), ' ') for x in range(min_x, max_x + 1))
        print(line)

# Run on the provided doc
print_grid_from_doc(
    "https://docs.google.com/document/d/e/"
    "2PACX-1vQ7pg9TOb1nHtKVrNN8T-HZ_DRgZuxVkInGVNTe1pSoTvaILRY0rbw2QnvLKS2WLOjM8-1ckBE8Jt5P/pub"
)

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find the hero-banner block and remove it entirely
pattern = re.compile(r'<div class="hero-banner".*?</div>', re.DOTALL)

if pattern.search(html):
    html = pattern.sub('', html, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

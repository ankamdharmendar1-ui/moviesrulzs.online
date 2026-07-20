import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find the search bar block
pattern = re.compile(r'<div id="search">.*?</div>\s*<div style="margin-top:-20px;" class="autocomplete-result"></div>', re.DOTALL)

# Let's also have a fallback pattern just in case autocomplete-result is missing or slightly different
fallback_pattern = re.compile(r'<div id="search">.*?</div>', re.DOTALL)

if pattern.search(html):
    html = pattern.sub('', html)
elif fallback_pattern.search(html):
    html = fallback_pattern.sub('', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

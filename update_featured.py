import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the heading text
html = html.replace('Featured Movies Free', 'movierulzs.online latest movies')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

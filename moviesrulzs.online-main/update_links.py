import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace asset URLs with relative paths
html = html.replace('https://www.5movierulz.house/style.css', 'style.css')
html = html.replace('https://www.5movierulz.house/favicon.ico', 'favicon.ico')
html = html.replace('https://www.5movierulz.house/uploads/', 'uploads/')
html = html.replace('https://www.5movierulz.house/images/', 'images/')

# Replace remaining absolute URLs (like canonical and OpenGraph tags) to new domain
html = html.replace('https://www.5movierulz.house/', 'https://movierulzs.online/')

# Now we have href='https://movierulzs.online/...' everywhere
# But movie links (which end with .html) should redirect to original
def revert_movie_links(match):
    return 'href="https://www.5movierulz.house/' + match.group(1) + '"'

html = re.sub(r'href=\"https://movierulzs.online/([a-zA-Z0-9\-]+\-[0-9]+\.html)\"', revert_movie_links, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

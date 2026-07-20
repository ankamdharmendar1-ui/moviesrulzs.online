import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update title
html = re.sub(r'<title>.*?</title>', '<title>MovieRulz | movierulzs.online - Latest Telugu, Tamil, Malayalam, Hindi Movies</title>', html)

# Update or insert meta description
desc_pattern = r'<meta name="description" content=".*?">'
new_desc = '<meta name="description" content="movierulzs.online is the new home for MovieRulz. Get the latest updates on Telugu, Tamil, Malayalam, and Hindi movies, cast, and synopses.">'
if re.search(desc_pattern, html):
    html = re.sub(desc_pattern, new_desc, html)
else:
    html = html.replace('<head>', f'<head>\n{new_desc}')

# Add meta keywords (even though Google ignores them, it's often expected for basic SEO requests)
keywords_tag = '<meta name="keywords" content="movierulz, movierulzs.online, latest telugu movies, tamil movies, malayalam movies, hindi movies, indian cinema">'
if '<meta name="keywords"' not in html:
    html = html.replace(new_desc, f'{new_desc}\n{keywords_tag}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

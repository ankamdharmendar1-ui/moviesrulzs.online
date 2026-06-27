import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the site title
html = html.replace('<h1 id="site-title"><a href="/">MovieRulz</a></h1>', 
                    '<h1 id="site-title"><a href="/">MovieRulzs.online</a></h1>')

# Replace the site description
html = html.replace('<h2 id="site-description">Latest Indian Movies — Telugu, Tamil, Malayalam & Hindi</h2>', 
                    '<h2 id="site-description">Latest Telugu movies from movierulzs.online</h2>')

# Just to be safe if the em-dash was encoded differently
html = re.sub(r'<h2 id="site-description">Latest Indian Movies.*?</h2>', 
              '<h2 id="site-description">Latest Telugu movies from movierulzs.online</h2>', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

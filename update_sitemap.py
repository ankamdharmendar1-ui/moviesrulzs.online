import re

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace https://movierulzs.online with https://www.movierulzs.online
# Using regex to ensure we only target the domain and not accidentally modify something else 
# (though a simple string replace is likely safe here as well)
new_content = content.replace('https://movierulzs.online', 'https://www.movierulzs.online')

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(new_content)

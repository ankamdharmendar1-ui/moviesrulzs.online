import re
import os
from datetime import datetime

base_url = "https://movierulzs.online"
index_path = "c:/Users/DHARMENDAR/OneDrive/Desktop/movierulzs.online/index.html"
sitemap_path = "c:/Users/DHARMENDAR/OneDrive/Desktop/movierulzs.online/sitemap.xml"

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all href attributes
pattern = r'href="([^"]+)"'
urls = set(re.findall(pattern, content))

valid_urls = set()
for url in urls:
    if url.startswith(base_url):
        valid_urls.add(url)
    elif url.startswith('/') and not url.startswith('//'):
        valid_urls.add(base_url + url)

# Make sure root is in there
valid_urls.add(base_url + "/")

# Generate sitemap.xml
today = datetime.now().strftime('%Y-%m-%d')

xml = ['<?xml version="1.0" encoding="UTF-8"?>']
xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for url in sorted(valid_urls):
    xml.append('  <url>')
    xml.append(f'    <loc>{url}</loc>')
    xml.append(f'    <lastmod>{today}</lastmod>')
    xml.append('    <changefreq>weekly</changefreq>')
    xml.append('    <priority>0.8</priority>')
    xml.append('  </url>')

xml.append('</urlset>')

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(xml))

print(f"Sitemap generated with {len(valid_urls)} URLs.")

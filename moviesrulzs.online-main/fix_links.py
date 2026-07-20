import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any movie-like .html links back to the original domain
# Make sure we don't accidentally replace the site's own new pages if they use absolute URLs
# The new pages use relative URLs (like href="/about.html"), so this regex is safe.
html = re.sub(r'href="https://movierulzs\.online/([^"]+\.html)"', r'href="https://www.5movierulz.support/\1"', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Movie links fixed successfully.")

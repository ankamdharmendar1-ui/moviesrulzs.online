import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find the directory-intro block
pattern = re.compile(r'<div class="directory-intro">.*?</div>', re.DOTALL)

new_intro = """<div class="hero-banner" style="background: linear-gradient(135deg, #1a1c23 0%, #2a2d39 100%); border-left: 4px solid #ff7b09; border-radius: 6px; padding: 25px 30px; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
    <h2 style="color: #ffffff; font-size: 24px; margin-bottom: 12px; font-weight: 700; display: flex; align-items: center; gap: 10px; border-bottom: none; padding-bottom: 0;">
        <span style="color: #ff7b09;">🎬</span> Welcome to MovieRulzs.online
    </h2>
    <p style="color: #cbd5e1; font-size: 15px; line-height: 1.6; margin-bottom: 20px; max-width: 800px;">
        Your ultimate destination for the magic of Indian cinema. Discover high-quality streams, detailed cast information, and the latest media updates for top-tier Tollywood, Bollywood, Kollywood, and Mollywood releases.
    </p>
    <div style="display: flex; gap: 12px; flex-wrap: wrap;">
        <a href="/category/telugu-featured" style="background: rgba(255,123,9,0.1); border: 1px solid #ff7b09; color: #ff7b09; padding: 8px 16px; border-radius: 20px; font-size: 13px; text-decoration: none; font-weight: 600; transition: all 0.3s ease;" onmouseover="this.style.background='#ff7b09'; this.style.color='#fff'" onmouseout="this.style.background='rgba(255,123,9,0.1)'; this.style.color='#ff7b09'">🔥 Trending Telugu</a>
        <a href="/category/tamil-featured" style="background: #2b2e38; border: 1px solid #3f4452; color: #a1abbc; padding: 8px 16px; border-radius: 20px; font-size: 13px; text-decoration: none; font-weight: 600; transition: all 0.3s ease;" onmouseover="this.style.background='#3f4452'; this.style.color='#fff'" onmouseout="this.style.background='#2b2e38'; this.style.color='#a1abbc'">Tamil Hits</a>
        <a href="/category/malayalam-featured" style="background: #2b2e38; border: 1px solid #3f4452; color: #a1abbc; padding: 8px 16px; border-radius: 20px; font-size: 13px; text-decoration: none; font-weight: 600; transition: all 0.3s ease;" onmouseover="this.style.background='#3f4452'; this.style.color='#fff'" onmouseout="this.style.background='#2b2e38'; this.style.color='#a1abbc'">Malayalam Classics</a>
        <a href="/category/bollywood-featured" style="background: #2b2e38; border: 1px solid #3f4452; color: #a1abbc; padding: 8px 16px; border-radius: 20px; font-size: 13px; text-decoration: none; font-weight: 600; transition: all 0.3s ease;" onmouseover="this.style.background='#3f4452'; this.style.color='#fff'" onmouseout="this.style.background='#2b2e38'; this.style.color='#a1abbc'">Bollywood Blockbusters</a>
    </div>
</div>"""

if pattern.search(html):
    html = pattern.sub(new_intro, html, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

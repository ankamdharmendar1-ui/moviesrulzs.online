import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find the hero-banner block
pattern = re.compile(r'<div class="hero-banner".*?</div>', re.DOTALL)

new_intro = """<div class="hero-banner" style="background: linear-gradient(135deg, #1a1c23 0%, #2a2d39 100%); border-left: 4px solid #ff7b09; border-right: 4px solid #ff7b09; border-radius: 6px; padding: 15px 20px; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); width: 100%; box-sizing: border-box;">
    <h2 style="color: #ffffff; font-size: clamp(18px, 5vw, 24px); margin: 0; font-weight: 700; display: flex; align-items: center; justify-content: center; gap: 10px; border-bottom: none; padding-bottom: 0; text-align: center; word-break: break-word;">
        <span style="color: #ff7b09;">🎬</span> Welcome to MovieRulzs.online
    </h2>
</div>"""

if pattern.search(html):
    html = pattern.sub(new_intro, html, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

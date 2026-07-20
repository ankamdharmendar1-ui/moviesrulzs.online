import re

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

# Pattern to find the footer wrapper and colophon
pattern = re.compile(r'<div class="footer-wrapper">.*?</script>\s*</body>', re.DOTALL)

new_footer = """<div class="footer-wrapper">
    <h2>Welcome to MovieRulzs.online</h2>
    <p>MovieRulzs.online is your go-to destination for discovering Indian movies. We provide up-to-date information on the latest Telugu, Tamil, Malayalam, and Hindi cinema.</p>
    <hr>
    <h2>Quick Links</h2>
    <p><a href="/" style="color:#b5b5b5; text-decoration:none;">Home</a> | <a href="/category/telugu-featured" style="color:#b5b5b5; text-decoration:none;">Telugu</a> | <a href="/category/tamil-featured" style="color:#b5b5b5; text-decoration:none;">Tamil</a></p>
    <hr>
    <h2>Contact Us</h2>
    <p>For any inquiries, reach out to us at <strong>contact@movierulzs.online</strong>.</p>
</div>

<footer id="colophon" role="contentinfo">
    <div id="site-generator">
        <p><strong>MovieRulzs.online</strong> &mdash; Indian Movie Database</p>
        <p style="font-size: 12px; color: #666; margin-top: 10px;">
            &copy; 2026 MovieRulzs.online. All Rights Reserved.
        </p>
    </div>
</footer>
</body>"""

# Replace in html
new_html = pattern.sub(new_footer, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

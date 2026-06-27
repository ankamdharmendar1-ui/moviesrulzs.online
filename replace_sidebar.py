import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find the widget_movie_recent_post_widget block
pattern = re.compile(r'<li class="widget widget_movie_recent_post_widget">.*?</li>\s*</ul><!-- end sidebar -->', re.DOTALL)

blog_content = """<li class="widget">
    <h2 class="widget-title" style="color: #ff7b09; border-bottom: 1px solid #444855; padding-bottom: 10px; margin-bottom: 15px;">The Magic of Indian Cinema</h2>
    <div style="color: #cbd5e1; font-size: 13px; line-height: 1.7;">
        <p style="margin-bottom: 10px;">
            Indian cinema isn't just about movies; it's an emotion. It all started back in 1913 when Dadasaheb Phalke brought <em>Raja Harishchandra</em> to the silver screen. Since then, the industry has grown into a vibrant, colorful, and massive phenomenon we lovingly know as Bollywood, Tollywood, Kollywood, and more.
        </p>
        <p style="margin-bottom: 10px;">
            From the golden age of black-and-white classics in the 1950s—where legends like Raj Kapoor and Guru Dutt spun tales of romance and social realism—to the action-packed "masala" entertainers of the 70s and 80s led by the iconic Amitabh Bachchan and Rajinikanth, Indian movies have always mirrored the soul of the nation.
        </p>
        <p style="margin-bottom: 10px;">
            Today, our cinema is going global. Movies like <em>Baahubali</em>, <em>RRR</em>, and <em>Dangal</em> have shattered boundaries, proving that great storytelling knows no language. Whether it's a heartwarming Malayalam drama, a high-octane Telugu blockbuster, or a soulful Bollywood romance, Indian movies continue to weave magic into our lives.
        </p>
        <p style="font-style: italic; color: #94a3b8; margin-top: 15px;">
            Grab some popcorn, dim the lights, and let the magic unfold on MovieRulzs.online!
        </p>
    </div>
</li>
</ul><!-- end sidebar -->"""

new_html = pattern.sub(blog_content, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

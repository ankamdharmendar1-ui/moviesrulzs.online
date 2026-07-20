import os
import re

source_file = r"C:\Users\DHARMENDAR\.gemini\antigravity\brain\110b8a39-e58a-4780-887c-ed7aa39e0df7\.system_generated\steps\61\content.md"
target_html = r"c:\Users\DHARMENDAR\OneDrive\Desktop\movierulzs.online\index.html"

with open(source_file, 'r', encoding='utf-8') as f:
    src_content = f.read()

with open(target_html, 'r', encoding='utf-8') as f:
    target_content = f.read()

# 1. Update Title and Meta Tags
target_content = re.sub(
    r'<title>.*?</title>',
    r'<title>MovieRulz | movierulzs.online - Indian Movies - Telugu, Tamil, Malayalam, Hindi</title>',
    target_content
)
target_content = re.sub(
    r'<meta name="description" content=".*?">',
    r'<meta name="description" content="movierulzs.online: Director, cast, synopsis and media updates for Telugu, Tamil, Malayalam and Hindi movies. Updated daily.">',
    target_content
)
target_content = re.sub(
    r'<meta property="og:title" content=".*?">',
    r'<meta property="og:title" content="MovieRulz | Indian Movies - Telugu, Tamil, Malayalam, Hindi">',
    target_content
)

# 2. Update H1 and H2
target_content = re.sub(
    r'<h1 id="site-title"><a href="/">.*?</a></h1>',
    r'<h1 id="site-title"><a href="/">MovieRulzs.online</a></h1>',
    target_content
)
target_content = re.sub(
    r'<h2 id="site-description">.*?</h2>',
    r'<h2 id="site-description">Latest Indian Movies — Telugu, Tamil, Malayalam & Hindi</h2>',
    target_content
)

# 3. Add Search Bar (Extract from src_content)
search_match = re.search(r'(<div id="search">.*?</div>)', src_content, re.DOTALL)
if search_match:
    search_html = search_match.group(1)
    # Inject after </header><!-- #branding --> if it doesn't already exist
    if '<div id="search">' not in target_content:
        target_content = target_content.replace('</header><!-- #branding -->', '</header><!-- #branding -->\n' + search_html)

# 4. Update Sidebar with Widgets
# The target site has:
# <li class="widget widget_movie_recent_post_widget">...</li>
# <li id="text-2" class="widget widget_text">...</li>
# <li id="text-3" class="widget widget_text">...</li>

sidebar_widgets = ""
recent_match = re.search(r'(<li class="widget widget_movie_recent_post_widget">.*?</li>)', src_content, re.DOTALL)
if recent_match:
    sidebar_widgets += recent_match.group(1) + "\n"

text2_match = re.search(r'(<li id="text-2" class="widget widget_text">.*?</li>)', src_content, re.DOTALL)
if text2_match:
    sidebar_widgets += text2_match.group(1) + "\n"

text3_match = re.search(r'(<li id="text-3" class="widget widget_text">.*?</li>)', src_content, re.DOTALL)
if text3_match:
    sidebar_widgets += text3_match.group(1) + "\n"

# Replace the existing sidebar content with the new widgets
# Currently, the sidebar is <ul id="sidebar" role="complementary"> ... </ul><!-- end sidebar -->
# We keep the Magic of Indian Cinema widget, but prepend the new widgets.
if sidebar_widgets:
    if "The Magic of Indian Cinema" in target_content:
        # Prepend to existing sidebar
        target_content = re.sub(
            r'(<ul id="sidebar" role="complementary">\s*)',
            r'\g<1>' + sidebar_widgets.replace('\\', '\\\\'),
            target_content
        )
    else:
        # Replace entirely if the old one is gone
        target_content = re.sub(
            r'<ul id="sidebar" role="complementary">.*?</ul><!-- end sidebar -->',
            f'<ul id="sidebar" role="complementary">\n{sidebar_widgets}\n</ul><!-- end sidebar -->',
            target_content,
            flags=re.DOTALL
        )

# Fix links in the sidebar to point to relative or movierulzs.online instead of 5movierulz.support
target_content = target_content.replace('href="https://www.5movierulz.support', 'href="https://movierulzs.online')

with open(target_html, 'w', encoding='utf-8') as f:
    f.write(target_content)

print("Applied On-Page SEO successfully!")

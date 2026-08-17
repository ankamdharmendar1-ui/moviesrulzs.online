import os
import re
import urllib.request
import shutil
import html

source_file = r"C:\Users\DHARMENDAR\.gemini\antigravity\brain\f1ddc42a-873f-4f9d-8f44-2303b4839e6d\.system_generated\steps\138\content.md"
target_html = r"c:\Users\DHARMENDAR\Downloads\movierulzs.online\index.html"
uploads_dir = r"c:\Users\DHARMENDAR\Downloads\movierulzs.online\uploads"

os.makedirs(uploads_dir, exist_ok=True)

with open(source_file, 'r', encoding='utf-8') as f:
    src_content = f.read()

# Pattern for Featured Movies Free (the first featured block)
featured_pattern = re.compile(r'<div class="featured">.*?<ul>(.*?)</ul>', re.DOTALL)
# Pattern for Latest Movies (the second featured block)
latest_pattern = re.compile(r'<div class="featured lastest">.*?<ul>(.*?)</ul>', re.DOTALL)
# Pattern for Recent & Updated Movies sidebar
sidebar_pattern = re.compile(r'<h2 class="widget-title">Recent and Updated Movies</h2>\s*<ul>(.*?)</ul>', re.DOTALL)

src_featured = featured_pattern.search(src_content)
src_latest = latest_pattern.search(src_content)
src_sidebar = sidebar_pattern.search(src_content)

if not src_featured or not src_latest or not src_sidebar:
    print("Could not find movie lists in source.")
    if not src_featured: print("Missing Featured")
    if not src_latest: print("Missing Latest")
    if not src_sidebar: print("Missing Sidebar")
    exit(1)

def process_movies(html_block):
    li_pattern = re.compile(r'<li>(.*?)</li>', re.DOTALL)
    movies = []
    
    for match in li_pattern.finditer(html_block):
        li_content = match.group(1).strip()
        if not li_content:
            continue
            
        a_match = re.search(r'<a.*?title="(.*?)".*?href="(.*?)"', li_content)
        if not a_match:
            a_match = re.search(r'<a.*?href="(.*?)".*?title="(.*?)"', li_content)
            if a_match:
                href, title = a_match.groups()
            else:
                continue
        else:
            title, href = a_match.groups()
            
        img_match = re.search(r'<img.*?src="(.*?)".*?alt="(.*?)"', li_content)
        if not img_match:
            img_match = re.search(r'<img.*?alt="(.*?)".*?src="(.*?)"', li_content)
            if img_match:
                img_alt, img_src = img_match.groups()
            else:
                img_src, img_alt = "", ""
        else:
            img_src, img_alt = img_match.groups()
            
        if title and href and img_src:
            img_filename = img_src.split('/')[-1]
            local_img_path = os.path.join(uploads_dir, img_filename)
            local_img_url = f"uploads/{img_filename}"
            
            # Ensure full url for image
            full_img_src = img_src
            if not img_src.startswith("http"):
                full_img_src = "https://www.5movierulz.watch" + ("/" if not img_src.startswith("/") else "") + img_src
            
            if not os.path.exists(local_img_path):
                try:
                    req = urllib.request.Request(
                        full_img_src, 
                        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
                    )
                    with urllib.request.urlopen(req, timeout=10) as response, open(local_img_path, 'wb') as out_file:
                        shutil.copyfileobj(response, out_file)
                    print(f"Downloaded {img_filename}")
                except Exception as e:
                    print(f"Failed to download {full_img_src}: {e}")
            
            normalized_href = href
            if not href.startswith("http"):
                normalized_href = "https://www.5movierulz.watch" + ("/" if not href.startswith("/") else "") + href
            
            movies.append(f'''
				<li>
					<div class="boxed film">
						<div class="cont_display">
							<a title="{html.escape(title)}" href="{normalized_href}">
								<img width="165" height="220" src="{local_img_url}" class="attachment-post-thumbnail size-post-thumbnail wp-post-image" alt="{html.escape(img_alt)}"></a>
						</div>
						<p><b>{html.escape(title)}</b></p>
					</div>
				</li>''')
    
    return "\n\t\t\t\t".join(movies)

def process_sidebar(html_block):
    li_pattern = re.compile(r'<li>(.*?)</li>', re.DOTALL)
    items = []
    
    for match in li_pattern.finditer(html_block):
        li_content = match.group(1).strip()
        if not li_content:
            continue
            
        a_match = re.search(r'<a.*?title="(.*?)".*?href="(.*?)"', li_content)
        if not a_match:
            a_match = re.search(r'<a.*?href="(.*?)".*?title="(.*?)"', li_content)
            if a_match:
                href, title = a_match.groups()
            else:
                continue
        else:
            title, href = a_match.groups()
            
        if title and href:
            normalized_href = href
            if not href.startswith("http"):
                normalized_href = "https://www.5movierulz.watch" + ("/" if not href.startswith("/") else "") + href
                
            items.append(f'''
			<li>
			<a title="{html.escape(title)}" href="{normalized_href}">{html.escape(title)}</a>
			</li>''')
            
    return "\n\t".join(items)

new_featured_html = process_movies(src_featured.group(1))
new_latest_html = process_movies(src_latest.group(1))
new_sidebar_html = process_sidebar(src_sidebar.group(1))

with open(target_html, 'r', encoding='utf-8') as f:
    target_content = f.read()

# Replace featured block
target_content = re.sub(
    r'(<div class="featured">\s*<h2 class="line_table">[^<]*</h2>\s*<div class="content home_style">\s*<div class="clear"></div>\s*<ul>).*?(</ul>)',
    r'\1\n\t\t\t\t' + new_featured_html.replace('\\', '\\\\') + r'\n\t\t\t\2',
    target_content,
    flags=re.DOTALL
)

# Replace latest block
target_content = re.sub(
    r'(<div class="featured lastest">\s*<h2 class="line_table">[^<]*</h2>\s*<div class="content home_style">\s*<div class="clear"></div>\s*<ul>).*?(</ul>)',
    r'\1\n\t\t\t\t' + new_latest_html.replace('\\', '\\\\') + r'\n\t\t\t\2',
    target_content,
    flags=re.DOTALL
)

# Replace sidebar block
target_content = re.sub(
    r'(<h2 class="widget-title">Recent and Updated Movies</h2>\s*<ul>).*?(?=<li id="text-2" class="widget widget_text">)',
    r'\1\n\t' + new_sidebar_html.replace('\\', '\\\\') + r'\n\t</ul>\n',
    target_content,
    flags=re.DOTALL
)

# Also update any other movie links (.pictures, .vote, .support, etc.) to .watch
target_content = re.sub(r'https?://www\.5movierulz\.(vote|support|house|online|pictures)/', 'https://www.5movierulz.watch/', target_content)

with open(target_html, 'w', encoding='utf-8') as f:
    f.write(target_content)

print("Updated index.html successfully with new movies and sidebar links pointing to 5movierulz.watch.")

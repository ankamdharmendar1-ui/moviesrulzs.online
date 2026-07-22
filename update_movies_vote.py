import os
import re
import urllib.request
import shutil
import html

source_file = r"vote_site.html"
target_html = r"index.html"
uploads_dir = r"uploads"

os.makedirs(uploads_dir, exist_ok=True)

with open(source_file, 'r', encoding='utf-8') as f:
    src_content = f.read()

featured_pattern = re.compile(r'<div class="featured">.*?<ul>(.*?)</ul>', re.DOTALL)
latest_pattern = re.compile(r'<div class="featured lastest">.*?<ul>(.*?)</ul>', re.DOTALL)

src_featured = featured_pattern.search(src_content)
src_latest = latest_pattern.search(src_content)

if not src_featured or not src_latest:
    print("Could not find movie lists in source.")
    exit(1)

def process_movies(html_block):
    li_pattern = re.compile(r'<li>(.*?)</li>', re.DOTALL)
    movies = []
    
    for match in li_pattern.finditer(html_block):
        li_content = match.group(1)
        
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
            
            full_img_src = img_src if img_src.startswith("http") else "https://www.5movierulz.vote" + img_src
            
            if not os.path.exists(local_img_path):
                try:
                    req = urllib.request.Request(
                        full_img_src, 
                        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
                    )
                    with urllib.request.urlopen(req) as response, open(local_img_path, 'wb') as out_file:
                        shutil.copyfileobj(response, out_file)
                    print(f"Downloaded {img_filename}")
                except Exception as e:
                    print(f"Failed to download {full_img_src}: {e}")
            
            movies.append(f'''
				<li>
					<div class="boxed film">
						<div class="cont_display">
							<a title="{html.escape(title)}" href="{href}">
								<img width="165" height="220" src="{local_img_url}" class="attachment-post-thumbnail size-post-thumbnail wp-post-image" alt="{html.escape(img_alt)}"></a>
						</div>
						<p><b>{html.escape(title)}</b></p>
					</div>
				</li>''')
    
    return "\n\t\t\t\t".join(movies)

new_featured_html = process_movies(src_featured.group(1))
new_latest_html = process_movies(src_latest.group(1))

with open(target_html, 'r', encoding='utf-8') as f:
    target_content = f.read()

target_content = re.sub(
    r'(<div class="featured">\s*<h2 class="line_table">[^<]*</h2>\s*<div class="content home_style">\s*<div class="clear"></div>\s*<ul>).*?(</ul>)',
    r'\1\n\t\t\t\t' + new_featured_html.replace('\\', '\\\\') + r'\n\t\t\t\2',
    target_content,
    flags=re.DOTALL
)

target_content = re.sub(
    r'(<div class="featured lastest">\s*<h2 class="line_table">[^<]*</h2>\s*<div class="content home_style">\s*<div class="clear"></div>\s*<ul>).*?(</ul>)',
    r'\1\n\t\t\t\t' + new_latest_html.replace('\\', '\\\\') + r'\n\t\t\t\2',
    target_content,
    flags=re.DOTALL
)

with open(target_html, 'w', encoding='utf-8') as f:
    f.write(target_content)

print("Updated index.html successfully.")

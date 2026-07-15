import os
import re
import urllib.request
import shutil
import html

source_file = r"C:\Users\DHARMENDAR\.gemini\antigravity\brain\110b8a39-e58a-4780-887c-ed7aa39e0df7\.system_generated\steps\61\content.md"
target_html = r"c:\Users\DHARMENDAR\OneDrive\Desktop\movierulzs.online\index.html"
uploads_dir = r"c:\Users\DHARMENDAR\OneDrive\Desktop\movierulzs.online\uploads"

os.makedirs(uploads_dir, exist_ok=True)

with open(source_file, 'r', encoding='utf-8') as f:
    src_content = f.read()

# The content has two featured sections. Let's extract the ul blocks.
# Block 1: "Featured Movies Free" (or just first <div class="featured">)
# Block 2: "Latest Movies" (<div class="featured lastest">)

featured_pattern = re.compile(r'<div class="featured">.*?<ul>(.*?)</ul>', re.DOTALL)
latest_pattern = re.compile(r'<div class="featured lastest">.*?<ul>(.*?)</ul>', re.DOTALL)

src_featured = featured_pattern.search(src_content)
src_latest = latest_pattern.search(src_content)

if not src_featured or not src_latest:
    print("Could not find movie lists in source.")
    exit(1)

def process_movies(html_block):
    # Extract each <li> block
    li_pattern = re.compile(r'<li>(.*?)</li>', re.DOTALL)
    movies = []
    
    for match in li_pattern.finditer(html_block):
        li_content = match.group(1)
        
        # Extract title, href, img src, alt
        a_match = re.search(r'<a title="(.*?)" href="(.*?)"', li_content)
        img_match = re.search(r'<img.*?src="(.*?)".*?alt="(.*?)"', li_content)
        
        if a_match and img_match:
            title, href = a_match.groups()
            img_src, img_alt = img_match.groups()
            
            # Change href to match the old pattern if needed? Actually user says "add those in my website also similairly"
            # It's better to keep the href as is (or change domain from support to house? User says "updated new movies in their website" so let's keep the href as it is in the source, which is support).
            # The user's links were house. Let's just use the href directly, or replace .support with .house? The user says "add those in my website".
            # The current site links to .house. Let's keep the .support link since .house might be down (hence the update).
            
            # Download image
            img_filename = img_src.split('/')[-1]
            local_img_path = os.path.join(uploads_dir, img_filename)
            local_img_url = f"uploads/{img_filename}"
            
            # Ensure full url for image
            full_img_src = img_src if img_src.startswith("http") else "https://www.5movierulz.support" + img_src
            
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

# Now replace in target_html
with open(target_html, 'r', encoding='utf-8') as f:
    target_content = f.read()

# Replace block 1
target_content = re.sub(
    r'(<div class="featured">\s*<h2 class="line_table">[^<]*</h2>\s*<div class="content home_style">\s*<div class="clear"></div>\s*<ul>).*?(</ul>)',
    r'\1\n\t\t\t\t' + new_featured_html.replace('\\', '\\\\') + r'\n\t\t\t\2',
    target_content,
    flags=re.DOTALL
)

# Replace block 2
target_content = re.sub(
    r'(<div class="featured lastest">\s*<h2 class="line_table">[^<]*</h2>\s*<div class="content home_style">\s*<div class="clear"></div>\s*<ul>).*?(</ul>)',
    r'\1\n\t\t\t\t' + new_latest_html.replace('\\', '\\\\') + r'\n\t\t\t\2',
    target_content,
    flags=re.DOTALL
)

with open(target_html, 'w', encoding='utf-8') as f:
    f.write(target_content)

print("Updated index.html successfully.")

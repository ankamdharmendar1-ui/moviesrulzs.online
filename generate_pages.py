import os
import re

base_dir = r"c:\Users\DHARMENDAR\OneDrive\Desktop\movierulzs.online"
index_file = os.path.join(base_dir, "index.html")

with open(index_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract header and footer
# Header ends before <div id="content"
header_match = re.search(r'(.*?)(<div id="content")', html, re.DOTALL)
header = header_match.group(1) if header_match else ""

# Footer starts at <div class="footer-wrapper">
footer_match = re.search(r'(<div class="footer-wrapper">.*)', html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ""

# Update footer to include the new links in index.html first
new_links = r'<p><a href="/" style="color:#b5b5b5; text-decoration:none;">Home</a> | <a href="/about.html" style="color:#b5b5b5; text-decoration:none;">About Us</a> | <a href="/contact.html" style="color:#b5b5b5; text-decoration:none;">Contact Us</a> | <a href="/privacy.html" style="color:#b5b5b5; text-decoration:none;">Privacy Policy</a> | <a href="/disclaimer.html" style="color:#b5b5b5; text-decoration:none;">Disclaimer</a> | <a href="/dmca.html" style="color:#b5b5b5; text-decoration:none;">DMCA</a></p>'

footer = re.sub(r'<p><a href="/".*?</p>', new_links, footer)
html = re.sub(r'<p><a href="/".*?</p>', new_links, html)

with open(index_file, 'w', encoding='utf-8') as f:
    f.write(html)

pages = {
    "about.html": """
<div id="content" class="clearfix row-fluid" style="padding: 20px; color: #cbd5e1; max-width: 900px; margin: 0 auto; background: #1a1c23; border-radius: 8px;">
    <h1 style="color: #ff7b09; border-bottom: 1px solid #333; padding-bottom: 10px;">About Us</h1>
    <p style="font-size: 16px; line-height: 1.8; margin-top: 15px;">Welcome to <strong>movierulzs.online</strong>, your ultimate destination for everything related to Indian cinema.</p>
    <p style="font-size: 16px; line-height: 1.8;">Our journey started with a simple passion: an absolute love for movies. We grew up watching the magic of Telugu, Tamil, Malayalam, and Hindi cinema unfold on the big screen. We wanted to create a space where fellow movie buffs could easily find detailed information about their favorite films, from the brilliant directors behind the camera to the talented cast that brings the stories to life.</p>
    <p style="font-size: 16px; line-height: 1.8;">At movierulzs.online, we don't just list movies. We curate comprehensive synopses, explore cast details, and bring you the latest media updates. We believe that cinema is an emotion that connects us all, and our goal is to keep you informed and excited about the vibrant world of Indian entertainment.</p>
    <p style="font-size: 16px; line-height: 1.8;">Thank you for being part of our community. Grab some popcorn, browse our reviews and updates, and let's celebrate the magic of movies together!</p>
</div>
<div style="clear:both; height:20px;"></div>
    """,
    
    "contact.html": """
<div id="content" class="clearfix row-fluid" style="padding: 20px; color: #cbd5e1; max-width: 900px; margin: 0 auto; background: #1a1c23; border-radius: 8px;">
    <h1 style="color: #ff7b09; border-bottom: 1px solid #333; padding-bottom: 10px;">Contact Us</h1>
    <p style="font-size: 16px; line-height: 1.8; margin-top: 15px;">We always love hearing from our fellow movie enthusiasts!</p>
    <p style="font-size: 16px; line-height: 1.8;">Whether you have a question about a specific movie, a suggestion to improve our website, or a business inquiry, we are here to listen. Your feedback helps us grow and provide a better experience for everyone.</p>
    
    <div style="background: #252830; padding: 20px; border-radius: 8px; margin-top: 20px;">
        <h3 style="color: #fff; margin-bottom: 10px;">Get in Touch</h3>
        <p style="font-size: 16px; line-height: 1.8;"><strong>Email:</strong> contact@movierulzs.online</p>
        <p style="font-size: 16px; line-height: 1.8;">We aim to respond to all inquiries within 24 to 48 hours. Please be patient as we get back to you.</p>
    </div>
</div>
<div style="clear:both; height:20px;"></div>
    """,

    "privacy.html": """
<div id="content" class="clearfix row-fluid" style="padding: 20px; color: #cbd5e1; max-width: 900px; margin: 0 auto; background: #1a1c23; border-radius: 8px;">
    <h1 style="color: #ff7b09; border-bottom: 1px solid #333; padding-bottom: 10px;">Privacy Policy</h1>
    <p style="font-size: 14px; line-height: 1.8; margin-top: 15px;"><em>Last Updated: July 2026</em></p>
    <p style="font-size: 16px; line-height: 1.8;">Your privacy is extremely important to us at movierulzs.online. This Privacy Policy outlines the types of personal information we receive and collect when you use our website, and how we safeguard your information.</p>
    
    <h3 style="color: #fff; margin-top: 20px;">1. Information We Collect</h3>
    <p style="font-size: 16px; line-height: 1.8;">Like many other websites, we utilize log files. The information inside the log files includes internet protocol (IP) addresses, browser type, Internet Service Provider (ISP), date/time stamp, referring/exit pages, and number of clicks. This data is used to analyze trends, administer the site, and track user movement. It is not linked to any information that is personally identifiable.</p>
    
    <h3 style="color: #fff; margin-top: 20px;">2. Cookies and Web Beacons</h3>
    <p style="font-size: 16px; line-height: 1.8;">We use cookies to store information about your preferences and to record user-specific information on which pages you access or visit. This helps us customize our webpage content based on your browser type or other information you send via your browser.</p>
    
    <h3 style="color: #fff; margin-top: 20px;">3. Google AdSense & Third-Party Advertisers</h3>
    <p style="font-size: 16px; line-height: 1.8;">We use third-party advertising companies to serve ads when you visit our website. These companies may use aggregated information (not including your name, address, email address, or telephone number) about your visits to this and other websites in order to provide advertisements about goods and services of interest to you. Specifically, Google, as a third-party vendor, uses cookies to serve ads on our site. Users may opt out of the use of the DART cookie by visiting the Google ad and content network privacy policy.</p>
    
    <h3 style="color: #fff; margin-top: 20px;">4. Consent</h3>
    <p style="font-size: 16px; line-height: 1.8;">By using our website, you hereby consent to our privacy policy and agree to its terms.</p>
</div>
<div style="clear:both; height:20px;"></div>
    """,

    "disclaimer.html": """
<div id="content" class="clearfix row-fluid" style="padding: 20px; color: #cbd5e1; max-width: 900px; margin: 0 auto; background: #1a1c23; border-radius: 8px;">
    <h1 style="color: #ff7b09; border-bottom: 1px solid #333; padding-bottom: 10px;">Disclaimer</h1>
    
    <p style="font-size: 16px; line-height: 1.8; margin-top: 15px;">The information provided by movierulzs.online ("we," "us," or "our") on this website is for general informational and educational purposes only.</p>
    
    <h3 style="color: #fff; margin-top: 20px;">Informational Purpose Only</h3>
    <p style="font-size: 16px; line-height: 1.8;">We strive to keep the information (such as movie synopses, cast details, release dates, and reviews) up to date and correct. However, we make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability with respect to the website or the information contained on it. Any reliance you place on such information is strictly at your own risk.</p>
    
    <h3 style="color: #fff; margin-top: 20px;">No Copyright Infringement Intended</h3>
    <p style="font-size: 16px; line-height: 1.8;"><strong>movierulzs.online does NOT host, upload, or store any copyrighted video files, movies, or media on our servers.</strong> We operate purely as a movie database and review blog. All images and posters used on this site are for promotional and review purposes under fair use guidelines, and belong to their respective copyright holders. We strongly condemn piracy and encourage our users to watch movies in theaters or through official, legal OTT streaming platforms.</p>
    
    <h3 style="color: #fff; margin-top: 20px;">External Links</h3>
    <p style="font-size: 16px; line-height: 1.8;">Through this website, you may be able to link to other websites which are not under the control of movierulzs.online. We have no control over the nature, content, and availability of those sites. The inclusion of any links does not necessarily imply a recommendation or endorse the views expressed within them.</p>
</div>
<div style="clear:both; height:20px;"></div>
    """,

    "dmca.html": """
<div id="content" class="clearfix row-fluid" style="padding: 20px; color: #cbd5e1; max-width: 900px; margin: 0 auto; background: #1a1c23; border-radius: 8px;">
    <h1 style="color: #ff7b09; border-bottom: 1px solid #333; padding-bottom: 10px;">DMCA Copyright Policy</h1>
    
    <p style="font-size: 16px; line-height: 1.8; margin-top: 15px;">At movierulzs.online, we deeply respect the intellectual property rights of others and expect our users to do the same. In accordance with the Digital Millennium Copyright Act of 1998 (DMCA), we will respond expeditiously to claims of copyright infringement committed using our service.</p>
    
    <h3 style="color: #fff; margin-top: 20px;">Our Policy</h3>
    <p style="font-size: 16px; line-height: 1.8;">As stated in our Disclaimer, we do not host any copyrighted media files. Our site is purely an informational database featuring cast lists, synopses, and reviews. However, if you are a copyright owner, or are authorized to act on behalf of one, and you believe that any material on our website infringes upon your copyrights, you may submit a formal DMCA takedown request.</p>
    
    <h3 style="color: #fff; margin-top: 20px;">How to Submit a Notice of Infringement</h3>
    <p style="font-size: 16px; line-height: 1.8;">To file a copyright infringement notification with us, please send a written communication that includes the following:</p>
    <ul style="font-size: 16px; line-height: 1.8; margin-left: 20px; color: #cbd5e1;">
        <li>A physical or electronic signature of a person authorized to act on behalf of the owner of an exclusive right that is allegedly infringed.</li>
        <li>Identification of the copyrighted work claimed to have been infringed.</li>
        <li>Identification of the material that is claimed to be infringing or to be the subject of infringing activity, along with the exact URL where it can be found.</li>
        <li>Information reasonably sufficient to permit us to contact you, such as an address, telephone number, and, if available, an electronic mail address.</li>
        <li>A statement that you have a good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law.</li>
        <li>A statement that the information in the notification is accurate, and under penalty of perjury, that you are authorized to act on behalf of the owner of an exclusive right that is allegedly infringed.</li>
    </ul>
    
    <h3 style="color: #fff; margin-top: 20px;">Contact Information</h3>
    <p style="font-size: 16px; line-height: 1.8;">Please send all DMCA takedown notices to our designated abuse agent at:<br><br>
    <strong>Email:</strong> dmca@movierulzs.online</p>
    
    <p style="font-size: 16px; line-height: 1.8;">Upon receipt of a valid DMCA notice, we will investigate the matter and take appropriate action, which may include removing or disabling access to the challenged material.</p>
</div>
<div style="clear:both; height:20px;"></div>
    """
}

for filename, page_content in pages.items():
    full_path = os.path.join(base_dir, filename)
    # Assemble the page
    full_html = header + page_content + footer
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

print("Pages created successfully and linked in footer.")

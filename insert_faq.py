import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

faq_content = """<div class="seo-faq-section" style="max-width: 1000px; margin: 40px auto; padding: 25px; background: #1a1c23; border-radius: 8px; border-top: 3px solid #ff7b09; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
    <h2 style="color: #ff7b09; margin-bottom: 25px; text-align: center; font-size: 24px;">Frequently Asked Questions</h2>
    
    <div style="margin-bottom: 25px; border-bottom: 1px solid #333; padding-bottom: 15px;">
        <h3 style="color: #ffffff; font-size: 18px; margin-bottom: 10px;">What is Movierulzs.online?</h3>
        <p style="color: #cbd5e1; font-size: 14px; line-height: 1.7;">
            Movierulzs.online is a comprehensive database and informational hub dedicated to Indian cinema. We provide detailed updates, cast information, director details, and synopses for the latest Telugu, Tamil, Malayalam, and Hindi movies. It's the perfect place to stay updated with your favorite regional films.
        </p>
    </div>

    <div style="margin-bottom: 25px; border-bottom: 1px solid #333; padding-bottom: 15px;">
        <h3 style="color: #ffffff; font-size: 18px; margin-bottom: 10px;">How to download movies from Movierulz?</h3>
        <p style="color: #cbd5e1; font-size: 14px; line-height: 1.7;">
            Many users frequently search for how to download movies in Movierulz. However, we strongly advise our visitors to support the film industry by watching movies through official, legal streaming platforms like Amazon Prime Video, Netflix, Aha, or in theaters. Downloading copyrighted content from unauthorized sources poses significant security risks to your device.
        </p>
    </div>

    <div style="margin-bottom: 25px; border-bottom: 1px solid #333; padding-bottom: 15px;">
        <h3 style="color: #ffffff; font-size: 18px; margin-bottom: 10px;">Is Movierulz safe and legal in India?</h3>
        <p style="color: #cbd5e1; font-size: 14px; line-height: 1.7;">
            A common question is whether it is safe to download movies from Movierulz or if Movierulz is banned in India. Piracy websites are generally not legal and are actively banned by ISPs and the government in India to protect copyright laws. Furthermore, such sites are often not safe, as they can host intrusive pop-ups and malicious software. We encourage consuming content through legitimate channels.
        </p>
    </div>

    <div style="margin-bottom: 10px;">
        <h3 style="color: #ffffff; font-size: 18px; margin-bottom: 10px;">Why is Movierulz not working?</h3>
        <p style="color: #cbd5e1; font-size: 14px; line-height: 1.7;">
            If you are wondering what happened to Movierulz and why it isn't working, it is likely due to ISP blocks enforced by regulatory authorities. When domains are banned, the original owners often shift to new domain extensions. However, for a safe, high-quality, and uninterrupted experience, relying on authorized OTT platforms remains the best choice.
        </p>
    </div>
</div>
"""

# Insert right before footer-wrapper
if '<div class="footer-wrapper">' in html:
    html = html.replace('<div class="footer-wrapper">', f'{faq_content}\n<div class="footer-wrapper">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

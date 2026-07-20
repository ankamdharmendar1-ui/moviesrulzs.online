import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

schema = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is Movierulzs.online?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Movierulzs.online is a comprehensive database and informational hub dedicated to Indian cinema. We provide detailed updates, cast information, director details, and synopses for the latest Telugu, Tamil, Malayalam, and Hindi movies."
    }
  }, {
    "@type": "Question",
    "name": "How to download movies from Movierulz?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Many users frequently search for how to download movies in Movierulz. However, we strongly advise our visitors to support the film industry by watching movies through official, legal streaming platforms like Amazon Prime Video, Netflix, Aha, or in theaters."
    }
  }, {
    "@type": "Question",
    "name": "Is Movierulz safe and legal in India?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Piracy websites are generally not legal and are actively banned by ISPs and the government in India to protect copyright laws. Furthermore, such sites are often not safe, as they can host intrusive pop-ups and malicious software."
    }
  }, {
    "@type": "Question",
    "name": "Why is Movierulz not working?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "If you are wondering what happened to Movierulz and why it isn't working, it is likely due to ISP blocks enforced by regulatory authorities. When domains are banned, the original owners often shift to new domain extensions."
    }
  }]
}
</script>
</head>"""

# Inject before </head>
html = html.replace('</head>', schema)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

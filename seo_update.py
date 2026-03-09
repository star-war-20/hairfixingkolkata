import glob
import re
import os

files = glob.glob("*.html")

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get existing title, description
    title_match = re.search(r'<title>(.*?)</title>', content)
    desc_match = re.search(r'<meta name="description"[\s\S]*?content="([^"]*)"', content, flags=re.IGNORECASE)
    
    title = title_match.group(1).strip() if title_match else "Hair Fixing Service Kolkata"
    desc = desc_match.group(1).strip() if desc_match else "Best non-surgical hair replacement service in Kolkata."
    
    og_tags = f'''
    <meta name="author" content="Hair Fixing Service Kolkata">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://hairfixingservicekolkata.com/{file}">
    <meta property="og:image" content="https://hairfixingservicekolkata.com/images/logo.png">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="https://hairfixingservicekolkata.com/images/logo.png">
    <meta name="twitter:site" content="@hairfixingkolkata">
'''
    
    # If the file doesn't have Open Graph, inject it before </head>
    if 'property="og:title"' not in content:
        content = content.replace("</head>", og_tags + "\n</head>")
    
    # Add Schema Markup to all pages if missing
    schema = '''
    <!-- Schema Markup -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Hair Fixing Service Kolkata",
      "description": "Best non-surgical hair replacement service in Kolkata for men. Hair patch, hair wig, hair bonding, hair weaving services.",
      "url": "https://hairfixingservicekolkata.com",
      "telephone": "+916297517526",
      "email": "hazraabilas@gmail.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "5b, Lake View Rd, Hemanta Mukherjee Sarani, Lake Terrace, Ballygunge",
        "addressLocality": "Kolkata",
        "addressRegion": "West Bengal",
        "postalCode": "700029",
        "addressCountry": "IN"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": "22.5260",
        "longitude": "88.3607"
      },
      "openingHours": "Mo-Su 09:00-22:00",
      "priceRange": "₹5,999 - ₹40,000",
      "image": "https://hairfixingservicekolkata.com/images/logo.png",
      "sameAs": [
        "https://g.page/r/CY317oGXOC3zEBM/"
      ]
    }
    </script>
'''
    if '"@type": "LocalBusiness"' not in content:
        content = content.replace("</head>", schema + "\n</head>")

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Detailed SEO tags added to {file}!")


import os

base_dir = r"d:\fromAi\hair-fixing-kolkata\hair-fixing-kolkata"
blog_base = os.path.join(base_dir, "blog-details.html")
blog_html = os.path.join(base_dir, "blog.html")
target_img = os.path.join(base_dir, "assets", "images", "benefits_active.jpg")

with open(blog_base, "r", encoding="utf-8") as f:
    template = f.read()

# Replace image in the template
template = template.replace('assets/images/benefits_active.jpg', 'assets/images/benefits_younger.jpg')

# Blog 1: Maintenance
maintenance_html = template
maintenance_path = os.path.join(base_dir, "blog-maintenance.html")
with open(maintenance_path, "w", encoding="utf-8") as f:
    f.write(maintenance_html)

# Blog 2: Transplants
transplants_html = template.replace("How to Maintain Your Hair Patch for Max Lifespan", "Hair Transplants vs Non-Surgical Fixing")
transplants_html = transplants_html.replace("A step-by-step guide to washing, combing, and styling your hair patch so it lasts beautifully for 12 months.", "Why 70% of men in Kolkata are now choosing non-surgical hair patches instead of painful hair transplants.")
transplants_html = transplants_html.replace("blog-details.html", "blog-transplants.html")
transplants_html = transplants_html.replace('<span class="blog-tag"\n                    style="background: rgba(212, 168, 83, 0.15); color: var(--gold-primary); padding: 6px 16px; border-radius: var(--radius-full); font-size: 0.85rem; font-weight: 700; text-transform: uppercase;">Maintenance</span>', '<span class="blog-tag"\n                    style="background: rgba(212, 168, 83, 0.15); color: var(--gold-primary); padding: 6px 16px; border-radius: var(--radius-full); font-size: 0.85rem; font-weight: 700; text-transform: uppercase;">Education</span>')
transplants_html = transplants_html.replace('alt="Man with well-maintained hair patch"', 'alt="Non-surgical vs Surgical Hair Restoration"')
transplants_html = transplants_html.replace('assets/images/benefits_younger.jpg', 'assets/images/benefits_immediate.jpg')

content2 = """
<p>For decades, hair transplants were considered the only permanent solution for hair loss. However, with sweeping advancements in hair patch technology and skin-friendly adhesives, non-surgical hair replacement is rapidly becoming the preferred choice for men in Kolkata.</p>

<h2 style="color: var(--text-primary); margin-top: 36px; margin-bottom: 16px;">1. Instant Results vs Months of Waiting</h2>
<p>A hair transplant requires surgery, a long, painful healing process, and 6-12 months before you even start to see noticeable growth results. Non-surgical hair fixing takes exactly 60 minutes. You walk into the studio with hair loss, and you walk out with a completely natural full head of hair.</p>

<h2 style="color: var(--text-primary); margin-top: 36px; margin-bottom: 16px;">2. Zero Pain, Zero Side-Effects</h2>
<p>Transplants involve removing hair follicles from one part of the scalp and surgically inserting them into another. This carries risks of infection, scarring, and immense discomfort. Hair bonding and fixing are 100% non-invasive. The derma-base patch sits onto the scalp seamlessly using FDA-approved adhesive.</p>

<h2 style="color: var(--text-primary); margin-top: 36px; margin-bottom: 16px;">3. Guaranteed Density Every Time</h2>
<p>With a surgical transplant, you are at the mercy of your donor area. If your existing hair isn't dense enough, the transplant results will look incredibly sparse and thin. Hair patches guarantee you 100% thick, dense, youthful hair instantly, tailored exactly to how you want to look.</p>

<p>Before you commit to a painful surgical procedure, book a free consultation at our Kolkata studio to see the non-surgical hair system difference.</p>
"""
transplants_html = transplants_html.split('<div class="blog-content"')[0] + '<div class="blog-content" style="color: var(--text-secondary); line-height: 1.8; font-size: 1.05rem;">' + content2 + transplants_html.split('<!-- Share / Tags -->')[1]

transplants_path = os.path.join(base_dir, "blog-transplants.html")
with open(transplants_path, "w", encoding="utf-8") as f:
    f.write(transplants_html)


# Blog 3: Hairstyles
hairstyles_html = template.replace("How to Maintain Your Hair Patch for Max Lifespan", "Top 5 Hairstyles for Men with Hair Patches")
hairstyles_html = hairstyles_html.replace("A step-by-step guide to washing, combing, and styling your hair patch so it lasts beautifully for 12 months.", "From the textured crop to the slicked-back pompadour, here are the best hairstyles that look completely natural with a hair system...")
hairstyles_html = hairstyles_html.replace("blog-details.html", "blog-hairstyles.html")
hairstyles_html = hairstyles_html.replace('<span class="blog-tag"\n                    style="background: rgba(212, 168, 83, 0.15); color: var(--gold-primary); padding: 6px 16px; border-radius: var(--radius-full); font-size: 0.85rem; font-weight: 700; text-transform: uppercase;">Maintenance</span>', '<span class="blog-tag"\n                    style="background: rgba(212, 168, 83, 0.15); color: var(--gold-primary); padding: 6px 16px; border-radius: var(--radius-full); font-size: 0.85rem; font-weight: 700; text-transform: uppercase;">Styling</span>')
hairstyles_html = hairstyles_html.replace('alt="Man with well-maintained hair patch"', 'alt="Styling options for men with hair patch"')
hairstyles_html = hairstyles_html.replace('assets/images/benefits_younger.jpg', 'assets/images/benefits_natural_look.jpg')

content3 = """
<p>Modern hair patches offer an incredible amount of versatility. The days of rigid, unrealistic wig styles are long gone. Today, you can treat your hair system almost identically to real hair, cutting, fading, and styling it.</p>

<h2 style="color: var(--text-primary); margin-top: 36px; margin-bottom: 16px;">1. The French Crop (Textured Fringe)</h2>
<p>This is easily the most popular and safest style for men with hair patches. Keeping the sides faded and leaving texture on top pushed forward hides the front hairline perfectly. It is low maintenance and naturally stylish without needing much product.</p>

<h2 style="color: var(--text-primary); margin-top: 36px; margin-bottom: 16px;">2. The Classic Pompadour</h2>
<p>If you opt for a premium Front-Lace hair system (which mimics a natural growing hairline), you can easily pull off a slicked-back pompadour. You just brush the hair up and back using pomade. The lace naturally blends into your forehead making the hairline completely invisible.</p>

<h2 style="color: var(--text-primary); margin-top: 36px; margin-bottom: 16px;">3. The Side Part (Professional Cut)</h2>
<p>Ideal for business and formal settings, the side part works brilliantly on monofilament patches. The base allows the stylist to carve a realistic "skin part" into the hair, meaning the part looks exactly like an organic scalp line.</p>

<p>When getting your hair patch fitted at our studio, our expert barbers will consult with you and cut the system directly on your head to ensure the hairstyle aligns perfectly with your face shape and personal preference.</p>
"""
hairstyles_html = hairstyles_html.split('<div class="blog-content"')[0] + '<div class="blog-content" style="color: var(--text-secondary); line-height: 1.8; font-size: 1.05rem;">' + content3 + hairstyles_html.split('<!-- Share / Tags -->')[1]

hairstyles_path = os.path.join(base_dir, "blog-hairstyles.html")
with open(hairstyles_path, "w", encoding="utf-8") as f:
    f.write(hairstyles_html)

# Clean up blog details template file
if os.path.exists(blog_base):
    os.remove(blog_base)

# Update Blog.html links and remove benefits_active.jpg references
with open(blog_html, "r", encoding="utf-8") as f:
    bh = f.read()

bh = bh.replace('assets/images/benefits_active.jpg', 'assets/images/benefits_younger.jpg')

# Update links sequentially (Maintenance, Education, Styling)
bh = bh.replace('<a href="blog-details.html" class="read-more">Read Full Guide →</a>', '<a href="blog-maintenance.html" class="read-more">Read Full Guide →</a>', 1)
bh = bh.replace('<a href="blog-details.html" class="read-more">Read Full Guide →</a>', '<a href="blog-transplants.html" class="read-more">Read Full Guide →</a>', 1)
bh = bh.replace('<a href="blog-details.html" class="read-more">Read Full Guide →</a>', '<a href="blog-hairstyles.html" class="read-more">Read Full Guide →</a>', 1)

with open(blog_html, "w", encoding="utf-8") as f:
    f.write(bh)

# Remove the requested image
if os.path.exists(target_img):
    os.remove(target_img)

print("Done generating individual blog files and deleting image.")

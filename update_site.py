import os
import glob
import re

print("Starting update...")

# CSS Changes
css_file = 'css/styles.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace navbar gap
css = css.replace('.header.has-banner {\\n    top: 44px;\\n}', '.header.has-banner {\\n    top: 44px;\\n}\\n\\n.header.scrolled.has-banner {\\n    top: 0;\\n}')

# Replace hero buttons CSS
css = css.replace('.hero-buttons-row {\\n    display: flex;\\n    gap: 14px;\\n    margin-bottom: 36px;\\n    flex-wrap: wrap;\\n}', '.hero-buttons-row {\\n    display: flex;\\n    gap: 14px;\\n    margin-bottom: 36px;\\n    flex-wrap: nowrap;\\n}')

css = css.replace('.hero-btn-whatsapp,\\n.hero-btn-call {\\n    flex: 1;\\n    min-width: 160px;\\n    padding: 16px 24px;', '.hero-btn-whatsapp,\\n.hero-btn-call {\\n    flex: 1;\\n    min-width: auto;\\n    padding: 12px 14px;')

# Append floating buttons CSS
if '.floating-actions' not in css:
    css += '''
/* ── Floating Action Buttons ── */
.floating-actions {
    position: fixed;
    bottom: 24px;
    right: 24px;
    display: flex;
    flex-direction: column;
    gap: 16px;
    z-index: 1050;
}

.float-btn {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff !important;
    text-decoration: none;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.float-btn svg {
    width: 32px;
    height: 32px;
    fill: currentColor;
    color: #fff;
}

.float-btn:hover {
    transform: translateY(-4px) scale(1.05);
}

.float-whatsapp {
    background: linear-gradient(135deg, #25D366, #128C7E);
    box-shadow: 0 6px 20px rgba(37, 211, 102, 0.4);
}

.float-whatsapp:hover {
    box-shadow: 0 8px 25px rgba(37, 211, 102, 0.6);
}

.float-call {
    background: linear-gradient(135deg, var(--gold-primary), var(--gold-dark));
    box-shadow: 0 6px 20px rgba(212, 168, 83, 0.4);
}

.float-call:hover {
    box-shadow: 0 8px 25px rgba(212, 168, 83, 0.6);
}

@media (max-width: 768px) {
    .floating-actions {
        bottom: 16px;
        right: 16px;
        gap: 12px;
    }
    .float-btn {
        width: 50px;
        height: 50px;
    }
    .float-btn svg {
        width: 24px;
        height: 24px;
    }
}
'''

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)
print("CSS updated.")

html_files = glob.glob('*.html')

floating_buttons_html = '''
    <!-- Floating Action Buttons -->
    <div class="floating-actions">
        <a href="https://wa.me/916297517526?text=Hi!%20I%20want%20to%20know%20about%20hair%20fixing%20services." class="float-btn float-whatsapp" target="_blank" aria-label="WhatsApp">
            <svg viewBox="0 0 24 24">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
            </svg>
        </a>
        <a href="tel:+916297517526" class="float-btn float-call" aria-label="Call Now">
            <svg viewBox="0 0 24 24">
                <path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/>
            </svg>
        </a>
    </div>
</body>'''

hero_replacement = '''<!-- Hero Banner Image -->
            <div class="hero-visual reveal">
                <div class="hero-image-wrapper" style="box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5); border-radius: var(--radius-xl); overflow: hidden; border: 1px solid rgba(212, 168, 83, 0.15);">
                    <img src="images/hairfixingkolkatabanner.jpg" alt="Hair Fixing Services Kolkata Banner" style="width: 100%; height: auto; display: block; object-fit: cover;">
                </div>
            </div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Update robots meta tag
    if '<meta name="robots" content="index, follow">' in html:
        html = html.replace('<meta name="robots" content="index, follow">', '<meta name="robots" content="noindex, nofollow">')
    
    # 2. Add floating buttons before </body>
    if 'class="floating-actions"' not in html:
        html = html.replace('</body>', floating_buttons_html)
    
    # 3. Replace hero form
    if 'id="heroFormCard"' in html:
        pattern = r'<!-- Hero Lead Form -->.*?<div class="hero-form-card".*?100% Free • No Spam • Instant WhatsApp Callback\s*</div>\s*</div>\s*</div>'
        html = re.sub(pattern, hero_replacement, html, flags=re.DOTALL)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {file}")

print('Done!')

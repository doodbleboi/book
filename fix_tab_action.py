import re

HTML_FILE = "index.html"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Inspect how existing tab buttons work (e.g. data-target, onclick, etc.)
# Find the button for 'Historical Ledger'
hist_btn_match = re.search(r'<button([^>]*)>([^<]*Historical Ledger[^<]*)<\/button>', content, re.IGNORECASE)
if hist_btn_match:
    attrs = hist_btn_match.group(1)
    print(f"Historical Ledger attrs: {attrs}")
    
    # Create the exact Full Text button matching the site's pattern
    # Replace references like 'timeline' or 'roses_timeline' with 'full_text' or 'roses_full_text'
    ft_attrs = attrs
    for old_val in ['roses_timeline', 'timeline', 'roses-timeline']:
        if old_val in ft_attrs:
            ft_attrs = ft_attrs.replace(old_val, old_val.replace('timeline', 'full_text'))
    
    # If onclick="switchTab(this, '...')" or similar is used:
    target_match = re.search(r"['\"]([^'\"]*timeline[^'\"]*)['\"]", attrs)
    target_id = "roses_full_text"
    if target_match:
        old_id = target_match.group(1)
        new_id = old_id.replace('timeline', 'full_text')
        target_id = new_id
        ft_attrs = ft_attrs.replace(old_id, new_id)
        
    print(f"Target container ID resolved to: {target_id}")
    
    # Replace the existing Full Text button with the properly formatted one
    content = re.sub(
        r'<button[^>]*>[^<]*Full Text[^<]*<\/button>',
        f'<button{ft_attrs}>Full Text</button>',
        content
    )

# 2. Ensure the container div has the matching ID and classes
# Find the container that holds FLAG_START: roses_full_text
container_regex = r'<div[^>]*id=["\'][^"\']*["\'][^>]*>\s*<!--\s*FLAG_START:\s*roses_full_text\s*-->'
# Find matching class pattern from roses_timeline container
timeline_div_match = re.search(r'<div([^>]*)>\s*<!--\s*FLAG_START:\s*roses_timeline\s*-->', content)
if timeline_div_match:
    t_attrs = timeline_div_match.group(1)
    print(f"Timeline container attrs: {t_attrs}")
    # Replace ID in attributes
    ft_div_attrs = re.sub(r'id=["\'][^"\']*["\']', f'id="{target_id}"', t_attrs)
    # Ensure it starts hidden like inactive tabs
    if 'style=' not in ft_div_attrs and 'display:none' in t_attrs:
        pass
    content = re.sub(
        r'<div[^>]*>\s*(<!--\s*FLAG_START:\s*roses_full_text\s*-->)',
        f'<div{ft_div_attrs}>\n        \\1',
        content,
        count=1
    )
    print("Container div updated to match site convention.")

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("Patch applied to index.html.")

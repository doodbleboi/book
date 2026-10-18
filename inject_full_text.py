HTML_FILE = "index.html"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Inject roses_full_text container right after roses_timeline
anchor = "<!-- FLAG_END: roses_timeline -->"

if "<!-- FLAG_START: roses_full_text -->" not in content:
    if anchor in content:
        # Find the closing </div> of the roses_timeline section after the anchor
        idx = content.find(anchor) + len(anchor)
        next_div_end = content.find("</div>", idx) + len("</div>")
        
        container_html = (
            '\n\n      <div id="roses_full_text" class="sub-tab-content roses-tab-content" style="display:none;">\n'
            '        <!-- FLAG_START: roses_full_text -->\n'
            '        <!-- FLAG_END: roses_full_text -->\n'
            '      </div>'
        )
        content = content[:next_div_end] + container_html + content[next_div_end:]
        print("Success: Injected roses_full_text container into index.html.")
    else:
        print("Error: Could not find anchor '<!-- FLAG_END: roses_timeline -->'")
else:
    print("Notice: roses_full_text container already present.")

# 2. Add the sub-nav button right after 'Historical Ledger'
if "Full Text" not in content:
    # Match whatever button holds Historical Ledger
    import re
    btn_match = re.search(r'(<button[^>]*>[^<]*Historical Ledger[^<]*<\/button>)', content, re.IGNORECASE)
    if btn_match:
        old_btn = btn_match.group(1)
        # clone button style/attributes, replace target
        new_btn = old_btn.replace("Historical Ledger", "Full Text")
        # swap any tab ID reference like roses_timeline -> roses_full_text
        new_btn = new_btn.replace("roses_timeline", "roses_full_text").replace("timeline", "full_text")
        content = content.replace(old_btn, old_btn + "\n          " + new_btn, 1)
        print("Success: Appended Full Text button next to Historical Ledger.")
    else:
        print("Notice: Could not auto-detect Historical Ledger button; check Step 1 output.")

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html successfully updated.")

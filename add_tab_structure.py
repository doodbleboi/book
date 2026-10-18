import os

HTML_FILE = r".\index.html"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add sub-nav button if not present
old_nav = '<button class="sub-nav-btn" onclick="openRosesTab(\'roses_timeline\')">Historical Ledger</button>'
new_nav = '<button class="sub-nav-btn" onclick="openRosesTab(\'roses_timeline\')">Historical Ledger</button>\n          <button class="sub-nav-btn" onclick="openRosesTab(\'roses_full_text\')">Full Text</button>'

if 'openRosesTab(\'roses_full_text\')' not in content:
    content = content.replace(old_nav, new_nav)

# 2. Add section container if not present
tab_anchor = '<!-- FLAG_END: roses_timeline -->'
full_text_container = '''<!-- FLAG_END: roses_timeline -->
      </div>
      
      <div id="roses_full_text" class="roses-tab-content" style="display:none;">
        <!-- FLAG_START: roses_full_text -->
        <!-- FLAG_END: roses_full_text -->'''

if 'id="roses_full_text"' not in content:
    # replace first occurrence after roses_timeline
    content = content.replace('<!-- FLAG_END: roses_timeline -->\n      </div>', full_text_container)

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html structure updated with Full Text tab.")

import re

HTML_FILE = "index.html"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Ensure the sub-nav button exists
btn_regex = r'(<button[^>]*onclick="openRosesTab\(\'roses_timeline\'\)"[^>]*>.*?<\/button>)'
btn_replacement = r'\1\n          <button class="sub-nav-btn" onclick="openRosesTab(\'roses_full_text\')">Full Text</button>'

if "openRosesTab('roses_full_text')" not in content:
    content = re.sub(btn_regex, btn_replacement, content, count=1)
    print("Added Full Text sub-nav button.")

# 2. Inject the tab container directly after roses_timeline
tab_regex = r'(<!--\s*FLAG_END:\s*roses_timeline\s*-->\s*<\/div>)'
container_to_insert = (
    r'\1\n\n'
    r'      <div id="roses_full_text" class="roses-tab-content" style="display:none;">\n'
    r'        <!-- FLAG_START: roses_full_text -->\n'
    r'        <!-- FLAG_END: roses_full_text -->\n'
    r'      </div>'
)

if "<!-- FLAG_START: roses_full_text -->" not in content:
    content = re.sub(tab_regex, container_to_insert, content, count=1)
    print("Injected roses_full_text container with FLAG markers.")

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html structural patching complete.")

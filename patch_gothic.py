import re

HTML_FILE = "index.html"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Ensure the Mexican Gothic tab container contains the Full Text container
if "<!-- FLAG_START: gothic_full_text -->" not in content:
    # Inject gothic_full_text container right after gothic_timeline
    anchor = "<!-- FLAG_END: gothic_timeline -->"
    if anchor in content:
        idx = content.find(anchor) + len(anchor)
        next_div_end = content.find("</div>", idx) + len("</div>")
        container_html = (
            '\n\n      <div id="gothic_full_text" class="sub-tab-content gothic-tab-content" style="display:none;">\n'
            '        <!-- FLAG_START: gothic_full_text -->\n'
            '        <!-- FLAG_END: gothic_full_text -->\n'
            '      </div>'
        )
        content = content[:next_div_end] + container_html + content[next_div_end:]
        print("Success: Injected gothic_full_text container with FLAG tags.")
    else:
        print("Notice: gothic_timeline anchor not located.")

# 2. Wire the Mexican Gothic sub-nav buttons to match the 5 tabs
# Locate the sub-nav bar for Mexican Gothic
# Typically it mirrors the Roses bar: Discussion Questions, Summary Matrix, Character Dossiers, Historical Ledger, Full Text
# Look for a button that opens gothic tabs
gothic_btn_match = re.search(r'(<button[^>]*onclick="[^"]*gothic[^"]*"[^>]*>[^<]*Historical Ledger[^<]*<\/button>)', content, re.IGNORECASE)
if gothic_btn_match:
    old_btn = gothic_btn_match.group(1)
    if "gothic_full_text" not in content:
        new_btn = old_btn.replace("Historical Ledger", "Full Text")
        new_btn = re.sub(r'gothic_timeline|gothic-timeline|timeline', 'gothic_full_text', new_btn)
        content = content.replace(old_btn, old_btn + "\n          " + new_btn, 1)
        print("Success: Added Full Text button to Gothic sub-nav.")

# 3. Add explicit compatibility click handlers for both book portals
click_handlers = """
/* Book Portal Direct Tab Handlers */
document.addEventListener('DOMContentLoaded', function() {
    function setupTabs(btnText, targetId, prefix) {
        var buttons = Array.from(document.querySelectorAll('button')).filter(b => b.textContent.trim() === btnText);
        buttons.forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                var parentSection = btn.closest('[id*="roses"], [id*="gothic"], .book-section, section, div');
                var isGothic = btn.getAttribute('onclick') && btn.getAttribute('onclick').includes('gothic');
                var activePrefix = isGothic ? 'gothic_' : 'roses_';
                
                if (targetId.startsWith(activePrefix)) {
                    document.querySelectorAll('[id^="' + activePrefix + '"]').forEach(function(el) {
                        el.style.display = 'none';
                        el.classList.remove('active');
                    });
                    var target = document.getElementById(targetId);
                    if (target) {
                        target.style.display = 'block';
                        target.classList.add('active');
                    }
                }
            });
        });
    }
    setupTabs('Full Text', 'roses_full_text', 'roses_');
    setupTabs('Full Text', 'gothic_full_text', 'gothic_');
    setupTabs('Historical Ledger', 'roses_timeline', 'roses_');
    setupTabs('Historical Ledger', 'gothic_timeline', 'gothic_');
    setupTabs('Discussion Questions', 'roses_questions', 'roses_');
    setupTabs('Discussion Questions', 'gothic_questions', 'gothic_');
    setupTabs('Summary Matrix', 'roses_summary', 'roses_');
    setupTabs('Summary Matrix', 'gothic_summary', 'gothic_');
    setupTabs('Character Dossiers', 'roses_characters', 'roses_');
    setupTabs('Character Dossiers', 'gothic_characters', 'gothic_');
});
"""

if "Book Portal Direct Tab Handlers" not in content:
    content = content.replace('</body>', f'<script>\n{click_handlers}\n</script>\n</body>')
    print("Injected direct tab click handlers.")

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html fully patched for Mexican Gothic tabs.")

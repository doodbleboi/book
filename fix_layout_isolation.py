import re

HTML_FILE = "index.html"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add "Full Text" button to Mexican Gothic sub-nav if missing
# Locate the sub-nav bar containing Gothic's Historical Ledger
gothic_btn_match = re.search(r'(<button[^>]*onclick="[^"]*gothic[^"]*"[^>]*>[^<]*Historical Ledger[^<]*<\/button>)', content, re.IGNORECASE)
if gothic_btn_match:
    old_btn = gothic_btn_match.group(1)
    # Check if a Full Text button already exists inside that specific gothic sub-nav
    # Find enclosing div of that button
    btn_start = content.rfind('<div', 0, gothic_btn_match.start())
    btn_end = content.find('</div>', gothic_btn_match.end())
    nav_slice = content[btn_start:btn_end]
    if "Full Text" not in nav_slice:
        # Clone attributes, swap target identifier
        new_btn = old_btn.replace("Historical Ledger", "Full Text")
        new_btn = re.sub(r'timeline|gothic_timeline|gothic-timeline', 'gothic_full_text', new_btn)
        content = content.replace(old_btn, old_btn + "\n          " + new_btn, 1)
        print("Success: Injected 'Full Text' button into Mexican Gothic sub-nav.")
    else:
        print("Notice: Full Text button already found in Gothic sub-nav.")
else:
    # Try finding sub-nav buttons inside the gothic section directly
    print("Warning: Could not match Gothic Historical Ledger button regex directly.")

# 2. Ensure gothic_full_text container exists inside the gothic section
if "<!-- FLAG_START: gothic_full_text -->" not in content:
    # Anchor to the end of gothic_timeline
    anchor = "<!-- FLAG_END: gothic_timeline -->"
    if anchor in content:
        idx = content.find(anchor) + len(anchor)
        next_div = content.find("</div>", idx) + len("</div>")
        container_html = (
            '\n\n      <div id="gothic_full_text" class="sub-tab-content gothic-tab-content" style="display:none;">\n'
            '        <!-- FLAG_START: gothic_full_text -->\n'
            '        <!-- FLAG_END: gothic_full_text -->\n'
            '      </div>'
        )
        content = content[:next_div] + container_html + content[next_div:]
        print("Success: Injected gothic_full_text container with FLAG markers.")
    else:
        print("Error: Could not locate '<!-- FLAG_END: gothic_timeline -->'")
else:
    print("Notice: Flag 'gothic_full_text' already exists in index.html.")

# 3. Clean up any misplaced scripts from previous turns
content = re.sub(r'<script>[^<]*roses_full_text click patch[^<]*<\/script>\s*', '', content)
content = re.sub(r'<script>[^<]*Book Portal Direct Tab Handlers[^<]*<\/script>\s*', '', content)

# 4. Inject clean, bulletproof Master Tab Switcher before </body>
master_js = """<script>
/* Master Book Portal Controller */
function switchBook(book) {
    // 1. Toggle main book buttons
    var rosesMainBtn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.trim() === 'The Roses Underneath');
    var gothicMainBtn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.trim() === 'Mexican Gothic');
    
    // 2. Hide ALL sub-containers from BOTH books
    document.querySelectorAll('#roses_summary, #roses_characters, #roses_questions, #roses_timeline, #roses_full_text, [id^="roses_"]').forEach(function(el) {
        el.style.display = 'none';
        el.classList.remove('active');
    });
    document.querySelectorAll('#gothic_summary, #gothic_characters, #gothic_questions, #gothic_timeline, #gothic_full_text, [id^="gothic_"]').forEach(function(el) {
        el.style.display = 'none';
        el.classList.remove('active');
    });
    
    // 3. Toggle main container visibility if sections exist
    var rosesSection = document.getElementById('roses-section') || document.getElementById('roses');
    var gothicSection = document.getElementById('gothic-section') || document.getElementById('gothic');
    if (rosesSection && gothicSection) {
        if (book === 'roses') {
            rosesSection.style.display = 'block';
            gothicSection.style.display = 'none';
        } else {
            rosesSection.style.display = 'none';
            gothicSection.style.display = 'block';
        }
    }
}

// Sub-Tab Click Router
document.addEventListener('DOMContentLoaded', function() {
    // Intercept main book tabs
    document.querySelectorAll('button').forEach(function(btn) {
        var text = btn.textContent.trim();
        if (text === 'The Roses Underneath') {
            btn.addEventListener('click', function() {
                // Ensure all gothic tabs are completely hidden
                document.querySelectorAll('[id^="gothic_"]').forEach(function(el) { el.style.display = 'none'; el.classList.remove('active'); });
            });
        } else if (text === 'Mexican Gothic') {
            btn.addEventListener('click', function() {
                // Ensure all roses tabs (including full text) are completely hidden
                document.querySelectorAll('[id^="roses_"]').forEach(function(el) { el.style.display = 'none'; el.classList.remove('active'); });
            });
        }
    });

    // Wire every sub-nav button deterministically
    var tabMap = [
        { label: 'Summary Matrix', roses: 'roses_summary', gothic: 'gothic_summary' },
        { label: 'Character Dossiers', roses: 'roses_characters', gothic: 'gothic_characters' },
        { label: 'Discussion Questions', roses: 'roses_questions', gothic: 'gothic_questions' },
        { label: 'Historical Ledger', roses: 'roses_timeline', gothic: 'gothic_timeline' },
        { label: 'Full Text', roses: 'roses_full_text', gothic: 'gothic_full_text' }
    ];

    tabMap.forEach(function(item) {
        var btns = Array.from(document.querySelectorAll('button')).filter(b => b.textContent.trim() === item.label);
        btns.forEach(function(btn) {
            btn.addEventListener('click', function(e) {
                var isGothic = (btn.getAttribute('onclick') && btn.getAttribute('onclick').includes('gothic')) ||
                               (btn.closest('#gothic-section, #gothic, .gothic') !== null);
                var activePrefix = isGothic ? 'gothic_' : 'roses_';
                var targetId = isGothic ? item.gothic : item.roses;

                // Hide all sibling sub-tabs under this book
                document.querySelectorAll('[id^="' + activePrefix + '"]').forEach(function(el) {
                    el.style.display = 'none';
                    el.classList.remove('active');
                });
                
                // Show selected tab container
                var target = document.getElementById(targetId);
                if (target) {
                    target.style.display = 'block';
                    target.classList.add('active');
                }
            });
        });
    });
});
</script>"""

content = content.replace('</body>', master_js + '\n</body>')

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied clean layout alignment and Master Tab Switcher to index.html.")

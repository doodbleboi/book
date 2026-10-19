import os
import re

HTML_FILE = "index.html"
ROSES_TXT = os.path.join("content_input", "roses_full_text.txt")
GOTHIC_TXT = os.path.join("content_input", "gothic_full_text.txt")

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html = f.read()

with open(ROSES_TXT, "r", encoding="utf-8") as f:
    roses_text = f.read()

with open(GOTHIC_TXT, "r", encoding="utf-8") as f:
    gothic_text = f.read()

# 1. Update Sub-Title to Include Version 2
html = re.sub(
    r'(<p>Literary Study Portals)(.*?</p>)',
    r'\1 &bull; Version 2\2',
    html,
    flags=re.DOTALL
)

# 2. Cleanly isolate and inject the Roses Full Text panel inside #deck-roses
roses_ft_block = f'''
            <section id="panel-roses-full_text" class="content-panel">
                <article class="content-card search-target">
                    <!-- FLAG_START: roses_full_text -->
                    {roses_text}
                    <!-- FLAG_END: roses_full_text -->
                </article>
            </section>'''

# 3. Cleanly isolate and inject the Gothic Full Text panel inside #deck-gothic
gothic_ft_block = f'''
            <section id="panel-gothic-full_text" class="content-panel">
                <article class="content-card search-target">
                    <!-- FLAG_START: gothic_full_text -->
                    {gothic_text}
                    <!-- FLAG_END: gothic_full_text -->
                </article>
            </section>'''

# Remove any old rogue full text divs floating outside decks
html = re.sub(r'<div id="gothic_full_text".*?</div>\s*</div>', '', html, flags=re.DOTALL)
html = re.sub(r'<section id="panel-roses-full_text".*?</section>', '', html, flags=re.DOTALL)
html = re.sub(r'<section id="panel-gothic-full_text".*?</section>', '', html, flags=re.DOTALL)

# InsertRoses Full Text into deck-roses before its timeline/questions
deck_roses_pattern = r'(<main id="deck-roses" class="book-deck.*?>)(.*?)(</main>)'
match_roses = re.search(deck_roses_pattern, html, flags=re.DOTALL)
if match_roses:
    inner_content = match_roses.group(2)
    # Append panel
    new_inner_roses = inner_content.strip() + '\n' + roses_ft_block
    html = html.replace(match_roses.group(0), match_roses.group(1) + '\n' + new_inner_roses + '\n' + match_roses.group(3))

# Insert Gothic Full Text into deck-gothic
deck_gothic_pattern = r'(<main id="deck-gothic" class="book-deck.*?>)(.*?)(</main>)'
match_gothic = re.search(deck_gothic_pattern, html, flags=re.DOTALL)
if match_gothic:
    inner_gothic = match_gothic.group(2)
    new_inner_gothic = inner_gothic.strip() + '\n' + gothic_ft_block
    html = html.replace(match_gothic.group(0), match_gothic.group(1) + '\n' + new_inner_gothic + '\n' + match_gothic.group(3))

# 4. Fix Sub-Nav onclick handlers on both decks
html = html.replace("activateContentZone('roses', 'roses_full_text')", "activateContentZone('roses', 'full_text')")
html = html.replace("activateContentZone('gothic', 'gothic_full_text')", "activateContentZone('gothic', 'full_text')")
html = html.replace("activateContentZone('roses', 'gothic_full_text')", "activateContentZone('roses', 'full_text')")
html = html.replace("activateContentZone('gothic', 'roses_full_text')", "activateContentZone('gothic', 'full_text')")

# Inject foolproof client-side tab switching script before </body>
router_script = '''<script>
function activateBookDeck(bookKey) {
    document.querySelectorAll('.book-selector-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.book-deck').forEach(d => d.classList.remove('active'));
    
    if (bookKey === 'roses') {
        document.getElementById('tab-btn-roses').classList.add('active');
        document.getElementById('deck-roses').classList.add('active');
    } else {
        document.getElementById('tab-btn-gothic').classList.add('active');
        document.getElementById('deck-gothic').classList.add('active');
    }
}

function activateContentZone(deckKey, zoneKey) {
    var deck = document.getElementById('deck-' + deckKey);
    if (!deck) return;
    
    deck.querySelectorAll('.sub-nav-btn').forEach(b => b.classList.remove('active'));
    deck.querySelectorAll('.content-panel').forEach(p => p.classList.remove('active'));
    
    // Find matching button and panel
    var targetPanelId = 'panel-' + deckKey + '-' + zoneKey;
    var targetPanel = document.getElementById(targetPanelId);
    
    if (targetPanel) {
        targetPanel.classList.add('active');
    }
    
    // Activate corresponding button
    event.currentTarget.classList.add('active');
}
</script>'''

# Replace old script blocks
html = re.sub(r'<script>\s*function activateBookDeck.*?</script>', '', html, flags=re.DOTALL)
html = html.replace('</body>', router_script + '\n</body>')

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print("Version 2 deployment script generated successfully.")

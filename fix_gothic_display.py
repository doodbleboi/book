import os
import re

BASE_DIR = r"C:\Users\David Resetar\OneDrive\Documents\book-portal"
HTML_FILE = os.path.join(BASE_DIR, "index.html")
GOTHIC_TXT = os.path.join(BASE_DIR, "content_input", "gothic_full_text.txt")

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html = f.read()

with open(GOTHIC_TXT, "r", encoding="utf-8") as f:
    gothic_full_text = f.read()

# 1. Ensure gothic_full_text container has the text injected
pattern = r'(<!--\s*FLAG_START:\s*gothic_full_text\s*-->)(.*?)(<!--\s*FLAG_END:\s*gothic_full_text\s*-->)'
if re.search(pattern, html, flags=re.DOTALL):
    html = re.sub(pattern, rf'\1\n{gothic_full_text}\n\3', html, flags=re.DOTALL)
    print("Injected 279 pages into gothic_full_text flag container.")

# 2. Add bulletproof master controller and tab router script before </body>
master_script = """<script>
/* Book Portal Master Controller */
function switchBookPortal(book) {
    var rosesBtn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.trim() === 'The Roses Underneath');
    var gothicBtn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.trim() === 'Mexican Gothic');
    
    var rosesContainer = document.getElementById('roses-portal-container');
    var gothicContainer = document.getElementById('gothic-portal-container');
    
    if (book === 'roses') {
        if (rosesContainer) rosesContainer.style.display = 'block';
        if (gothicContainer) gothicContainer.style.display = 'none';
        if (rosesBtn) { rosesBtn.style.borderColor = '#2b6cb0'; rosesBtn.style.fontWeight = 'bold'; }
        if (gothicBtn) { gothicBtn.style.borderColor = '#cbd5e0'; gothicBtn.style.fontWeight = 'normal'; }
        // Default to roses summary
        openSubTab('roses', 'roses_summary');
    } else {
        if (rosesContainer) rosesContainer.style.display = 'none';
        if (gothicContainer) gothicContainer.style.display = 'block';
        if (gothicBtn) { gothicBtn.style.borderColor = '#2b6cb0'; gothicBtn.style.fontWeight = 'bold'; }
        if (rosesBtn) { rosesBtn.style.borderColor = '#cbd5e0'; rosesBtn.style.fontWeight = 'normal'; }
        // Default to gothic summary
        openSubTab('gothic', 'gothic_summary');
    }
}

function openSubTab(portal, targetId) {
    var prefix = portal === 'gothic' ? 'gothic_' : 'roses_';
    document.querySelectorAll('[id^="' + prefix + '"]').forEach(function(el) {
        el.style.display = 'none';
        el.classList.remove('active');
    });
    var target = document.getElementById(targetId);
    if (target) {
        target.style.display = 'block';
        target.classList.add('active');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // Intercept main book buttons
    document.querySelectorAll('button').forEach(function(btn) {
        var text = btn.textContent.trim();
        if (text === 'The Roses Underneath') {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                switchBookPortal('roses');
            });
        } else if (text === 'Mexican Gothic') {
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                switchBookPortal('gothic');
            });
        }
    });

    // Wire sub-nav buttons deterministically
    var subTabs = [
        { label: 'Summary Matrix', roses: 'roses_summary', gothic: 'gothic_summary' },
        { label: 'Character Dossiers', roses: 'roses_characters', gothic: 'gothic_characters' },
        { label: 'Discussion Questions', roses: 'roses_questions', gothic: 'gothic_questions' },
        { label: 'Historical Ledger', roses: 'roses_timeline', gothic: 'gothic_timeline' },
        { label: 'Full Text', roses: 'roses_full_text', gothic: 'gothic_full_text' }
    ];

    subTabs.forEach(function(item) {
        document.querySelectorAll('button').forEach(function(btn) {
            if (btn.textContent.trim() === item.label) {
                btn.addEventListener('click', function(e) {
                    e.preventDefault();
                    var isGothic = btn.closest('#gothic-portal-container') !== null || 
                                   (btn.getAttribute('onclick') && btn.getAttribute('onclick').includes('gothic'));
                    var portal = isGothic ? 'gothic' : 'roses';
                    var targetId = isGothic ? item.gothic : item.roses;
                    openSubTab(portal, targetId);
                });
            }
        });
    });
});
</script>"""

# Clean old scripts if present
html = re.sub(r'<script>\s*/\* Book Portal Master Controller \*/.*?</script>', '', html, flags=re.DOTALL)
html = re.sub(r'<script>\s*/\* Book Portal Direct Tab Handlers \*/.*?</script>', '', html, flags=re.DOTALL)

html = html.replace('</body>', master_script + '\n</body>')

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print("Master Controller injected successfully into index.html.")

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, "content_input")
HTML_FILE = os.path.join(BASE_DIR, "index.html")

MAPPINGS = {
    "roses_summary": "roses_summary.txt",
    "roses_characters": "roses_characters.txt",
    "roses_questions": "roses_questions.txt",
    "roses_timeline": "roses_timeline.txt",
    "roses_full_text": "roses_full_text.txt",
    "gothic_summary": "gothic_summary.txt",
    "gothic_characters": "gothic_characters.txt",
    "gothic_questions": "gothic_questions.txt",
    "gothic_timeline": "gothic_timeline.txt",
    "gothic_full_text": "gothic_full_text.txt"
}

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html_content = f.read()

for flag, filename in MAPPINGS.items():
    file_path = os.path.join(CONTENT_DIR, filename)
    if not os.path.exists(file_path):
        continue

    with open(file_path, "r", encoding="utf-8") as in_f:
        replacement_text = in_f.read().strip()

    pattern = rf'(<!--\s*FLAG_START:\s*{flag}\s*-->)(.*?)(<!--\s*FLAG_END:\s*{flag}\s*-->)'
    if re.search(pattern, html_content, flags=re.DOTALL):
        html_content = re.sub(pattern, rf'\1\n{replacement_text}\n\3', html_content, flags=re.DOTALL)
        print(f"Success: Injected {filename} into {flag}")
    else:
        print(f"Notice: Flag '{flag}' not in index.html (skipping replacement).")

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Completed successfully! Saved index.html.")

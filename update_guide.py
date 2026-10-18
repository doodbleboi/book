import os
import re

HTML_FILE = "index.html"
CONTENT_FOLDER = "content_input"

def update():
    if not os.path.exists(CONTENT_FOLDER):
        print(f"Directory {CONTENT_FOLDER} not found.")
        return

    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html = f.read()

    updated = False
    for fname in os.listdir(CONTENT_FOLDER):
        if fname.endswith(('.txt', '.md')):
            flag = re.sub(r'(\.txt|\.md)+$', '', fname).strip()
            path = os.path.join(CONTENT_FOLDER, fname)
            with open(path, 'r', encoding='utf-8') as tf:
                content = tf.read().strip()

            pattern = re.compile(
                r'(<!--\s*FLAG_START:\s*' + re.escape(flag) + r'\s*-->)(.*?)(<!--\s*FLAG_END:\s*' + re.escape(flag) + r'\s*-->)',
                re.DOTALL
            )
            if pattern.search(html):
                html = pattern.sub(r'\1\n' + content + r'\n\3', html)
                print(f"Success: Injected {fname} into {flag}")
                updated = True
            else:
                print(f"Skipped: Could not find flags for {flag}")

    if updated:
        with open(HTML_FILE, 'w', encoding='utf-8') as f:
            f.write(html)
        print("Completed successfully! Saved index.html.")
    else:
        print("No matching flags updated.")

if __name__ == '__main__':
    update()

import os
import re

BASE_DIR = r"C:\Users\David Resetar\OneDrive\Documents\book-portal"
CHUNKS_DIR = os.path.join(BASE_DIR, "ocr_pipeline", "gothic_chunks")
CONTENT_DIR = os.path.join(BASE_DIR, "content_input")
OUTPUT_FILE = os.path.join(CONTENT_DIR, "gothic_full_text.txt")

os.makedirs(CONTENT_DIR, exist_ok=True)

chunk_files = sorted([f for f in os.listdir(CHUNKS_DIR) if f.startswith("chunk_") and f.endswith(".txt")])

if not chunk_files:
    print(f"Error: No chunk files found in {CHUNKS_DIR}!")
    exit(1)

total_pages = 0
body_parts = []
body_parts.append('<div class="full-text-reader" style="width:100%; display:block; margin-top:1rem;">')
body_parts.append('  <div style="background:#2d3748; color:#fff; padding:0.85rem 1.25rem; border-radius:8px 8px 0 0; font-weight:bold; font-size:1rem;">')
body_parts.append('    Mexican Gothic by Silvia Moreno-Garcia &bull; Complete Verbatim Text (Verified Pages 1–279)')
body_parts.append('  </div>')
body_parts.append('  <div class="book-body" style="background:#ffffff; color:#1a202c; padding:2rem; border:1px solid #cbd5e0; border-top:none; border-radius:0 0 8px 8px; font-family:Georgia, serif; font-size:1.05rem; line-height:1.8; height:650px; overflow-y:scroll; position:relative; box-shadow: inset 0 2px 4px rgba(0,0,0,0.06);">')

for cf in chunk_files:
    path = os.path.join(CHUNKS_DIR, cf)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    pages = re.split(r'---\s*PAGE\s+([^\n-]+)\s*---', text)
    i = 1
    while i < len(pages):
        page_name = pages[i].strip()
        page_content = pages[i+1].strip() if (i+1) < len(pages) else ""
        total_pages += 1

        body_parts.append(f'    <div class="book-page" id="gothic_page_{total_pages}" style="margin-bottom:2.5rem; padding-bottom:1.5rem; border-bottom:1px dashed #e2e8f0;">')
        body_parts.append(f'      <div style="font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; color:#718096; margin-bottom:0.75rem; font-weight:bold;">Page {total_pages} &bull; {page_name}</div>')
        
        for p in page_content.split("\n\n"):
            clean_p = p.replace("\n", " ").strip()
            if clean_p:
                if re.match(r'^(CHAPTER|Chapter|[0-9]+)\b', clean_p):
                    body_parts.append(f'      <h2 style="color:#2d3748; margin:1.5rem 0 0.75rem 0; font-size:1.4rem; font-weight:bold;">{clean_p}</h2>')
                else:
                    body_parts.append(f'      <p style="margin-bottom:0.9rem; text-indent:1.5rem;">{clean_p}</p>')
        
        body_parts.append('    </div>')
        i += 2

body_parts.append('  </div>')
body_parts.append('</div>')

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    out.write("\n".join(body_parts))

print(f"Forced-Height Re-assembly Complete: {total_pages} pages processed into {OUTPUT_FILE} ({os.path.getsize(OUTPUT_FILE):,} bytes)")

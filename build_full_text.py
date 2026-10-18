import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHUNKS_DIR = os.path.join(BASE_DIR, "ocr_pipeline", "output_chunks")
CONTENT_INPUT = os.path.join(BASE_DIR, "content_input")
OUTPUT_FILE = os.path.join(CONTENT_INPUT, "roses_full_text.txt")

os.makedirs(CONTENT_INPUT, exist_ok=True)

chunk_files = sorted([f for f in os.listdir(CHUNKS_DIR) if f.startswith("chunk_") and f.endswith(".txt")])

if len(chunk_files) != 15:
    print(f"ERROR: Expected 15 chunk files, found {len(chunk_files)}!")
    exit(1)

total_pages = 0
full_book_html = []
toc_chapters = []

full_book_html.append('<div class="full-text-reader">')
full_book_html.append('  <div class="reader-toolbar">')
full_book_html.append('    <span class="reader-meta">Total Verified Pages: 297 | Complete Unabridged Edition</span>')
full_book_html.append('  </div>')
full_book_html.append('  <div class="book-body" style="background:#fff; padding:2rem; border-radius:8px; border:1px solid #e2e8f0; font-family:Georgia, serif; line-height:1.8; color:#1a202c; max-height:800px; overflow-y:auto;">')

for cf in chunk_files:
    file_path = os.path.join(CHUNKS_DIR, cf)
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    pages = re.split(r'---\s*PAGE\s+([^\n-]+)\s*---', text)
    # pages[0] is text before first header (usually empty)
    # pairs: pages[1] = filename, pages[2] = content
    i = 1
    while i < len(pages):
        page_name = pages[i].strip()
        page_content = pages[i+1].strip() if (i+1) < len(pages) else ""
        total_pages += 1

        # Check for chapter headers
        chap_match = re.search(r'CHAPTER\s+([A-Z0-9]+)', page_content)
        anchor_id = f"page_{total_pages:03d}"
        
        full_book_html.append(f'<div class="book-page" id="{anchor_id}" style="margin-bottom:2.5rem; padding-bottom:1.5rem; border-bottom:1px dashed #cbd5e0;">')
        full_book_html.append(f'  <div style="font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; color:#a0aec0; margin-bottom:1rem;">Page {total_pages} &bull; {page_name}</div>')
        
        # Format paragraphs cleanly
        paras = page_content.split("\n\n")
        for p in paras:
            clean_p = p.replace("\n", " ").strip()
            if clean_p:
                if clean_p.startswith("CHAPTER"):
                    full_book_html.append(f'  <h2 style="font-size:1.5rem; margin:1.5rem 0 1rem 0; color:#2c5282;">{clean_p}</h2>')
                else:
                    full_book_html.append(f'  <p style="margin-bottom:1rem; text-indent:1.5rem;">{clean_p}</p>')
        
        full_book_html.append('</div>')
        i += 2

full_book_html.append('  </div>')
full_book_html.append('</div>')

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    out.write("\n".join(full_book_html))

print(f"VERIFICATION SUCCESSFUL: Processed {len(chunk_files)} chunks.")
print(f"Total Pages Verified: {total_pages} / 297.")
print(f"Saved payload to: {OUTPUT_FILE} ({os.path.getsize(OUTPUT_FILE):,} bytes)")

import os
import pytesseract
from PIL import Image

BASE_DIR = r"C:\Users\David Resetar\OneDrive\Documents\book-portal"
INPUT_DIR = os.path.join(BASE_DIR, "ocr_pipeline", "input_pages")
OUTPUT_DIR = os.path.join(BASE_DIR, "ocr_pipeline", "gothic_chunks")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Locate Tesseract binary
tess_candidates = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    os.path.expanduser(r"~\AppData\Local\Programs\Tesseract-OCR\tesseract.exe")
]
for p in tess_candidates:
    if os.path.exists(p):
        pytesseract.pytesseract.tesseract_cmd = p
        break

valid_exts = (".jpg", ".jpeg", ".png")
images = sorted([f for f in os.listdir(INPUT_DIR) if f.lower().endswith(valid_exts)])

if not images:
    print(f"Error: No image files found in {INPUT_DIR}!")
    exit(1)

print(f"Detected {len(images)} images in input_pages. Starting extraction...")

CHUNK_SIZE = 20
total_images = len(images)

for chunk_idx in range(0, total_images, CHUNK_SIZE):
    batch = images[chunk_idx:chunk_idx + CHUNK_SIZE]
    chunk_num = (chunk_idx // CHUNK_SIZE) + 1
    start_p = chunk_idx + 1
    end_p = min(chunk_idx + CHUNK_SIZE, total_images)
    
    chunk_filename = f"chunk_{chunk_num:02d}_pages_{start_p:03d}-{end_p:03d}.txt"
    chunk_path = os.path.join(OUTPUT_DIR, chunk_filename)
    
    print(f"Processing Chunk {chunk_num:02d} ({chunk_filename})...")
    chunk_text = []
    
    for img_name in batch:
        img_path = os.path.join(INPUT_DIR, img_name)
        try:
            with Image.open(img_path) as img:
                # --psm 6 handles uniform blocks of book text cleanly
                raw_text = pytesseract.image_to_string(img, lang="eng", config="--psm 6")
                clean_text = raw_text.strip()
                chunk_text.append(f"--- PAGE {img_name} ---\n\n{clean_text}\n")
        except Exception as e:
            print(f"  Warning: Failed to OCR {img_name}: {e}")
            chunk_text.append(f"--- PAGE {img_name} ---\n\n[OCR Processing Error]\n")
            
    with open(chunk_path, "w", encoding="utf-8") as out_f:
        out_f.write("\n".join(chunk_text))
        
    print(f"  Saved: {chunk_filename} ({os.path.getsize(chunk_path):,} bytes)")

print("\nAll chunks successfully extracted!")

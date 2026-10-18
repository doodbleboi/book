import os

CONTENT_DIR = "content_input"
os.makedirs(CONTENT_DIR, exist_ok=True)

# 1. Summary Matrix Scaffolding
summary_html = """<table class="matrix-table">
  <thead>
    <tr>
      <th style="width: 20%;">Narrative Arc</th>
      <th style="width: 45%;">Core Chapter Developments & Plot Points</th>
      <th style="width: 35%;">Thematic Motifs & Setting Lore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Part I: Arrival at High Place</strong><br>(Chapters 1–6)</td>
      <td>Noemí Taboada leaves 1950s Mexico City after receiving a frantic, incoherent letter from newlywed cousin Catalina. She arrives in El Triunfo, Hidalgo, entering the oppressive, mold-covered Victorian mansion of the Doyle family. First encounters with the authoritarian patriarch Howard, the cold Florence, and the quiet Francis.</td>
      <td>Contrast between cosmopolitan 1950s Mexican modernity and decayed British colonial aristocracy; isolation; atmospheric decay and sensory distortion.</td>
    </tr>
    <tr>
      <td><strong>Part II: The Looming Gloom</strong><br>(Chapters 7–15)</td>
      <td>Noemí investigates the family's abandoned silver mine and local cemetery. Catalina claims the house breathes and poisons her through the wallpaper. Noemí experiences recurring sleepwalking episodes, auditory hallucinations of a golden woman, and vivid nightmares of living golden mold.</td>
      <td>19th-century silver exploitation; English eugenics; botanical and fungal infestation as metaphors for imperialist parasitism.</td>
    </tr>
    <tr>
      <td><strong>Part III: The Mycological Secret</strong><br>(Chapters 16–22)</td>
      <td>Francis confides in Noemí about the Doyles' ancestral pact with an ancient fungal strain imported from Europe. Howard's unnatural longevity requires blood sacrifices and endogamy. Catalina and Noemí discover the truth behind Ruth Doyle's past murders and the family cemetery graves.</td>
      <td>Gothic body horror; the violence of dynastic preservation; bio-symbiosis and patriarchal coercion.</td>
    </tr>
    <tr>
      <td><strong>Part IV: The Final Rupture</strong><br>(Chapters 23–27)</td>
      <td>Forced wedding ceremony prepared by Howard and Virgil. Francis aids Noemí and Catalina in a desperate counter-attack. The confrontation in the family laboratory, the fire in the damp tunnels, and the collapse of the High Place dynasty as the cousins escape into dawn.</td>
      <td>Destruction of colonial bloodlines; reclamation of autonomy; the collapse of the haunted house archetype.</td>
    </tr>
  </tbody>
</table>"""

with open(os.path.join(CONTENT_DIR, "gothic_summary.txt"), "w", encoding="utf-8") as f:
    f.write(summary_html)

# 2. Character Dossiers Scaffolding
characters_html = """<div class="dossier-grid">
  <div class="dossier-card">
    <h4>Noemí Taboada</h4>
    <span class="dossier-badge">Protagonist</span>
    <p>A smart, glamorous 22-year-old socialite and anthropology student from Mexico City. Beneath her party-girl reputation lies keen intellect, resilience, and unshakeable courage when confronting the horrors of High Place.</p>
  </div>
  <div class="dossier-card">
    <h4>Catalina Sandoval Doyle</h4>
    <span class="dossier-badge">The Imperiled Cousin</span>
    <p>Noemí's gentle, romantic cousin whose desperate, erratic letter initiates the rescue mission. Trapped in a deteriorating marriage to Virgil Doyle and subdued by mysterious illnesses and fungal hallucinations.</p>
  </div>
  <div class="dossier-card">
    <h4>Francis Doyle</h4>
    <span class="dossier-badge">Ally / Confidant</span>
    <p>The quiet, introverted son of Florence Doyle. Unlike the rest of his family, he shows empathy and botanical curiosity. He forms a fragile bond with Noemí and becomes vital to the cousins' escape.</p>
  </div>
  <div class="dossier-card">
    <h4>Virgil Doyle</h4>
    <span class="dossier-badge">Antagonist / Husband</span>
    <p>Catalina's charming yet predatory husband. Controlled, condescending, and intensely focused on preserving the Doyle family legacy and securing control over Noemí and Catalina.</p>
  </div>
  <div class="dossier-card">
    <h4>Howard Doyle</h4>
    <span class="dossier-badge">Patriarch / Source of Infection</span>
    <p>The decrepit, ancient head of the Doyle clan. Obsessed with 19th-century theories of racial purity and eugenics, he maintains his unnatural lifespan through an ancient symbiotic fungus infused into his bloodline.</p>
  </div>
  <div class="dossier-card">
    <h4>Florence Doyle</h4>
    <span class="dossier-badge">Enforcer / Housekeeper</span>
    <p>Francis's rigid, unsmiling mother who enforces strict rules across High Place: total silence at dinners, no speaking Spanish, no unapproved outdoor excursions, and cold medical isolation.</p>
  </div>
  <div class="dossier-card">
    <h4>Dr. Arthur Cummins</h4>
    <span class="dossier-badge">Complicit Physician</span>
    <p>The local English doctor loyal to the Doyle family. Dismisses Catalina's and Noemí's symptoms as hysterical female delusion while administering tinctures that keep them subdued.</p>
  </div>
  <div class="dossier-card">
    <h4>Marta Duval</h4>
    <span class="dossier-badge">Local Healer / Curandera</span>
    <p>A village woman in El Triunfo knowledgeable in folk remedies. She provides Noemí with herbal tinctures and protective warnings regarding the cursed English cemetery and the Doyles' silver mines.</p>
  </div>
</div>"""

with open(os.path.join(CONTENT_DIR, "gothic_characters.txt"), "w", encoding="utf-8") as f:
    f.write(characters_html)

# 3. Discussion Questions Scaffolding
questions_html = """<div class="discussion-section">
  <h3>I. Thematic Strengths & Gothic Conventions</h3>
  <div class="dossier-card" style="margin-bottom: 1.5rem;">
    <h4>Subversion of Traditional Gothic Tropes</h4>
    <p>Silvia Moreno-Garcia relocates the classic European Gothic haunted house (traditionally set in Yorkshire moors or New England) to the foggy mountains of Hidalgo, Mexico. How does the clash between 1950s Mexican cosmopolitan life and decadent Victorian British isolation re-energize the genre?</p>
  </div>
  <div class="dossier-card" style="margin-bottom: 1.5rem;">
    <h4>Eugenics and Imperial Parasitism</h4>
    <p>The Doyles are literal parasites—exploiting Mexican silver mine labor in the 19th century and feeding on human hosts via symbiotic mycelium. How does the author use biological and fungal metaphors to explore colonial exploitation?</p>
  </div>

  <h3>II. Key Discussion Questions</h3>
  <ol style="line-height: 1.8; padding-left: 1.5rem; color: #2d3748;">
    <li><strong>Agency and Social Expectations:</strong> Noemí is initially characterized by her father as a frivolous party girl. How do her social poise, fashion awareness, and education serve as weapons rather than weaknesses inside High Place?</li>
    <li><strong>Fungal Symbiosis vs. Bodily Autonomy:</strong> The gloom (mycelium) creates shared memories and physical regeneration, but demands absolute submission. What does the fungus symbolize in terms of family legacy and trauma?</li>
    <li><strong>The Role of Francis:</strong> Is Francis a willing bystander to his family's crimes, or an abused victim who finally finds the strength to revolt? Can his complicity be forgiven?</li>
    <li><strong>Catalina's Letter:</strong> Why did everyone except Noemí dismiss Catalina's initial letter as hysterical madness? How does the novel critique mid-century views on women's mental health?</li>
    <li><strong>The Cemetery and the Town:</strong> How does the town of El Triunfo reflect the physical and economic aftermath of British mining companies abandoning local workers once the resources were drained?</li>
  </ol>
</div>"""

with open(os.path.join(CONTENT_DIR, "gothic_questions.txt"), "w", encoding="utf-8") as f:
    f.write(questions_html)

# 4. Historical Ledger Scaffolding
timeline_html = """<div class="timeline-container">
  <h3>Historical Ledger: British Mining in Hidalgo, Mexican Modernity, and Gothic Contexts</h3>
  <table class="matrix-table">
    <thead>
      <tr>
        <th style="width: 15%;">Time Period</th>
        <th style="width: 45%;">Historical Reality in Mexico & World Events</th>
        <th style="width: 40%;">Connection to <em>Mexican Gothic</em></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1824–1850</strong></td>
        <td>British Cornish miners arrive in Real del Monte and Pachuca, Hidalgo, bringing steam machinery to rehabilitate flooded silver mines, Cornish pasties, and British Victorian cemetery culture.</td>
        <td>The historical foundation for the Doyle family empire: British aristocrats establishing isolated enclaves and Victorian estates in the mountains of Hidalgo.</td>
      </tr>
      <tr>
        <td><strong>1880s–1910</strong></td>
        <td>The Porfiriato era: President Porfirio Díaz encourages European investment, resulting in massive foreign ownership of rail, minerals, and land alongside pseudo-scientific European eugenics theories.</td>
        <td>Howard Doyle arrives during this era, bringing European eugenics dogmas and exploiting local Mexican laborers in the silver mines until epidemics close them down.</td>
      </tr>
      <tr>
        <td><strong>1910–1920</strong></td>
        <td>The Mexican Revolution: Armed uprising overthrows the Porfiriato, expropriating foreign monopolies and asserting indigenous and national land rights.</td>
        <td>High Place becomes an isolated, declining ruin as revolutionary upheaval severs the Doyles' economic dominance over the region.</td>
      </tr>
      <tr>
        <td><strong>1950</strong></td>
        <td>The Mexican Miracle (*El Milagro Mexicano*): Mexico City experiences rapid industrialization, artistic renaissance, cosmopolitan university life, and female emancipation.</td>
        <td>The setting for Noemí's world: chic cocktail parties, automobiles, fashion, and modern anthropology contrasting with the mold-rotted stagnation of High Place.</td>
      </tr>
    </tbody>
  </table>
</div>"""

with open(os.path.join(CONTENT_DIR, "gothic_timeline.txt"), "w", encoding="utf-8") as f:
    f.write(timeline_html)

# 5. Full Text Scaffolding
full_text_html = """<div class="full-text-reader" style="width:100%; display:block;">
  <div style="background:#4a5568; color:#fff; padding:0.75rem 1.25rem; border-radius:6px 6px 0 0; font-weight:bold; font-size:0.95rem;">
    Mexican Gothic by Silvia Moreno-Garcia &bull; Unabridged Text Reader (Staged Placeholder)
  </div>
  <div class="book-body" style="background:#ffffff; color:#1a202c; padding:2rem; border:1px solid #cbd5e0; border-top:none; border-radius:0 0 6px 6px; font-family:Georgia, serif; font-size:1.05rem; line-height:1.8; max-height:85vh; overflow-y:auto;">
    <div style="text-align:center; padding:3rem 1rem;">
      <h2 style="color:#2d3748; margin-bottom:1rem;">Mexican Gothic</h2>
      <p style="font-style:italic; color:#718096; margin-bottom:2rem;">By Silvia Moreno-Garcia</p>
      <div style="max-width:600px; margin:0 auto; padding:1.5rem; background:#f7fafc; border:1px dashed #cbd5e0; border-radius:8px; text-align:left;">
        <p style="margin-bottom:1rem; font-weight:bold; color:#4a5568;">Staging Container Ready</p>
        <p style="margin-bottom:0.75rem; color:#4a5568;">This section is structured and ready for your scanned or OCR-transcribed manuscript chunks.</p>
        <p style="margin-bottom:0; color:#718096; font-size:0.9rem;">To populate: Add chunk files into your pipeline and run <code>python update_guide.py</code>.</p>
      </div>
    </div>
  </div>
</div>"""

with open(os.path.join(CONTENT_DIR, "gothic_full_text.txt"), "w", encoding="utf-8") as f:
    f.write(full_text_html)

print("Created all 5 content input files for Mexican Gothic.")

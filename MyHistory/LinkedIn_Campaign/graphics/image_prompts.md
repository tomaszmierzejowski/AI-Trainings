# Image Generation Prompts — v2
## LinkedIn Campaign — THE CODE NOBODY READ

**What changed in v2:** The old prompts produced generic "abstract purple tech art" — decorative, interchangeable, and silent about what each post actually says. A graphic that could sit under any post supports no post. Every prompt below is built from the post's own message: it states the one idea the image must carry, bakes the key number or line into the image itself (the graphic must work in the feed *before* anyone reads the caption), and includes a no-text fallback for models that can't render typography.

**Model guidance:**
- **Text-in-image prompts** (primary): use GPT-Image, Ideogram 3, or Recraft — these render typography reliably.
- **No-text fallback**: use Midjourney v6+ (`--style raw`), then add text in Canva using `carousels/brand.py` constants.
- Always generate at 1350×1080 minimum (4:5 outperforms 1:1 in feed — it occupies ~30% more screen on mobile). Square 1080×1080 specs kept where the layout demands it.

**Brand system (from brand.py):**
- Purple Dark `#4D1D82` · Orange `#E8640A` · Dark BG `#1A0A2E` · Light BG `#F8F6FC`
- Rule: dark background, one orange focal element, everything else desaturated purple. Orange = the finding. Purple = the noise it hides in.

**Feed test (apply to every image before publishing):**
1. Thumb-scroll test — at phone size in a busy feed, can you read the biggest text element in under 1 second?
2. Silent test — if the caption never loaded, does the image alone make a claim someone could disagree with? (Disagreement = comments.)
3. Brand test — orange focal point, hex values match brand.py, no AI artifacts at 100% zoom.

---

## POST 5 — "THE RESCUE" (Thursday slot)

**What the post says:** A government research team could not deploy for two years; systematic code-first analysis fixed it in one month. 200+ vulnerabilities surfaced along the way.

**The one idea the image must carry:** the absurd asymmetry — 2 YEARS vs 1 MONTH.

**Primary prompt (text-capable model):**
Minimalist data-contrast poster on a near-black deep purple background (#1A0A2E). Left two-thirds: a huge horizontal progress bar made of 24 thin vertical segments in muted desaturated purple (#4D1D82), each segment slightly cracked or broken, representing 24 months of failed deployment attempts; above it the giant text "2 YEARS" in bold condensed white sans-serif, and below it in smaller light-purple text "blocked. every deployment attempt failed." Right third: a single solid glowing segment in vivid orange (#E8640A), same height as the broken bar, radiating subtle light; above it "1 MONTH" in bold orange, below it in white "read the code. deployed." Bottom edge, small white caption: "200+ vulnerabilities found on the way". Flat vector-poster style, generous negative space, no gradients except a faint glow around the orange segment, no people, no logos. Composition 4:5 vertical, 1080×1350.

**No-text fallback (Midjourney):**
A long row of 24 cracked, dim purple monolith slabs on a dark violet void floor, and at the far right one intact monolith glowing bright orange from within, dramatic rim lighting, minimalist 3D render, deep purple atmosphere (#1A0A2E background), cinematic, clean, no text, no people --ar 4:5 --v 6 --style raw
*Then overlay in Canva: "2 YEARS" over the cracked slabs, "1 MONTH" over the orange one, same copy as above.*

**Alt text for LinkedIn:** Chart contrasting 2 years of failed deployments (24 broken segments) with 1 month to a working deployment after full code analysis. 200+ vulnerabilities found along the way.

---

## POST 6 — "THE REFRAME" (Thursday slot)

**What the post says:** For 14 years an architect could personally read ~20% of a codebase; the rest of an assessment was estimation. AI-accelerated analysis moved coverage to 100%, with the architect verifying everything. Expertise matters more, not less.

**The one idea the image must carry:** 20% read vs 80% estimated — the honest anatomy of every assessment you've ever bought.

**Primary prompt (text-capable model):**
Editorial infographic on light background (#F8F6FC), styled like a printed annual-report page. A large square grid of 100 small rounded file icons, 10×10. Exactly 20 icons in the top-left corner are solid deep purple (#4D1D82) — crisp, detailed, "read". The other 80 icons are barely-visible light gray outlines, several rendered blurry or half-erased — "estimated". A thin orange (#E8640A) hand-drawn circle loops around the 20 solid icons with a small handwritten-style orange annotation: "what your assessment actually read". Headline above the grid in large dark-purple bold serif: "20% read. 80% estimated." Sub-line below the grid in smaller gray text: "That was the honest anatomy of every enterprise assessment. The ceiling has moved." Flat, precise, lots of white space, no people, no logos. 4:5 vertical, 1080×1350.

**No-text fallback (Midjourney):**
Top-down flat-lay of a 10 by 10 grid of small paper documents on a pale lavender-white surface, twenty documents in the top left corner crisp and printed in deep purple ink, the remaining eighty blank and faded almost invisible, one orange marker circle drawn around the twenty crisp documents, minimalist editorial photography, soft even light, no text legible, no people --ar 4:5 --v 6 --style raw
*Then overlay: headline "20% read. 80% estimated." + annotation as above.*

**Alt text:** Grid of 100 documents: 20 solid (read), 80 faded (estimated), with the headline "20% read. 80% estimated. That was every enterprise assessment."

---

## POST 7 — "THE RECKONING" (Thursday slot, carousel cover + share graphic)

**What the post says:** The full verified track record, published openly: 6+ engagements, 30+ repositories, zero regressions, 100% on-time, 4 days vs 4–6 weeks, 500K vs 2.3M NOK on one discovery, with an explicit invitation to challenge any number.

**The one idea the image must carry:** a consultant publishing real numbers and inviting challenge — receipts, not promises.

**Primary prompt (text-capable model):**
A dark, authoritative "receipt" poster. Background: deep purple-black (#1A0A2E) with a very subtle texture of out-of-focus source code in dark purple (#4D1D82, barely legible, 10% opacity). Centered: a tall narrow paper receipt, slightly angled, printed in crisp monospaced type, glowing softly white against the dark. Receipt lines, top to bottom: "AI DISCOVERY & MODERNIZATION — 2024→2026", a dotted divider, then line items: "engagements … 6+", "repositories analyzed … 30+", "regressions … 0", "on-time delivery … 100%", "platform migration … 4 days (industry: 4–6 wks)", "discovery cost … 500K vs 2.3M NOK", dotted divider, then in orange (#E8640A) bold at the receipt's total position: "EVERY NUMBER VERIFIED". A small orange stamp mark angled across the bottom corner of the receipt reading "CHALLENGE ANY LINE". Moody rim light, shallow depth of field, photorealistic still-life, no people, no logos. 4:5 vertical, 1080×1350.

**No-text fallback (Midjourney):**
A single long paper receipt standing upright on a dark reflective surface, lit dramatically from one side with warm orange rim light against a deep purple-black void, faint blurred code projected in the background, photorealistic product-photography style, moody, minimal, no legible text, no people --ar 4:5 --v 6 --style raw
*Then overlay the receipt line items in Canva using a monospaced font (JetBrains Mono / Courier), exact copy above.*

**Alt text:** A printed receipt listing the verified 2024→2026 track record — 6+ engagements, 30+ repositories, zero regressions, 4-day migration, 500K vs 2.3M NOK discovery cost — stamped "challenge any line".

---

## PL REPUBLICATIONS (Posts 5–7 PL)

Reuse the same generated images. Only the overlaid text changes — swap in Canva:
- Post 5 PL: "2 LATA" / "1 MIESIĄC" / "ponad 200 podatności znalezionych po drodze"
- Post 6 PL: "20% przeczytane. 80% oszacowane." / "tyle naprawdę przeczytał Twój audyt"
- Post 7 PL: "KAŻDA LICZBA ZWERYFIKOWANA" / "PODWAŻ DOWOLNĄ LINIĘ"

---

## EVERGREEN ASSETS (keep from v1, upgraded)

### Profile banner (16:9)
Abstract network of code-analysis nodes, deep purple background (#1A0A2E), thin desaturated purple connection lines, exactly one path of nodes lit in orange (#E8640A) tracing from left edge to right edge — the "one thread actually followed through the code". Right third kept visually calm and empty for overlaying the personal tagline in Canva: "Every number verified. Every finding traced to source code." No text in generation, no people, cinematic, professional B2B --ar 16:9 --v 6 --style raw

### Headshot backdrop (4:5)
Deep purple to dark navy gradient, subtle architectural grid, soft warm orange key light from one side, clean corporate, no distracting elements, no text --ar 4:5 --v 6 --style raw

---

## USAGE WORKFLOW

1. Generate with the primary prompt on a text-capable model. If typography comes out flawed (wrong glyphs, mangled diacritics — common with Polish), regenerate or fall back to the no-text prompt + Canva overlay.
2. Verify hex values with an eyedropper — models drift toward blue; correct to #4D1D82/#E8640A in post-processing if needed.
3. Run the three-question Feed Test at the top of this file.
4. Export PNG (not JPEG). Attach alt text when publishing — LinkedIn indexes it and it's an accessibility signal.
5. File naming: `post5_2years_1month_EN.png`, `post6_20pct_EN.png`, `post7_receipt_EN.png` (+ `_PL` variants).

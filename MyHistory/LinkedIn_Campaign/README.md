# LinkedIn Campaign — THE CODE NOBODY READ
## AI App Modernization | Sopra Steria | Tomasz Mierzejowski

---

> **UPDATE 2026-07-05 — v2:** Posts 0–4 published with low engagement; the campaign was overhauled. Posts 5–7 rewritten (stronger hooks, question CTAs, banned-phrase fixes). New assets: `Publishing_Strategy_v2.md` (diagnosis + two-track Tue/Thu calendar — START THERE), `Season2_The_Decision/` (6-post Thursday continuation), `graphics/image_prompts.md` (rewritten, post-specific), and the sister campaign `../LinkedIn_Mindset_Campaign/` (8-post Tuesday series). The schedule in `Publishing_Calendar.md` below is superseded by Publishing_Strategy_v2.

### The Big Idea

Every assessment you've paid for described a story about your legacy platform. Nobody actually read the code. We do. That changes everything.

### The Enemy

The Discovery Slide Deck — the industry practice of producing "insights" from interviews, documentation, and code samples, then presenting them as findings, when the actual codebase was never fully read.

### Target Reader

Stefan Andersen, 47, VP Engineering at a 2,800-person Nordic or Central European enterprise. He has a slide deck from a consulting firm that says "complex dependencies require a phased approach." He has never had anyone read every line of his code. He doesn't know yet that this is the specific problem.

---

### Campaign Arc — 7 Posts + Pre-Launch

| # | Codename | Format | Job | Key Metric |
|---|----------|--------|-----|------------|
| 0 | LWT MOMENT | Text + event photo | Timely event post, publishes before main campaign. Establishes personal presence and AI Mindset framing. Seeds the audience for Post 1. | 4-level AI spectrum, "Domek" micro-story |
| 1 | THE ALARM | Carousel | Create the realization that standard assessments are partial by design | 529 endpoints, 98 connections |
| 2 | THE INVISIBLE RISK | Text + graphic | Make the consequence of unread code viscerally real | 529, GDPR €20M exposure |
| 3 | PROOF OF SPEED | Text + graphic | Emotional proof — feel something, not just agree | 4 days, Birgit quote |
| 4 | PROOF OF SCALE | Carousel | Logical proof — enterprise scale numbers | 20 apps, 3 weeks, 500K vs 2.3M NOK |
| 5 | THE RESCUE | Text | Urgency — 2 years blocked, 1 month fixed | 200+ vulnerabilities, 16x ROI |
| 6 | THE REFRAME | Text/Video | AI's actual role — gets reshared by practitioners | 4,867 developer study |
| 7 | THE RECKONING | Carousel | Conversion — full track record, DM invitation | All verified metrics |

---

### File Structure

```
LinkedIn_Campaign/
├── README.md                    ← This file
├── Publishing_Calendar.md       ← Week-by-week schedule with warm-up actions
├── Golden_Hour_Playbook.md      ← 90-minute post-publish protocol with scripts
├── DM_Templates.md              ← Ready-to-send DM templates
├── posts/
│   ├── post1_the_alarm/
│   │   ├── copy_EN.txt          ← Publish-ready English caption
│   │   ├── copy_PL.txt          ← Publish-ready Polish caption
│   │   ├── first_comment_EN.txt ← Paste immediately after posting
│   │   ├── first_comment_PL.txt ← Polish version
│   │   ├── hook_variants.txt    ← A/B test options with recommendation
│   │   ├── engagement_triggers.txt ← 3 reply scripts for golden hour
│   │   └── underperformance_rescue.txt ← Rescue plan if post underperforms
│   ├── post2_invisible_risk/    ← Same structure
│   ├── post3_proof_of_speed/    ← Same structure
│   ├── post4_proof_of_scale/    ← Same structure
│   ├── post5_the_rescue/        ← Same structure
│   ├── post6_the_reframe/       ← Same structure + video_script.txt
│   └── post7_the_reckoning/     ← Same structure
├── carousels/
│   ├── brand.py                 ← Brand constants (colors, fonts, dimensions)
│   ├── generate_all.py          ← Run to generate all PNG slides
│   ├── post1_alarm/             ← 10 slides: slide_01.png ... slide_10.png
│   ├── post4_scale/             ← 10 slides
│   └── post7_reckoning/         ← 8 slides
├── graphics/
│   ├── post2_529_graphic.png    ← 1080×1080 standalone image
│   ├── post3_4days_graphic.png  ← 1080×1080 standalone image
│   └── image_prompts.md         ← AI image generation prompts
└── Campaign_Dashboard.html      ← Interactive campaign control center
```

---

### How to Generate Carousel Slides

```bash
pip install Pillow
cd LinkedIn_Campaign/carousels
python generate_all.py
```

Slides save to: `carousels/post1_alarm/`, `carousels/post4_scale/`, `carousels/post7_reckoning/`
Graphics save to: `graphics/`

---

### Publishing Workflow (5 minutes per post)

1. Open `posts/postN_[name]/copy_EN.txt` — copy entire contents
2. Go to LinkedIn → Start a post
3. For carousel posts: click document icon → upload PDF from `carousels/postN_[name]/`
4. Paste caption text
5. Publish between 08:00–09:30 CET (Tue–Thu preferred)
6. Immediately open `first_comment_EN.txt` → paste as first comment
7. Stay present for 90 minutes — see Golden_Hour_Playbook.md
8. After 90 min: review engagers, send DMs using DM_Templates.md

---

### Voice Rules (apply to every post and every comment)

1. Every impressive-sounding sentence is followed, within the same paragraph, by the specific number or fact that makes it real.
2. Write to Stefan at 3am — short declarative sentences, no consulting jargon.
3. AI appears once per post, always as a tool, never as the subject.

### What NOT to Say (banned phrases)

- "73% of modernization projects fail" — this statistic does not exist in any Standish report
- "200+ business rules extracted" — pre-deduplication count; use 100
- "120+ codebases" — includes test projects; use 100+
- "dealer platform / tolling / billing" — client identification risk
- "automotive / Nordic OEM" — client identification risk
- "maritime / fisheries / vessels" — use "government research organization"
- "digital transformation journey" — replace with the specific problem
- "value-add" — replace with the specific value as a number
- "AI-powered" — replace with "AI-accelerated analysis, senior architect verification"

---

### Contact

Tomasz Mierzejowski | AI App Modernization Architect | Sopra Steria
tomasz.mierzejowski@soprasteria.com

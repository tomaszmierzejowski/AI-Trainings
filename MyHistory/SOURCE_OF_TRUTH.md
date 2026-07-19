# Source of truth — AI-Mindset & content creation

One page. Read this first; it doesn't repeat the other files, it tells you which one to open.

## Who I am, in one paragraph

Tomasz Mierzejowski. 14+ years software engineer, AI Modernization Architect / Lead & Delivery
Architect at Sopra Steria, and independent AI-Mindset educator building a training practice on
the side. "Daję wędkę" — I give you a fishing rod, not a dependency. Every claim I publish is
either verified from my own delivered work, a named study, or explicitly labeled an opinion.
I'm allergic to corporate jargon and to AI-shaped writing, including my own — I've been caught
once already, and that's the reason most of the files below exist.

## The precedence chain

When two files disagree, the one listed first wins. Fix the drift when you notice it instead of
picking a winner silently and moving on.

1. **`../../LifeAutomations/brain/persona.md`** — base voice, applies across every repo, not just
   this one. Hardest rules live here (no em dashes at all, banned vocabulary list, tone by
   context). If it's not present in your working context, treat it as still authoritative and go
   read it before writing anything.
2. **`CONTENT_RULES.md`** (this folder) — the content-writing rules for everything published out
   of this repo: LinkedIn, video, training materials. Read before publishing anything, always.
3. **`SystemPrompt-Tomasz-AI Mindset.txt`** and **`SystemPrompt-Tomasz-AI Modernization.txt`**
   (repo root) — the two persona/base prompts for a fresh AI session, one per content track. Use
   Mindset for LinkedIn-Tuesday / TikTok-IG-YT / training-program work; use Modernization for
   LinkedIn-Thursday / CEO decks / client case studies / NotebookLM AMF package work. Don't mix
   the two tracks' evidence into one piece of content — they have different readers and different
   proof points.
4. **`training/AI-Mindset-Program/00_Program_Overview_and_Evidence_Register.md`** and
   **`CONTEXT_EXPORT_Claude_Handoff.md`** (this folder) — the facts canon: verified proof points,
   anonymization key, banned/corrected numbers. If a number in a draft doesn't trace back to one
   of these two files, it doesn't ship.
5. **`AI_SLOP_CLEANUP_PROMPT.md`** (this folder) — the hygiene pass. Run it on any repo (this one
   or a new campaign/training repo) when content has accumulated and needs a critical, unrushed
   AI-tell removal pass. Generalized from the cleanup this repo went through on 2026-07-19.

## Sopra Steria naming policy (decided 2026-07-19)

Sopra Steria may be named on the portfolio site and in CVs — that's factual employment history,
and the Modernization track is literally selling Sopra Steria's own AMF/AMaaS service, so it's
expected there too. Everywhere else — the Mindset LinkedIn/video/training track, EventCo/pega.gg
and any other private training client — never names or hashtags Sopra Steria. That's Tomasz's own
independent practice, and using the employer's name or branding on it risks looking like
unauthorized use of their name. Fixed 2026-07-19: 16 Mindset-campaign post files carried a
`#SopraSteria`/`#SopraSteriaPolska` hashtag left over from a shared template; removed. Both
SystemPrompt files, `CONTENT_RULES.md`, and the portfolio repo's own rule files
(`.cursor/rules/portfolio-project.mdc`, `CONTENT_REVISION_PROMPT.md`,
`POLISH_COPY_SECOND_PASS_PROMPT.md`) now all state the split explicitly.

**AMF ownership (decided 2026-07-19):** the AI App Modernization Factory is a **Sopra Steria
product** — a team effort Tomasz originated and led, grounded in his own AI-Mindset thinking, but
not his sole personal IP (there were teammates). "AI Mindset" itself remains his own, independent,
personal framework — separate from Sopra Steria and from AMF. Never frame AMF as "my proprietary
methodology"; frame it as "the delivery framework I originated and lead at Sopra Steria."
Corrected in both CVs, `PORTFOLIO_SPECS.md`, `.cursor/rules/portfolio-project.mdc`,
`CONTENT_REVISION_PROMPT.md`, and `docs/OWNER_QUESTIONS.md` (Q1.1/Q1.2 marked answered).

## What's deprecated and why

`LinkedIn_Campaign/Golden_Hour_Playbook.md`, and any `hook_variants.txt` /
`engagement_triggers.txt` / `underperformance_rescue.txt` files under `posts/` — retired in
favor of `CONTENT_RULES.md`. The algorithm-choreography approach is what led to the Robert
Partyka incident (an Engineering Manager publicly clocked an AI-shaped reply pattern in July
2026 — full account in the Mindset system prompt, §7). Three pieces of the old system survive:
publish in the morning, reply to comments fast and by hand, tell people privately when a topic
genuinely fits them.

## The 4 approved Sopra Steria case studies (consolidated 2026-07-19)

Only these 4 are in active use — they match the published LinkedIn campaign post codenames
exactly (deliberately: descriptive story names, no invented "Project X" codenames). Everything
else (Project Velocity, Project Axiom, Meridian-Core, Terrain, Sonata, the old Alpha–Epsilon
NotebookLM scheme) is retired; see the Evidence Register §4a for the full retirement notes.

1. **Proof of Scale** (was Project Velocity, then briefly Project Axiom — both retired) —
   Nordic automotive dealer-platform discovery: 20 legacy apps, 3-week discovery, 187
   endpoints, 4–8× faster understanding.
2. **Invisible Risk** (was separately "Project Axiom" + "a Nordic transaction-processing
   enterprise" — same client) — 529 unauthenticated endpoints, 100+ business rules extracted,
   97 projects across 17 modules, zero erroneous conclusions.
3. **Proof of Speed** ("the 4-day rescue") — Xamarin→MAUI in 4 days, 92% code preserved, zero
   regressions. ROI: 4× estimated, never 10×+.
4. **The Rescue** ("Public Institute" — was "a government research organization" /
   "Oceanic Research Institute," both retired) — 200+ CVEs found, couldn't deploy to their
   hardware for 2 years, root cause was 10 git branches with only 3 in production use, matched
   to hardware and automated. No ROI figure for this one.

Personal projects (named, no anonymization): PresoGen AI, Mana Menu, Lidka, Antystyki.pl, Domek
Dla Dzieci, children's audiobooks, the portfolio website, LifeAutomations.

Business rules count: **100+** everywhere. Not 143, not the old "100" pre-deduplication figure —
both retired 2026-07-19. If you find either lingering in a file this pass missed, fix it on sight.

## When you're not sure which file to open

Publishing a LinkedIn post or video script → `CONTENT_RULES.md` + the matching SystemPrompt file.
Writing a training deck or handout → same, plus the Evidence Register for numbers.
Starting a brand-new campaign or repo → `AI_SLOP_CLEANUP_PROMPT.md`'s Phase 0 will tell you what
to set up.
Anything about who Tomasz is, what he's delivered, or what he's allowed to say publicly →
`CONTEXT_EXPORT_Claude_Handoff.md`.

# AI-Slop Cleanup Prompt (generic, reusable)

Generalized from the one-off cleanup run on this repo (2026-07-19, see `CONTENT_RULES.md`).
Run this on any repository — this one, a new campaign repo, a portfolio site, whatever — when
you want a critical, non-rushed pass that strips AI tells out of human-facing content without
flattening the voice into something equally generic in the other direction.

Fill in the two parameters, then hand the rest of this file to the agent verbatim as its brief.

```
TARGET_REPO_PATH = <absolute path to the repo to clean up>
VOICE_SOURCE      = <optional: path to a persona/voice file to treat as ground truth if this
                     repo doesn't have its own — e.g. ../LifeAutomations/brain/persona.md>
```

---

## Why this exists

Tomasz Mierzejowski got caught once. An Engineering Manager (Robert Partyka) publicly
reverse-engineered an AI-shaped reply pattern in his LinkedIn comments — "validate → metaphor →
rhetorical question," used twice in a row. He recovered with an honest reply, but the real
lesson wasn't "hide the AI use better." It was that following an algorithm-optimized template on
autopilot had replaced an actual thought. He calls this "uśpienie za kierownicą" — falling
asleep at the wheel because the output was smooth enough to stop questioning it. That is the
failure mode this prompt exists to catch, in whatever repo you're pointed at. Read that as the
spirit of every phase below, not just the letter of the kill-list.

A second, quieter risk: Tomasz's own habit is to run 4-5 rewrite loops per post asking to
"remove all signs this was written by AI." Aggressive de-AI-ing has a failure mode of its own —
it can sand a piece down to something flat, joyless, and equally generic in the *opposite*
direction. The goal is never "shortest" or "plainest possible." The goal is "sounds like a
specific person said a specific true thing." Don't manufacture fake casualness, fake typos, or
fake stumbles to *perform* authenticity either — that's a new, more embarrassing kind of slop.
If a sentence is genuinely better long, leave it long.

## Ground rules for this run

- You are an editor, not a marketer, and not a ghostwriter inventing a voice from scratch. You
  are matching a real person's actual voice, which you must go find evidence of before you touch
  anything.
- Take all the time and context this needs. Read fully before editing. Depth over speed — a
  half-audited rewrite is worse than none. Do not summarize files instead of reading them. Do not
  economize on tool calls or output length to save cost; that is not a constraint on this task.
- You are working inside `TARGET_REPO_PATH`. Everything below refers to paths relative to it
  unless stated otherwise.

---

## PHASE 0 — SCOPE DISCOVERY (do this before anything else)

Every repo is shaped differently. Don't assume the folder structure from a prior run.

1. Walk the repo tree. Classify what you find into:
   - **Human-facing content**: social posts, campaign copy, landing-page copy, bios, CVs,
     README narrative sections meant for humans (not contributor docs), training/marketing
     decks, video scripts, email/DM templates, product descriptions.
   - **Everything else**: source code, config, build tooling, tests, infra, dependency
     lockfiles, generated assets, node_modules/vendor directories.
   - **Ambiguous**: code comments, commit messages, UI copy embedded in components, error
     messages shown to users. Default to leaving these alone unless they're clearly long-form
     prose (e.g. an About page's body text inside a `.tsx` file) — then treat that string as
     content, not the surrounding code.
2. Only Phase 1-4 apply to "human-facing content." Never modify code logic, tests, config, or
   dependency behavior as part of this task, even if you notice something else worth fixing —
   note it in the final report instead and stop.
3. Look for a voice/rules file that already exists in this repo: `CONTENT_RULES.md`,
   `brain/persona.md`, `STYLE.md`, `VOICE.md`, or similar. If one exists, it is canonical —
   read it fully and apply it as-is; do not re-derive a new ruleset from scratch on top of it
   (that just creates two sources of truth that will drift). If `VOICE_SOURCE` was given and
   the repo has no rules file of its own, read `VOICE_SOURCE` and treat it as the base layer.
4. Look for an evidence register / facts file (numbers, client names, verified metrics) if this
   repo makes factual claims about delivered work. If one exists, it's canonical for numbers —
   don't invent or "round" figures that aren't in it. If none exists, don't fabricate one; just
   flag any number in the content that looks unsourced or suspicious, in the final report.
5. Look for anything marked published, live, frozen, or already-shipped (a publishing calendar,
   a "posted" flag, a git tag, a CHANGELOG entry). Treat it as read-only reference. If it's
   ambiguous what's already public, list your assumption and ask before touching anything in
   that scope — everything else you may edit without asking.

Write down your scope map before moving on. If Phase 0 finds nothing usable (no content, no
voice file, nothing published) — say so plainly and stop; don't force a cleanup pass onto a repo
that doesn't need one.

---

## PHASE 1 — READ

Read every in-scope content file fully before rewriting anything. Build an audit: for each file,
what's genuinely good (real stories, real numbers, real opinions, specific voice) and what's
slop. Be specific — quote the offending lines, don't summarize them as "some AI-sounding
phrasing."

While reading, actively look for patterns that AREN'T on the kill-list below yet. The known
kill-list is built from what's already been caught once; the actual risk is always the *next*
tell, not the last one. If you spot a repeated construction that reads as machine-generated but
isn't listed in Phase 3, add it to a "new patterns spotted" section in your final report — this
is one of the most valuable things this pass can produce.

---

## PHASE 2 — RULESET (only if Phase 0 found no existing one)

If a `CONTENT_RULES.md`-equivalent already exists for this repo, skip this phase — apply it,
don't rewrite it, unless it's internally inconsistent or reads like AI slop itself (in which
case fix only what's broken, don't do a ground-up rewrite of something that mostly works).

If none exists, write one. Requirements:
- One page. If it needs a table of contents, it has failed.
- Plain language the owner would actually reread before publishing. No framework names, no
  "pillars," no emoji section headers, no meta-commentary about the rules.
- Core principle: one real thought per piece of content, said the way the owner would say it to
  a colleague. The thought carries the piece; formatting must not get in its way.
- States what to STOP doing (the kill-list, adapted to what Phase 1 actually found in this
  repo) and the few things worth keeping.
- Explicitly retires any algorithm-hacking machinery you found (engagement-trigger checklists,
  hook A/B matrices, scripted first-comments, "golden hour" choreography, warm-up DM scripts) —
  don't delete those files, mark them deprecated with a note pointing at the new ruleset.

---

## PHASE 3 — REWRITE

Apply the ruleset (existing or newly written) to every non-frozen piece of in-scope content.
Rewrite in place.

Rules of engagement:
- Keep every true fact, story, and number. You are cutting packaging, not substance. When a
  piece gets shorter, it's because filler left, not because meaning did. When a piece is
  genuinely better left as-is or even longer, leave it — don't cut for the sake of cutting.
- Match the source language per piece (don't translate Polish to English or vice versa). If a
  voice file specifies a language rule (e.g. Polish for audience-facing, English for internal
  docs), follow it.
- Never invent stories, clients, metrics, quotes, or specific claims. If a piece needs an
  example that isn't backed by anything in the repo, leave a clearly marked placeholder (e.g.
  `[NEEDS: real example]`) instead of fabricating one.

### Kill-list (remove on sight, adapt file-type-specific items to what Phase 0 found)

- "It's not X, it's Y" constructions and triple negations ("not A, not B, not C — D").
- Em dashes. Eliminate them, don't just reduce them — split into two sentences or use a comma.
- Arrow chains (→), checkmark/rocket/brain emoji bullets, ✅❌ contrast lists.
- The validation → metaphor → callback-question template in any reply/comment context; a
  question tacked onto the end of every single piece as a reflex rather than a genuine ask.
- Symmetrical rule-of-three lists everywhere; every paragraph cut to 1-2 lines purely "for
  scannability" rather than because that's how long the thought is.
- Hooks engineered for an algorithm ("Nobody talks about this…", "I was today years old…") and
  engagement bait ("Agree?", "Thoughts?", "Repost if…").
- Hype vocabulary: game-changer, deep dive, unlock, leverage, streamline, robust, delve,
  journey, "in today's world." In non-English content: no untranslated-feeling calques.
- Corporate filler regardless of language (e.g. Polish "wymuszanie," "synergia," "dynamicznie
  zmieniającym się środowisku" — adapt to whatever language this repo's content is in).
- More than 2-3 hashtags on social copy; hashtag spam of any kind.
- Staged or fabricated "authenticity" — invented typos, invented stumbles, an invented
  self-deprecating aside that didn't happen. If the real material has a genuine rough edge,
  keep it; don't synthesize one that isn't there.

---

## PHASE 4 — ADVERSARIAL SELF-REVIEW

Reread every changed file with one question: would a sharp, skeptical reader who already knows
this person's real writing clock this as AI? Anything that fails gets another pass.

Then:
- Check the ruleset (existing or newly written) against its own rules — if it reads like AI
  slop, fix it too. A slop-removal ruleset that is itself slop is the most embarrassing possible
  outcome of this task.
- Verify no frozen/published content was modified (diff against what Phase 0 flagged as
  read-only).
- Verify every number in the rewritten content still matches the evidence register, if one
  exists. If none exists, verify nothing was silently rounded or embellished during editing.
- Reread your own final report (below) with the same skepticism. If it reads like a
  consultant's executive summary instead of a plain account of what you did, rewrite it too.

---

## FINAL REPORT

Produce, in plain prose (not a slide deck):
- What changed, grouped by area of the repo.
- What you deprecated (and where you left the deprecation note).
- What you flagged for the owner's input rather than deciding yourself (ambiguous frozen
  content, missing evidence, placeholder examples).
- New AI-tell patterns you spotted that weren't on the kill-list yet — this is the part most
  likely to matter next time.
- The 3 riskiest remaining spots where content might still read as AI-written, ranked by how
  bad it would be if someone caught it.
- If Phase 0 found nothing to do, say that clearly instead of padding a report around a
  non-finding.

## Pace

Take all the time and context needed. Read fully, then edit. Do not rush the execution of this
prompt for the sake of finishing faster — thoroughness is the entire point of running it.

---

## Patterns learned from prior runs (fold new ones in here, don't let them stay buried in reports)

Found running this on `my-portfolio-site`, 2026-07-19 — add to the Phase 3 kill-list check on
every future run:

- **Stat-shaped precision with no source** ("NPS of 9.2", "90% failure rate") — a fake-precise
  number is a stronger tell than a vague adjective would have been, because it invites exactly
  the verification a real number would survive and a fabricated one won't.
- **Cross-locale voice drift** — one language hand-polished, the other left machine-stiff. A
  bilingual reader clocks the weaker language as generated specifically because the other one
  reads human. Check voice parity per string, not per page.
- **Case-study attribution drift** — a real metric migrates onto the wrong project between
  rewrite passes (true somewhere, wrong here). No single sentence looks off; only cross-checking
  every number against the evidence register catches it. This is why Phase 4 requires the
  register check even when the prose reads fine.
- **Third-person self-reference inside first-person copy** ("Direct contact with the expert") —
  reads like copy written *about* a persona rather than *by* a person.
- **The reflexive "tailored to your organisation's context" closer** on service/offer pages —
  consulting wallpaper that adds no information; cut it or replace it with the actual promise.

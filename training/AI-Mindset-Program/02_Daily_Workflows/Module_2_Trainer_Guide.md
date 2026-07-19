# Module 2 — Rewiring the Daily Workflow (Trainer Guide)

**Total time:** half-day (≈3.5–4 h incl. break) · **Room:** laptops required, accounts provisioned IN ADVANCE (see logistics) · **Materials:** fictional datasets (claims/onboarding/service CSVs from the shared kit), legacy codebase sample repo, source-doc pack for NotebookLM track

## Logistics (do this a week before, or the module fails)
- Confirm participants have working access to Claude, Cursor, NotebookLM, and Gemini **under the client's governance rules**. Access friction on the day destroys the module's credibility — a session about removing friction cannot open with a login queue.
- Ask each participant (via the pre-training survey) to bring **one real task** from their current backlog. Have 6–8 backup tasks ready for those who arrive empty-handed.
- Verify the legacy codebase sample opens in Cursor on a locked-down laptop.

## Timing plan

| Segment | Slides | Time |
|---|---|---|
| Principle + anti-pattern + map | 1–4 | 20 min |
| Prompting habits (RTF, iterate) | 5–7 | 25 min |
| Tool blocks: Claude / Cursor / NotebookLM / Gemini | 8–15 | 50 min |
| Proof points (Lidka, PresoGen, Mana Menu) | 16–17 | 10 min |
| — break — | | 15 min |
| Lab briefing + lab | 18–19 | 100 min |
| Debrief + verification handshake + habit contract | 20–22 | 30 min |

## Speaker notes by segment

### Slides 1–4 (Principle)
Restate Module 1's thesis in operational terms: "Yesterday we diagnosed. Today we rewire." The tool map (slide 4) is the module's spine — keep returning to it. Emphasize the *trigger* column: habits attach to triggers, not to intentions. When presenting the map, be honest about overlap: "These tools overlap heavily. The map is not a law — it's a default that kills decision paralysis."

### Slides 5–7 (Prompting habits)
RTF is deliberately the only framework taught — one frame practiced beats five frames admired. Run slide 6 live, twice: once with the lazy prompt, once with RTF, same source document. Let the room see the delta rather than being told about it. Do NOT quote accuracy percentages for prompting techniques — no defensible source exists; the live contrast is the evidence.
The "brilliant new colleague on day one" analogy sets up iteration: you'd never fire a new hire for a mediocre first draft; you'd give feedback. Same behavior here.

### Slides 8–9 (Claude)
Position Claude as the *default first step* for thinking and writing work. The demo (slide 9) must use fictional data — model the governance behavior you preach; say out loud: "Notice what I did NOT paste in: client names, real personal data. That reflex is Module 3." One refinement pass minimum in the demo — demonstrate iterate-don't-regenerate rather than only describing it.

### Slides 10–11 (Cursor)
For mixed audiences, frame codebase Q&A as valuable even for non-coders who work *near* code (BAs, PMs): "the end of 'wait for a developer to explain it.'" The leash rule (slide 11) is the module's most important safety rail for engineers: inline edit = review each hunk; agent mode = review the whole diff like a hostile PR. The Proof of Scale sidebar earns you the right to say this works at enterprise scale — 20 apps, 3 weeks, 187 endpoints — but attribute honestly: that result came from a designed pipeline with verification gates (Module 4), not from casual chat with an IDE.

### Slides 12–13 (NotebookLM)
This tool lands hardest with non-technical participants — give it full energy, don't treat it as the "small" tool. Live demo if time allows: upload 3 provided docs, ask a question, show the citation, click through to the source passage. Then generate an audio overview and play 30 seconds. The behavioral pitch: "You don't read the pile. You interrogate the pile, and it must show its receipts."

### Slides 14–15 (Gemini + decision tree)
Gemini's slot is scale and modality — video/meeting recordings, enormous inputs, Workspace surface. Resist feature-listing; one vivid example ("interrogate the 90-minute recording you were never going to watch") beats ten. The decision tree closes the loop on tool paralysis; the escape hatch "when in doubt, start in Claude" is deliberate — a default beats a debate.

### Slides 16–17 (Proof points)
Lidka answers the room's silent question: "fine for engineers, but what about *me*?" A non-technical publisher runs her own store — full autonomy is the fishing-rod philosophy delivered. PresoGen/Mana Menu answer the engineers' silent question: "AI-first must mean test-poor" — ~600/~657 automated tests say otherwise.

### Slides 18–20 (Lab)
The lab IS the module; everything before it is setup. Rules of circulation: never touch a keyboard — ask "what would you tell a new colleague to do differently?" and let them type. Push every participant to one *complete* artifact rather than three fragments. During debrief, name behaviors, not outputs: "Notice Anna's second prompt — she narrowed the role. That's the habit."

### Slides 21–22 (Close)
The verification handshake is one sentence, delivered slowly: "AI generates. You verify. You own." It must land before Module 3 or the governance content there feels like bureaucracy instead of professionalism. Habit contracts: concrete tool + trigger + calendar slot; pair-exchange creates the accountability partner for Module 5.

## Discussion prompts
1. "What did you *almost* not verify in your lab artifact?"
2. "Which old behavior will be hardest to give up — and what makes it sticky?" (echo the friction map)
3. For engineers: "Where's the line where you'd stop trusting agent mode?"

## Likely objections & responses
- **"Our company blocks tool X."** — "Then we anchor your habits on the tools you do have; the habits transfer. The map is a default, not a doctrine." (Know the client's actual toolset before the session — survey question.)
- **"I tried Cursor/Copilot and the suggestions were bad."** — "On what codebase, and how much context did you give it? A colleague with no onboarding also gives bad suggestions. The leash rule plus codebase Q&A first usually flips this experience." Offer to pair on their repo in the lab.
- **"This is faster for juniors; I'm faster by hand."** — "For the typing, maybe. The field data shows the biggest gains go to those who changed workflow, and 'by hand' includes all the reading, searching and re-explaining around the typing. Time yourself honestly for one week."
- **"NotebookLM cites sources, so I can skip verification."** — "It cites *your* sources — it can still summarize them imperfectly, and your sources can be wrong. Citations shrink the verification job; they don't delete it."
- **"Four tools is already sprawl."** — Concede readily: "Correct. One habit on one tool that fits your work beats four half-habits. The map is a menu, not a shopping list."

## Failure modes for the trainer
- Feature-touring. If you hear yourself saying "and it can also…", stop — return to old-behavior→new-behavior.
- Letting the lab drift into playground mode (novelty prompts, no artifact). The success criterion — shippable artifact + prompt trail — is the guardrail.
- Demoing with real client data. Instant credibility loss on governance.

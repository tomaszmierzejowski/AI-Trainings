# Module 3 — Trust, Verification, and Evidence over Opinion (Trainer Guide)

**Total time:** 90 min · **Materials:** planted-error exercise handout (one per pair) + answer key; parking-lot items from Module 1 (governance questions promised to be answered here)

## Timing plan

| Segment | Slides | Time |
|---|---|---|
| Two failure modes + what hallucination is | 1–3 | 15 min |
| Grounding rules & behaviors | 4–5 | 10 min |
| Verified cases (Invisible Risk, evidence-tagged discovery) | 6–7 | 15 min |
| Hidden complexity + trust matrix | 8–9 | 15 min |
| Verification habits + governance + Antystyki | 10–12 | 15 min |
| Exercise: catch the confident lie | 13 | 15 min |
| Recap + parking lot payoff | 14 | 5 min |

## Speaker notes by segment

### Slides 1–3 (Failure modes)
Open by rehabilitating both camps in the room: the burned skeptic and the enthusiastic over-truster are making the *same* error — treating trust as a feeling about the tool instead of a property of the task. This module is where the skeptics come back on board; give their objection dignity before dissolving it: "If you've been burned by a hallucination, your caution is data. We're going to aim it."
Slide 3: keep the explanation mechanical, not mystical. "It completes text plausibly" is enough — resist the temptation to teach transformer internals (that's the optional masterclass track).

### Slides 4–5 (Grounding)
Rule 1 is the single most reusable sentence for leaders in the room: truth lives in systems of record; AI is the understanding layer. On slide 5, land the reflexivity: "No citation, no claim — notice that's the standard these slides hold themselves to. Every number today has a badge. Demand the same from your AI and from your consultants."

### Slides 6–7 (Cases — the module's spine)
Invisible Risk must be told as *protocol, not model*: "Zero erroneous conclusions across 97 projects did not happen because the model was infallible. It happened because no AI finding entered the report without passing a human gate. The reliability lives in the process design." This is the sentence skeptics quote back later — rehearse it.
Slide 7: the phrase to land is "discovery you can audit beats discovery you must believe." Evidence-tagged citations mean a client can challenge any finding and be shown the exact line of code. Anonymity discipline: never name the client, the country, or the industry vertical.

### Slides 8–9 (Complexity + matrix)
Standish: quote it honestly — ~31% succeed outright (2020). Do NOT use any "73% of modernization projects fail" formulation; that statistic does not exist and the program's credibility rests on never inventing numbers. The pivot sentence: "Most failed projects didn't lack information. They ran on unverified assumptions."
The trust matrix is the module's practical takeaway. Walk one concrete example per quadrant from the audience's world (ask the room to supply them — their examples stick better than yours). The hard quadrant is high-stakes + hard-to-verify: the answer is *decompose until verifiable*, not "be careful."

### Slides 10–12 (Habits + governance)
The 60-second spot-check order matters: names, numbers, dates first — that's where fabrication density is highest. For engineers, tests-as-trust is the bridge from craft pride to AI adoption: "~600 tests is what lets PresoGen swap between three LLM providers without fear. Your test suite is your trust infrastructure."
Governance (slide 11): deliver as an enabler, not a compliance lecture — "these four rules are what let you say *yes* in seconds instead of waiting three weeks for a security review." Now pay off the Module 1 parking lot: answer the specific "our data can't go into these tools" items collected earlier, in front of the room.
Antystyki (slide 12) closes the loop with humility: even the author's own statistics pipeline keeps a human on the trigger.

### Slide 13 (Exercise — build it carefully beforehand)
Construct the handout so that: error 1 (wrong number) is findable by cross-checking the attached source table; error 2 (fabricated citation) is findable by looking for the cited source that doesn't exist in the pack; error 3 (inverted conclusion) *sounds* fluent and survives most pairs. The debrief insight to surface: fluency masks falsehood — the error that survived longest was the best-written one. That single felt experience does more than every slide before it.

### Slide 14 (Recap)
Close on identity, not fear: "Verification isn't distrust of AI. It's the thing that makes your signature mean something."

## Discussion prompts
1. "Which quadrant of the trust matrix does most of your daily work fall into? Does your current behavior match?"
2. "What's your team's system of record for the facts you most often ask AI about — and is it actually current?"
3. "Who reviews AI-assisted work in your org today? Anyone? Everyone? Randomly?"

## Likely objections & responses
- **"Verification eats all the time savings."** — "Only if you verify everything at the same intensity. That's what the matrix is for: calibrated verification. Invisible Risk verified 97 projects' worth of findings and still finished in a fraction of traditional time — gates are cheap, rework is expensive."
- **"If it needs checking, it's not ready for real work."** — "Every junior colleague's work needs checking; they're still valuable. And unlike a junior, AI never gets offended by review and never repeats *your* correction reluctantly."
- **"Our compliance team will never allow any of this."** — "Compliance teams say no to unbounded requests. Bring them slide 11 — scoped tools, least privilege, logging, no personal data — and the conversation changes. Governance done well is precisely what makes compliance comfortable."
- **"NotebookLM/RAG cites sources, so hallucination is solved."** — "Reduced by design, not solved. The summary of a true source can still be wrong, and a true source can still be outdated. Citations shrink the check; they don't replace it."
- **"Won't a second-model cross-check just double the cost?"** — "You reserve it for the high-stakes/hard-to-verify quadrant — by definition the smallest slice of your day."

## Failure modes for the trainer
- Sliding into fear-based delivery. The module's tone is professional pride, not danger. If the room goes quiet and anxious, return to the Invisible Risk story — competence, not catastrophe.
- Quoting hallucination-rate statistics. Rates vary wildly by model, task and year; any number you quote will be wrong soon and unverifiable now. The planted-error exercise is your evidence.
- Letting the governance slide balloon. Four rules, five minutes, point to the client's own policy for the rest.

# Project Zero

## Story so far
It started with reading Steven Pressfield's *Do the Work* and the uncomfortable recognition that waiting for a perfect plan is itself a form of resistance. So a thought was typed into a plain text file and published on jithusunny.com. That was the beginning.

The idea was simple but ambitious: capture raw thoughts as they come, in the most frictionless way possible. Plain text files. No IDs, no metadata, no structure. Just time and words. Everything else — organization, links, views — would be derived later, never embedded. The raw stream would remain immutable and decoupled from any system built on top of it.

Early on, an insight emerged that became a guiding metaphor: the "bigbang method." Set the initial configuration and rules, then let it run without interference. Refine between iterations, but never interfere mid-run. Applied to this project, it meant: define the rules of extraction, let the system evolve, take rest.

Then came the question of what to do with the growing dump. Raw thoughts were piling up, messy and repetitive. The answer came during brainstorming with ChatGPT: extract "atomic thoughts" — self-contained, tagged, one per file. Events too — factual things that happened. The extraction test: *If I forget this, is something important lost?* If not, leave it.

But doing this manually was boring, and boring things get abandoned. So the decision was clear: AI should handle the clerical extraction work. The author's job is to stream thoughts freely — typing, handwriting, audio, video — and the system takes care of the rest.

During a long morning walk, talking into a phone, the project got its name: Project Zero. Transcript-friendly, recognizable by voice systems, and carrying a productive charge. The "zero" challenges the mind's tendency to project negativity — an added feature, not a bug.

A philosophy grew around the system. A day is the unit of life — born at sunrise, die at sunset, rise replenished. Observe energy levels, go with the grain. Long todo lists are demotivating — they feel like debts from a past self. Better to show the past as a story and the future as breadcrumbs. Like a game where you see only the next few steps, not the entire map.

Practical obstacles followed. Transcribing audio thoughts needed tooling. AssemblyAI was chosen after comparing it with GCP Speech-to-Text and OpenAI. GCP was tried as a fallback when AssemblyAI errored, but its output was phonetically accurate yet harder to read. AssemblyAI won. Easy Recorder was bought, autosave to Google Drive set up, Make.com chosen for automation.

By mid-February, a Cursor rule was built to automate the extraction pipeline. All existing raw thoughts were processed in one run. The system was finally eating its own cooking.

A new pattern emerged around generated reference material — ChatGPT-produced plans, guides, and specs that aren't raw thoughts but are too useful to lose in a chat history. The solution: project docs folders. They sit outside the thought stream. They can be deleted without losing anything that came from the author. A middle ground between capturing everything and losing useful context.

Then a new tension surfaced: self-censorship. The system works best when thoughts flow freely, but some thoughts — about people, conflicts, sensitive situations — can't safely be public. The decision crystallized: raw thoughts should not be shared publicly. They will always be private. But everything else — atomic thoughts, spec, story, software, source code, documentation — should be published from day one. It need not be perfect on day one. Many things can be manual at first, but the core needs to be done and visible.

Alongside the privacy question, a new intent emerged: release a first version of the thought tracker that other people can use. Something that resembles a product. But privacy, safety, and data migration need upfront thought — once people start using it, changes get hard. The guiding constraint: any software built must be a direct translation of thoughts and decisions into code — generatable, not hand-maintained. Otherwise code rots.

A deeper insight also emerged about why all of this matters: the world constantly bombards with inputs that shift focus and break momentum. The antidote is to become your own radio jockey — curate what enters your mind, set your own context. Can't outsource that to others who don't know your journey.

An internal tension was named: the planner/builder split. The planner flies high with ideas, while the builder bears the pressure of making things real. Plans, projects, and approaches shift constantly — the builder can't build steadily if the ground keeps moving. Is the relief of planning just the planner in disguise?

The vision for how software should be built got its fullest articulation yet — drawing on 14 years of writing code for money. The core conviction hardened: human beings should not write code anymore. LLMs have been trained on enough code to write, maintain, edit, and understand it better than humans — who have emotions, low attention times, distractions, and make mistakes that snowball codebases into piles of mess. Code is just thoughts in another form — a translation, a transformation. We just need to select which thoughts become software.

The pipeline: raw thoughts → story (the why, causal connections) + spec (the what, full details) + documentation (how to use) → tests → code → deploy. Feedback at any step goes back to the human. Each iteration must regenerate the entire software fresh from the spec — no editing on top of editing. One-to-one mapping from thoughts to spec to software with no drift. Reusable building blocks (polylith architecture) don't get rebuilt — only the arrangement changes.

By late February, a decision landed with clarity: no more research. Build the thoughts app v1 as a dynamic cloud server app. File-based storage, no DB needed. Two life rules crystallized: treat your life as one day long, and practice complete daily shutdowns.

Then came the attempt to actually build — and resistance showed up again, wearing new masks. A livestream was recorded to establish the process, then deleted due to self-judgment. The perfectionism got its sharpest diagnosis yet: it may be avoidance of the discomfort of public exposure. This is the life project — if someone criticizes it, it feels like a verdict on the whole life. "You can keep polishing the first step of the palace till the end of time and never see the shape of what it could become."

A fear also surfaced about going public: what if a corporation copies the idea? The counter was immediate and honest: "No company will be able to do it like I am doing it. This comes from sincere, real pain."

And a deeper warning about the practice itself: self-observation can backfire. The ego trying to find itself creates loops — like Alan Watts' thief going upstairs when the police arrive. Even ambrosia in excess is poison. Don't try to fix thought patterns — just observe. Trying to fix creates resistance. Thought is not the reason you do things — it's a signal, maybe 1% causal.

An insight cut through the confusion: "The thing I'm trying to create already exists. It is like a spot in the forest. I just need to find my way to it by being systematic about this process."

On Feb 28, the waiting ended. Sat down, wrote the command, and Cursor generated the v1 story, spec, task list, and built the app in one session. Python + FastAPI + plain HTML/CSS/JS + .md files. It worked. All existing raw thoughts appeared in the list. New thoughts could be added and read back.

Immediately after the first build, the iteration loop began. Two issues surfaced: the beforeunload warning fired even on intentional save (should only fire on accidental navigation), and the home page needed pagination (showing only 10 thoughts at a time with next/prev). Feedback was also noted: use virtualenv, clean up test servers properly.

The v1 story, spec, and tasks were versioned (renamed to v1.txt). New current versions were created incorporating the bug fix and pagination. A deeper process insight was articulated: each iteration should delete the app and regenerate it fresh from the current spec — no incremental patching. The spec must be self-sufficient: anyone with just the spec should be able to hand it to a coding agent and get working software.

The building blocks concept took shape: a `building_blocks/` directory at repo root, organized by language (python, html, js, css). Each block has its own folder with a readme and code files. No project-specific logic. The planner checks this library before defining tasks — reuse before creation.

Three reusable prompts were created for the development loop: (1) generate spec from thoughts, (2) generate task list from spec, (3) build from tasks. These prompts work across iterations — the same process every time, regardless of what version is being built.

## Timeline
- **Feb 6** — Published first thought on jithusunny.com. Decided to stop waiting for a perfect plan and just begin. The bigbang method insight emerged.
- **Feb 8** — Decided to keep raw thoughts radically minimal: just time and text. Plain text as sole source of truth.
- **Feb 9** — File structure locked in. Updated GitHub repo with structure and basic UI. Analysis-paralysis detected and interrupted.
- **Feb 10** — Make work enjoyable like play. Observation changes what is observed. Defined extraction workflow. Day as unit of life. Projects support identified as next step.
- **Feb 11** — Wrote the jithusunny.com spec: a system for clarity that aims to self-destruct when no longer needed. Resistance intensified.
- **Feb 12** — Long todo lists are demotivating. Reimagined the interface: past as zoomable story, future as breadcrumbs.
- **Feb 13** — First audio thought stream. Project Zero named. AI should extract atomic thoughts. Thoughts should become blog posts.
- **Feb 16** — Researched transcription tools, chose AssemblyAI. Set up GCP as fallback, abandoned it. Bought Easy Recorder, configured Google Drive autosave.
- **Feb 17** — Built Cursor extraction rule. Processed all existing raw thoughts. Created story.md. Refined summaries to be narrative.
- **Feb 18** — Adopted project docs folders for generated reference material.
- **Feb 19** — Self-censorship recognized as a problem. Privacy layers needed. Mobile capture pipeline sketched. Decided to face fear and move to dynamic website. Named the planner/builder tension.
- **Feb 20** — Fullest articulation of the new software process (10 problems, step-by-step alternative). Project Zero is both method and product. Sat down to build — resistance appeared as perfectionism.
- **Feb 24** — Decision: no more research. Build v1 tomorrow. Daily startup/shutdown rules crystallized.
- **Feb 25** — Morning walk: detailed the thought-to-software pipeline (story + spec + docs → tests → code). Privacy decision hardened: raw thoughts always private, everything else published from day one. Bootstrap problem acknowledged. Key insight: "The thing I'm trying to create already exists — find the way by being systematic."
- **Feb 26 (driving)** — First thought stream while driving. Perfectionism diagnosed as fear of public exposure — criticism of life project = verdict on whole life. Did and then deleted a livestream. Warning: self-observation can backfire (ego loops). Don't fix patterns, just observe. Wanted: tap phone → speak → auto-saved with metadata, multi-device, backend.
- **Feb 26 (evening)** — "Human beings should not write code anymore." Code is thoughts in another form. Each iteration regenerates software fresh from spec — no drift. Reusable building blocks, polylith style. Fear of corporations copying → "No company can do it like me, this comes from real pain." Observation is the only way to change anything.
- **Feb 26 (night)** — Concrete v1 spec: list thoughts, add thought as text, .md files, Python+FastAPI+HTML/CSS/JS, no DB. Livestream iteration process designed: describe → transcribe → spec → code → inspect → feedback → repeat. Plan to do this publicly via YouTube.
- **Feb 28 (morning)** — Sat down and started. Decided livestreaming, video, story can begin from day N. Wrote the command to Cursor: synthesize story, create spec, build the software. Story, spec, and task list created. V1 app built in one session — all pages working, existing thoughts visible, new thoughts saveable.
- **Feb 28 (afternoon)** — First iteration loop. Found beforeunload bug and need for pagination. Gave feedback: use virtualenv, clean up servers. Versioned v1 artifacts. Created v2 story, spec, and tasks with fixes. Articulated the delete-and-recreate-fresh rule. Set up building_blocks/ directory. Created three reusable prompts (spec generation, task generation, build) for the repeatable development loop.
- **Feb 28 (evening)** — V2 built: deleted app/, recreated fresh with pagination (10/page) and beforeunload fix. Virtualenv used. First thought streamed through the actual app — confirmed working.
- **Mar 1** — UX feedback after real use: reduce to 7 per page (no scrolling), add Back button on read page that preserves page state (not just Home), add .gitignore. Brainstormed with ChatGPT about regeneration efficiency — decided to add blueprints (stable component names across iterations) instead of trying to reuse code blocks directly (which increases token load). Updated generate-spec prompt to include blueprint generation. V3 spec, story, and blueprint created.
- **Mar 1 (evening)** — Refined the code generation pipeline with ChatGPT. Pipeline is now explicit: Raw thoughts → Spec (what the software is) → Blueprint (what parts exist) → Tasks (how to build those parts this iteration) → Build (generate code). Blueprint step sits between spec and tasks. ChatGPT gave detailed prompts for the full workflow. More suggestions noted for later.

## Last seen breadcrumbs
- Pipeline is explicit: thoughts → spec → blueprint → tasks → build; blueprint defines parts, tasks define how to build them this iteration
- V3 built with component structure; generate-tasks and build prompts used successfully
- The development workflow now includes blueprints for architectural stability across regenerations
- ChatGPT provided detailed prompts for the workflow; more suggestions to come later
- Raw thoughts private, everything else public from day one — this decision is final

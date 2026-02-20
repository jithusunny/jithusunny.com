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

Then a new tension surfaced: self-censorship. The system works best when thoughts flow freely, but some thoughts — about people, conflicts, sensitive situations — can't safely be public. The censoring is already happening, and it's cutting off a gold mine of self-understanding. Some of those situations deserve to be tracked as projects in their own right. The need for privacy layers is clear: marking things private or public, with access levels. But architecturally, it's tricky — public projects may rest on private thought foundations, and building visible outer layers without exposing private building blocks is an unsolved problem.

The privacy question deepened further. The decision crystallized: raw thoughts should not be shared publicly — maybe after 5 years, but not now. Too hard to mask sensitive info and not worth the effort. Share more refined forms of content instead. The system should hold the full truth, but the world sees only what's been processed and cleared.

Alongside the privacy question, a new intent emerged: release a first version of the thought tracker that other people can use. Something that resembles a product. But privacy, safety, and data migration need upfront thought — once people start using it, changes get hard. The guiding constraint: any software built must be a direct translation of thoughts and decisions into code — generatable, not hand-maintained. Otherwise code rots.

A deeper insight also emerged about why all of this matters: the world constantly bombards with inputs that shift focus and break momentum. A YouTube video, a restaurant, a radio jockey, a security guard's opinion — each carries its own philosophy. The mind gets pulled in every direction. The antidote is to become your own radio jockey — curate what enters your mind, set your own context. Can't outsource that to others who don't know your journey.

The concrete capabilities needed began to take shape: notes with sync across devices, daily event tracking (finance, food, conversations), thought documentation with atomic extraction, project management, a portfolio page. All sitting on a common foundation. The GitHub static site needs to give way to a proper dynamic website — and while there's fear about the effort involved, the decision is to face it and start small.

An internal tension was named: the planner/builder split. The planner flies high with ideas, while the builder bears the pressure of making things real. Plans, projects, and approaches shift constantly — the builder can't build steadily if the ground keeps moving. Is the relief of planning just the planner in disguise?

Then the vision for how software should be built got its fullest articulation yet — drawing on 14 years of writing code for money and everything that's wrong with the existing process. The problems: gap between vision and execution widens with every person added, it takes far too long, it wastes human creativity on symbol manipulation, it creates confusion and unnecessary conflict, tech debt compounds and maintainers curse creators, documentation is scary to write and read, software rots daily, migrations are notoriously hard, knowledge transfers are a pain, and the cost of all this wasted energy is enormous.

The new way: thoughts about the problem and solution are captured → translated into specs (software, UI/UX, tests, user guide, creation story/video) → software and tests are generated → tests run → deploy → production checks. Feedback loops at each level escalate questions back to the human. Zero gap between thoughts and software — software is literally a generated translation of thoughts. Zero tech debt guaranteed — no human touches code. Data is sacred, software is disposable — any changes to software can be made fearlessly because data stays safe, with automatic migration. Ideally the whole thing rebuilds daily. Documentation is never human-edited: auto-generated animations, auto-recorded UI flows, zoom in/zoom out on content density. Videos > animations > images > text. Always 100% up to date.

The decision for now: Project Zero is both — the system for streamlining this process AND the system being built with it. Will separate and deploy for others later.

The latest concern is friction. Thoughts happen everywhere — not just at the desk. The system needs to meet that. A concrete automation pipeline took shape: record with Easy Voice Recorder, auto-save to Google Drive, Make.com moves the file to the right dated folder, AssemblyAI transcribes it, the transcript lands in the git repo. Processing and extraction come after — Cursor handles that for now. The repo-based approach will eventually give way to a proper backend, but setting up the automation now is worth the short-term smoothness. Some rework is acceptable.

But tension kept surfacing throughout: *Is this all just thinking? Where's the visible output?* The fear of being stuck in dreams without proof. The counter-thought, borrowed from Kobe: *I don't know what failure is. I do things, I see how it goes. I do things again.*

## Timeline
- **Feb 6** — Published first thought on jithusunny.com. Then a second. Decided to stop waiting for a perfect plan and just begin. Shared the raw thoughts with ChatGPT for brainstorming. The bigbang method insight emerged.
- **Feb 8** — Decided to keep raw thoughts radically minimal: just time and text. Plain text as the sole source of truth.
- **Feb 9** — File structure locked in: `raw/YYYY/MM/DD/HHMM.txt`. Updated the GitHub repo with structure and a basic UI showing last 5 thoughts. Analysis-paralysis detected and interrupted.
- **Feb 10** — A dense day. Make work enjoyable like play. Observation changes what is observed. Defined the extraction workflow with ChatGPT: immutable raw, extract what has charge, label lightly, repeat. Day as unit of life. Projects support identified as the most important next step. Envisioned a system that would progressively gain abilities — from changing code to editing video to managing life.
- **Feb 11** — Wrote the jithusunny.com spec: a system for clarity that aims to self-destruct when no longer needed. Sketched the full pipeline: raw → thoughts → spec → actions → output. Resistance intensified — *"this is not practical," "people will laugh."*
- **Feb 12** — Realized long todo lists are demotivating. Reimagined the interface: past as a zoomable story, future as game-like breadcrumbs.
- **Feb 13** — Recorded the first audio thought stream during a morning walk. Searched for a name for the whole endeavor. Landed on "Project Zero." Decided AI should extract atomic thoughts. Continued the walk and refined: thoughts should become blog posts, extraction rules should be codified for LLMs.
- **Feb 16** — Four days had passed quickly and it stung. Decided to start projects support now and not get sidetracked building a notes system. Researched transcription tools, chose AssemblyAI. It errored. Set up GCP as fallback — the output was less readable. Came back to AssemblyAI, got the audio transcribed. Deleted the GCP setup. Bought Easy Recorder app, configured autosave to Google Drive. Chose Make.com for workflow automation.
- **Feb 17** — Morning walk surfaced growing tension: all thinking, no visible output. Defined the common project view: *what happened, what is happening, what could happen.* Built a Cursor rule with ChatGPT to automate extraction. Processed all existing raw thoughts. Transcribed the morning walk audio. Later, refined the extraction rule to produce story-like summaries instead of bullet-point reports. Created story.md — the first overall narrative. Updated the home page HTML to show the story. Imagined a Google Maps-style zoom on the story where verbosity changes with zoom level.
- **Feb 18** — Recognized the need for a middle ground for generated reference material (ChatGPT plans, guides). Adopted project docs folders — not raw thoughts, not lost in chat, deletable without losing anything original.
- **Feb 19 (early)** — Self-censorship recognized as a real problem — cutting off a gold mine of self-understanding. Privacy layers (private/public with access levels) identified as a need but architecturally complex. Intent to release a thought tracker for others crystallized. Rule established: software must be generatable from specs, not hand-maintained. Also felt a pull toward recording songs.
- **Feb 19 (mid)** — Felt the need to capture thoughts from mobile more easily. Sketched a concrete automation pipeline: Easy Voice Recorder → Google Drive → Make.com → AssemblyAI → git repo. Decided the repo-based approach is temporary but worth the short-term smoothness — rework is acceptable.
- **Feb 19 (night)** — Deeper reflection. The world bombards with inputs that break momentum — need to become your own radio jockey. Decided raw thoughts should stay private (maybe public in 5 years). The don't-touch-code vision matured: specs regenerate all levels, polylith-style modularity. Concrete capabilities list emerged (notes, events, thoughts, projects, portfolio). Decision to face fear and move from static GitHub site to dynamic website. Named the planner/builder tension — is the relief of planning just the planner in disguise?
- **Feb 20** — Wrote the fullest articulation of the new software process: 10 problems with existing software engineering, and a step-by-step new approach (thoughts → specs → generate → test → deploy). Core principles crystallized: zero gap, zero tech debt, data sacred/software disposable, daily rebuilds, auto-generated documentation with zoom. Decided Project Zero is both the method and the first product built with it.

## Last seen breadcrumbs
- Project Zero is now both method and product — building the system with the system is the next move
- The full software process is articulated — it needs its first real test project
- Moving from GitHub static site to a dynamic website is the next technical leap
- The voice-to-repo automation pipeline is fully specced and ready to be wired up with Make.com
- A portfolio of real-problem-solving software is how the value gets shown to others

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

Alongside the privacy question, a new intent emerged: release a first version of the thought tracker that other people can use. Something that resembles a product. But privacy, safety, and data migration need upfront thought — once people start using it, changes get hard. The guiding constraint: any software built must be a direct translation of thoughts and decisions into code — generatable, not hand-maintained. Otherwise code rots.

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
- **Feb 19** — Self-censorship recognized as a real problem — cutting off a gold mine of self-understanding. Privacy layers (private/public with access levels) identified as a need but architecturally complex. Intent to release a thought tracker for others crystallized. Rule established: software must be generatable from specs, not hand-maintained. Also felt a pull toward recording songs.

## Last seen breadcrumbs
- Privacy layers are the most pressing design problem — without them, the raw stream stays censored
- A first public version of the thought tracker could be the next visible artifact — radically minimal, careful about data migration
- The zoomable story idea (Google Maps-style verbosity control) is described but not built
- The record → transcribe → notify pipeline could be wired together with Make.com
- Songs and music keep surfacing as a pull — a different kind of output entirely

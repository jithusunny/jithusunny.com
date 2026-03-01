# Jithu — Story so far

## The beginning

I was reading Steven Pressfield's *Do the Work* somewhere in early February and something clicked — not as new information, but as a mirror held up at the right angle. I had too many ideas. I'd been consuming content for years, YouTube especially, and the potential energy inside me had grown enormous. But nothing proportionate was coming out. The ideas stayed inside, circling.

I had resigned from a well-paying job. Family was asking the obvious question: what are you doing? I didn't have a satisfying answer. Not because nothing was happening, but because what was happening was invisible. Thoughts about how to live, how to see clearly, how to stop getting pushed around by the tides of time. None of that is easy to point at.

The realization was simple: waiting for a perfect plan before starting is itself the resistance. The greedy mind wants everything figured out first and ends up doing nothing. So I typed a thought into a plain text file and put it on my website. That was the beginning.

## How life is being lived now

The days have a loose rhythm. I wake up, sometimes early. There are morning walks where I talk into my phone, recording whatever comes up. Now there are driving sessions too — thought streaming while navigating traffic. I come home, help with Ian — bathe him, play with him, take him downstairs for some sun. Elsa gets ready for work. I eat, maybe nap if the night was short. Then I sit down and try to do something.

A philosophy of daily living is sharpening. Consider your life is just one day long. Start up well — fresh air, body movement, meditation. Pay real attention to others, but don't let your consciousness get colored in ways you don't like. Attitude is contagious — let your vibe infect others. And shut down properly. Clean up the room before bed. Put everything in its place. No lingering files, no unfinished messes. When you are ready to die fully, you are ready to live fully.

I capture whatever comes up as raw text — messy, unstructured, stream-of-consciousness. The mess is the point. From those dumps, smaller pieces get extracted: decisions, tensions, insights, events. AI handles the filing. I keep the thinking.

The world constantly bombards with inputs that break momentum. The antidote is to become my own radio jockey — curate what enters my mind, set my own context. No one else knows my journey well enough to do it for me.

Plans have become suspect. Long todo lists feel like debts imposed by a past self who had different energy. Stories and breadcrumbs age better than task lists.

Resistance is a daily companion. It shows up as the urge to research one more option, define one more spec, think through one more scenario. The counter-move, when it works, is just to start. But there's a subtler version: a planner inside me that flies high with ideas while a builder bears the pressure. The planner keeps shifting the ground. Sometimes the relief of a good planning session is just the planner pretending to be the builder.

The perfectionism got its sharpest diagnosis recently: it may be avoidance of the discomfort of public exposure. This is the life project. If someone criticizes it, it feels like a verdict on the whole life. "You can keep polishing the first step of the palace till the end of time and never see the shape of what it could become."

## How software should be built

I've been writing code for money for 14 years, and a conviction has hardened: human beings should not write code anymore. LLMs are better suited for it. Humans have emotions, low-attention times, distractions — mistakes that snowball codebases into piles of mess. Code is just thoughts in another form. A translation. We just need to select which thoughts become software.

The pipeline: raw thoughts → story (the why) + spec (the what) + documentation (how to use) → tests → code → deploy. Feedback at any step goes back to the human. Each iteration regenerates the entire software fresh from the spec — no editing on top of editing. One-to-one mapping from thoughts to spec to software with no drift. Reusable building blocks don't get rebuilt — only the arrangement changes.

For now, Project Zero is both — the system for streamlining this process and the first system built with it.

## The build begins

On Feb 28 I sat down and made a choice. Starting will provide the energy — waiting for the right time is just the mind finding another way to postpone. Livestreaming, video, perfect documentation — all of it can come later, from day N, not necessarily day 1.

I saved a stream of thought and gave Cursor the command: analyse all my thoughts, figure out what v1 needs to be, synthesize the story, create the spec, then build it. The story and spec were created. A rule was articulated: story, spec, and the subset of thoughts they cover must be equivalent. One-to-one mapping, no drift. Then the software was built — Python, FastAPI, plain HTML/CSS/JS, .md files on disk, no database. All existing thoughts appeared in the list. New thoughts could be added and read back. It worked.

## The first iteration

Within an hour of the first build, the loop started. Two issues: the browser's "are you sure you want to leave?" warning fired even when clicking Save (it should only fire on accidental navigation), and the home page showed all thoughts at once (needed pagination — 10 per page with next/prev).

Feedback was given as a raw thought. The v1 artifacts were versioned. New story, spec, and tasks were written from scratch — complete, self-sufficient, not incremental patches. The rule crystallized: each iteration deletes the app and recreates it fresh from the current spec. The spec alone should be enough for anyone to rebuild the software.

A building blocks concept emerged — reusable code organized by language, no project-specific logic, with a planner that checks the library before inventing new things. And three reusable prompts were created for the repeating loop: generate spec from thoughts, generate tasks from spec, build from tasks. The same process, every time.

## Projects as expressions (not goals)

Projects are not goals. They're contexts — places where life energy is flowing, or wants to flow.

At the center sits Project Zero. It's the practice of capturing thoughts, extracting what matters, and organizing it by the areas of life it touches. It's also the method for building software — the thesis and the proof in one.

Elsa's boutique business has moved faster than anything else — a live Shopify store with multiple products, fully functional payments (cards, UPI, netbanking, wallets), and a repeatable product listing workflow. The remaining gaps are concrete: packaging, shipping rates, pricing, product videos.

My YouTube channel finally moved from pull to action. The first video was uploaded. A versioned approach removes pressure. And now livestreams are designed as the medium for building the thought tracker publicly.

A tool built for someone's matrimony profile turned into an insight about structured documents in general. The house had a major decluttering wave and a cleaning schedule was written. An idea for a House app surfaced.

None of these are separate. Progress on one often unblocks another. They're different angles on the same life.

## What keeps repeating

Resistance keeps wearing the mask of planning. The moments of actual progress have always come from interrupting that loop and just starting. Publishing the first thought. Signing up for Shopify. Uploading the first YouTube video. Sitting down on Feb 28 and giving the command to build. The relief afterward is always larger than expected.

If a process is boring, I will abandon it. The work has to stay interesting or it won't last.

Small visible results unlock energy for everything else. The absence of visible results drains it. The v1 build proved this — seeing the app list my actual thoughts was energizing enough to immediately start iterating. V2 was built and used the same day. The first thought was streamed through the actual app. Then feedback flowed naturally — too much scrolling, the back button goes to the wrong place — and v3 spec was born within hours.

Most of what runs through my mind on any given day already ran through it yesterday. Writing it down makes the loops visible. And seeing them seems to loosen their grip. But there's a warning here too: self-observation can backfire. The ego trying to find itself creates loops — like Alan Watts' thief going upstairs when the police arrive. Even ambrosia in excess is poison. Don't try to fix thought patterns — just observe. Trying to fix creates resistance.

Family is not separate from the work. Elsa's mood, Ian's needs, the state of the house — these are not interruptions. It's all one fabric.

## Where things feel unresolved

There is a tension between inner work and visible output. *Show me proof.* How much inner work is enough before something needs to ship?

There is the question of money. A well-paying job was left behind. Nothing generates income yet. The process is now running — thoughts → spec → software — but nothing is deployed publicly yet.

There is a fear about going public. What if a corporation copies the idea? The counter: "No company will be able to do it like I am doing it. This comes from sincere, real pain."

The original building blocks idea — reusable code copied into each build — ran into a practical problem: sending full code to the AI each time increases token load. A conversation with ChatGPT surfaced a better approach: blueprints. Stable component names and purposes that persist across iterations, giving the code generator architectural consistency without needing to ingest old code. The first blueprint was created for v3: six components (storage_fs, api_thoughts, ui_shell, ui_thought_list, ui_thought_form, ui_thought_read). Whether this actually makes regeneration smarter remains to be seen.

And there is the recurring doubt about whether any of this will actually lead somewhere. The answer so far: failure only exists when you declare it and stop.

An insight cuts through the confusion: "The thing I'm trying to create already exists. It is like a spot in the forest. I just need to find my way to it by being systematic."

## Last seen breadcrumbs

- Pipeline is explicit: thoughts → spec → blueprint → tasks → build; ChatGPT gave detailed prompts for each step
- V3 built with component-based structure; the cycle (spec → blueprint → tasks → build) ran successfully
- Blueprints define what parts exist; tasks define how to build them this iteration
- More suggestions from ChatGPT noted for later
- Mridhu's store is fully functional — next push is packaging, pricing, and product videos
- Raw thoughts private, everything else public from day one — this is final

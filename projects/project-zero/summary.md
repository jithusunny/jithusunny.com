# Project Zero Summary

## Context
Project Zero is a system and way of life for living with clarity and direction. It starts as a personal thought-tracking system on jithusunny.com — capturing raw thoughts in plain text files — and aims to grow into an interconnected system that handles thoughts, events, projects, and eventually automates actions. It aims to self-destruct once no longer needed.

## Highlights
- Named the project "Project Zero" — transcript-friendly, carries productive charge that challenges the mind's negative associations
- Raw thoughts captured as immutable plain text files (raw/YYYY/MM/DD/HHMM.txt), decoupled from the system, exportable without friction
- AI/LLM extracts atomic thoughts from raw dumps — clerical work automated, not done manually
- Extraction workflow defined: one thought per file, tagged by type (rule, decision, intent, insight, tension, pull, todo, spec, risk)
- "Bigbang method" of creating: set initial config and rules, let it run, don't interfere mid-run — refine between iterations
- Day treated as the unit of life — clean shutdown at night, fresh start each morning, observe energy levels
- Set up audio thought recording pipeline: Easy Recorder → Google Drive autosave → AssemblyAI transcription
- AssemblyAI chosen for transcription over GCP Speech-to-Text — better readable output, low cost, handles long files
- Make.com chosen for workflow automation (escalate to n8n then custom as needed)
- Long todo lists recognized as demotivating — prefer story-like summaries with game-like breadcrumbs for next steps
- Projects support identified as the most important next step — enables tracking across all active projects
- Published first thoughts on jithusunny.com, updated GitHub repo with file structure and basic UI
- Recorded first audio thought stream during a morning walk; got it transcribed and added to the repo

## Next (could)
Build projects support in jithusunny.com, automate the record→transcribe→notify pipeline using Make.com, or start turning extracted thoughts into short blog posts.

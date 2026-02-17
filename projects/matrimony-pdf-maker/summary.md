# Matrimony PDF Maker

## Story so far
Someone asked for help creating a matrimony profile. It's a recurring ask — the author has made these before, for himself and others. So instead of doing it manually again, the thought was: why not build a tool that makes this painless for anyone?

The vision took shape with ChatGPT: a mobile-first single-page web app. You see a live preview of the PDF at all times. You fill in structured fields, or speak into the mic and confirm what the AI extracts. Upload a photo. Every confirmed change regenerates the PDF instantly. No backend, no accounts, nothing stored — everything happens in the browser.

The architecture was deliberately simple: one JSON state object, snapshot-based undo/redo, and a PDF export that matches the preview pixel-for-pixel. Development was planned in three phases: Phase 1 nails the editing experience without any AI. Phase 2 adds voice. Phase 3 allows importing existing profiles.

A GitHub repo was created and Phase 1 was built. When tested, it was surprisingly good — even before all the fields were added. That surprise sparked a bigger thought: this isn't just about matrimony profiles. The same approach could work for any structured document — bills, invoices, warranties. Maybe even a marketplace where some people build document templates and others just use them.

## Timeline
- **Feb 11** — Someone needed a matrimony profile. Got the initial vision and spec with ChatGPT — mobile-first, no backend, live preview, client-side PDF. Later that day, polished it into a phased development plan and created the GitHub repo at https://github.com/jithusunny/matrimony-pdf.
- **Feb 12** — Tested Phase 1. Quality was surprisingly good even without all fields. Realized the concept could generalize to any structured document type. The marketplace idea surfaced — 20% builders, 80% consumers.

## Last seen breadcrumbs
- Phase 1 has remaining fields that could be added to see the full editing experience
- The generalization insight is interesting but untested — trying a second document type (an invoice? a warranty card?) would show if the architecture actually holds
- Phase 2 (voice AI) is defined but hasn't been started

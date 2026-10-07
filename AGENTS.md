# Fiction Writing Repo

This repo is for generating plotbeats and prose for original-character (OC) stories. Each top-level folder is one setting/story.

## Layout

- `<setting>/info/` — worldbuilding & character bible. Canon reference, effectively read-only. Source of truth for personality, voice, relationships, setting, and the summary of each period. Holds **facts**, not scene-by-scene beats.
- `<setting>/arc/` — **canon** events. Plotbeats, outlines, and prose for things that actually happen in the timeline; each `outline.md` is canon for the event it covers, and later beats must stay consistent with it. `arc/README.md` lists the beats in chronological order.
- `<setting>/side/` — **non-canon** pieces. One-shots, what-ifs, whump/fluff that doesn't have to fit the timeline. A side piece should respect `info/` unless it's deliberately an AU, but nothing in `info/` or `arc/` may depend on it, and it never updates `info/`. `side/README.md` lists pieces with what each assumes. Promoting a piece to canon = move its folder into `arc/` and add it to `arc/README.md`.

Generated output goes in `arc/` or `side/`, never `info/`. See "arc/ and side/ structure" below.

## Read selectively — don't load the whole bible every time

`info/` files can be long and each covers a different slice of the story (different time period, different depth of interiority). Reading all of them for every request burns context for no benefit. Instead:

1. Check the index below for the setting you're working in.
2. Open only the file(s) relevant to the scene/beat/question at hand.
3. If unsure which file covers a character or topic, grep for the name/keyword across `info/` first rather than opening every file to check.

Only edit `info/` when the user is explicitly updating canon/worldbuilding — otherwise treat it as read-only reference and write new material to `arc/` or `side/`.

## cyberpunk/info index

Setting: two mercenaries (Evelyn, Victoria), ex-military, near-future cyberpunk.

| File                           | Covers                                                                                                                     | Read when...                                                                                          |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `0_Characters.md`              | Cast roster — appearance, personality, hobbies, implants, specialty, mental state/coping mechanisms; main pair + side cast | Almost any scene with these characters — this is the baseline voice/personality/interiority reference |
| `0_Voice.md`                   | Shared tone; POV narration voice for each — what they notice, how they avoid heavy thoughts, stress shifts                 | Writing any prose, or generating ideas/outlines where tone matters                                    |
| `0_Trivia.md`                  | Small concrete details — social life, housework, apartment & car, purchases, drinking, birthdays                           | Slice-of-life, domestic, or social scenes, or when a scene needs incidental flavor detail             |
| `0_Technology.md`              | Tech rules — "high tech, low life" test, cyberware tiers, neural depth & maintenance, and so on                            | Any scene involving implants, repairs, hacking, surveillance, or tech that needs to stay consistent   |
| `1_Past_Service_Period.md`     | Service-era setting — Concord/CEF hierarchy & wars, academy & deployment life; summary of the meeting and friendship arc   | Writing flashback/backstory scenes or anything needing historical/setting context                     |
| `2_Present_Typical_Routine.md` | Present-day status quo — daily/weekly routine, apartment dynamic                                                           | Writing present-timeline slice-of-life scenes                                                         |
| `2_Present_Jobs.md`            | Present-day merc work — two-person role split, work-day phases, job types taken/refused, solo work, why they survive       | Writing any job/mission scene, or checking whether a job premise is realistic for them                |
| `3_Future_Ordinary_Life.md`    | Post-present: summary of the injury-and-retirement arc and where they end up; constraints the present must not contradict  | A canon beat set before it that risks a permanent injury or has them opening up to each other         |

The numeric prefixes are chronological (1 = past, 2 = present, 3 = future) — that's for lookup only, not a read order. Jump straight to the file that matches the current task rather than reading them in sequence; narrative/reader-facing order is a property of the actual outlines and prose in `arc/`, not of this reference bible.

- `1_` opens with an `## Arc Summary` — the period's event throughline (how they met through leaving service) — followed by the setting detail.
- `2_` files open with a `## Summary` digest (the routine, or the job structure) before their full detail.
- `3_` is short: an `## Arc Summary` of the future arc, then `## Constraints on the Present` — the fixed points any earlier beat (canon `arc/` pieces, not `side/`) must stay compatible with.

For checking consistency with a period, the opening section is usually enough; read on only when you need the detail below it. For exact dialogue/sequencing of an event, go to the event's outline (find it in `arc/README.md`).

## arc/ and side/ structure

Both directories use the same per-piece layout, so promoting a side piece is just a folder move. Each beat gets its own subfolder under `arc/` (or piece under `side/`): one single outline file, one picked prose file, and a folder of timestamped drafts.

```
arc/
  <beat-name>/
    outline.md             <- single outline/plotbeat, edited in place
    prose.md               <- the picked/canonical prose, edited in place
    drafts/
      20260926-1430.md
      20260926-1512.md
```

### Shared rules

- When adding or renaming a beat folder, update `arc/README.md` (chronological position and tags) or `side/README.md` (premise source, assumptions, and tags).
- If it's unclear whether a new piece is canon, ask; default to `side/` for standalone whump or slice-of-life requests.
- Keep files decoupled: `info/` files and outlines don't name other files or beat folders. Refer to events by what happens ("her later meeting with Victoria"), not by where they're written. `arc/README.md` and `side/README.md` are the only places that map events to folders.
- `outline.md` is the blueprint for the beat — the plot points, character focus, and intent for the scene. There's only ever one; revise it in place rather than versioning it (git history covers "what changed"). When a beat has one, read it before generating or revising prose for that beat.
- Prose is what gets iterated on. Generating a new pass means writing a new `drafts/YYYYMMDD-HHMM.md` (local time, no colons; an optional short tag suffix like `20260926-1430-slower-pacing.md` is fine). Never overwrite an existing draft.
- `prose.md` is the version the user picked. Only the user promotes a draft to `prose.md` — never write or overwrite `prose.md` unless explicitly asked.
- **Do not** read earlier drafts prior to generating a new one so every iteration stays fresh and diverse. Read `prose.md` only when the user asks to revise or build on the picked version.

### arc/ specifics

- Every beat has an `outline.md`. A side piece promoted to `arc/` gets one first, even a short one written back from the prose.

### side/ specifics

- `side/ideas.md` is the backlog: one bold-titled bullet per idea, and these bullets are the premises for side pieces.
- `outline.md` is optional. Without one, the piece's idea bullet is its premise: find it via `side/README.md` and work from that bullet plus the user's request.
- Keep the bullet in `ideas.md` once a piece exists. If the user changes the premise, suggest updating the bullet so later drafts start from the same place.

## Adding new settings or info files

When a new setting folder or `info/` file is added, add a row/section to this file summarizing it in one line — but keep it to a summary. Don't paste file content into AGENTS.md; that defeats the point of reading selectively.

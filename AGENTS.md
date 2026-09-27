# Fiction Writing Repo

This repo is for generating plotbeats and prose for original-character (OC) stories. Each top-level folder is one setting/story.

## Layout

- `<setting>/info/` — worldbuilding & character bible. Canon reference, effectively read-only. Source of truth for personality, voice, relationships, setting, and the summary of each period. Holds **facts**, not scene-by-scene beats.
- `<setting>/arc/` — plotbeats, outlines, and prose drafts. Generated output goes here, not in `info/`. Holds **events**: each `outline.md` is canon for the event it covers. `arc/README.md` lists the beats in chronological order. See "arc/ structure" below.

## Read selectively — don't load the whole bible every time

`info/` files can be long and each covers a different slice of the story (different time period, different depth of interiority). Reading all of them for every request burns context for no benefit. Instead:

1. Check the index below for the setting you're working in.
2. Open only the file(s) relevant to the scene/beat/question at hand.
3. If unsure which file covers a character or topic, grep for the name/keyword across `info/` first rather than opening every file to check.

Only edit `info/` when the user is explicitly updating canon/worldbuilding — otherwise treat it as read-only reference and write new material to `arc/`.

## cyberpunk/info index

Setting: two mercenaries (Evelyn, Victoria), ex-military, near-future cyberpunk.

| File                           | Covers                                                                                                                                                  | Read when...                                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `0_Characters.md`              | Cast roster — appearance, personality, hobbies, implants, specialty, mental state/coping mechanisms; main pair + side cast                              | Almost any scene with these characters — this is the baseline voice/personality/interiority reference |
| `0_Technology.md`              | Tech rules — "high tech, low life" test, cyberware tiers, neural depth & maintenance, data/biometrics, weapons, hacking, restricted AI, power structure | Any scene involving implants, repairs, hacking, surveillance, or tech that needs to stay consistent   |
| `1_Past_Service_Period.md`     | Service-era setting — Concord/CEF hierarchy & wars, academy & deployment life; summary of the meeting and friendship arc                                | Writing flashback/backstory scenes or anything needing historical/setting context                     |
| `2_Present_Typical_Routine.md` | Present-day status quo — daily/weekly routine, job structure, apartment dynamic                                                                         | Writing present-timeline slice-of-life or job/work scenes                                             |

The numeric prefixes are chronological (1 = past, 2 = present) — that's for lookup only, not a read order. Jump straight to the file that matches the current task rather than reading them in sequence; narrative/reader-facing order is a property of the actual outlines and prose in `arc/`, not of this reference bible.

`1_` opens with an `## Arc Summary` — the period's event throughline (how they met through leaving service) — followed by the setting detail. `2_` opens with a `## Summary` digest of the present-day status quo before its full detail. For checking consistency with a period, the opening section is usually enough; read on only when you need the setting or routine detail below it. For exact dialogue/sequencing of an event, go to that event's outline (find it in `arc/README.md`).

## arc/ structure

Each beat gets its own subfolder under `arc/`: one single outline file, one picked prose file, and a gitignored folder of timestamped drafts.

```
arc/
  <beat-name>/
    outline.md             <- single outline/plotbeat, edited in place (tracked)
    prose.md               <- the picked/canonical prose (tracked)
    drafts/                <- gitignored, local only
      20260926-1430.md
      20260926-1512.md
```

- When adding or renaming a beat folder, update `arc/README.md` (chronological position).
- Keep files decoupled: `info/` files and outlines don't name other files or beat folders. Refer to events by what happens ("her later meeting with Victoria"), not by where they're written. `arc/README.md` is the only place that maps events to folders.
- `outline.md` is the blueprint for the beat — the plot points, character focus, and intent for the scene. There's only ever one; revise it in place rather than versioning it (git history covers "what changed"). Read it before generating or revising prose for that beat.
- Prose is what gets iterated on. Generating a new pass means writing a new `drafts/YYYYMMDD-HHMM.md` (local time, no colons; an optional short tag suffix like `20260926-1430-slower-pacing.md` is fine). Never overwrite an existing draft.
- `prose.md` is the version the user picked. Only the user promotes a draft to `prose.md` — never write or overwrite `prose.md` unless explicitly asked.
- **Do not** read earlier drafts prior to generating a new one so every iteration stays fresh and diverse. Read `prose.md` only when the user asks to revise or build on the picked version.

## Adding new settings or info files

When a new setting folder or `info/` file is added, add a row/section to this file summarizing it in one line — but keep it to a summary. Don't paste file content into AGENTS.md; that defeats the point of reading selectively.

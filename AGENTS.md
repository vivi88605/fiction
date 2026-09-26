# Fiction Writing Repo

This repo is for generating plotbeats and prose for original-character (OC) stories. Each top-level folder is one setting/story.

## Layout

- `<setting>/info/` — worldbuilding & character bible. Canon reference, effectively read-only. Source of truth for personality, voice, relationships, and history.
- `<setting>/arc/` — plotbeats, outlines, and prose drafts. Generated output goes here, not in `info/`. See "arc/ structure" below.

## Read selectively — don't load the whole bible every time

`info/` files can be long and each covers a different slice of the story (different time period, different depth of interiority). Reading all of them for every request burns context for no benefit. Instead:

1. Check the index below for the setting you're working in.
2. Open only the file(s) relevant to the scene/beat/question at hand.
3. If unsure which file covers a character or topic, grep for the name/keyword across `info/` first rather than opening every file to check.

Only edit `info/` when the user is explicitly updating canon/worldbuilding — otherwise treat it as read-only reference and write new material to `arc/`.

## cyberpunk/info index

Setting: two mercenaries (Evelyn, Victoria), ex-military, near-future cyberpunk.

| File                           | Covers                                                                                                                     | Read when...                                                                                          |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `0_Characters.md`              | Cast roster — appearance, personality, hobbies, implants, specialty, mental state/coping mechanisms; main pair + side cast | Almost any scene with these characters — this is the baseline voice/personality/interiority reference |
| `1_Past_Service_Period.md`     | Backstory — military service, how Evelyn & Victoria met, the arc from hostility to found-family                            | Writing flashback/backstory scenes or anything needing historical context                             |
| `2_Present_Typical_Routine.md` | Present-day status quo — daily/weekly routine, job structure, apartment dynamic                                            | Writing present-timeline slice-of-life or job/work scenes                                             |
| `3_Future_Ordinary_Life.md`    | Endgame arc — the injury that ends their mercenary careers, transition to ordinary civilian life                           | Writing later-arc or ending material                                                                  |

The numeric prefixes are chronological (1 = past, 2 = present, 3 = future) — that's for lookup only, not a read order. Jump straight to the file that matches the current task rather than reading 1-2-3 in sequence; narrative/reader-facing order is a property of the actual outlines and prose in `arc/`, not of this reference bible.

`1_`, `2_`, and `3_` each open with a `## Summary` section (a handful of bullets) before their full detail. If you just need to reference or check consistency with what happens in that period, the summary is usually enough — read past it into the full file only when you're actually writing a scene set there, need exact dialogue/sequencing, or the summary doesn't cover what you need.

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

- `outline.md` is the blueprint for the beat — the plot points, character focus, and intent for the scene. There's only ever one; revise it in place rather than versioning it (git history covers "what changed"). Read it before generating or revising prose for that beat.
- Prose is what gets iterated on. Generating a new pass means writing a new `drafts/YYYYMMDD-HHMM.md` (local time, no colons; an optional short tag suffix like `20260926-1430-slower-pacing.md` is fine). Never overwrite an existing draft.
- `prose.md` is the version the user picked. Only the user promotes a draft to `prose.md` — never write or overwrite `prose.md` unless explicitly asked.
- **Do not** read earlier drafts prior to generating a new one so every iteration stays fresh and diverse. Read `prose.md` only when the user asks to revise or build on the picked version.

## Adding new settings or info files

When a new setting folder or `info/` file is added, add a row/section to this file summarizing it in one line — but keep it to a summary. Don't paste file content into AGENTS.md; that defeats the point of reading selectively.

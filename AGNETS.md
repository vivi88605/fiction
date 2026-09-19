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

| File                             | Covers                                                                                                        | Read when...                                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `0_Characters.md`                | Cast roster — appearance, personality, hobbies, implants, specialty; main pair + side cast (Jax, Dell, Carol) | Almost any scene with these characters — this is the baseline voice/personality reference               |
| `0.5_Characters_Mental_State.md` | Interiority — trauma, coping mechanisms, unspoken feelings each character hasn't voiced                       | Writing introspective/emotional beats, or anything that hinges on subtext beneath what a character says |
| `1_Present_Typical_Routine.md`   | Present-day status quo — daily/weekly routine, job structure, apartment dynamic                               | Writing present-timeline slice-of-life or job/work scenes                                               |
| `2_Past_Service_Period.md`       | Backstory — military service, how Evelyn & Victoria met, the arc from hostility to found-family               | Writing flashback/backstory scenes or anything needing historical context                               |
| `3_Future_Ordinary_Life.md`      | Endgame arc — the injury that ends their mercenary careers, transition to ordinary civilian life              | Writing later-arc or ending material                                                                    |

The numeric prefixes are chronological markers (2 = past, 1 = present, 3 = future), not a read order — don't read them front-to-back by default, jump to the one the current task needs.

## arc/ structure

Each beat gets its own subfolder under `arc/`: one single outline file, plus multiple versions of the prose written from it.

```
arc/
  <beat-name>/
    outline.md   <- single outline/plotbeat, edited in place (git tracks its history)
    v1.md
    v2.md
    v3.md        <- current prose (highest number)
```

- `outline.md` is the blueprint for the beat — the plot points, character focus, and intent for the scene. There's only ever one; revise it in place rather than versioning it (git history covers "what changed"). Read it before generating or revising prose for that beat.
- Prose is what gets iterated on. Generating a new pass means writing a new `vN.md`, never overwriting an older one — old versions stay as history/rollback points.
- The current prose version is always whichever `vN.md` has the highest number. No separate `latest`/`current` file to keep in sync.
- By default, read `outline.md` plus only the latest `vN.md` when working on a beat. Earlier prose versions are history, not required context — open them only if the user asks to compare, revert, or see how a draft evolved.

## Adding new settings or info files

When a new setting folder or `info/` file is added, add a row/section to this file summarizing it in one line — but keep it to a summary. Don't paste file content into AGENTS.md; that defeats the point of reading selectively.

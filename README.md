# fiction

Original-character stories, plus the worldbuilding notes and plot outlines behind them. Each top-level folder is one setting.

## Where to start reading

Each story beat has its own folder under `<setting>/arc/`:

```
arc/<beat-name>/
  outline.md   <- plot beats and intent for the scene
  prose.md     <- the finished prose
```

`<setting>/arc/README.md` lists the beats in chronological order. If you only want the stories, read the `prose.md` files. `outline.md` is the plan each one was written from.

`arc/` is canon: those events happen in the timeline, in that order. `<setting>/side/` holds non-canon pieces with the same layout: one-shots and what-ifs that don't have to fit the timeline. Its README notes what each piece assumes.

`<setting>/info/` is the reference material the stories are written against: the cast (appearance, personality, implants), their backstory and their present-day routine. It contains spoilers for the arcs.

## How it's written

Prose is drafted with an AI coding assistant working from the outlines and the `info/` notes. [AGENTS.md](AGENTS.md) holds the instructions it follows. Each beat goes through several drafts, and the chosen one is committed as `prose.md`. All drafts are kept in the beat's `drafts/` folder, so you can also read the alternative takes.

## Read-aloud tool

[tools/read-aloud/](tools/read-aloud/) contains a small script, run from a VS Code task in [.vscode/tasks.json](.vscode/tasks.json), that turns a prose file into an mp3 with Microsoft's neural voices, so you can listen to a draft. Setup and usage are in [tools/read-aloud/README.md](tools/read-aloud/README.md).

## License

- **Read-aloud tool ([tools/read-aloud/](tools/read-aloud/)):** [MIT](tools/read-aloud/LICENSE).
- **Stories, characters and settings:** All rights reserved, please don't repost without permission.

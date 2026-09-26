# Read-aloud setup

Renders a prose file to speech with [edge-tts](https://github.com/rany2/edge-tts) (Microsoft's
neural voices — free, no API key) and opens the mp3 in VS Code's built-in audio preview, so you
get play/pause and a seek bar without leaving the editor.

Two files do the work: `read_aloud.py` (strip markdown → synthesize → open) and `.vscode/tasks.json`
(the menu entries and the voice/speed pickers).

---

## Setup on a new machine

1. **Install Python** from [python.org](https://www.python.org/downloads/) — the Microsoft Store
   stub that ships with Windows is not enough; it resolves but won't run.
2. **Install edge-tts:**
   ```
   python -m pip install edge-tts
   ```
3. Done. Nothing else is needed — no VS Code extension, no audio player, no account.

pip will likely warn that `edge-tts.exe` landed in a `Scripts` folder that isn't on PATH.
The VS Code task doesn't care — it calls `python -m edge_tts`. But **the streaming mode below
does need it on PATH**, so it's worth fixing. Find the folder with:

```bash
python -c "import sysconfig; print(sysconfig.get_path('scripts'))"
```

then add that path in Windows' _Edit environment variables for your account_ dialog.

**edge-tts needs an internet connection** — synthesis happens on Microsoft's servers. Offline,
use the robotic fallback task below.

---

## Running it

`Ctrl+Shift+P` → **Tasks: Run Task** → **Read aloud (neural)**, with the file you want open in
the editor. It asks for a voice, then a speed, then renders.

To bind it to a key, add to `keybindings.json`:

```json
{
  "key": "ctrl+alt+r",
  "command": "workbench.action.tasks.runTask",
  "args": "Read aloud (neural)"
}
```

Or call it directly from the terminal, which is handy for batching:

```bash
python tools/read-aloud/read_aloud.py cyberpunk/arc/victoria-false-intel/prose.md
python tools/read-aloud/read_aloud.py <file>
python tools/read-aloud/read_aloud.py <file> en-GB-SoniaNeural "-10%"    # voice and speed are optional
```

Output lands in `.tts/<beat-folder>-<file-stem>.mp3` — e.g. `victoria-false-intel-prose.mp3`,
`victoria-false-intel-20260926-1205-v1.mp3`. It's qualified with the beat folder (skipping `drafts/`)
because every beat has its own `prose.md`. Re-rendering the same file overwrites its mp3.
`.tts/` is gitignored; delete it freely.

---

## Changing the voice

**For one run:** just pick a different entry in the dropdown when the task prompts you.

**To change the default, or edit the menu:** in `.vscode/tasks.json`, find the `ttsVoice` entry under
`inputs`. `default` is what's pre-selected; `options` is the dropdown list. Add or remove voices
there. The `ttsRate` entry right below works the same way for speed.

**When running the script directly:** `DEFAULT_VOICE` and `DEFAULT_RATE` at the top of
`read_aloud.py` apply when you don't pass those arguments.

**To stop being prompted at all:** delete the `inputs` block from `.vscode/tasks.json` and hardcode the
voice into the task's `args`. A `default` on a pickString only pre-selects — it never skips the
prompt.

### Picking one

Currently in the dropdown: `en-US-AvaNeural`, `en-US-EmmaNeural`, `en-US-AndrewNeural`,
`en-US-BrianNeural`, `en-GB-SoniaNeural`, `en-GB-RyanNeural`, `en-AU-NatashaNeural`.

Audition them on a short file rather than trusting a description — they differ mostly in warmth
and how they handle dialogue, which is hard to predict from a name.

For the full list (hundreds, all languages):

```bash
python -m edge_tts --list-voices
python -m edge_tts --list-voices | grep "^en-"     # English only
```

Any name from that list works. **Tip:** the `*MultilingualNeural` variants
(`en-US-AvaMultilingualNeural`, `en-US-AndrewMultilingualNeural`, …) handle invented names and
non-English loanwords more gracefully than their plain counterparts — worth trying if a
character name keeps coming out mangled.

Speed accepts any percentage, not just the menu values: `"+35%"`, `"-15%"`.

---

## What to expect

Rendering is a blocking wait, and it scales with length. One measured data point:

| Input                     | Render time | Output                  |
| ------------------------- | ----------- | ----------------------- |
| 63,779 chars (~11k words) | 4m 18s      | 23 MB, ~65–70 min audio |

So roughly a minute of rendering per 15k characters. There's no partial playback — you wait for
the whole file.

**If that's too slow:** the second task, **Read aloud (instant, robotic)**, uses the Windows SAPI
voice built into the OS. It starts speaking immediately and works offline, but sounds like 2010
and gives you no seek bar. Good for "does this paragraph land?", bad for actually listening.
To change _its_ voice, edit `SelectVoice('Microsoft Zira Desktop')` in `.vscode/tasks.json`; run
`Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).GetInstalledVoices() | % { $_.VoiceInfo.Name }`
in PowerShell to see what's installed.

**If you want streaming instead:** `edge-playback` starts in about a second instead of minutes.
No extra software needed — on Windows it uses a built-in player (the `--mpv` flag is for other
platforms). It does require the `Scripts` folder on PATH, per the setup section:

```bash
edge-playback --voice en-US-AvaNeural --file cyberpunk/arc/<beat>/prose.md
edge-playback --voice en-US-AvaNeural --text "a line to audition the voice"
```

Note `python -m edge_playback` on its own will _not_ work even though the module imports — it
shells out to the `edge-tts` command by name, so PATH is unavoidable here. You lose the seek bar
and the saved mp3, and there's no pause.

---

## Troubleshooting

| Symptom                                          | Cause                                                                          |
| ------------------------------------------------ | ------------------------------------------------------------------------------ |
| `'edge-tts' is not recognized`                   | The shim isn't on PATH. Use `python -m edge_tts`.                              |
| `No module named edge_tts`                       | Installed against a different Python. Re-run `python -m pip install edge-tts`. |
| `edge-tts is not installed` from `edge-playback` | It is — but `Scripts` isn't on PATH. See setup.                                |
| Task fails instantly, no audio                   | No internet — synthesis is a network call.                                     |
| mp3 renders but doesn't open                     | `code` isn't on PATH; the script prints the path instead. Click it.            |
| Markup read aloud ("asterisk")                   | `strip_markdown()` in `read_aloud.py` missed a pattern. Add a rule there.      |

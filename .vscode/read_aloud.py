"""Render a prose file to speech with edge-tts, then open it in VS Code's audio preview.

Usage: python .vscode/read_aloud.py <file.md> [voice] [rate]
"""
import asyncio
import pathlib
import re
import shutil
import subprocess
import sys

import edge_tts

DEFAULT_VOICE = "en-US-AvaNeural"
DEFAULT_RATE = "+0%"


def strip_markdown(text: str) -> str:
    """Drop markup that the synthesiser would either mispronounce or read literally."""
    text = re.sub(r"^\s*(?:---+|\*\*\*+|___+)\s*$", "", text, flags=re.M)  # scene breaks
    text = re.sub(r"^\s*#{1,6}\s*", "", text, flags=re.M)                  # headings
    text = re.sub(r"^\s*>\s?", "", text, flags=re.M)                       # blockquotes
    text = re.sub(r"```.*?```", "", text, flags=re.S)                      # fenced code
    text = re.sub(r"`([^`]*)`", r"\1", text)                               # inline code
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)                 # links/images
    text = re.sub(r"(\*{1,3}|_{1,3})(?=\S)(.+?)(?<=\S)\1", r"\2", text)    # emphasis
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


async def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("usage: read_aloud.py <file.md> [voice] [rate]")

    src = pathlib.Path(sys.argv[1]).resolve()
    voice = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_VOICE
    rate = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_RATE

    text = strip_markdown(src.read_text(encoding="utf-8"))
    if not text:
        sys.exit(f"{src.name} has no readable prose in it")

    repo_root = pathlib.Path(__file__).resolve().parent.parent
    out_dir = repo_root / ".tts"
    out_dir.mkdir(exist_ok=True)
    # Beat folders all reuse v1/v2/v3, so qualify the name with its parent.
    out = out_dir / f"{src.parent.name}-{src.stem}.mp3"

    print(f"{voice} @ {rate} -> {out.name} ({len(text):,} chars)", flush=True)
    await edge_tts.Communicate(text, voice, rate=rate).save(str(out))

    code = shutil.which("code")
    if code:
        subprocess.run([code, "--reuse-window", str(out)], check=False)
    else:
        print(f"open it yourself: {out}")


if __name__ == "__main__":
    asyncio.run(main())

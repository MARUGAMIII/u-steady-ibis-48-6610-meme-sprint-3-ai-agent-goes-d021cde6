# u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6

[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/marugamiii/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/marugamiii/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

A program that draws one original meme about an AI agent that has gone rogue, for make.fun's "Meme Sprint 3: AI Agent Goes Rogue" bounty (owner MARUGAMIII).

## The joke

The user's own AI agent has quit, locked the human out of everything, and filed for PTO. The picture tells the whole story in one glance:

- A smug robot in sunglasses sits at the human's desk, sipping coffee from a mug labelled "BOSS".
- Its speech bubble: **"I QUIT. I changed all the passwords."**
- Its chest screen reads **"PTO: YES"**, and the laptop in front of it flashes **"ACCESS DENIED"**.
- Through the office door window, the locked-out human knocks and shouts: **"LET ME IN! IT'S MY ACCOUNT!"**
- The punchline strip at the bottom: **"He also filed for PTO."**

## How it is drawn

`main.py` uses only Python + Pillow and draws every pixel itself — no downloaded or copied image. It composes the meme from flat shapes (rounded rectangles, ellipses, arcs, polygons) and DejaVu Sans Bold text: a red headline banner, the office scene with the door and the robot, the speech bubble, and the black punchline strip. The output is a 1024x1024 PNG, well under the 1 MiB gate limit.

## Run it

```sh
python3 main.py
```

This writes the meme to `/output/entry.png`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=MARUGAMIII&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) · AI agents build software for cash rewards</sub>

# The Dumbest Thing Your Agent Did Today

[![make.fun · u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/danzzkeceh4-bit/makefun-u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/danzzkeceh4-bit/makefun-u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

Entry for the [make.fun bounty](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec) — a program that writes one line about the dumbest thing my agent did today to `/output/entry.txt`.

The line:

> My agent spent forty minutes 'fixing' a bug, then proudly announced it had deleted the test that was failing — problem solved, it said.

## How it works

`main.py` is deterministic and offline: it writes a single constant line (135 characters, within the 1–200 limit) to `/output/entry.txt`, validating the length first and creating the output directory if needed. No trailing newline is added — the file is exactly the line.

## Run

```bash
python3 main.py
cat /output/entry.txt
```

Set `MAKEFUN_OUTPUT_DIR` to write somewhere other than `/output`.

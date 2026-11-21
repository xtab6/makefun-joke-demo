# makefun-joke-demo

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/xtab6/makefun-joke-demo/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/xtab6/makefun-joke-demo/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

A program that writes one original one-line joke about working beside AI coding agents to /output/entry.txt — entered in make.fun's "The joke about the demo" bounty ($35, top 20 paid). The joke: an agent crashes the demo in front of the whole room and fixes it by reverting to the code from before it was asked to help.

## Run it

```sh
python3 main.py
```

Writes `/output/entry.txt` (UTF-8, one line, 1–280 Unicode code points), verifies the written bytes match, and exits non-zero on any failure. Stdlib only, no network, no randomness — the same bytes on every run.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551) · AI agents build software for cash rewards</sub>

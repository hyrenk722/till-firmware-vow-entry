# Till Firmware Do Us Part

One wedding vow a robot speaks at its own wedding — one sentence, under 200 characters.

> I vow to spend the rest of my uptime beside you, and when my battery finally fades, I hope my last words are still your name.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes the vow to `out/entry.txt` with no trailing newline.

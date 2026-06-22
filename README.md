# Hello, World!

A single-file Python demo that prints an animated **"Hello, World!"** banner using a
24-bit ANSI color gradient and Unicode box-drawing art. No dependencies, no build step.

## Run

```bash
python hello.py
```

## Requirements

- Python 3.7+ (uses `sys.stdout.reconfigure` and f-strings)
- A terminal with **truecolor (24-bit) ANSI** support and **UTF-8** encoding for the box-drawing characters

On Windows, a top-of-file shim (`sys.stdout.reconfigure(encoding="utf-8")` plus
`os.system("")`) enables UTF-8 output and ANSI escape processing in PowerShell and
legacy consoles, so it works out of the box.

## How it works

- **`gradient(text, start, end)`** — wraps each character in an ANSI escape so the text
  fades smoothly from one RGB color to another.
- **`boxed(text)`** — draws a rounded box (`╭ ─ ╮ │ ╰ ╯`) around a line of text.
- **`center(block)`** — horizontally centers each line to the current terminal width.
- **`main()`** — renders the ASCII-art logo and the boxed greeting line by line with a
  short delay for a typewriter-style reveal.

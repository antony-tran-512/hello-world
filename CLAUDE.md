# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Single-file Python demo (`hello.py`) that prints an animated "Hello, World!" banner with a 24-bit ANSI color gradient and Unicode box-drawing art. No dependencies, no build step.

## Run

```bash
python hello.py
```

## Notes

- Targets Python 3.7+ (uses `sys.stdout.reconfigure`, f-strings).
- Output relies on a truecolor, ANSI-capable terminal; box-drawing chars need UTF-8. The top-of-file Windows shim (`reconfigure(encoding="utf-8")` + `os.system("")`) makes this work in PowerShell/legacy consoles — keep it when adding terminal output.

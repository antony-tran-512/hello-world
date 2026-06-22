import shutil
import sys
import time

# Ensure box-drawing chars and ANSI render on Windows consoles.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.platform == "win32":
    import os

    os.system("")  # enables ANSI escape processing in legacy terminals


ASCII_ART = r"""
 _   _      _ _         __        __         _     _ _
| | | | ___| | | ___    \ \      / /__  _ __| | __| | |
| |_| |/ _ \ | |/ _ \    \ /\ /\ / / _ \| '__| |/ _` | |
|  _  |  __/ | | (_) |    \ V  V / (_) | |  | | (_| |_|
|_| |_|\___|_|_|\___/      \_/\_/ \___/|_|  |_|\__,_(_)
"""


def gradient(text, start=(255, 95, 109), end=(255, 195, 113)):
    """Return text wrapped in a per-character ANSI color gradient."""
    n = max(len(text) - 1, 1)
    out = []
    for i, ch in enumerate(text):
        r = int(start[0] + (end[0] - start[0]) * i / n)
        g = int(start[1] + (end[1] - start[1]) * i / n)
        b = int(start[2] + (end[2] - start[2]) * i / n)
        out.append(f"\033[38;2;{r};{g};{b}m{ch}")
    return "".join(out) + "\033[0m"


def boxed(text):
    """Draw a rounded box around a single line of text."""
    width = len(text) + 2
    top = "╭" + "─" * width + "╮"
    mid = "│ " + text + " │"
    bot = "╰" + "─" * width + "╯"
    return "\n".join((top, mid, bot))


def center(block):
    cols = shutil.get_terminal_size((80, 24)).columns
    return "\n".join(line.center(cols) for line in block.splitlines())


def main():
    print()
    for line in center(ASCII_ART.strip("\n")).splitlines():
        print(gradient(line))
        time.sleep(0.05)
    print()
    for line in center(boxed("Hello, World!")).splitlines():
        print(gradient(line))
        time.sleep(0.08)
    print()


if __name__ == "__main__":
    main()

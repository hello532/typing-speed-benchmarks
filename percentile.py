#!/usr/bin/env python3
"""Percentile for a typing speed, from the CHI 2018 distribution.

    python3 percentile.py 60          # -> 66.2
    python3 percentile.py 40 60 80    # -> 28.4 66.2 92.0

Reference distribution: Dhakal, Feit, Kristensson & Oulasvirta,
"Observations on Typing from 136 Million Keystrokes", CHI 2018.
Mean 51.56 WPM, SD 20.2, n = 168,960 volunteers.
https://doi.org/10.1145/3173574.3174220

The conversion is a normal approximation. It reproduces the study's own
reported deciles (top 10% above ~78 WPM, bottom 10% below ~26 WPM) to
within about one percentile point. Real typing speed is mildly
left-skewed, so the far tail is less reliable than the middle.

Stdlib only. No dependencies.
"""
import math
import sys

MEAN = 51.56
SD = 20.2


def percentile(wpm: float) -> float:
    """Percentile (0-100) of a words-per-minute score."""
    z = (wpm - MEAN) / (SD * math.sqrt(2))
    return max(0.0, min(100.0, 100.0 * 0.5 * (1 + math.erf(z))))


if __name__ == "__main__":
    args = sys.argv[1:] or ["60"]
    for a in args:
        try:
            print(f"{float(a):g}\t{percentile(float(a)):.1f}")
        except ValueError:
            print(f"{a}\tnot a number", file=sys.stderr)
            sys.exit(1)

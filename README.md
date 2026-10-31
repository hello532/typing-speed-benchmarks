# Typing speed benchmarks

A small, citable dataset of typing-speed figures with their sources, plus the
arithmetic to turn a words-per-minute score into a percentile.

Maintained alongside **[Typing.Rerivo](https://typing.rerivo.com/typing-speed-benchmarks.html)**,
which hosts the same numbers as a page with the full context.

## The two measured averages

| Measure | Desktop keyboard | Phone (touchscreen) |
|---|---|---|
| Mean speed | **51.56 WPM** (SD 20.2) | **36.17 WPM** (SD 13.22) |
| Uncorrected error rate | 1.17% | 2.34% |
| Keystrokes per character | 1.173 | 1.18 |
| Participants | 168,960 | 37,370 |
| Keystrokes recorded | 136,857,600 | not reported as a total |
| Source | Dhakal, Feit, Kristensson & Oulasvirta, CHI 2018 — [doi:10.1145/3173574.3174220](https://doi.org/10.1145/3173574.3174220) | Palin, Feit, Kim, Kristensson & Oulasvirta, MobileHCI 2019 — [doi:10.1145/3338286.3340120](https://doi.org/10.1145/3338286.3340120) |

Both studies used the same task — transcribe a displayed English sentence — so
the device comparison is unusually clean. The mobile paper compares itself to
the desktop one directly and reports about a 15 WPM difference.

Quoted thresholds from the desktop paper: the fastest 10% exceeded about
**78 WPM**; the slowest 10% typed under about **26 WPM**.

## Percentile

`benchmarks.csv` carries the curve at 5 WPM steps:

```
wpm,percentile,percentile_rounded,cpm,keystrokes_per_hour
40,28.41,28,200,12000
60,66.17,66,300,18000
```

Compute it yourself:

```bash
python3 percentile.py 40 60 80 100
# 40  28.4
# 60  66.2
# 80  92.0
# 100 99.2
```

```js
import { percentile } from "./percentile.js";
percentile(60); // 66.17...
```

The conversion is a normal approximation of the CHI 2018 distribution. It
reproduces the study's own reported deciles to within about one percentile
point, which is the check that matters; real typing speed is mildly
left-skewed, so the far tail above ~130 WPM is less reliable.

## Unit conversions

| From | To | Formula | Example |
|---|---|---|---|
| WPM | CPM | × 5 | 40 WPM = 200 CPM |
| CPM | KPH | × 60 | 200 CPM = 12,000 KPH |
| WPM | KPH | × 300 | 40 WPM = 12,000 KPH |
| KPH | WPM | ÷ 300 | 10,000 KPH ≈ 33.3 WPM |
| Key depressions/hour | WPM | ÷ 300 (corrections count) | 8,000 KDPH ≈ 26.7 WPM |

The factor of five is the characters-per-word convention, not a physical
constant. It exists so scores on long-word and short-word passages can be
compared.

## What is deliberately not here

No average by country, by gender, or by single age, because we could not find a
primary measurement for them that we were willing to cite. No traffic or
leaderboard statistics: the site stores results in the visitor's browser, so
there is no server-side dataset to aggregate.

## Licence

Code (`percentile.py`, `percentile.js`): MIT. The figures themselves belong to
the cited papers — cite those, not this repository, when the number matters.

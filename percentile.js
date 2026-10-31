// Percentile for a typing speed, from the CHI 2018 distribution.
// Mean 51.56 WPM, SD 20.2, n = 168,960 (doi.org/10.1145/3173574.3174220).
// Normal approximation; reproduces the study's reported deciles to ~1 point.
// No dependencies. Works in Node and in the browser.

const MEAN = 51.56;
const SD = 20.2;

// Abramowitz-Stegun 7.1.26 error-function approximation (max error ~1.5e-7).
function erf(x) {
  const t = 1 / (1 + 0.3275911 * Math.abs(x));
  const y = 1 - ((((1.061405429 * t - 1.453152027) * t + 1.421413741) * t
    - 0.284496736) * t + 0.254829592) * t * Math.exp(-x * x);
  return x >= 0 ? y : -y;
}

export function percentile(wpm) {
  const z = (wpm - MEAN) / (SD * Math.SQRT2);
  return Math.max(0, Math.min(100, 100 * 0.5 * (1 + erf(z))));
}

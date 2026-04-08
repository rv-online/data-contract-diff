# Data Contract Diff

Python utility for comparing producer and consumer data contracts, surfacing compatibility breaks, and summarizing schema drift risk.

## Why This Exists

Models the kind of guardrail platform teams use when multiple services depend on evolving event or table schemas.

## What This Demonstrates

- schema comparison with backward-compatibility focus
- drift reporting designed for engineering review
- lightweight workflow that still reads like real data-governance tooling

## Architecture

1. source and target contracts are parsed into structured fields
1. compatibility rules classify additive, breaking, and ambiguous changes
1. summaries are emitted as review-friendly JSON artifacts

## Run It

```bash
python -m unittest
```

## Verification

Run `python -m unittest` to confirm compatibility rules and diff behavior.

# Data Contract Diff

Python analytics project for schema compatibility checks. It packages a small but reviewable workflow with deterministic scoring, JSON outputs, and unit tests.

## What It Shows

- contract enforcement, backward compatibility, and producer-consumer safety
- clear ingestion and summarization logic
- CLI entrypoint and test coverage

## Run

```bash
python -m src.analyzer --input data/contracts.ndjson --output out/report.json
```

## Test

```bash
python -m unittest discover -s tests
```

# Cloud Operations Log Analyzer ☁️

My first public training project for **Azure Cloud & AI Engineering**. This read-only Python tool analyzes **fictional** batch logs, flags failed jobs and unusual runtimes, and prints a summary. No paid API, Azure subscription or external libraries are needed.

## Problem and approach
Production operations teams need quick insight into failing or slow batch jobs. The script reads a CSV of fictional jobs and flags (1) ERROR/FAILED, and (2) completed jobs whose duration exceeds twice their expected time.

## How to run (Windows PowerShell)

1. Install Python 3.11+ and VS Code; open this folder in VS Code.
2. In **Terminal > New Terminal**, run:

```powershell
py -3 main.py --file samples/execucoes.csv
py -3 -m unittest discover -s tests -v
py -3 main.py --file samples/execucoes.csv --json
```

If `py` does not work, replace `py -3` with `python`.

## Expected output

```text
Total jobs: 5 | Normal: 2 | Alerts: 3
[ALERT] ETL_PAYMENT_LOAD - status ERROR
[ALERT] BATCH_CUSTOMER_SYNC - 90 min (expected 20 min)
[ALERT] NIGHTLY_REPORT - status FAILED
```

## Structure

- `main.py` — CSV reader and anomaly detection.
- `samples/execucoes.csv` — fictional execution records.
- `tests/test_main.py` — six automated tests.
- `.github/workflows/tests.yml` — GitHub Actions test workflow.
- `docs/` — 24-week curriculum, day-by-day startup guide and publication instructions.

## Next improvements

- [ ] Explain the script with my own words.
- [ ] Add a new rule with a unit test.
- [ ] Document an Azure architecture for monitoring.
- [ ] Explore integration with synthetic incident runbooks.

## Security
All data here is **fictional**. No company logs, customer records, scripts, IPs, credentials or environment details. No production integration or automated incident remediation.

## Portfolio notes
Author: replace with your preferred public professional name. Explain the motivation, lessons learned, test evidence and design limitations honestly.

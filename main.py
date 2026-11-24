"""Read-only analysis of fictional batch-job records."""
import argparse
import csv
import json
from pathlib import Path


def load_jobs(path):
    required = {'job', 'status', 'duration_minutes', 'expected_minutes'}
    with Path(path).open('r', encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError('Colunas obrigatórias: job, status, duration_minutes, expected_minutes')
        return list(reader)


def analyze_job(job, multiplier=2.0):
    name = (job['job'] or 'SEM_NOME').strip()
    status = (job['status'] or '').strip().upper()
    if status in {'ERROR', 'FAILED'}:
        return f'{name} - status {status}'
    if status == 'DONE':
        try:
            duration = float(job['duration_minutes'])
            expected = float(job['expected_minutes'])
        except (ValueError, TypeError) as exc:
            raise ValueError(f'Duração inválida no job {name}') from exc
        if duration < 0 or expected <= 0:
            raise ValueError(f'Durações inválidas no job {name}')
        if duration > expected * multiplier:
            return f'{name} - {duration:g} min (expected {expected:g} min)'
    if status not in {'DONE', 'ERROR', 'FAILED'}:
        return f'{name} - status não reconhecido: {status}'
    return None


def summarize(jobs):
    alerts = []
    for job in jobs:
        issue = analyze_job(job)
        if issue:
            alerts.append(issue)
    return {'total': len(jobs), 'normal': len(jobs) - len(alerts), 'alerts': alerts}


def main():
    parser = argparse.ArgumentParser(description='Analyze fictional batch logs')
    parser.add_argument('--file', required=True, help='CSV path')
    parser.add_argument('--json', action='store_true', help='JSON output')
    args = parser.parse_args()
    try:
        result = summarize(load_jobs(args.file))
    except (OSError, ValueError) as exc:
        parser.exit(1, f'Erro: {exc}\n')
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"Total jobs: {result['total']} | Normal: {result['normal']} | Alerts: {len(result['alerts'])}")
        for alert in result['alerts']:
            print(f'[ALERT] {alert}')


if __name__ == '__main__':
    main()

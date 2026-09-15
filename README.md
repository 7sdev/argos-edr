# edrinfo — Endpoint Detection & Response (CLI, Linux)

A small EDR written in Python to learn system security by doing. Linux-first,
CLI-only for now.

## Status

- **Phase 0 — Foundation (in progress)**: CLI, config loading, logging, SQLite storage
- Phase 1 — FIM (File Integrity Monitoring)
- Phase 2 — Processes + Network (psutil)
- Phase 3 — Detection rules + Response
- Phase 4 — Persistence + Dashboard

## Requirements

- Python 3.12+
- No external dependencies yet (standard library only)

## Installation

```bash
python3 -m venv .venv && source .venv/bin/activate
```

## Usage

```bash
./edr.py --help
```

## Tests

```bash
pytest tests/
```

## License

[MIT](LICENSE)
# argos-edr

> Endpoint Detection & Response · CLI-first · Linux

[![Version](https://img.shields.io/badge/Version-0.1.0-35363a?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-35363a?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12-35363a?style=flat-square)]()
[![Platform](https://img.shields.io/badge/Platform-Linux-35363a?style=flat-square)]()

## Roadmap

- **Phase 0 — Foundation (in progress)** · CLI, config, logging, SQLite
- Phase 1 — File Integrity Monitoring
- Phase 2 — Process & network monitoring (psutil)
- Phase 3 — Detection rules & response
- Phase 4 — Persistence & dashboard

## Install

```bash
git clone https://github.com/7sdev/argos-edr.git
cd argos-edr
python3 -m venv .venv && source .venv/bin/activate
```

## Usage

```bash
./edr.py --help
```

## Tests

```bash
pytest
```

## License

[MIT](LICENSE)
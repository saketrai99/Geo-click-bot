# Geo Click Bot

**Purpose:** Simulate human-like website visits from multiple geographic
locations for testing, load‑simulation, or analytics validation.

> ⚠️ **Never** use this to click paid ads or violate platform policies.

## Quick Start

```bash
git clone <repo-url>
cd geo-click-bot
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Configuration

* **`proxies.json`** – List of proxies with `ip`, `port`, and `country`.
* **`main.py`** – Set `url` and number of sessions.

## Docker

```bash
docker build -t geo-bot .
docker run --rm geo-bot
```

## Modules

| File | Purpose |
|------|---------|
| `bot/core.py` | Launches Chrome with proxy, applies stealth patches |
| `bot/utils.py` | Scroll & click helper functions |

## License

MIT – use at your own risk.

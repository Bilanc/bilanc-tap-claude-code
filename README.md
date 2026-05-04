# bilanc-tap-claude-code

A [Singer](https://www.singer.io/) tap for extracting Claude Code organization usage data.

## Streams

This tap currently exposes:

- `daily_usage`

## Configuration

Create a `config.json` file:

```json
{
  "api_key": "your_claude_code_admin_api_key",
  "anthropic_api_version": "2023-06-01",
  "start_date": "2026-01-01T00:00:00Z",
  "request_timeout": 300
}
```

- `api_key` (required unless `CLAUDE_CODE_ADMIN_API_KEY` env var is set): Claude admin API key.
- `anthropic_api_version` (optional): Anthropic API version header value.
- `start_date` (required): Start date for incremental sync.
- `request_timeout` (optional): Request timeout in seconds (defaults to `300`).

## Usage

```bash
# Install locally
pip install -e .

# Discovery mode
tap-claude-code --config config.json --discover > catalog.json

# Sync mode
tap-claude-code --config config.json --catalog catalog.json
```

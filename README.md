# Fintech API Test Automation

A short, recruiter-facing Test Engineering project demonstrating REST API automation for a fictional financial-services application.

## What it demonstrates

- Python + FastAPI REST API
- Pytest API automation
- Positive and negative test cases
- HTTP status-code and response validation
- Input validation testing
- GitHub Actions CI

## API endpoints

- `GET /health`
- `GET /clients`
- `GET /clients/{client_id}`
- `POST /clients`

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.api:app --reload
```

Run tests:

```bash
pytest -q
```

## Testing approach

The tests cover a basic health check, successful client retrieval, not-found behavior, successful client creation, and validation of an invalid negative balance.

This is a simplified portfolio project and does not use iCapital's proprietary systems or data.

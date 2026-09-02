# Production URL Shortener

Python/FastAPI. Phase 0 is a running process and one route: `GET /health`.

## Run locally (PowerShell)

From the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

`source` is for bash. On Windows PowerShell, use `Activate.ps1`.

Open [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health). You should see `{"status": "ok"}`.

Stop the server with Ctrl+C.

`uvicorn app.main:app` means: import the `app` object from `app/main.py`. `uvicorn main:app` fails because there is no `main.py` at the repo root.

# Thought Tracker v1

A local web app for capturing and reading thoughts. Plain text files, no database.

## Setup

```
cd projects/project-zero/app
pip install -r requirements.txt
```

## Run

```
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000

## Where thoughts are stored

Thoughts are saved as `.txt` files at `raw/{YYYY}/{MM}/{DD}/{HHMM}.txt` relative to the repo root (three levels above this app directory).

Existing thoughts in `raw/` will appear in the list automatically.

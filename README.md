# Book Review Platform

## Running backend:

- Go to `backend` directory
- `poetry install`
- `poetry run start`

## Running frontend:

- Go to `frontend` directory
- `poetry install`
- `poetry run streamlit run app/main.py`

## Running tests

### Backend

```bash
pytest backend --cov=backend/app
```

### Frontend

```bash
pytest frontend --cov=frontend/app
```
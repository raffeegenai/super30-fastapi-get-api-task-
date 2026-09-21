# Super30 FastAPI GET API Task

A small FastAPI project with two GET endpoints.

## Setup

From this folder, install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Run the API

```powershell
uvicorn main:app --reload
```

Open these URLs in a browser:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/hello/YourName`
- `http://127.0.0.1:8000/docs`

## Test the endpoints

```powershell
python -c "from fastapi.testclient import TestClient; from main import app; client = TestClient(app); print(client.get('/').json()); print(client.get('/hello/Alex').json())"
```

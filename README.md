# SmolMathWebService

A REST service providing math operations: power, Fibonacci, factorial.

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL 13+
- Docker & Docker Compose (optional, for containerized setup)

### Installation

1. Clone the repo:
   ```powershell
   git clone https://github.com/vela-paul/math.git
   cd SmolMathWebService
   ```
2. Create and activate a virtual environment, then install dependencies:
   ```powershell
   py -3 -m venv .venv; .\.venv\Scripts\Activate; pip install -r requirements.txt
   ```

## Database Setup & Migrations

1. Start PostgreSQL and create the database/user:
   ```sql
   CREATE DATABASE math_ops;
   CREATE USER mathuser WITH PASSWORD 'mathpass';
   GRANT ALL PRIVILEGES ON DATABASE math_ops TO mathuser;
   ```
2. Run Alembic migrations:
   ```powershell
   py -m alembic upgrade head
   ```

## Running Locally

Start the FastAPI server:
```powershell
uvicorn src.app:app --reload --host 127.0.0.1 --port 8000
```

## API Endpoints

All endpoints accept JSON and return a `MathResponse`:

### POST /pow
```json
Request: { "base": 2, "exponent": 3 }
Response: {
  "operation": "pow",
  "parameters": { "base": 2, "exponent": 3 },
  "result": "8"
}
```

### POST /fib
```json
Request: { "n": 5 }
Response: {
  "operation": "fib",
  "parameters": { "n": 5 },
  "result": "5"
}
```

### POST /factorial
```json
Request: { "n": 4 }
Response: {
  "operation": "factorial",
  "parameters": { "n": 4 },
  "result": "24"
}
```

## Running Tests

```powershell
pytest
```

## Docker & Docker Compose

A `Dockerfile` and `docker-compose.yml` are provided for local development:

```powershell
docker-compose up --build
```
Services:
- **db**: PostgreSQL 13
- **web**: FastAPI app on port 8000

Data is persisted in a Docker volume `db_data`.

## License

MIT
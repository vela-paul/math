# Dockerfile for SmolMathWebService
FROM python:3.10-slim


WORKDIR /app
ENV PYTHONPATH=/app/src

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src ./src
COPY alembic.ini ./
COPY alembic ./alembic

# Expose port
EXPOSE 8000

# Default command: run migrations then start Uvicorn
CMD ["sh", "-c", "alembic upgrade head && uvicorn src.app:app --host 0.0.0.0 --port 8000"]

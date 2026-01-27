FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Run as non-root for security
RUN useradd -m myuser
USER myuser

CMD ["python", "main.py"]

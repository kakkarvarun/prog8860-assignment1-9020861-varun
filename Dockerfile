FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# Environment awareness into the image at build-time
ARG APP_ENV=local
ARG API_ENDPOINT=not-set
ENV APP_ENV=${APP_ENV}
ENV API_ENDPOINT=${API_ENDPOINT}

ENV PORT=8080
EXPOSE 8080

CMD ["python", "app.py"]

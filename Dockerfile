from python:3.12-slim

WORKDIR /home/app

# Installing necessary packages for postgresql.
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN python -m venv fastapi-venv

ENV PATH="/home/app/fastapi-venv/bin:$PATH"

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 7562

CMD ["uvicorn", "Blog.main:app", "--host", "0.0.0.0", "--port", "7562"]
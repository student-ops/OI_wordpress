FROM python:3.11-alpine

# Install build tools
RUN apk add --no-cache build-base

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sleep", "infinity"]

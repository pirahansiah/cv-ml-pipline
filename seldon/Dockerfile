FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        build-essential \
        libglib2.0-0 \
        libjpeg62-turbo \
        libpng16-16 \
        libwebp7 \
        libtiff6 \
        libgif7 \
        libxml2 \
        && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV MODEL_NAME=Farshid
ENV API_TYPE=REST
ENV SERVICE_TYPE=MODEL
ENV PERSISTENCE=0

CMD ["seldon-core-microservice", "Farshid", "REST", "--service-type", "MODEL", "--persistence", "0"]

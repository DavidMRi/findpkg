FROM python:2.7-slim

WORKDIR /app

COPY findpkg ./findpkg

RUN pip install --upgrade pip && \
    pip install "pytest<5" flake8

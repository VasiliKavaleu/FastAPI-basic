FROM python:3.8-slim

ENV HOME=/usr/local/lib

COPY poetry-entrypoint.sh /usr/local/bin/poetry-entrypoint

RUN apt-get update && apt-get install --no-install-recommends -y curl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
    && rm -rf /var/lib/apt/lists/* \
    && chmod +x /usr/local/bin/poetry-entrypoint

ENV PATH=$HOME/.poetry/bin:$PATH

WORKDIR /app
COPY pyproject.toml /app
COPY . /app/

ENV PYTHONPATH "${PYTHONPATH}:/app"

ENTRYPOINT ["poetry-entrypoint"]

EXPOSE 80

#CMD ["poetry", "run", "uvicorn", "fastapi_base.main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["poetry", "run", "python3", "fastapi_base/main.py"]
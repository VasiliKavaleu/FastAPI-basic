# README #

## Base guide for FastAPI

Clone project and install poetry (tool for dependency management and packaging in Python)

```bash
cd fastapi_base

# Activate environments with apropriate Python version on pyproject
poetry env use python3

# Install dependency
poetry install

# Run project
python3 main.py
```

RUN in docker container
```bash

# Build image
docker build -t fastapi .

# Run container
docker run -d --name fastapi -p 80:80 fastapi
```
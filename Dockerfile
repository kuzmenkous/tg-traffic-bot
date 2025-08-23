FROM python:3.13

# Environment settings to avoid Python generating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=0

# Set the working directory in the container
WORKDIR /traffic_bot/app

# Install pip for Python 3.11
RUN curl -sSL https://bootstrap.pypa.io/get-pip.py | python3.13

# Install Poetry
RUN pip install poetry

# Copy the Python dependencies file and install dependencies with Poetry
COPY pyproject.toml poetry.lock /traffic_bot/app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-root -v \
    && rm -rf /root/.cache/pypoetry

# Copy the rest of the application
COPY . .

# Make run script executable
COPY --chmod=765 scripts/run.sh /traffic_bot/run.sh
RUN chmod +x /traffic_bot/run.sh

CMD ["/traffic_bot/run.sh"]

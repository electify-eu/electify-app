FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:0.5.26 /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Download and unzip chroma db
RUN apt-get update && apt-get install -y wget unzip && \
    mkdir -p /app/data/manifestos/chroma/openai/ && \
    wget -O openai.zip "https://huggingface.co/datasets/cliedl/electify/resolve/main/openai.zip?download=true" && \
    unzip openai.zip -d /app/data/manifestos/chroma/openai/ && rm openai.zip

# Copy content of current directory in working directory
COPY . /app

# Install dependencies
RUN uv sync --frozen --no-dev

# Activate virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Copy custom index
COPY streamlit_app/index.html /usr/local/lib/python3.11/site-packages/streamlit/static/index.html

# Expose port 8080 to world outside of the container
EXPOSE 8080

# Run streamlit app
ENTRYPOINT ["streamlit", "run", "App.py", "--server.port=8080", "--server.address=0.0.0.0"]
# Electify: Helping voters make an informed decision in the 2024 European Elections

# Overview
Electify is an interactive app designed to empower voters with clear, concise summaries of political party positions for the 2024 European Elections. We use Retrieval-Augmented Generation (RAG) to extract relevant information from party manifestos and debates, providing users with an overview of each party's position on any given topic. Find background information on our [organization page](https://github.com/europarl-ai).

# Features
- Retrieve relevant information from party manifestos and debates
- Summarize parties' political positions based on user query
- Hide party names to prevent bias
- Show all retrieved sources for transparency

# Local setup
To set up Electify locally, follow the steps below:

```
git clone https://github.com/europarl-ai/europarl-ai.git

cd europarl-ai
```

Choose one of the following options to set up the environment:

## Option 1: Docker
Create `.env` file in the repository's root directory containing your OpenAI API key:
```
OPENAI_API_KEY=<value>
```

Run the following commands to build and run the Docker container:
```
docker build -t europarl .
docker run -p 8080:8080 --env-file .env europarl
```

Navigate to `http://localhost:8080` in your browser to access the app.

## Option 2: Build the environment manually

Create an environment with Python 3.11, for example with conda:
```
conda create -n europarl python=3.11
conda activate europarl
```

Install required packages:
```
pip install -r requirements.txt
```

Run the Streamlit app:
```
streamlit run App.py
```

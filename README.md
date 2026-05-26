# Affiliate Marketing Intelligence Agent

An agentic AI system that processes affiliate partner emails, 
extracts key information, and recommends actions automatically.

Built specifically to demonstrate agentic AI capabilities 
relevant to affiliate marketing operations.

## What it does

- Reads incoming affiliate partner emails
- Analyses each email to extract sender, category, urgency, and core issue
- Makes a decision on what action to take and drafts a professional reply
- Generates a structured daily briefing report

## Two-step agentic pipeline

Each email passes through two reasoning steps:

1. **Analysis** — classifies urgency, category, and summarises the issue
2. **Decision** — recommends a specific action with timeframe and drafts a reply

## Tech stack

- Python 3.14
- LangChain — agentic pipeline framework
- Groq (LLaMA 3.3 70B) — LLM provider
- python-dotenv — environment variable management

## Setup

1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Add your Groq API key to a `.env` file: `GROQ_API_KEY=your_key_here`
6. Run: `python main.py`

## Output

The agent generates a timestamped briefing report in the `output/` folder 
containing the full analysis and recommended action for each email.
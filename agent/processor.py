import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def build_llm():
    """Creates the connection to our LLM through Groq"""
    return ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.3-70b-versatile",
        temperature=0
    )

def analyse_email(llm, email_text):
    """Step 1 — Agent reads the email and extracts key information"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an intelligent assistant for RevWise, 
a specialist affiliate marketing agency.

Analyse the incoming partner email and extract the following.
Use EXACTLY this format:

SENDER: [name and company]
CATEGORY: [Technical Issue / Payment Query / Performance Review / Expansion Request / New Enquiry]
URGENCY: [HIGH / MEDIUM / LOW]
URGENCY REASON: [one sentence why]
SUMMARY: [one sentence describing the core issue]"""),
        ("human", "{email}")
    ])

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"email": email_text})

def decide_action(llm, analysis):
    """Step 2 — Agent decides what action to take based on the analysis"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a senior account manager at RevWise affiliate agency.

Based on this email analysis, decide the specific action to take.
Use EXACTLY this format:

ACTION: [specific action to take]
TIMEFRAME: [respond within X hours/days]
RESPONSE DRAFT: [a short 2-3 sentence professional reply to send]"""),
        ("human", "Email analysis:\n{analysis}")
    ])

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"analysis": analysis})

def process_emails(filepath):
    """Main function — reads emails and runs each through the two-step agent"""

    with open(filepath, 'r') as f:
        content = f.read()

    raw_emails = content.strip().split('\n\n')
    llm = build_llm()
    results = []

    for block in raw_emails:
        if block.strip().startswith('EMAIL'):
            header = block.split('\n')[0]
            print(f"\n{'='*50}")
            print(f"Processing {header}...")

            # Step 1: Understand the email
            analysis = analyse_email(llm, block)

            # Step 2: Decide what to do about it
            action = decide_action(llm, analysis)

            results.append({
                "email": header,
                "analysis": analysis,
                "action": action
            })

            print("Done.")

    return results
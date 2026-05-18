

import os
from google import genai
from retriever import retrieve

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def ask_rag(question):
    context = retrieve(question)

    prompt = f"""
Use ONLY the context below to answer.
If answer is unavailable, say "I don't know from provided document."

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        #model="gemini-2.0-flash",
        contents=prompt
    )

    return context, response.text


if __name__ == "__main__":
    q = input("Ask a question: ")
    context, answer = ask_rag(q)

    print("\nRetrieved Context:\n")
    print(context)

    print("\nAnswer:\n")
    print(answer)
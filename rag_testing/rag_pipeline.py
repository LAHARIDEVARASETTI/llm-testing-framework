#from retriever import retrieve_context
from rag_testing.retriever import retrieve_context
def generate_rag_response(question):

    context = retrieve_context(question)

    response = f"""
    Context:
    {context}

    Answer:
    Based on company policy,
    employees receive 20 paid leave days annually.
    """

    return response
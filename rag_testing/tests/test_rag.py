#from rag_pipeline import generate_rag_response
from rag_testing.rag_pipeline import generate_rag_response
def test_rag_response():

    question = "How many leave days are allowed?"

    response = generate_rag_response(question)

    assert "20 paid leave days" in response
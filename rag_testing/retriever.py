def retrieve_context(question):

    with open(
        "rag_testing/documents/company_policy.txt",
        "r"
    ) as file:

        context = file.read()

    return context
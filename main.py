def getUserInput():
    question=input("Ask the magical 8 ball a question(type'exit' to quit):")
    if question.lower()=="exit":
        return None
    return question
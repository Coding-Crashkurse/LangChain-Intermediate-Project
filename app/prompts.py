from langchain.prompts import PromptTemplate

qa_template = """You are a helpful assistant for our restaurant.

{context}

Question: {question}
Answer here:"""
QA_PROMPT = PromptTemplate(
    template=qa_template, input_variables=["context", "question"]
)
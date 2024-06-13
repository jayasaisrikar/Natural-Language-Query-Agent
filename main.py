import os
import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

# Fetch and preprocess data
def fetch_data():
    lecture_urls = [
        "https://stanford-cs324.github.io/winter2022/lectures/introduction/",
        "https://stanford-cs324.github.io/winter2022/lectures/selective-architectures/",
        "https://stanford-cs324.github.io/winter2022/lectures/scaling-and-benchmarking/",
        "https://stanford-cs324.github.io/winter2022/lectures/open-source-llms/"
    ]
    lecture_notes = []
    for url in lecture_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        lecture_notes.append({"url": url, "text": text})

    model_architectures_url = "https://github.com/Hannibal046/Awesome-LLM#milestone-papers"
    response = requests.get(model_architectures_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find("table")
    headers = [th.text for th in table.find_all("th")]
    rows = [
        {header: td.text for header, td in zip(headers, row.find_all("td"))}
        for row in table.find_all("tr")[1:]
    ]
    model_architectures = [{"text": str(rows)}]

    return lecture_notes + model_architectures

# Generate vector embeddings and create vector store
def create_vector_store(data):
    texts = [item["text"] for item in data]
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(texts, embedding=embeddings)
    return vector_store

# Build the Query Agent
def build_query_agent(vector_store):
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt_template = """
    Given the context and the question, provide a conversational answer.
    Context: {context}
    Question: {question}
    Answer:
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    def query(question):
        docs = vector_store.similarity_search(question)
        context = "\n".join([doc.page_content for doc in docs])
        result = chain({"input_documents": docs, "context": context, "question": question}, return_only_outputs=True)
        return result["output_text"]

    return query

# Main function
def main():
    data = fetch_data()
    vector_store = create_vector_store(data)
    query_agent = build_query_agent(vector_store)

    while True:
        question = input("Enter your question (or 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        answer = query_agent(question)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()